import streamlit as st
import send_email

st.header("Let's get in touch!")

with st.form(key="contact_form"):

    name = st.text_input("Name")
    email = st.text_input("Email")
    query = st.selectbox("What's on your mind?",
                         ("Project Proposal", "Saying Hi!", "Complement/Feedback", "Something Else"))
    message = st.text_area("Message")
    submit = st.form_submit_button("Submit")

if submit:
    send_email.send_mail(email, name, query, message)
    st.info(f"{name}, thanks for getting in touch. I'll get back to you soon. Cya!")
