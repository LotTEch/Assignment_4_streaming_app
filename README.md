# Streaming App for Music 🎵

## Overview

This project is a **streaming app for music**, designed to manage users, playlists, songs, and listening history. The database schema is based on the provided **EER diagram**, and the application is implemented using **Python**, **FastAPI**, and **SQLAlchemy** for backend logic, with a **PostgreSQL** database.

---

## Project Structure

### 1. **Database Files**

#### `database/init_db.sql`

- **Purpose**: Defines the database schema based on the EER diagram.
- **Relation to EER Diagram**:
  - Implements all tables (`users`, `free_users`, `premium_users`, `artists`, `songs`, `playlists`, `playlist_songs`, `listening_history`, `subscriptions`).
  - Includes additional fields like `device_used` in `listening_history` and `position_in_playlist` in `playlist_songs`.
- **Future Improvements**:
  - Add constraints for data validation (e.g., `CHECK` constraints for valid dates).
  - Optimize indexes for frequently queried fields (e.g., `listened_at` in `listening_history`).

#### `database/seed_data.sql`

- **Purpose**: Populates the database with initial data for testing.
- **Relation to EER Diagram**:
  - Inserts sample data for all tables, ensuring relationships between entities are respected.
- **Future Improvements**:
  - Add more realistic and diverse data for testing edge cases.
  - Automate data generation for scalability.

---

### 2. **Backend Files**

#### `backend/config.py`

- **Purpose**: Stores the database connection string.
- **Relation to EER Diagram**:
  - Connects the application to the PostgreSQL database.
- **Future Improvements**:
  - Use environment variables for sensitive data (e.g., `DATABASE_URL`).
  - Add support for multiple environments (e.g., development, testing, production).

#### `backend/db.py`

- **Purpose**: Sets up the SQLAlchemy engine, session, and base class for ORM models.
- **Relation to EER Diagram**:
  - Provides the foundation for interacting with the database tables.
- **Future Improvements**:
  - Implement connection pooling for better performance.
  - Add logging for database queries.

#### `backend/models/users.py`

- **Purpose**: Defines ORM models for `users`, `free_users`, and `premium_users`.
- **Relation to EER Diagram**:
  - Implements the `users` table and its subtypes (`free_users`, `premium_users`).
- **Future Improvements**:
  - Add validation logic for user input (e.g., email format).
  - Implement methods for user-specific queries (e.g., fetching all playlists for a user).

#### `backend/models/songs.py`

- **Purpose**: (Empty) Will define ORM models for the `songs` table.
- **Relation to EER Diagram**:
  - Will implement the `songs` table and its relationship with `artists`.
- **Future Improvements**:
  - Add methods for querying songs by genre, artist, or release date.

#### `backend/models/playlists.py`

- **Purpose**: (Empty) Will define ORM models for `playlists` and `playlist_songs`.
- **Relation to EER Diagram**:
  - Will implement the `playlists` table and its many-to-many relationship with `songs` via `playlist_songs`.
- **Future Improvements**:
  - Add methods for managing playlists (e.g., adding/removing songs, reordering).

#### `backend/models/subscription.py`

- **Purpose**: (Empty) Will define ORM models for the `subscriptions` table.
- **Relation to EER Diagram**:
  - Will implement the `subscriptions` table and its relationship with `users`.
- **Future Improvements**:
  - Add methods for managing subscription renewals and cancellations.

---

### 3. **App Files**

#### `app/api.py`

- **Purpose**: Provides a REST API for interacting with the `users` table.
- **Relation to EER Diagram**:
  - Implements basic CRUD operations for the `users` table.
- **Future Improvements**:
  - Add endpoints for other tables (e.g., `songs`, `playlists`).
  - Implement authentication and authorization.

#### `app/visualizations.py`

- **Purpose**: (Empty) Will generate visualizations based on `listening_history`.
- **Relation to EER Diagram**:
  - Will analyze and visualize data from `listening_history` (e.g., most played songs, user activity).
- **Future Improvements**:
  - Use libraries like `Matplotlib` or `Plotly` for interactive charts.
  - Add support for exporting visualizations as images or PDFs.

#### `app/main.py` 

- **Purpose**: (Empty) Will serve as the entry point for the application.
- **Relation to EER Diagram**:
  - Will integrate all components (API, visualizations, database interactions).
- **Future Improvements**:
  - Add a CLI or web interface for user interaction.
  - Implement error handling and logging.

---

## Future Steps for High Achievement

### 1. **Database Enhancements** 

- **Normalization**: Ensure all tables are in at least 3NF to avoid redundancy.
- **Indexes**: Add indexes on frequently queried fields (e.g., `email`, `listened_at`).
- **Stored Procedures**: Implement stored procedures for complex queries (e.g., generating user statistics).
- **Backups**: Set up automated backups for data integrity.

### 2. **Python Development**

- **ORM Models**: Complete the implementation of all ORM models.
- **Unit Tests**: Write tests for all models and API endpoints using `pytest`.
- **Error Handling**: Add robust error handling for database and API operations.
- **Performance**: Optimize queries and reduce API response times.

### 3. **API Development**

- **Endpoints**: Add endpoints for all tables and relationships.
- **Pagination**: Implement pagination for large datasets (e.g., songs, playlists).
- **Authentication**: Add user authentication and role-based access control.

### 4. **Visualizations**

- **User Insights**: Create dashboards for user activity and song popularity.
- **Export Options**: Allow users to export data as CSV or Excel files.
- **Real-Time Updates**: Use WebSockets for real-time updates in visualizations.

### 5. **Documentation**

- **API Docs**: Use tools like Swagger or Redoc to generate API documentation.
- **User de**: Write a de for setting up and using the application.
- **Code Comments**: Add comments to all files for better maintainability.

---

## Key Considerations for Success

1. **Scalability**: Design the database and API to handle a growing number of users and songs.
2. **Security**: Protect sensitive data (e.g., user emails, subscription details).
3. **User Experience**: Focus on intuitive interfaces and fast response times.
4. **Testing**: Ensure all components are thoroughly tested to avoid bugs.
5. **Extensibility**: Design the system to easily accommodate new features (e.g., video streaming).

---

## Conclusion

This project is well-structured and aligned with the EER diagram. By completing the missing components and following the outlined steps, you can build a robust and scalable streaming app for music. Let me know if you need help with any specific part of the implementation.

---

# Streaming App for Music 🎵


## Overview


Dette prosjektet er en **streamingtjeneste for musikk**, som lar deg administrere brukere, spillelister, sanger og lyttehistorikk. Systemet er bygd med **Python**, **Streamlit**, **SQLAlchemy** og **MySQL**, og databasen er basert på et **EER-diagram** med fullstendig normalisering.

---

## Prosjektstruktur

### 1. 📁 `database/`

#### `init_db.sql`

- **Formål**: Oppretter alle tabeller, indekser, constraints og triggere basert på EER-diagrammet.
- **Dekker**: `users`, `account_types`, `artists`, `songs`, `playlists`, `playlist_songs`, `listening_history`, `subscriptions`
- **Inneholder**:
  - `FOREIGN KEY`-relasjoner
  - `CHECK`-constraints (f.eks. epostvalidering, positive lengder)
  - Trigger for å oppdatere antall sanger i spillelister
  - Lagret prosedyre for å hente de mest spilte sangene

#### `seed_data.sql`

- **Formål**: Populerer databasen med testdata for utvikling og testing.
- **Inneholder**:
  - Eksempeldata for brukere, artister, sanger, spillelister og lyttehistorikk
  - Full respekt for fremmednøkkel-relasjoner

---

### 2. 📂 `backend/`

#### `config.py`

- Leser databasenøkkel fra `.env`
- Klargjort for ulike miljøer (lokalt, test, prod)

#### `db.py`

- Konfigurerer `SQLAlchemy` motor, sesjon og baseklasse
- Brukes til å opprette tabeller fra modeller

#### `crud/`

- Inneholder CRUD-funksjoner for:
  - `users.py`: Opprett, hent, oppdater, slett brukere
  - `songs.py`: Operasjoner for sanger og artister
  - `playlists.py`: Håndtering av spillelister og sanger i dem
  - `subscriptions.py`: Opprett og administrer abonnement

#### `models/`

- Python-klasser som representerer tabeller i databasen
- Eksempler:
  - `users.py` (inkl. relasjoner til `account_types`, `subscriptions`, `listening_history`)
  - `songs.py` (inkl. relasjon til `artists` og `listening_history`)
  - `playlists.py`, `playlist_songs.py`
  - `listening_history.py`, `subscription.py`, `account_types.py`, `artists.py`

---

### 3. 📃 App-filer

#### `main.py`

- Streamlit-GUI som lar brukeren utføre CRUD-operasjoner
- Meny for: Brukere, Sanger, Spillelister, Statistikk
- Dynamisk skjema for input og visning av data

#### `api.py`

- Knytte sammen `CRUD` og `models`
- Returnerer data fra tabellene til GUI

#### `visualizations.py`

- Bruker SQL og ORM til å hente og visualisere:
  - Mest spilte sanger (top 10)
  - Fordeling av abonnementstyper
- Bruker `Plotly` for å lage interaktive grafer

---

## Fremtidige steg

### 1. 📊 Forbedre database

- Legg til flere `CHECK`-begrensninger og indekser
- Lag backup-script og importfunksjon for data

### 2. 🤖 Python-utvikling

- Legg til flere API-funksjoner (f.eks. brukerspesifikk aktivitet)
- Bedre feilhåndtering og logging

### 3. 🚩 API-utvikling

- Utvid `api.py` med flere tabeller
- Legg til filtrering, sortering og paginering

### 4. 📊 Visualisering

- Bruk Dashboards (eks: Streamlit tabs eller Plotly Dash)
- Eksportfunksjon (CSV, Excel)

### 5. 📖 Dokumentasjon

- Generer automatisk dokumentasjon med `pdoc` eller Swagger
- Forklar arkitektur og datamodell

---

## Vurdering av prosjektet per nå

| Komponent | Status | Kommentar |
|----------|--------|-----------|
| Database | ✅ | Strukturert, normalisert, komplett |
| Backend  | ✅ | CRUD-funksjoner og modeller på plass |
| GUI      | ✅ | Streamlit med dynamiske skjema |
| Visualisering | ✅ | Interaktive grafer fra real-time data |
| Dokumentasjon | ✅ | README under utvikling, godt grunnlag |

---

## Konklusjon

Prosjektet er ryddig strukturert, og det er god sammenheng mellom database, modeller og GUI. Med den siste justeringen (overgang fra `user_type` til `account_type_id`) er alle strukturelle avvik mellom modell og database rettet opp.

Du har et sterkt fundament for innlevering eller videreutvikling.

---

## 🌟 Bonus: Hva du får hjelp med videre

### 1. README.md generert (denne teksten)

### 2. EER-diagram:

- Vi lager et diagram for deg i Draw.io-format eller som bilde basert på `init_db.sql`

### 3. Testing

- Jeg hjelper deg gjerne med en `test_api.py` som bruker `pytest` for å teste alle CRUD-funksjoner automatisk

Vil du jeg starter med ⊕ EER-diagram eller ⊕ testing først?

