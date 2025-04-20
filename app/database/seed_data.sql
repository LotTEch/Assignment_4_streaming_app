-- Nullstill data
TRUNCATE TABLE subscriptions, listening_history, playlist_songs, playlists, songs, artists, users, account_types RESTART IDENTITY CASCADE;


-- =========================
-- Kontotyper (må samsvare med CHECK!)
-- =========================
INSERT INTO account_types (name, ads_enabled, plan_type)
VALUES
('Gratis konto', TRUE, 'free'),
('Månedlig abonnement', FALSE, 'monthly'),
('Årlig abonnement', FALSE, 'yearly');

-- =========================
-- Brukere
-- =========================
INSERT INTO users (first_name, last_name, email, account_type_id, registration_date)
VALUES
('John', 'Doe', 'john.doe@example.com', 1, '2023-01-01'),
('Jane', 'Smith', 'jane.smith@example.com', 2, '2023-02-01'),
('Alice', 'Wong', 'alice.w@example.com', 1, '2023-04-01'),
('Bob', 'Andersen', 'bob.a@example.com', 3, '2023-05-10');

-- =========================
-- Artister
-- =========================
INSERT INTO artists (name, genre, country)
VALUES
('Adele', 'Pop', 'UK'),
('Imagine Dragons', 'Rock', 'USA'),
('Kygo', 'EDM', 'Norway');

-- =========================
-- Sanger
-- =========================
INSERT INTO songs (title, duration, genre, release_date, artist_id)
VALUES
('Hello', 300, 'Pop', '2023-01-01', 1),
('Believer', 200, 'Rock', '2023-02-15', 2),
('Firestone', 240, 'EDM', '2022-12-01', 3),
('Demons', 220, 'Rock', '2021-11-20', 2);

-- =========================
-- Spillelister
-- =========================
INSERT INTO playlists (user_id, name, created_date)
VALUES
(1, 'My Favs', '2023-03-01'),
(2, 'Workout Mix', '2023-04-10');

-- =========================
-- Spilleliste-sanger
-- =========================
INSERT INTO playlist_songs (playlist_id, song_id, added_date)
VALUES
(1, 1, '2023-03-02'),
(1, 3, '2023-03-03'),
(2, 2, '2023-04-11'),
(2, 4, '2023-04-12');

-- =========================
-- Lyttehistorikk
-- =========================
INSERT INTO listening_history (user_id, song_id, listened_at, device_used)
VALUES
(1, 1, '2023-03-03 10:00:00', 'Phone'),
(1, 3, '2023-03-04 11:00:00', 'Tablet'),
(2, 2, '2023-04-12 12:00:00', 'PC'),
(2, 4, '2023-04-13 13:00:00', 'Phone'),
(3, 2, '2023-05-01 09:00:00', 'Laptop');

-- =========================
-- Abonnementer
-- =========================
INSERT INTO subscriptions (user_id, start_date, end_date, type)
VALUES
(2, '2023-02-01', '2024-02-01', 'gold'),
(4, '2023-05-10', '2024-05-10', 'platinum');

-- Flere artister
INSERT INTO artists (name, genre, country)
VALUES
('Taylor Swift', 'Pop', 'USA'),
('Ed Sheeran', 'Pop', 'UK'),
('The Weeknd', 'R&B', 'Canada');

-- Flere spillelister
INSERT INTO playlists (user_id, name, created_date)
VALUES
(3, 'Chill Vibes', '2023-06-01'),
(4, 'Party Hits', '2023-07-01');