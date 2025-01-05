import streamlit as st

def home_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Loan Prediction System</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Center the image
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://defisolutions.com/wp-content/uploads/selected-1-1.png" style="max-width: 50%;">
        </div>
        """,
        unsafe_allow_html=True
    )
