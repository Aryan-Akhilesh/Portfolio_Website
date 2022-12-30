import streamlit as st

st.set_page_config(layout="wide")

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
