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

    # Center the image
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://img.freepik.com/free-vector/premium-cash-reward-bonus-work-done-best-employee-rewarding-promotion-order-efficiency-stimulation-boss-subordinate-cartoon-characters_335657-2984.jpg" style="max-width: 40%;">
        </div>
        """,
        unsafe_allow_html=True
    )
