import streamlit as st

# Setting page layout to wide
st.set_page_config(layout="wide", page_title="Dave's Letter", page_icon="images/mario.png")

col3, col4 = st.columns([2,4])

with col3:
    st.image("images/mario.png", caption="Toad")

with col4:
    st.markdown("<h1 style='text-align: center;'>¿Como juzgar el éxito?</h1>", unsafe_allow_html=True)
    with open("letter.txt", 'r', encoding="utf-8") as file:
        carta = file.read()

    st.warning(carta)

    st.markdown("""
    <a href="https://www.flaticon.com/free-icons/super-mario" title="super mario icons">
        Super Mario icons created by Freepik - Flaticon
    </a>
    """, unsafe_allow_html=True)