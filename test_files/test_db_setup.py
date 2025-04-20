import os
from app.backend.db import engine
from sqlalchemy import text

def run_seed_data():
    # Bygg absolutt sti til seed_data.sql
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    seed_file_path = os.path.join(base_dir, "app", "database", "seed_data.sql")

    with engine.connect() as conn:
        with open(seed_file_path, "r") as file:
            sql_commands = file.read()
            conn.execute(text(sql_commands))
        conn.commit()

if __name__ == "__main__":
    run_seed_data()
    print("✅ Seed-data ble lagt inn i databasen.")