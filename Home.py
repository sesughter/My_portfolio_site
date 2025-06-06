import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, col3, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sesugh Iortsor")
    content = '''
    Hi, I am Sesugh! I am a python programmer. I graduated in 2024 with a BSc in Economics from University of Abuja
    in Abuja, Nigeria. I have worked on various python projects, from little projects to main scale projects. 
    '''
    st.info(content)

content2 = """
Below you can find some of the apps I have built in python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({row['url']})")
