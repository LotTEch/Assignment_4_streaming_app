# gui/view/compare_view.py
import streamlit as st
from app.backend.api import get_users, get_songs

def show():
    st.title("Sammenlign Brukere og Sanger")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Brukere")
        users = get_users()
        for u in users:
            st.write(f"{u['first_name']} {u['last_name']}")

    with col2:
        st.subheader("Sanger")
        songs = get_songs()
        for s in songs:
            st.write(f"{s['title']} ({s['genre']})")
