import streamlit as st
import pandas
#pandas to use images  and csv file in tabular format

col1,col2=st.columns(2)#(2) space btw two cols

with col1:
    st.image("images/profile_photo.jpg",width=213)

with col2:
    st.title(":blue[Raghvendra Shetty]")
    content="""I finally got around to starting this Python project course I bought on Udemy. It's pretty tough, but it's also really cool and inspiring!"""
    st.write(content)

content2=""" Below are the upcoming projects from the course 🧑🏾‍💻"""

st.info(content2,icon="📢")

#from here we are allocating projects in col3 and col4
col3,emp_col, col4 =st.columns([2,1,2])

df=pandas.read_csv("data.csv",sep=";")
with col3:
    for i,row in df[:7].iterrows():
        st.header(row["title"])#title
        st.image("images/" + row["image"])#image
        st.write(row["description"])#dis


with col4:
    for i,row in df[7:14].iterrows():
      st.header(row["title"])
      st.image("images/" + row["image"])
      st.write(row["description"])


