import streamlit as st

st.set_page_config(layout="wide")

header_col1, header_col2 = st.columns(2)

with header_col1:
    st.image("images/photo.png", width=400)

with header_col2:
    st.title("Motaal Ahmed")
    content = """
    Hi! I am Motaal. I am a software developer, technology enthusiast and
    a cyber security analyst. I have been working with various technologies for over a decade
    now. I graduated in 2013 with a bachelor's degree in Computer Science from
    the Vellore Institute of Technology, India. I have co-founded few IT companies mainly dealing
    with networking and server management.
    """
    st.info(content)
