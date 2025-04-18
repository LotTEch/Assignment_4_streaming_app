# layout/views.py
import streamlit as st
from GUI.view import user_view, song_view, compare_view, table_view

def show_view():
    valgt = st.session_state.get("valgt_view", "Brukere")

    if valgt == "Brukere":
        user_view.show()
    elif valgt == "Sanger":
        song_view.show()
    elif valgt == "Sammenlign":
        compare_view.show()
    elif valgt == "Tabellvisning":
        table_view.show()
    else:
        st.warning("Ingen visning valgt.")
