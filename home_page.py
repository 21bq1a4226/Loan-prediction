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
        background-image: url('https://www.shutterstock.com/image-photo/child-boy-using-tablet-looking-600nw-2225757071.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.5);
        background-blend-mode: overlay;
    }
    </style>
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
