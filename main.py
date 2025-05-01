import streamlit as st
import os
import pandas as pd

path_image = os.path.join(os.getcwd(),"data","images")
path_data = os.path.join(os.getcwd(),"data")
path_dp = os.path.join(path_image,"photo.jpg")

st.set_page_config(page_title = "@asheshjyoti",layout="wide")

col1, col2 = st.columns([1,3])
with col1:
    st.image(path_dp, use_container_width = True)

with col2:
    bio = """
    ### Hi, I'm Ashesh Jyoti Majumdar

I'm a curious and driven B.Tech undergraduate in Artificial Intelligence & Machine Learning. I enjoy building thoughtful tech solutions and continuously learning across domains like computer vision, machine learning, and full-stack development.

I've participated in multiple hackathons and love collaborating on meaningful projects. You’ll often find me exploring new tools, tinkering with code, or diving into open-source.

**Connect with me:**  
[GitHub](https://github.com/asheshjyotii) | [LinkedIn](https://www.linkedin.com/in/asheshjyoti/)

    """
    st.title("Ashesh Jyoti Majumdar | Portfolio")
    st.info(bio)

_,col,_ = st.columns([1,3,1])

st.markdown("---")
st.header("🛠️ Below are some of the projects I built!")

# creating the projects section
df = pd.read_csv(os.path.join(path_data,"data.csv"))
df.reset_index(inplace = True)
l = len(df)//2+1 # a variable which is used to divide the data into two parts


col3, _,col4 = st.columns([3,1,3])

for index, rows in df.iterrows():
    title = rows["Title"]
    desc = rows["Description"]
    url = rows["URL"]
    img = rows["Image"]
    if (index+1)%2 != 0:
        with col3:
            st.header(title)
            st.write(desc)
            st.image(os.path.join(path_image,img))
            st.info(url)
    else:
        with col4:
            st.header(title)
            st.write(desc)
            st.image(os.path.join(path_image, img))

