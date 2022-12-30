import streamlit as st
import pandas

# Configures page layout to Wide
st.set_page_config(layout="wide")

# Creates two columns for name,description and image
col1, col2 = st.columns(2)

with col1:
    st.image("images/img.png")

with col2:
    st.title("Aryan Akhilesh")
    content = """Hi,I'm Aryan! I'm currently a 2nd year student at McGill University.
                 I'm pursuing a Bachelor of Science in Software Engineering with a 
                 minor in Mathematics."""
    st.info(content)

st.write("""<h5> Below you can find some of the apps that I have built in python.
            Feel free to contact me!</h5>""", unsafe_allow_html=True)

col3, col4 = st.columns(2)

# Creates a data frame of the data. We use ";" as the seperator
df = pandas.read_csv("data.csv", sep=";")

# We iterate over the data frame's rows as index, row since
# iterrows uses (index,series) pair
# We then display the first 10 rows of the "title" column in col3
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
