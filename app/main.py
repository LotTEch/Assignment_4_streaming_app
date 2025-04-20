"""
main.py – Streamlit GUI for musikkstrømmetjenesten
Støtter CRUD for brukere og sanger + visualisering av data fra databasen
"""

import streamlit as st
import app.backend.api as api
import app.visualizations as vis

# ============================
# HOVEDTITTEL
# ============================
st.set_page_config(page_title="Musikkadmin", layout="wide")
st.title("🎵 Musikkstrømmetjeneste – Adminverktøy")

# ============================
# SIDEBAR
# ============================
section = st.sidebar.radio("Navigasjon", ["Brukere", "Sanger", "Statistikk"])

# ============================
# BRUKERADMINISTRASJON
# ============================
import re  # For e-postvalidering

if section == "Brukere":
    crud_action = st.sidebar.selectbox("Velg operasjon", ["Opprett", "Les", "Oppdater", "Slett"])

    if crud_action == "Opprett":
        st.header("➕ Opprett ny bruker")
        first_name = st.text_input("Fornavn")
        last_name = st.text_input("Etternavn")
        email = st.text_input("E-post", help="Må være gyldig format")
        account_types = api.get_account_types()  # Hent tilgjengelige kontotyper
        account_type_map = {atype.name: atype.id for atype in account_types}
        account_type_name = st.selectbox("Kontotype", list(account_type_map.keys()))

        if st.button("Opprett bruker"):
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("❌ Ugyldig e-postadresse.")
            else:
                data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "account_type_id": account_type_map[account_type_name]
                }
                api.create_user(data)
                st.success(f"✅ Bruker {first_name} {last_name} ble opprettet.")

    elif crud_action == "Les":
        st.header("📄 Alle brukere")
        users = api.get_users()
        for u in users:
            st.write(f"{u.id}: {u.first_name} {u.last_name} – {u.email} ({u.user_type})")

    elif crud_action == "Oppdater":
        st.header("✏️ Oppdater bruker")
        user_id = st.number_input("Bruker-ID", min_value=1)
        first_name = st.text_input("Nytt fornavn")
        last_name = st.text_input("Nytt etternavn")
        email = st.text_input("Ny e-post")
        user_type = st.selectbox("Ny brukertype", ["free", "premium"])

        if st.button("Oppdater bruker"):
            result = api.update_user(user_id, {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "user_type": user_type
            })
            if result:
                st.success("✅ Oppdatert!")
            else:
                st.error("❌ Fant ikke bruker")

    elif crud_action == "Slett":
        st.header("🗑️ Slett bruker")
        user_id = st.number_input("Bruker-ID", min_value=1)
        if st.button("Slett bruker"):
            if api.delete_user(user_id):
                st.success("🧹 Bruker slettet")
            else:
                st.warning("Bruker ikke funnet")

# ============================
# SANGADMINISTRASJON
# ============================
if section == "Sanger":
    crud_action = st.sidebar.selectbox("Velg operasjon", ["Opprett", "Les", "Oppdater", "Slett"])

    if crud_action == "Opprett":
        st.header("➕ Legg til ny artist")
        name = st.text_input("Navn")
        genre = st.text_input("Sjanger")
        country = st.text_input("Land")

        if st.button("Opprett artist"):
            data = {"name": name, "genre": genre, "country": country}
            api.create_artist(data)
            st.success(f"✅ Artist '{name}' ble opprettet!")

    elif crud_action == "Les":
        st.header("🎵 Alle artister")
        artists = api.get_artists()
        for artist in artists:
            st.write(f"{artist.id}: {artist.name} – {artist.genre}, {artist.country}")

    elif crud_action == "Oppdater":
        st.header("✏️ Oppdater artist")
        artist_id = st.number_input("Artist-ID", min_value=1)
        name = st.text_input("Nytt navn")
        genre = st.text_input("Ny sjanger")
        country = st.text_input("Nytt land")

        if st.button("Oppdater artist"):
            data = {"name": name, "genre": genre, "country": country}
            api.update_artist(artist_id, data)
            st.success("✅ Artist oppdatert!")

    elif crud_action == "Slett":
        st.header("🗑️ Slett artist")
        artist_id = st.number_input("Artist-ID", min_value=1)
        if st.button("Slett artist"):
            if api.delete_artist(artist_id):
                st.success("🧹 Artist slettet")
            else:
                st.warning("Artist ikke funnet")
# ============================
# VISUALISERINGER
# ============================
elif section == "Statistikk":
    st.header("📊 Statistikk og visualisering")

    # Velg visualiseringstype
    chart_type = st.selectbox("Velg visualisering", [
        "Mest spilte sanger", "Abonnementstyper"
    ])

    if chart_type == "Mest spilte sanger":
        vis.plot_most_played()

    elif chart_type == "Abonnementstyper":
        vis.subscription_distribution()
