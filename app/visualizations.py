"""
visualizations.py – Henter og visualiserer aggregerte data fra databasen.
Denne filen brukes i GUI for å vise innsikt, f.eks. mest spilte sanger, brukerfordeling m.m.
"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sqlalchemy.sql import text
from app.backend.db import SessionLocal

def get_most_played_songs():
    """
    Henter topp 10 mest spilte sanger via lagret SQL-prosedyre.
    """
    with SessionLocal() as session:
        result = session.execute(text("SELECT * FROM get_most_played_songs()")).fetchall()
        return result

def plot_most_played():
    """
    Plotter topp 10 mest spilte sanger i bar chart.
    """
    st.header("📊 Mest spilte sanger")

    data = get_most_played_songs()
    if not data:
        st.warning("Ingen lyttedata tilgjengelig.")
        return

    df = pd.DataFrame(data, columns=["song_id", "play_count"])
    st.bar_chart(df.set_index("song_id"))

def subscription_distribution():
    """
    Viser fordeling av abonnementstyper.
    """
    with SessionLocal() as session:
        query = """
        SELECT type, COUNT(*) as count
        FROM subscriptions
        GROUP BY type
        """
        result = session.execute(text(query)).fetchall()
        df = pd.DataFrame(result, columns=["type", "count"])
        st.header("📈 Abonnementstyper")
        st.bar_chart(df.set_index("type"))
