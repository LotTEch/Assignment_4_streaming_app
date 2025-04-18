# layout/sidebar.py
import streamlit as st

def show_sidebar():
    st.sidebar.title("🎛️ Kontrollpanel")

    st.sidebar.markdown("### Navigasjon")
    st.session_state["valgt_view"] = st.sidebar.selectbox(
        "Gå til seksjon",
        ["Brukere", "Sanger", "Sammenlign", "Tabellvisning"]
    )

    st.sidebar.markdown("### CRUD-handlinger")
    if st.sidebar.button("➕ Opprett ny post"):
        st.session_state["crud_action"] = "create"
    if st.sidebar.button("✏️ Endre valgt post"):
        st.session_state["crud_action"] = "edit"
    if st.sidebar.button("🗑️ Slett valgt post"):
        st.session_state["crud_action"] = "delete"
    