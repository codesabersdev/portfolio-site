import streamlit as st
import pandas

st.set_page_config(layout="wide")

header_col1, head_empty, header_col2 = st.columns([1.5, 0.5, 1.5])

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

st.markdown('#')

content_1 = """
<h5><b>Below you can find some of the apps I have built in Python. Feel free to contact me!</b></h5>
"""
st.write(content_1, unsafe_allow_html=True)
st.markdown('###')

showcase_col1, empty_col, showcase_col2 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with showcase_col1:
    for index, row in df[::2].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.link_button(label="Source Code", url=row["url"])
        st.markdown('#')

with showcase_col2:
    for index, row in df[1::2].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.link_button(label="Source Code", url=row["url"])
        st.markdown('#')
