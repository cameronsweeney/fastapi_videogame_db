# Phases of "Reverse Waterfall" App Generation

## Phase 1

A database of your games (board games or video games) with a schedule of the next times you want to play with friends that pulls from a public google calendar

## Phase 2

- game title
- system
- year
- genre
- real-time vs turn/wait
- solo vs multiplayer
- easy vs hard
- grind vs think

## Phase 3

I want to make a web application using FastAPI and Postgres, using a basic, native browser implementation of a video game database.
At a minimum I want to keep track of the following pieces of information for each video game:

- game title
- system
- year published
- completion level: not started vs playing vs completed vs 100%ed
- genre
- time vibe: real-time vs turn/wait
- solo vs multiplayer
- difficulty vibe: rating out of 5 (1 is easiest, 5 is hardest)
- action vibe: action-packed vs cozy
- brainspace vibe: how much thinking/decision-making is needed to play this game - 1 is just grinding, no thoughts; 5 is very strategy-focused or mentally taxing

Please include any other fields you can think of.

I want the front-end to show a count of games at each completion level and allow browsing by genre and vibe.

Please return a clear and detailed requirements document describing the application UI features as a list, and the data requirements for those UI features, separated into two sections, UI Features and Data Requirements.

For the UI Requirements, please make sure to include these pages:

- A front page
- a list-view page, listing all of the things
- a detail view page for showing a single thing
- a filtered-list-view page for showing some of the things by category

## Phase 4

SQLChat -> execute schema in Neon Database

## Phase 5

### Requirements Document for Video Game Database Web Application

---

#### UI Features

1. **Front Page**
   - Display a welcome message or brief description of the database.
   - Show a dashboard summary of games by completion level (Not Started, Playing, Completed, 100%ed), with counts for each category.
   - Navigation menu to access List View, Filtered List View, and potentially an Add/Edit Game page.

2. **List View Page**
   - Display all video games in a table format.
   - Columns for game title, system, year published, genre, and a summarized vibe overview (possibly as icons or short tags).
   - Options to sort by various attributes like title, year, genre, etc.
   - Clickable game titles leading to the Detail View Page of each game.

3. **Detail View Page**
   - Show detailed information about a single video game.
   - Include fields such as game title, system, year, completion level, genre, time vibe, solo/multiplayer, difficulty vibe, action vibe, brainspace vibe.
   - Provide options to edit or delete the game entry (if the application has user authentication and permissions).
   - Link to return to the List View or Filtered List View.

4. **Filtered List View Page**
   - Allow users to filter the list of video games by various criteria such as genre, system, completion level, vibes (time, action, brainspace), etc.
   - Display the filtered results in a format similar to the List View Page.
   - Include a reset filter option to return to the full list.

#### Data Requirements

- **Game Information**
  - `game_title`: Text field to store the title of the video game.
  - `system`: Text field to specify the platform/system the game runs on (e.g., PlayStation, Xbox, PC, etc.).
  - `year_published`: Integer field for the release year of the game.
  - `completion_level`: Enumeration or text field to track the game's progress (Not Started, Playing, Completed, 100%ed).
  - `genre`: Text field to specify the genre of the game (e.g., Action, RPG, Puzzle, etc.).
  - `time_vibe`: Text field to indicate if the game runs in real-time or has a turn/wait mechanism.
  - `solo_multiplayer`: Text field to specify if the game is solo or multiplayer.
  - `difficulty_vibe`: Integer field to rate the game's difficulty from 1 (easiest) to 5 (hardest).
  - `action_vibe`: Text field to describe the game's pace (Action-packed vs Cozy).
  - `brainspace_vibe`: Integer field to rate the intellectual engagement required from 1 (minimal thinking) to 5 (strategy-focused or mentally taxing).

- **Additional Fields**
  - `developer`: Text field for the game's developer.
  - `publisher`: Text field for the game's publisher.
  - `rating`: Text field to store ESRB rating or similar.
  - `play_time`: Text field to record typical or average playtime required to complete the game.
  - `user_rating`: Decimal field to store user ratings, averaged out if multiple.
  - `notes`: Text field for users to add personal notes or reviews.

This document outlines the essential UI features and data requirements for your video game database application using FastAPI and Postgres. The application will serve as a functional tool to not only catalog but also explore various aspects of gaming preferences and experiences.

Here is the database schema:
CREATE TABLE Games (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    game_title VARCHAR(255) NOT NULL,
    system VARCHAR(100) NOT NULL,
    year_published INT,
    completion_level ENUM('Not Started', 'Playing', 'Completed', '100%ed') NOT NULL,
    genre VARCHAR(100),
    time_vibe ENUM('Real-time', 'Turn/Wait') NOT NULL,
    solo_multiplayer ENUM('Solo', 'Multiplayer') NOT NULL,
    difficulty_vibe INT CHECK (difficulty_vibe BETWEEN 1 AND 5),
    action_vibe ENUM('Action-packed', 'Cozy') NOT NULL,
    brainspace_vibe INT CHECK (brainspace_vibe BETWEEN 1 AND 5),
    developer VARCHAR(255),
    publisher VARCHAR(255),
    play_time VARCHAR(100),
    notes TEXT
);

Please create a RESTful FastAPI

Please continue to implement the server-side logic given the schema. Use psycopg2 to connect to the DATABASE_URL in the environment variables. Please implement all the required routes for the UI to function and complete implementations including all needed server-side validation of data.

Please write the entire FastAPI in a single file. Do not tell me how to install any necessary packages - I already have an appropriate Python environment.
