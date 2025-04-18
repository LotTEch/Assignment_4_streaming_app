import streamlit as st
from app.gui.view.user_form import show as user_view
from app.gui.view.compare_view import show as compare_view
from app.gui.layout.table_view import show as table_view

def show_view():
    """
    Viser hovedvinduet basert på brukerens valg i sidepanelet.
    """
    valgt = st.session_state.get("valgt_view", "Brukere")

    if valgt == "Brukere":
        user_view()
    elif valgt == "Sanger":
        st.warning("Sangvisning er ikke implementert ennå.")
    #elif valgt == "Sammenlign":
        #compare_view()
    elif valgt == "Tabellvisning":
        table_view()
    else:
        st.warning("Ingen visning valgt.")