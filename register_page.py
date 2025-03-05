import streamlit as st
import re
from db_manager import register_user

def register_page():
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://www.bluebricks.com.my/wp-content/uploads/2023/05/image2-2-1024x576.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color:rgba(255,255,255,0.6);
            background-blend-mode: overlay;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Center the registration form container using Streamlit form layout
    with st.form(key="register_form"):
        # Title
        st.title("Register Page")
        col1,col2,col3,col4=st.columns(4)
        # Form Fields
        name = col1.text_input("Name")
        email = col2.text_input("Email")
        gender = col3.selectbox('Choose Gender',['Male','Female','Other'])
        weight = col4.number_input('Enter the weight (kg)',min_value=10)
        hereditary_disease = col1.selectbox('Do you have any hereditary disease?',['NoDisease', 'Epilepsy', 'EyeDisease', 'Alzheimer', 'Arthritis',
       'HeartDisease', 'Diabetes', 'Cancer', 'High BP', 'Obesity'])
        age = col2.slider('Enter the age',min_value=1,max_value=100,value=18)
        smoking = col3.selectbox('Do you smoke?',['Yes','No'])
        regular_bp_level = col4.number_input('Enter the regular blood pressure level',min_value=120)
        col1,col2,col3,col4=st.columns(4)
        diabetes = col1.selectbox('Do you have diabetes?',['Yes','No'])
        regular_exercise = col2.selectbox('Do you do regular exercise?',['Yes','No'])
        marital_status = col3.selectbox('Choose Marital Status',['Married','Unmarried','Divorced','Widowed'])
        no_of_dependents = col4.number_input('Enter the number of dependents',min_value=0)
        education = col1.selectbox('Choose Education',['Graduate','Non Graduate'])
        employment = col2.selectbox('Choose Employment',['Salaried','Self-Employed', 'Freelancer', 'Student', 'Unemployed'])
        property_status = col3.selectbox('Choose Property Status',['Rural','Urban','Semi Urban'])
        credit_score = col4.number_input('Enter the credit score',min_value=0)
        col1,col2,col3,col4=st.columns(4)
        credit_history = col1.selectbox('Choose Credit History',['Good','Bad','Average'])
        annual_income = col2.number_input('Enter the annual income (K)',min_value=0)
        co_applicant_annual_income = col3.number_input('Enter the co-applicant annual income (K)',min_value=0)
        loan_amount = col4.number_input('Enter the loan amount (K)',min_value=0)
        loan_duration = col1.number_input('Enter the loan duration (years)',min_value=1,step=1)
        existing_loan = col2.selectbox('Choose Existing Loan',['Yes','No'])
        existing_loan_amount = col3.number_input('Enter the existing loan amount',min_value=0)
        existing_loan_duration = col4.number_input('Enter the existing loan duration (years)',min_value=1,step=1)
        col1,col2,col3,col4=st.columns(4)
        existing_loan_type=col1.selectbox('Choose Existing Loan Type',['Home Loan','Personal Loan','Car Loan','Bank Loan','Others'])
        language = col2.selectbox("Preferred Language", ["English", "Telugu", "Hindi"])
        password = col3.text_input("Password", type="password")
        retype_password = col4.text_input("Retype Password", type="password")
        otp=0
        

        # Submit Button inside the form
        register_button = st.form_submit_button("Register",type='primary')

        # Handling form submission
        if register_button and name and email and password and retype_password and gender and weight and hereditary_disease and age and smoking and regular_bp_level and diabetes and regular_exercise and marital_status and no_of_dependents and education and employment and property_status and credit_score and credit_history and annual_income and co_applicant_annual_income and loan_amount and loan_duration and existing_loan and existing_loan_amount and existing_loan_duration and existing_loan_type and language:
            # Validate email using regex
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, email):
                st.error("Invalid Email!")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters long!")
            elif password != retype_password:
                st.error("Passwords do not match!")
            else:
                if register_user(name, email,gender,weight,hereditary_disease,age,smoking,regular_bp_level,diabetes,regular_exercise,marital_status,no_of_dependents,education,employment,property_status,credit_score,credit_history,annual_income,co_applicant_annual_income,loan_amount,loan_duration,existing_loan,existing_loan_amount,existing_loan_duration,existing_loan_type,language,otp,password):
                    st.success("Registration Successful!")
                else:
                    st.error("Email already exists!")
        else:
            st.warning("All fields are required!")
