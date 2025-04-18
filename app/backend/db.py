"""
Sentral del av oppsettet for å koble applikasjonen din til databasen ved hjelp 
av SQLAlchemy, som er en populær ORM (Object-Relational Mapper) i Python.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.backend.config import DATABASE_URL

# Opprett database-tilkobling
engine = create_engine(DATABASE_URL)
# engine: Dette er selve tilkoblingen til databasen. Den brukes av SQLAlchemy til å kommunisere med databasen.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
SessionLocal: En fabrikk for å opprette database-økter. Hver økt brukes til å utføre spørringer og transaksjoner mot databasen.
autocommit=False: Transaksjoner må eksplisitt committes.
autoflush=False: Endringer blir ikke automatisk sendt til databasen før du committer.
"""

Base = declarative_base()
# Base: Dette er grunnlaget for alle database-modellene dine. Alle tabeller i databasen defineres som klasser som arver fra Base.

def init_db():
    """
    init_db: Funksjonen som oppretter alle tabellene i databasen basert på modellene som er definert.
    import backend.models.users: Importerer alle databasemodellene. Dette må gjøres for å sikre at de blir registrert med SQLAlchemy.
    Base.metadata.create_all(bind=engine): Oppretter alle tabellene i databasen hvis de ikke allerede eksisterer.
    """
    import app.backend.models.users  # Importer alle modeller
    import app.backend.models.playlists  # Importer alle modeller
    import app.backend.models.songs  # Importer alle modeller
    import app.backend.models.subscription  # Importer alle modeller
    Base.metadata.create_all(bind=engine)