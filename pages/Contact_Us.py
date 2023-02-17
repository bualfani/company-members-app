import streamlit as st
import pandas
from send_email import send_email

st.set_page_config(layout="wide" )

with st.form(key='form', clear_on_submit=True):
    user_email = st.text_input("Your Email Address")
    user_topic = st.selectbox("What topic do you want to discuss?", pandas.read_csv('topics.csv'))
    raw_message = st.text_area('Text')
    user_message = f"""\
Subject: {user_email}

From: {user_email}
Topic: {user_topic}
{raw_message}
"""

    button = st.form_submit_button("Send")

    if button:
        send_email(user_message)
        st.info("Email Sent Successfully")