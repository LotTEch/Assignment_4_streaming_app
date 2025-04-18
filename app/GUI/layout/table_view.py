# GUI/view/table_view.py

import pandas as pd
from awesome_table import AwesomeTable
from awesome_table.column import Column, ColumnDType
import streamlit as st

def show():
    st.title("🎧 Brukeroversikt")

    # Dummy data – bytt ut med data fra databasen senere
    data = [
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "subscription": "Premium",
            "joined": "2023-01-01",
            "_url.social": "https://twitter.com/alice",
            "_url.avatar": "https://avatars.githubusercontent.com/u/1"
        },
        {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com",
            "subscription": "Free",
            "joined": "2023-02-01",
            "_url.social": "https://twitter.com/bob",
            "_url.avatar": "https://avatars.githubusercontent.com/u/2"
        }
    ]

    df = pd.json_normalize(data)

    columns = [
        Column(name="id", label="ID"),
        Column(name="name", label="Navn"),
        Column(name="email", label="E-post"),
        Column(name="subscription", label="Abonnementstype"),
        Column(name="joined", label="Registrert"),
        Column(name="_url.avatar", label="Avatar", dtype=ColumnDType.IMAGE),
        Column(name="_url.social", label="Sosial", dtype=ColumnDType.ICONBUTTON, icon="fa-brands fa-twitter"),
    ]

    AwesomeTable(
        df,
        columns=columns,
        show_order=True,
        show_search=True,
        show_search_order_in_sidebar=True
    )
