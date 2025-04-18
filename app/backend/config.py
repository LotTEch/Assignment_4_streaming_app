from dotenv import load_dotenv
import os  # Legg til denne linjen for å bruke os.getenv()

# Last inn miljøvariabler fra .env-filen
load_dotenv()

# Hent databasekonfigurasjon fra miljøvariabler
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Sett opp database-URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"