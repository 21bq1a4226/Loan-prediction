import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from db_manager import update_user,get_user_by_email
import pickle
import matplotlib.pyplot as plt
import joblib
import seaborn as sns
import random
def user_profile():
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://img.freepik.com/free-vector/futuristic-background-with-lines_23-2148487905.jpg?semt=ais_hybrid');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    # Extracting user data
    #name, email, gender, weight, hereditary_disease, age, smoking, regular_bp_level, diabetes, regular_exercise, marital_status, no_of_dependents, education, employment, property_status, credit_score, credit_history, annual_income, co_applicant_annual_income, loan_amount, loan_duration, existing_loan, existing_loan_amount, existing_loan_duration, existing_loan_type, language, password
    user_data = st.session_state.get('user', ['', 'Unknown', 'Unknown'])
    user_data=get_user_by_email(user_data[2])
    name = user_data[1]
    email = user_data[2]
    gender = user_data[3]
    weight = user_data[4]
    hereditary_disease = user_data[5]
    age=user_data[6]
    smoking=user_data[7]
    regular_bp_level=user_data[8]
    diabetes=user_data[9]
    regular_exercise=user_data[10]
    marital_status=user_data[11]
    no_of_dependents=user_data[12]
    education=user_data[13]
    employment=user_data[14]
    property_status=user_data[15]
    credit_score=user_data[16]
    credit_history=user_data[17]
    annual_income=user_data[18]
    co_applicant_annual_income=user_data[19]
    loan_amount=user_data[20]
    loan_duration=user_data[21]
    existing_loan=user_data[22]
    existing_loan_amount=user_data[23]
    existing_loan_duration=user_data[24]
    existing_loan_type=user_data[25]
    language=user_data[26]

    
    # General image link
    image_link = "https://static.vecteezy.com/system/resources/previews/043/987/923/non_2x/loan-papers-3d-icon-png.png"  # Replace with your image URL

    # CSS Styling
    profile_css = """
    <style>
        .profile-container {
            background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-jOCuD46_00GQu3qlaWE_lTjARY6wKVEUCKhK6k_m3XSL-91nl2Pg1lg1h633d3cG5K0&usqp=CAU');
            background-size: cover;
            background-position: center;
            padding: 60px;
            border-radius: 50px;
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
            max-width: 600px;
            margin: auto;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .profile-details {
            flex: 1;
        }
        .profile-header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
            color: red;
        }
        .profile-item {
            font-size: 18px;
            margin-bottom: 2px;
            color: #555;
        }
        .profile-image {
            bordwe-radius: 50px;
            margin-left: 20px;
            margin-bottom: 100px;
        }
        .profile-image img {
            border-radius: 50px;
            margin-top: 80px;
            max-width: 250px;
            max-height: 500px;
        }
    </style>
    """

    # HTML Structure
    profile_html = f"""
    <div class="profile-container">
        <div class="profile-details">
            <div class="profile-header">𝚄𝚜𝚎𝚛 𝙿𝚛𝚘𝚏𝚒𝚕𝚎</div>
            <div class="profile-item"><strong>𝕹𝖆𝖒𝖊:</strong> {name}</div>
            <div class="profile-item"><strong>𝕰𝖒𝖆𝖎𝖑:</strong> {email}</div>
            <div class="profile-item"><strong>𝕲𝖊𝖓𝖉𝖊𝖗:</strong> {gender}</div>
            <div class="profile-item"><strong>𝖂𝖊𝖎𝖌𝖍𝖙:</strong> {weight}</div>
            <div class="profile-item"><strong>𝕬𝖌𝖊:</strong> {age}</div>
            <div class="profile-item"><strong>𝕾𝖒𝖔𝖐𝖎𝖓𝖌:</strong> {smoking}</div>
            <div class="profile-item"><strong>𝕸𝖆𝖗𝖎𝖙𝖆𝖑 𝕾𝖙𝖆𝖙𝖚𝖘:</strong> {marital_status}</div>
            <div class="profile-item"><strong>𝕰𝖉𝖚𝖈𝖆𝖙𝖎𝖔𝖓:</strong> {education}</div>
            <div class="profile-item"><strong>𝕰𝖒𝖕𝖑𝖔𝖞𝖒𝖊𝖓𝖙:</strong> {employment}</div>
            <div class="profile-item"><strong>𝕮𝖗𝖊𝖉𝖎𝖙 𝕾𝖈𝖔𝖗𝖊:</strong> {credit_score}</div>
            <div class="profile-item"><strong>𝕬𝖓𝖓𝖚𝖆𝖑 𝕴𝖓𝖈𝖔𝖒𝖊:</strong> {annual_income}</div>
        </div>
        <div class="profile-image">
            <img src="{image_link}" alt="User Image">
        </div>
    </div>
    """

    # Display styled content
    st.markdown(profile_css + profile_html, unsafe_allow_html=True)

def loan_page():
    #display existing loan details from the user
    user_data = st.session_state.get('user', ['', 'Unknown', 'Unknown'])
    user_data=get_user_by_email(user_data[2])
    existing_loan=user_data[22]
    existing_loan_amount=user_data[23]*1000
    existing_loan_duration=user_data[24]
    existing_loan_type=user_data[25]
    #display the existing loan details in ui
    st.markdown(
    """
    <div style="text-align: center; padding: 5px; background-image: url('https://img.freepik.com/premium-vector/stock-market-investment-trading-graph-graphic-concept-suitable-financial-investment_258787-30.jpg?semt=ais_hybrid');
    background-size: cover; background-position: center; background-repeat: no-repeat;
                border-radius: 20px; border: 1.5px solid black; margin-bottom: 10px;">
        <p style="color: red; font-size: 30px;"><b>Existing Loan Details</b></p>
        <div style="display: flex; justify-content: space-around; padding: 10px; font-size: 18px;">
            <div style="flex: 1; padding: 10px;"><b> Loan Type:</b> {existing_loan_type}</div>
        </div>
        <div style="display: flex; justify-content: space-around; padding: 10px; font-size: 18px;">
            <div style="flex: 1; padding: 10px;"><b> Loan Amount:</b> {existing_loan_amount} INR</div>
            <div style="flex: 1; padding: 10px;"><b> Loan Duration:</b> {existing_loan_duration} years</div>
        </div>
    </div>
    """.format(
        existing_loan=existing_loan,
        existing_loan_amount=existing_loan_amount,
        existing_loan_duration=existing_loan_duration,
        existing_loan_type=existing_loan_type,
    ),
    unsafe_allow_html=True
    )
    loans=['Bank Loan','Home Loan','Vehicle Loan','Health insurance Loan','Personal Loan']
    bank_loan=0
    home_loan=0
    vehicle_loan=0
    health_insurance_loan=0
    personal_loan=0
    #health inputs are age, sex,weight,bmi,hereiditary disease,no of dependtss, smoking, city, bp,diabetes, regular exercise, job title
    age=user_data[6]
    sex = 0 if user_data[3] == 'Female' else 1
    weight=user_data[4]
    bmi=weight/((weight/100)**2)
    dic={'NoDisease':0, 'Epilepsy':1, 'EyeDisease':2, 'Alzheimer':3, 'Arthritis':4,
       'HeartDisease':5, 'Diabetes':6, 'Cancer':7, 'High BP':8, 'Obesity':9}
    hereditary_disease=dic[user_data[5]]
    no_of_dependents=user_data[12]
    smoking=1 if user_data[7]=='Yes' else 0
    city=0
    bp=user_data[8]
    diabetes=1 if user_data[9]=='Yes' else 0
    regular_exercise=1 if user_data[10]=='Yes' else 0
    val=[ 2, 16,  0, 10, 22, 12, 32, 13, 30, 33, 15, 28, 29,  5,  8,  6,  9,
       26,  1, 19, 34, 18,  4, 23, 20,  7, 31, 14,  3, 11, 24, 17, 25, 27,
       21]
    job_title=random.choice(val)
    model = joblib.load("Health Loan/health_insurance_model.pkl")
    input_data = pd.DataFrame([[
        age, sex, weight, bmi, hereditary_disease, no_of_dependents, smoking, city, bp, diabetes, regular_exercise, job_title
    ]])
    prediction = model.predict(input_data)
    health_insurance_loan=prediction[0]

    
    #inputs for home loan are Gender, Married, Dependents, Education, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area
    gender=1 if user_data[3] == 'Male' else 0
    married=0 if user_data[11]=='Unmarried' else 1
    dependents=user_data[12]
    education=1 if user_data[13]=='Graduate' else 0
    coapplicant_income=user_data[19]
    loan_amount=user_data[20]
    loan_amount_term=user_data[21]
    credit_history=1 if user_data[17]=='Good' else 0.5 if user_data[17]=='Average' else 0
    property_area=0 if user_data[15]=='Rural' else 2 if user_data[15]=='Urban' else 1
    model = joblib.load("Home Loan/home_loan_model.pkl")
    scaler = joblib.load("Home Loan/home_loan_scaler.pkl")
        # Convert categorical inputs
    user_df=[[gender,married, dependents,education,coapplicant_income,loan_amount, loan_amount_term
             , credit_history,property_area]]
    user_df_scaled = scaler.transform(user_df)
    # Make prediction
    prediction = model.predict(user_df_scaled)
    if prediction[0]==1:
        home_loan=1
    #inputs vehicle loan
    #gender, Existing Customer, Employment Profile, Age Income, Credit Score, Credit History Length,Number of Existing Loans,Loan Amount, Loan Tenure, LTV Ratio, Profile Score
    gender=1 if user_data[3]=='Male' else 0
    existing_customer=1 if user_data[22]=='Yes' else 0
    l=['Salaried', 'Self-Employed', 'Freelancer', 'Student' ,'Unemployed']
    employment_profile=l.index(user_data[14])
    age=user_data[6]
    income=user_data[18]
    credit_score=user_data[16]
    dic={'Good':1,'Bad':0,'Average':0.5}
    credit_history_length=dic[user_data[17]]
    number_of_existing_loans=1
    loan_amount=user_data[20]
    loan_tenure=user_data[21]
    ltv_ratio=loan_amount/loan_tenure   
    profile_score=1
    input_data={'Gender':gender,'Existing Customer':existing_customer,'Employment Profile':employment_profile,'Age':age,'Income':income,'Credit Score':credit_score,'Credit History Length':credit_history_length,'Number of Existing Loans':number_of_existing_loans,'Loan Amount':loan_amount,'Loan Tenure':loan_tenure,'LTV Ratio':ltv_ratio,'Profile Score':profile_score}
    model = joblib.load('Vehicle Loan/vehicle_model.pkl')
    input_transformed = pd.DataFrame([input_data])
    prediction = model.predict(input_transformed)
    if prediction[0]==1:
        vehicle_loan=1
    #inputs for bank loan
    #gender, married, dependents, education, self employed, applicant income, coapplicant income, loan amount, loan amount term, credit history, property area
    gender=0 if user_data[3]=='Male' else 1
    married=1 if user_data[11]=='Yes' else 0
    dependents=user_data[12]
    education=1 if user_data[13]=='Graduate' else 0
    self_employed=1 if user_data[14]=='Yes' else 0
    applicant_income=user_data[18]
    coapplicant_income=user_data[19]
    loan_amount=user_data[20]
    loan_amount_term=user_data[21]
    credit_history=1 if user_data[17]=='Yes' else 0
    property_area=2 if user_data[15]=='Semiurban' else 1 if user_data[15]=='Urban' else 0
    banK_loan_model = joblib.load("Bank Loan/bank_loan_model.pkl")
    bank_loan_scaler = joblib.load("Bank Loan/bank_loan_scaler.pkl")
    data=[[gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]]
    data = bank_loan_scaler.transform(data)
    prediction = banK_loan_model.predict(data)
    if prediction[0]==1:
        bank_loan=1
    
    #display the loans that are available to the user
    existing_loan_name=user_data[25]
    #if the user has existing loan then remove that loan from the available loans
    hl=0
    bl=0
    cl=0
    hil=0
    if existing_loan_name=='Bank Loan':
        bl=1
    elif existing_loan_name=='Home Loan':
        hl=1
    elif existing_loan_name=='Car Loan':
        cl=1
    elif existing_loan_name=='Personal Loan':
        hil=1
    else:
        pass
    #display the available loans
    st.markdown('<h4 style="color: green; text-align: center;">Loans that are available to you</h4>', unsafe_allow_html=True)
    st.markdown('----')
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">BANK LOAN</h3>', unsafe_allow_html=True)
        st.markdown('<a href="https://sbi.co.in/web/personal-banking/loans/personal-loans" target="_blank"><img src="https://cdni.iconscout.com/illustration/premium/thumb/bank-loan-illustration-download-in-svg-png-gif-file-formats--paper-mortgage-property-policy-document-operations-pack-finance-illustrations-4833670.png?f=webp" alt="Bank Loan" style="width:115%;height:100%;"></a>', unsafe_allow_html=True)
        if bank_loan==1 and bl!=1:
            st.markdown(
                """
                <style>
                    .approved-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: green;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approved-button:hover {
                        background-color: darkgreen;
                    }
                </style>
                <button class="approved-button">Approved</button>
                """,
                unsafe_allow_html=True
            )
        elif bank_loan==0 and bl!=1:
            st.markdown(
                """
                <style>
                    .apply-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: red;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .apply-button:hover {
                        background-color: darkred;
                    }
                </style>
                <button class="apply-button">Denied</button>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                    .appro-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: orange;
                        color: black;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approved-button:hover {
                        background-color:orange;
                    }
                </style>
                <button class="appro-button">Exists</button>
                """,
                unsafe_allow_html=True
            )
    with col2:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">HOME LOAN</h3>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.hdfc.com/home-loan" target="_blank"><img src="https://static.vecteezy.com/system/resources/thumbnails/035/048/659/small/ai-generated-house-in-hand-real-estate-concept-on-transparent-background-ai-generated-png.png" alt="Home Loan" style="width:105%;height:100%;"></a>', unsafe_allow_html=True)
        if home_loan==1 and hl!=1:
            st.markdown(
                """
                <style>
                    .approved-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: green;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approved-button:hover {
                        background-color: darkgreen;
                    }
                </style>
                <button class="approved-button">Approved</button>
                """,
                unsafe_allow_html=True
            )
        elif home_loan==0 and hl!=1:
            st.markdown(
                """
                <style>
                    .apply-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: red;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .apply-button:hover {
                        background-color: darkred;
                    }
                </style>
                <button class="apply-button">Denied</button>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                    .appr-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: orange;
                        color: black;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approved-button:hover {
                        background-color: darkgreen;
                    }
                </style>
                <button class="appr-button">Exists</button>
                """,
                unsafe_allow_html=True
            )
    with col3:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">VEHICLE LOAN</h3>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.hdfcbank.com/personal/loans/car-loan" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2132/2132830.png" alt="Vehicle Loan" style="width:105%;height:100%;"></a>', unsafe_allow_html=True)
        if vehicle_loan==1 and cl!=1:
            st.markdown(
                """
                <style>
                    .approved-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: green;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approved-button:hover {
                        background-color: darkgreen;
                    }
                </style>
                <button class="approved-button">Approved</button>
                """,
                unsafe_allow_html=True
            )
        elif vehicle_loan==0 and cl!=1:
            st.markdown(
                """
                <style>
                    .apply-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: red;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .apply-button:hover {
                        background-color: darkred;
                    }
                </style>
                <button class="apply-button">Denied</button>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                    .approv-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: orange;
                        color: white;
                        font-size: 15px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approv-button:hover {
                        background-color: darkgreen;
                    }
                </style>
                <button class="approved-button">Exists</button>
                """,
                unsafe_allow_html=True
            )
    with col4:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">HEALTH LOAN</h3>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.policybazaar.com/health-insurance/" target="_blank"><img src="https://www.cashe.co.in/wp-content/uploads/2023/12/Medical-2-1.png" alt="Health Insurance Loan" style="width:105%;height:60%;"></a>', unsafe_allow_html=True)
        if health_insurance_loan and hil!=1:
            st.markdown(
                """
                <style>
                    .approved-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: green;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approved-button:hover {
                        background-color: darkgreen;
                    }
                </style>
                <button class="approved-button">Approved</button>
                """,
                unsafe_allow_html=True
            )
        elif health_insurance_loan==0 and hil!=1:
            st.markdown(
                """
                <style>
                    .apply-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: red;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .apply-button:hover {
                        background-color: darkred;
                    }
                </style>
                <button class="apply-button">Denied</button>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                    .approve-button {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        background-color: orange;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                        padding: 10px 10px;
                        border-radius: 10px;
                        border: none;
                        cursor: pointer;
                        text-align: center;
                        width: 150px;
                        margin: auto;
                    }
                    .approve-button:hover {
                        background-color: orange;
                    }
                </style>
                <button class="approve-button">Exists</button>
                """,
                unsafe_allow_html=True
            )
    st.markdown('----')
    #select box which loans are denied
    deniel=[]
    if home_loan==0 and hl!=1:
        deniel.append('Home Loan')
    elif bank_loan==0 and bl!=1:
        deniel.append('Bank Loan')
    elif vehicle_loan==0 and cl!=1:
        deniel.append('Vehicle Loan')
    elif health_insurance_loan==0 and hil!=1:
        deniel.append('Health Insurance Loan')
    col1,col2,col3=st.columns([1,2,1])
    sel=col2.selectbox('Select the loan that is denied',deniel)
    if sel=='Home Loan':
        #plot the reasons for denial
        #home loan are Gender, Married, Dependents, Education, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area
        gender = 1 if user_data[3]=='Male' else 0
        married = 0 if user_data[11]=='Unmarried' else 1
        dependents = user_data[12]
        education = 1 if user_data[13]=='Graduate' else 0
        coapplicant_income = user_data[19]
        loan_amount = user_data[20]
        loan_amount_term = user_data[21]
        credit_history = 1 if user_data[17]=='Good' else 0.5 if user_data[17]=='Average' else 0
        property_area = 0 if user_data[15]=='Rural' else 2 if user_data[15]=='Urban' else 1

        # Create DataFrame with reasons for denial
        df = pd.DataFrame({
            "Feature": ["Coapplicant Income", "Loan Amount", "Loan Amount Term", "Credit History"],
            "Current Value": [coapplicant_income, loan_amount, loan_amount_term, credit_history]
        })

        # Set threshold values for approval
        threshold_values = {
            "Coapplicant Income": 5000,
            "Loan Amount": 100,
            "Loan Amount Term": 360,
            "Credit History": 1
        }

        df["Threshold for Approval"] = df["Feature"].map(threshold_values)
        col2.markdown('----')
        st.markdown('<h3 style="color: red; text-align: center;">Loan Denial Factors</h3>', unsafe_allow_html=True)
        col1,col2=st.columns(2)
        # Display DataFrame in Streamlit
        # Plot 1: Bar Chart with different colors
        plt.figure(figsize=(10, 5))
        colors = sns.color_palette("husl", len(df))  # Different colors
        plt.bar(df["Feature"], df["Current Value"], color=colors)
        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Factors Affecting Loan Denial")
        col1.pyplot(plt)

        # Plot 3: Approval vs Denial Comparison
        plt.figure(figsize=(10, 5))
        bar_width = 0.4

        plt.bar(df["Feature"], df["Current Value"], width=bar_width, label="Current Value", color="red")
        plt.bar(df["Feature"], df["Threshold for Approval"], width=bar_width, label="Threshold for Approval", color="green", alpha=0.7)

        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Loan Approval Thresholds Comparison")
        plt.legend()
        col2.pyplot(plt)
    elif sel=='Bank Loan':
        #plot the reasons for denial
        #gender, married, dependents, education, self employed, applicant income, coapplicant income, loan amount, loan amount term, credit history, property area
        gender=0 if user_data[3]=='Male' else 1
        married=1 if user_data[11]=='Yes' else 0
        dependents=user_data[12]
        education=1 if user_data[13]=='Graduate' else 0
        self_employed=1 if user_data[14]=='Yes' else 0
        applicant_income=user_data[18]
        coapplicant_income=user_data[19]
        loan_amount=user_data[20]
        loan_amount_term=user_data[21]
        credit_history=1 if user_data[17]=='Yes' else 0
        property_area=2 if user_data[15]=='Semiurban' else 1 if user_data[15]=='Urban' else 0
        # Create DataFrame with reasons for denial
        df = pd.DataFrame({
            "Feature": ["Applicant Income", "Coapplicant Income", "Loan Amount", "Loan Amount Term", "Credit History"],
            "Current Value": [applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history]
        })

        # Set threshold values for approval
        threshold_values = {
            "Applicant Income": 5000,
            "Coapplicant Income": 5000,
            "Loan Amount": 100,
            "Loan Amount Term": 360,
            "Credit History": 1
        }

        df["Threshold for Approval"] = df["Feature"].map(threshold_values)

        # Display DataFrame in Streamlit
        col2.markdown('----')
        st.markdown('<h3 style="color: red; text-align: center;">Loan Denial Factors</h3>', unsafe_allow_html=True)
        col1,col2=st.columns(2)

        # Plot 1: Bar Chart with different colors
        plt.figure(figsize=(10, 5))
        colors = sns.color_palette("husl", len(df))  # Different colors
        plt.bar(df["Feature"], df["Current Value"], color=colors)
        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Factors Affecting Loan Denial")
        col1.pyplot(plt)

        # Plot 3: Approval vs Denial Comparison
        plt.figure(figsize=(10, 5))
        bar_width = 0.4

        plt.bar(df["Feature"], df["Current Value"], width=bar_width, label="Current Value", color="red")
        plt.bar(df["Feature"], df["Threshold for Approval"], width=bar_width, label="Threshold for Approval", color="green", alpha=0.7)

        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Loan Approval Thresholds Comparison")
        plt.legend()
        col2.pyplot(plt)
    elif sel=='Vehicle Loan':
        #plot the reasons for denial
        #gender, Existing Customer, Employment Profile, Age Income, Credit Score, Credit History Length,Number of Existing Loans,Loan Amount, Loan Tenure, LTV Ratio, Profile Score
        st.write('You are denied a Vehicle Loan')
        gender=1 if user_data[3]=='Male' else 0
        existing_customer=1 if user_data[22]=='Yes' else 0
        l=['Salaried', 'Self-Employed', 'Freelancer', 'Student' ,'Unemployed']
        employment_profile=l.index(user_data[14])
        age=user_data[6]
        income=user_data[18]
        credit_score=user_data[16]
        dic={'Good':1,'Bad':0,'Average':0.5}
        credit_history_length=dic[user_data[17]]
        number_of_existing_loans=1
        loan_amount=user_data[20]
        loan_tenure=user_data[21]
        ltv_ratio=loan_amount/loan_tenure
        profile_score=1

        # Create DataFrame with reasons for denial
        df = pd.DataFrame({
            "Feature": ["Income", "Credit Score", "Credit History Length", "LTV Ratio"],
            "Current Value": [income, credit_score, credit_history_length, ltv_ratio]
        })

        # Set threshold values for approval
        threshold_values = {
            "Income": 5000,
            "Credit Score": 500,
            "Credit History Length": 1,
            "LTV Ratio": 0.5
        }

        df["Threshold for Approval"] = df["Feature"].map(threshold_values)

        # Display DataFrame in Streamlit
        col2.markdown('----')
        st.markdown('<h3 style="color: red; text-align: center;">Loan Denial Factors</h3>', unsafe_allow_html=True)
        col1,col2=st.columns(2)

        # Plot 1: Bar Chart with different colors
        plt.figure(figsize=(10, 5))
        colors = sns.color_palette("husl", len(df))  # Different colors
        plt.bar(df["Feature"], df["Current Value"], color=colors)
        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Factors Affecting Loan Denial")
        col1.pyplot(plt)

        # Plot 3: Approval vs Denial Comparison
        plt.figure(figsize=(10, 5))
        bar_width = 0.4

        plt.bar(df["Feature"], df["Current Value"], width=bar_width, label="Current Value", color="red")
        plt.bar(df["Feature"], df["Threshold for Approval"], width=bar_width, label="Threshold for Approval", color="green", alpha=0.7)

        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Loan Approval Thresholds Comparison")
        plt.legend()
        col2.pyplot(plt)
    elif sel=='Health Insurance Loan':
        #plot the reasons for denial
        #health inputs are age, sex,weight,bmi,hereiditary disease,no of dependtss, smoking, city, bp,diabetes, regular exercise, job title
        age=user_data[6]
        sex = 0 if user_data[3] == 'Female' else 1
        weight=user_data[4]
        bmi=weight/((weight/100)**2)
        dic={'NoDisease':0, 'Epilepsy':1, 'EyeDisease':2, 'Alzheimer':3, 'Arthritis':4,
        'HeartDisease':5, 'Diabetes':6, 'Cancer':7, 'High BP':8, 'Obesity':9}
        hereditary_disease=dic[user_data[5]]
        no_of_dependents=user_data[12]
        smoking=1 if user_data[7]=='Yes' else 0
        city=0
        bp=user_data[8]
        diabetes=1 if user_data[9]=='Yes' else 0
        regular_exercise=1 if user_data[10]=='Yes' else 0
        val=[ 2, 16,  0, 10, 22, 12, 32, 13, 30, 33, 15, 28, 29,  5,  8,  6,  9,
        26,  1, 19, 34, 18,  4, 23, 20,  7, 31, 14,  3, 11, 24, 17, 25, 27,
        21]
        job_title=random.choice(val)

        # Create DataFrame with reasons for denial
        df = pd.DataFrame({
            "Feature": ["Age", "Weight", "BMI", "Hereditary Disease", "No of Dependents", "Smoking", "BP", "Diabetes", "Regular Exercise", "Job Title"],
            "Current Value": [age, weight, bmi, hereditary_disease, no_of_dependents, smoking, bp, diabetes, regular_exercise, job_title]
        })

        # Set threshold values for approval
        threshold_values = {
            "Age": 18,
            "Weight": 50,
            "BMI": 18.5,
            "Hereditary Disease": 0,
            "No of Dependents": 0,
            "Smoking": 0,
            "BP": 120,
            "Diabetes": 0,
            "Regular Exercise": 1,
            "Job Title": 0
        }

        df["Threshold for Approval"] = df["Feature"].map(threshold_values)

        col2.markdown('----')
        st.markdown('<h3 style="color: red; text-align: center;">Loan Denial Factors</h3>', unsafe_allow_html=True)
        col1,col2=st.columns(2)

        # Plot 1: Bar Chart with different colors
        plt.figure(figsize=(10, 5))
        colors = sns.color_palette("husl", len(df))  # Different colors
        plt.bar(df["Feature"], df["Current Value"], color=colors)
        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Factors Affecting Loan Denial")
        col1.pyplot(plt)

        # Plot 3: Approval vs Denial Comparison
        plt.figure(figsize=(10, 5))
        bar_width = 0.4

        plt.bar(df["Feature"], df["Current Value"], width=bar_width, label="Current Value", color="red")
        plt.bar(df["Feature"], df["Threshold for Approval"], width=bar_width, label="Threshold for Approval", color="green", alpha=0.7)

        plt.xticks(rotation=45)
        plt.ylabel("Values")
        plt.title("Loan Approval Thresholds Comparison")
        plt.legend()
        col2.pyplot(plt)


def visualizations_page():
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://www.onlinecredit.com.sg/wp-content/uploads/2021/08/woman-hand-holding-money-bag-concept-saving-finance-accounting-scaled.jpg');
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
    st.title('Update Your Details')
    st.write('Please update your details below')
    # Extracting user data
    user_data = get_user_by_email(st.session_state.get('user', ['', 'Unknown', 'Unknown'])[2])
    col1,col2,col3=st.columns(3)
    weight = col1.number_input('Enter the weight (kg)',min_value=10,value=user_data[4])
    hereditary_disease = col2.selectbox('Do you have any hereditary disease?',['NoDisease', 'Epilepsy', 'EyeDisease', 'Alzheimer', 'Arthritis',
       'HeartDisease', 'Diabetes', 'Cancer', 'High BP', 'Obesity'])
    age = col3.slider('Enter the age',min_value=1,value=user_data[6])
    col1,col2,col3,col4=st.columns(4)
    smoking = col1.selectbox('Do you smoke?',['Yes','No'])
    regular_bp_level = col2.number_input('Regular blood pressure level',value=user_data[8])
    diabetes = col3.selectbox('Do you have diabetes?',['Yes','No'])
    regular_exercise = col4.selectbox('Do you do regular exercise?',['Yes','No'])
    col1,col2,col3,col4=st.columns(4)
    marital_status = col1.selectbox('Choose Marital Status',['Married','Unmarried','Divorced','Widowed'])
    no_of_dependents = col2.number_input('Number of dependents',min_value=0,value=user_data[12])
    education = col3.selectbox('Choose Education',['Graduate','Non Graduate'])
    employment = col4.selectbox('Choose Employment',['Salaried', 'Self-Employed', 'Freelancer', 'Student', 'Unemployed'])
    col1,col2,col3,col4=st.columns(4)
    property_status = col1.selectbox('Choose Property Status',['Rural','Urban','Semi Urban'])
    credit_score = col2.number_input('Enter the credit score',min_value=0,value=user_data[16])
    credit_history = col3.selectbox('Choose Credit History',['Good','Bad','Average'])
    annual_income = col4.number_input('Enter the annual income (K)',min_value=0,value=user_data[18])
    col1,col2,col3,col4=st.columns(4)
    co_applicant_annual_income = col1.number_input('Co-applicant Income (K)',min_value=0,value=user_data[19])
    loan_amount = col2.number_input('Enter the loan amount (K)',min_value=0,value=user_data[20])
    loan_duration = col3.number_input('Enter the loan duration (years)',min_value=1,value=user_data[21],step=1)
    existing_loan = col4.selectbox('Choose Existing Loan',['Yes','No'])
    col1,col2,col3,col4=st.columns(4)
    existing_loan_amount = col1.number_input('Existing loan amount',min_value=0,value=user_data[23])
    existing_loan_duration = col2.number_input('Existing loan duration (years)',min_value=1,value=user_data[24],step=1)
    existing_loan_type=col3.selectbox('Choose Existing Loan Type',['Home Loan','Personal Loan','Car Loan','Bank Loan','Others'],index=0 if user_data[25]=='Home Loan' else 1 if user_data[25]=='Personal Loan' else 2 if user_data[25]=='Car Loan' else 3 if user_data[25]=='Education Loan' else 4)
    language = col4.selectbox("Preferred Language", ["English", "Telugu", "Hindi"],index=0 if user_data[26]=='English' else 1 if user_data[26]=='Telugu' else 2)
    if st.button('Update',type='primary',key='update'):
        # Ensure that 'user_data' has exactly 26 values
        user_id = user_data[0]

        # Prepare user data excluding the password
        user_data = [
            weight, hereditary_disease, age, smoking, regular_bp_level, diabetes, 
            regular_exercise, marital_status, no_of_dependents, education, employment, property_status, 
            credit_score, credit_history, annual_income, co_applicant_annual_income, loan_amount, 
            loan_duration, existing_loan, existing_loan_amount, existing_loan_duration, existing_loan_type, 
            language
        ]

        # Call the update_user function
        res=update_user(user_id, *user_data)
        if res:
            st.success('Updated Successfully')
        else:
            st.error('Error')

def user_home_page():
    # Navigation menu for user dashboard
    
    with st.sidebar:
        col1,col2,col3=st.columns([1,4,1])
        col2.image('https://cdn-icons-png.flaticon.com/512/1177/1177568.png',use_column_width=True)
        name=st.session_state['user'][1]
        st.markdown(f"<h1 style='text-align: center; color: black;'><b>{name}'s Dashboard</b></h1>", unsafe_allow_html=True)
        selected_tab = option_menu(
            menu_title=None,
            options=["User Profile", "Update Page", "Loans",'Logout'],
            icons=['person','bar-chart','bank'], menu_icon="cast", default_index=0,
        styles={
        "nav-link-selected": {"background-color": "red", "color": "white", "border-radius": "30px"},
        }
        )
    if selected_tab == "User Profile":
        user_profile()
    elif selected_tab == "Loans":
        loan_page()
    elif selected_tab == "Update Page":
        visualizations_page()
    elif selected_tab=='Logout':
        # Logout functionality
        st.session_state.clear()  # Clear session state to "log out"
        st.experimental_rerun()