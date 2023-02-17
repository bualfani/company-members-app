import streamlit as st
import pandas

st.set_page_config(layout="wide" )

with st.form('form1', clear_on_submit=True):
    st.text_input("Your Email Address")
    st.selectbox("What topic do you want to discuss?", pandas.read_csv('topics.csv'))
    st.text_area("Text")

    st.form_submit_button("Send")