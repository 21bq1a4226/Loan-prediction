import streamlit as st
import random
from db_manager import valid_user, update_otp, get_otp, update_password, fetch_password
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_alert_email(to_email, subject, message, from_email, from_password):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        pass

def about_page():
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://deepsense.ai/wp-content/smush-webp/2024/11/Wait-so-loans-need-to-be-repaid-The-home-credit-risk-prediction-competition-on-Kaggle-1024x303.jpg.webp');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: rgba(255, 255, 255, 0.5); /* Add a semi-transparent overlay */
            background-blend-mode: overlay; /* Blend the image with the overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize session states
    if "reset_step" not in st.session_state:
        st.session_state["reset_step"] = "email_input"
    if "reset_email" not in st.session_state:
        st.session_state["reset_email"] = None
    if "otp_verified" not in st.session_state:
        st.session_state["otp_verified"] = False

    # Step 1: Email Input
    if st.session_state["reset_step"] == "email_input":
        col1,col2,col3=st.columns([1,4,1])
        with col2.form(key="forgot_password_form"):
            st.title("Forgot Password 🔒")
            email = st.text_input("Enter your email")
            if st.form_submit_button("Submit", type="primary"):
                if valid_user(email):
                    otp = random.randint(1000, 9999)
                    to_email=email
                    subject = "OTP for Loan Prediction System"
                    body = f"Hello,\n\nYour OTP is {otp}. Please enter this OTP to reset your password.\n\nRegards,\nTeam Loan Prediction System"
                    from_email = 'loan95941@gmail.com'
                    from_password = 'xmqltsuqtyqjlbdd'  
                    # Send the alert email
                    send_alert_email(to_email, subject, body, from_email, from_password)
                    update_otp(email, otp)
                    st.session_state["reset_email"] = email
                    st.session_state["reset_step"] = "otp_verification"
                    st.experimental_rerun()
                else:
                    st.error("Invalid Email!")

    # Step 2: OTP Verification
    elif st.session_state["reset_step"] == "otp_verification":
        col1,col2,col3=st.columns([1,3,1])
        with col2.form(key="otp_form"):
            st.title("Verify OTP 🔑")
            otp_input = st.text_input("Enter OTP")
            if st.form_submit_button("Verify OTP", type="primary"):
                stored_otp = get_otp(st.session_state["reset_email"])[0]
                st.write(stored_otp)
                if int(otp_input) == int(stored_otp):
                    st.session_state["otp_verified"] = True
                    st.session_state["reset_step"] = "password_reset"
                    st.experimental_rerun()
                else:
                    st.error("Invalid OTP!")

    # Step 3: Password Reset
    elif st.session_state["reset_step"] == "password_reset":
        col1,col2,col3=st.columns([1,3,1])
        with col2.form(key="reset_password_form"):
            st.title("Reset Password 🔐")
            new_password = st.text_input("Enter New Password", type="password")
            confirm_password = st.text_input("Confirm New Password", type="password")
            old_password = fetch_password(st.session_state["reset_email"])

            if st.form_submit_button("Update Password", type="primary"):
                if new_password == old_password:
                    st.error("New password cannot be the same as the old password!")
                elif new_password == confirm_password:
                    update_password(st.session_state["reset_email"], new_password)
                    st.success("Password Updated Successfully! ✅")
                    st.session_state["reset_step"] = "email_input"
                else:
                    st.error("Passwords do not match!")
