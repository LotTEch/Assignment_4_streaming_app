INSERT INTO users (first_name, last_name, email, user_type, registration_date)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'free', '2023-01-01'),
('Jane', 'Smith', 'jane.smith@example.com', 'premium', '2023-02-01');

INSERT INTO free_users (user_id, ads_enabled)
VALUES 
(1, TRUE);

INSERT INTO premium_users (user_id, subscription_start, subscription_end, plan_type)
VALUES 
(2, '2023-02-01', '2024-02-01', 'gold');

INSERT INTO artists (name, genre, country)
VALUES 
('Artist A', 'Pop', 'USA'),
('Artist B', 'Rock', 'UK');

INSERT INTO songs (title, duration, genre, release_date, artist_id)
VALUES 
('Song 1', 210, 'Pop', '2023-01-01', 1),
('Song 2', 180, 'Rock', '2023-02-01', 2);

INSERT INTO playlists (user_id, name, created_date)
VALUES 
(1, 'My Playlist', '2023-03-01');

INSERT INTO playlist_songs (playlist_id, song_id, added_date)
VALUES 
(1, 1, '2023-03-02');

INSERT INTO listening_history (user_id, song_id, listened_at)
VALUES 
(1, 1, '2023-03-03 10:00:00');

INSERT INTO subscriptions (user_id, start_date, end_date, type)
VALUES 
(2, '2023-02-01', '2024-02-01', 'gold');