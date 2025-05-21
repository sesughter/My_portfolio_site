import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_input = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
subject: New email from {user_input}

from: {user_input}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("your email was sent successfully")
