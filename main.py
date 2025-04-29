import streamlit as st
import os

path_image = os.path.join(os.getcwd(),"data","images")
path_dp = os.path.join(path_image,"photo.jpg")

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image(path_dp,width=250)

with col2:
    bio = """
    ### Hi, I'm Ashesh Jyoti Majumdar

I'm a curious and driven B.Tech undergraduate in Artificial Intelligence & Machine Learning. I enjoy building thoughtful tech solutions and continuously learning across domains like computer vision, machine learning, and full-stack development.

I've participated in multiple hackathons and love collaborating on meaningful projects. You’ll often find me exploring new tools, tinkering with code, or diving into open-source.

**Connect with me:**  
[GitHub](https://github.com/asheshjyotii) | [LinkedIn](https://www.linkedin.com/in/asheshjyoti/)

    """
    st.title("Ashesh Jyoti Majumdar")
    st.markdown(bio)

