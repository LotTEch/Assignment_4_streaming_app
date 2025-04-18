# app/gui/view/user_form.py

import streamlit as st

def show():
    st.title("👤 Brukeradministrasjon")

    action = st.session_state.get("crud_action", None)

    if action == "create":
        st.info("Opprett en ny bruker:")
        with st.form("create_user_form"):
            name = st.text_input("Navn")
            email = st.text_input("E-post")
            submitted = st.form_submit_button("Opprett")
            if submitted:
                st.success(f"✅ Bruker '{name}' opprettet! (Simulert)")
                st.session_state["crud_action"] = None  # Tilbakestill

    elif action == "edit":
        st.warning("✏️ Redigeringsmodus (ikke implementert)")
        st.session_state["crud_action"] = None

    elif action == "delete":
        st.error("🗑️ Slettemodus (ikke implementert)")
        st.session_state["crud_action"] = None

    st.subheader("📋 Eksisterende brukere")
    st.write("💡 Her kunne du listet brukere fra databasen.")
