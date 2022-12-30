import streamlit as st
from send_email import send_email

st.header("Contact Me")

# Creates a webform
with st.form(key="form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Enter Your Message")
    message = f'''\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
'''
    submit_button = st.form_submit_button()
    if submit_button:
        send_email(message)
        st.info("Your Email was sent successfully!")
