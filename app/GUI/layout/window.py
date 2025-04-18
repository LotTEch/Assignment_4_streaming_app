import streamlit as st
from app.gui.layout.sidebar import show_sidebar
from app.gui.layout.views import show_view

def init_layout():
    """
    Initialiserer layouten for Streamlit-applikasjonen.
    """
    st.set_page_config(layout="wide")  # Sett bred layout for applikasjonen

    show_sidebar()  # Viser sidepanelet
    show_view()     # Viser hovedvinduet basert på brukerens valg