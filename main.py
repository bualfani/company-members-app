import streamlit as st
import pandas

st.set_page_config(layout="wide" )

st.sidebar.title('Home')
st.sidebar.title("Contact Us")

st.title("The Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(content)

st.subheader("Our Team")

df = pandas.read_csv('data1.csv', sep=',')

col1, col2, col3, col4, col5 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        st.header(row['first name'] + ' ' + row['last name'])
        st.write(row['role'])
        st.image("image1/" + row['image'])


with col3:
    for index, row in df[4:8].iterrows():
        st.header(row['first name'] + ' ' + row['last name'])
        st.write(row['role'])
        st.image("image1/" + row['image'])


with col5:
    for index, row in df[8:12].iterrows():
        st.header(row['first name'] + ' ' + row['last name'])
        st.write(row['role'])
        st.image("image1/" + row['image'])
