from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


from pydantic import BaseModel, conint, Field
from typing import List, Optional, Annotated
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import os

from dotenv import load_dotenv



app = FastAPI()

# CORS setup for frontend interaction, adjust origins as necessary.
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection setup
load_dotenv()  # This method will load the variables from .env
DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(
    DATABASE_URL,
    sslmode='require'  # Use 'verify-full' for full SSL verification (recommended)
)

class Game(BaseModel):
    game_id: Optional[int]
    game_title: str
    system: str
    year_published: Optional[int]
    completion_level: str
    genre: Optional[str]
    time_vibe: str
    solo_multiplayer: str
    difficulty_vibe: Optional[Annotated[int, conint(ge=1, le=5)]] = Field(default=None, description="Rate the game difficulty from 1 (easiest) to 5 (hardest)")
    action_vibe: str
    brainspace_vibe: Optional[Annotated[int, conint(ge=1, le=5)]] = Field(default=None, description="Rate the intellectual engagement from 1 (least) to 5 (most)")
    developer: Optional[str]
    publisher: Optional[str]
    play_time: Optional[str]
    notes: Optional[str]

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route to serve the index.html
@app.get("/")
def read_index():
    return FileResponse("templates/index.html")




@app.post("/games/", response_model=Game)
def create_game(game: Game):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            INSERT INTO Games (game_title, system, year_published, completion_level, genre, time_vibe, solo_multiplayer, difficulty_vibe, action_vibe, brainspace_vibe, developer, publisher, rating, play_time, user_rating, notes) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;
        """, (game.game_title, game.system, game.year_published, game.completion_level, game.genre, game.time_vibe, game.solo_multiplayer, game.difficulty_vibe, game.action_vibe, game.brainspace_vibe, game.developer, game.publisher, game.rating, game.play_time, game.user_rating, game.notes))
        conn.commit()
        new_game = cur.fetchone()
        return new_game

@app.get("/games/", response_model=List[Game])
def read_games(skip: int = 0, limit: int = 100):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM Games OFFSET %s LIMIT %s;", (skip, limit))
        games = cur.fetchall()
        return games

@app.get("/games/{game_id}", response_model=Game)
def read_game(game_id: int):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM Games WHERE game_id = %s;", (game_id,))
        game = cur.fetchone()
        if game is None:
            raise HTTPException(status_code=404, detail="Game not found")
        return game

@app.put("/games/{game_id}", response_model=Game)
def update_game(game_id: int, game: Game):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            UPDATE Games SET game_title=%s, system=%s, year_published=%s, completion_level=%s, genre=%s, time_vibe=%s, solo_multiplayer=%s, difficulty_vibe=%s, action_vibe=%s, brainspace_vibe=%s, developer=%s, publisher=%s, rating=%s, play_time=%s, user_rating=%s, notes=%s WHERE game_id=%s RETURNING *;
        """, (game.game_title, game.system, game.year_published, game.completion_level, game.genre, game.time_vibe, game.solo_multiplayer, game.difficulty_vibe, game.action_vibe, game.brainspace_vibe, game.developer, game.publisher, game.rating, game.play_time, game.user_rating, game.notes, game_id))
        updated_game = cur.fetchone()
        conn.commit()
        if updated_game is None:
            raise HTTPException(status_code=404, detail="Game not found")
        return updated_game

@app.delete("/games/{game_id}", status_code=204)
def delete_game(game_id: int):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM Games WHERE game_id = %s;", (game_id,))
        conn.commit()
        return {"message": "Game deleted"}

