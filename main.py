import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sesugh Iortsor")
    content = '''
    Hi, I am Sesugh! I am a python programmer. I graduated in 2024 with a BSc in Economics from University of Abuja
    in Abuja, Nigeria. I have worked on various python projects, from little projects to main scale projects. 
    '''
    st.info(content)
