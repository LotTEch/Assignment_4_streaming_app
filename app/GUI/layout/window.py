# layout/window.py
import streamlit as st
from layout.sidebar import show_sidebar
from layout.views import show_view

def init_layout():
    st.set_page_config(layout="wide")

    show_sidebar()  # Sidebar med valg
    show_view()     # Hovedvindu basert på valg
