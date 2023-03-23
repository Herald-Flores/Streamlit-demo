import streamlit as st

st.set_page_config(page_title="Boombit Insights", page_icon=":sparkles:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("assets/style.css")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, Everyone :purple_heart:")
    st.title("Python - Boombit Insights EP 4!")
    st.write(
        "Python is a great programming language to learn in 2023, is a versatile language with many applications in the software development industry."
    )
    st.write("[Learn More >](https://docs.streamlit.io/)")
    st.write("##")


# ---- About Me ----
with st.container():
    st.write("---")
    st.write("##")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            - I'm happily married :couple:
            - I have 2 Dogs :dog: :dog:
            - I'm working at Boombit Agency 🚀
            - I'm based in Nicaragua 🌍
            - I'm a Web Developer and Talent Acquisition Specialist :star2:
            - I am a person who is always looking for something new to learn and share. :boom:
            """
        )
    with right_column:
        st.image( 
            "https://github.com/Herald-Flores/Herald-Flores/raw/dev/assets/herald-flores.png", caption='Herald Flores'
        )
