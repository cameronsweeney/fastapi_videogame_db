-- Create ENUM types for the respective fields
CREATE TYPE completion_level AS ENUM ('Not Started', 'Playing', 'Completed', '100%ed');
CREATE TYPE time_vibe AS ENUM ('Real-time', 'Turn/Wait');
CREATE TYPE solo_multiplayer AS ENUM ('Solo', 'Multiplayer');
CREATE TYPE action_vibe AS ENUM ('Action-packed', 'Cozy');

-- Create the table using the newly defined ENUMs
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,
    game_title VARCHAR(255) NOT NULL,
    system VARCHAR(100) NOT NULL,
    year_published INT,
    completion_level completion_level NOT NULL,
    genre VARCHAR(100),
    time_vibe time_vibe NOT NULL,
    solo_multiplayer solo_multiplayer NOT NULL,
    difficulty_vibe INT CHECK (difficulty_vibe BETWEEN 1 AND 5),
    action_vibe action_vibe NOT NULL,
    brainspace_vibe INT CHECK (brainspace_vibe BETWEEN 1 AND 5),
    developer VARCHAR(255),
    publisher VARCHAR(255),
    play_time VARCHAR(100),
    notes TEXT
);
