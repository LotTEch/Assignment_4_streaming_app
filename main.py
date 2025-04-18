import streamlit as st
from app.backend.db import SessionLocal
from app.backend.models.users import User

# Funksjon for å hente alle brukere
def get_users():
    with SessionLocal() as session:
        return session.query(User).all()

# Funksjon for å opprette en ny bruker
def create_user(first_name, last_name, email, user_type):
    with SessionLocal() as session:
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_type=user_type
        )
        session.add(new_user)
        session.commit()

# Funksjon for å oppdatere en bruker
def update_user(user_id, first_name, last_name, email, user_type):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.user_type = user_type
            session.commit()

# Funksjon for å slette en bruker
def delete_user(user_id):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()

# Streamlit GUI
st.title("Brukeradministrasjon")

# Velg CRUD-operasjon
operation = st.sidebar.selectbox("Velg operasjon", ["Opprett", "Les", "Oppdater", "Slett"])

if operation == "Opprett":
    st.header("Opprett en ny bruker")
    first_name = st.text_input("Fornavn")
    last_name = st.text_input("Etternavn")
    email = st.text_input("E-post")
    user_type = st.selectbox("Brukertype", ["free", "premium"])
    if st.button("Opprett"):
        create_user(first_name, last_name, email, user_type)
        st.success(f"Bruker {first_name} {last_name} opprettet!")

elif operation == "Les":
    st.header("Liste over brukere")
    users = get_users()
    for user in users:
        st.write(f"ID: {user.id}, Navn: {user.first_name} {user.last_name}, E-post: {user.email}, Type: {user.user_type}")

elif operation == "Oppdater":
    st.header("Oppdater en bruker")
    user_id = st.number_input("Bruker-ID", min_value=1, step=1)
    first_name = st.text_input("Nytt fornavn")
    last_name = st.text_input("Nytt etternavn")
    email = st.text_input("Ny e-post")
    user_type = st.selectbox("Ny brukertype", ["free", "premium"])
    if st.button("Oppdater"):
        update_user(user_id, first_name, last_name, email, user_type)
        st.success(f"Bruker med ID {user_id} oppdatert!")

elif operation == "Slett":
    st.header("Slett en bruker")
    user_id = st.number_input("Bruker-ID", min_value=1, step=1)
    if st.button("Slett"):
        delete_user(user_id)
        st.success(f"Bruker med ID {user_id} slettet!")