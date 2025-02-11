import streamlit as st
from db_manager import validate_user

def login_page():
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://img.freepik.com/premium-photo/hand-holding-plant-that-grow-coins-investment-concept_693425-2891.jpg?w=1060');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: rgba(255, 255, 255, 0.6); /* Add a semi-transparent overlay */
            background-blend-mode: overlay; /* Blend the image with the overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Center the login form using Streamlit form layout
    with st.form(key="login_form"):
        # Title
        st.title("Login Page")

        # Email and Password inputs
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # Submit button inside the form
        login_button = st.form_submit_button("Login")

        # Handling form submission
        if login_button:
            user = validate_user(email, password)
            if user:
                # Set session state to user_home and store user details
                st.session_state["page"] = "user_home"
                st.session_state["user"] = user  # Store user info (e.g., name, email)
                st.session_state["user_tab"] = "Loan Page"  # Default tab after login
                st.experimental_rerun()
            else:
                st.error("Invalid Email or Password!")
