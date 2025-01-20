import streamlit as st

def home_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>LOAN PREDICTION SYSTEM</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://i.pinimg.com/736x/66/90/34/669034397b1a8ff259af8867c94e0fbd.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
