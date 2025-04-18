-- Forbedret SQL med begrensninger, indekser, triggers og prosedyrer

CREATE TABLE account_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    ads_enabled BOOLEAN DEFAULT TRUE,
    plan_type VARCHAR(50) CHECK (plan_type IN ('monthly', 'yearly', 'free'))
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE CHECK (email LIKE '%@%.%'),
    registration_date DATE DEFAULT CURRENT_DATE,
    account_type_id INTEGER REFERENCES account_types(id)
);

CREATE INDEX idx_users_email ON users(email);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    country VARCHAR(100)
);

CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    duration INTEGER CHECK (duration > 0),
    genre VARCHAR(100),
    release_date DATE,
    artist_id INTEGER REFERENCES artists(id)
);

CREATE INDEX idx_songs_release_date ON songs(release_date);

CREATE TABLE playlists (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    name VARCHAR(255),
    created_date DATE,
    song_count INTEGER DEFAULT 0
);

CREATE TABLE playlist_songs (
    playlist_id INTEGER REFERENCES playlists(id),
    song_id INTEGER REFERENCES songs(id),
    added_date DATE,
    position_in_playlist INTEGER,
    PRIMARY KEY (playlist_id, song_id)
);

CREATE TABLE listening_history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    song_id INTEGER REFERENCES songs(id),
    listened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    device_used VARCHAR(100)
);

CREATE INDEX idx_listening_history_timestamp ON listening_history(listened_at);

CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    start_date DATE,
    end_date DATE,
    type VARCHAR(50)
);

-- Trigger for å holde styr på antall sanger i en spilleliste
CREATE OR REPLACE FUNCTION update_song_count() RETURNS TRIGGER AS $$
BEGIN
    UPDATE playlists SET song_count = song_count + 1
    WHERE id = NEW.playlist_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_song_count
AFTER INSERT ON playlist_songs
FOR EACH ROW
EXECUTE FUNCTION update_song_count();

-- Stored Procedure for å hente mest spilte sanger
CREATE OR REPLACE FUNCTION get_most_played_songs()
RETURNS TABLE(song_id INTEGER, play_count INTEGER) AS $$
BEGIN
    RETURN QUERY
    SELECT song_id, COUNT(*) as play_count
    FROM listening_history
    GROUP BY song_id
    ORDER BY play_count DESC
    LIMIT 10;
END;
$$ LANGUAGE plpgsql;
