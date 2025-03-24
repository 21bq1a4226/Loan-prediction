import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from db_manager import update_user,get_user_by_email
import pickle
import gdown
import matplotlib.pyplot as plt
import joblib
import seaborn as sns
import random
from sklearn.preprocessing import MinMaxScaler
import json
import plotly.express as px
import numpy as np
from googletrans import Translator
file_id = "1W8O2C5tQ5fHs8FASyRHigYccHT-gCdyj"
output='health_insurance_model.pkl'
url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, output, quiet=False)
file_id = "1ZPGq1xBviVipK6jiKoFL3PluIABlY2x5"
fraud_model='fraud_detection_model.sav'
url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, fraud_model, quiet=False)

def translate_to_telugu(text):
    translator = Translator()
    translated = translator.translate(text, src="en", dest="te")
    return translated.text
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
    name = translate_to_telugu(user_data[1])
    email = user_data[2]
    gender = translate_to_telugu(user_data[3])
    weight = user_data[4]
    hereditary_disease = user_data[5]
    age=user_data[6]
    smoking=translate_to_telugu(user_data[7])
    regular_bp_level=user_data[8]
    diabetes=user_data[9]
    regular_exercise=user_data[10]
    marital_status=translate_to_telugu(user_data[11])
    no_of_dependents=user_data[12]
    education=translate_to_telugu(user_data[13])
    employment=translate_to_telugu(user_data[14])
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
            <div class="profile-header">ప్రొఫైల్</div>
            <div class="profile-item"><strong>పేరు:</strong> {name}</div>
            <div class="profile-item"><strong>లింగం:</strong> {gender}</div>
            <div class="profile-item"><strong>వయస్సు:</strong> {age}</div>
            <div class="profile-item"><strong>ధూమపానం:</strong> {smoking}</div>
            <div class="profile-item"><strong>వైవాహిక స్థితి:</strong> {marital_status}</div>
            <div class="profile-item"><strong>విద్య:</strong> {education}</div>
            <div class="profile-item"><strong>ఉపాధి:</strong> {employment}</div>
            <div class="profile-item"><strong>క్రెడిట్ స్కోర్:</strong> {credit_score}</div>
            <div class="profile-item"><strong>వార్షిక ఆదాయం:</strong> {annual_income}</div>
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
    existing_loan_type=translate_to_telugu(existing_loan_type)
    #display the existing loan details in ui
    st.markdown(
    """
    <div style="text-align: center; padding: 5px; background-image: url('https://img.freepik.com/premium-vector/stock-market-investment-trading-graph-graphic-concept-suitable-financial-investment_258787-30.jpg?semt=ais_hybrid');
    background-size: cover; background-position: center; background-repeat: no-repeat;
                border-radius: 20px; border: 1.5px solid black; margin-bottom: 10px;">
        <p style="color: red; font-size: 30px;"><b>ఇప్పటికే ఉన్న లోన్ వివరాలు</b></p>
        <div style="display: flex; justify-content: space-around; padding: 10px; font-size: 18px;">
            <div style="flex: 1; padding: 10px;"><b> రుణ రకం:</b> {existing_loan_type}</div>
        </div>
        <div style="display: flex; justify-content: space-around; padding: 10px; font-size: 18px;">
            <div style="flex: 1; padding: 10px;"><b> రుణ మొత్తం:</b> {existing_loan_amount} </div>
            <div style="flex: 1; padding: 10px;"><b> రుణ వ్యవధి:</b> {existing_loan_duration} సంవత్సరాలు</div>
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
    

    # Google Drive file ID extracted from the link
    
    health_model=joblib.load('health_insurance_model.pkl')
    input_data = pd.DataFrame([[
        age, sex, weight, bmi, hereditary_disease, no_of_dependents, smoking, city, bp, diabetes, regular_exercise, job_title
    ]])
    prediction = health_model.predict(input_data)
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
    st.markdown('<h4 style="color: green; text-align: center;">మీకు అందుబాటులో ఉన్న రుణాలు</h4>', unsafe_allow_html=True)
    st.markdown('----')
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">బ్యాంక్ లోన్</h3>', unsafe_allow_html=True)
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
                        text-align: center;
                    }
                    .approved-button:hover {
                        background-color: darkgreen;
                    }
                </style>
                <button class="approved-button">ఆమోడించు</button>
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
                <button class="apply-button">తిరస్కరించు</button>
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
                <button class="appro-button">ఉంది</button>
                """,
                unsafe_allow_html=True
            )
    with col2:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">గృహ రుణం</h3>', unsafe_allow_html=True)
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
                <button class="approved-button">ఆమోడించు</button>
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
                <button class="apply-button">తిరస్కరించు</button>
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
                <button class="appr-button">ఉంది</button>
                """,
                unsafe_allow_html=True
            )
    with col3:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">వాహన రుణ</h3>', unsafe_allow_html=True)
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
                <button class="approved-button">ఆమోడించు</button>
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
                <button class="apply-button">తిరస్కరించు</button>
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
                <button class="approved-button">ఉంది</button>
                """,
                unsafe_allow_html=True
            )
    with col4:
        st.markdown('<h3 style="color: #9c0399; text-align: center;">ఆరోగ్య రుణ</h3>', unsafe_allow_html=True)
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
                <button class="approved-button">ఆమోడించు</button>
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
                <button class="apply-button">తిరస్కరించు</button>
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
                <button class="approve-button">ఉంది</button>
                """,
                unsafe_allow_html=True
            )
    st.markdown('----')
    #select box which loans are denied
    deniel=[]
    if home_loan==0 and hl!=1:
        deniel.append('గృహ రుణం')
    elif bank_loan==0 and bl!=1:
        deniel.append('బ్యాంక్ లోన్')
    elif vehicle_loan==0 and cl!=1:
        deniel.append('వాహన రుణం')
    elif health_insurance_loan==0 and hil!=1:
        deniel.append('ఆరోగ్య బీమా లోన్')
    col1,col2,col3=st.columns([1,2,1])
    sel=col2.selectbox('తిరస్కరించబడిన రుణాన్ని ఎంచుకోండి.',deniel)
    if sel=='గృహ రుణం':
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
        st.markdown('<h3 style="color: red; text-align: center;">రుణ తిరస్కరణ కారకాలు</h3>', unsafe_allow_html=True)
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
    elif sel=='బ్యాంక్ లోన్':
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
        st.markdown('<h3 style="color: red; text-align: center;">రుణ తిరస్కరణ కారకాలు</h3>', unsafe_allow_html=True)
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
    elif sel=='వాహన రుణం':
        #plot the reasons for denial
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
        st.markdown('<h3 style="color: red; text-align: center;">రుణ తిరస్కరణ కారకాలు</h3>', unsafe_allow_html=True)
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
    elif sel=='ఆరోగ్య బీమా లోన్':
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
        st.markdown('<h3 style="color: red; text-align: center;">రుణ తిరస్కరణ కారకాలు</h3>', unsafe_allow_html=True)
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
def classify_profession(education, employment, annual_income, hereditary_disease, smoking, regular_exercise, credit_score):
    if education == "Graduate" and employment == "Salaried" and annual_income > 700:
        return "Executive"  # High income and salaried professional
    elif education == "Graduate" and employment == "Self-Employed" and annual_income > 500:
        return "Engineer"  # Self-employed with good income, likely in engineering
    elif hereditary_disease in ["HeartDisease", "High BP", "Diabetes", "Cancer"] and not smoking and regular_exercise == "Yes":
        return "Healthcare"  # Likely in healthcare field due to health awareness
    elif employment == "Self-Employed" and annual_income > 300:
        return "Artist"  # Self-employed, moderate income suggests creative work
    elif employment == "Student":
        return "Other"  # Students are not professionals yet
    elif employment == "Unemployed":
        return "Other"  # No active profession
    elif education == "Graduate" and employment == "Freelancer":
        return "Entertainment"  # Freelancers may work in entertainment
    elif education == "Non Graduate" and employment in ["Salaried", "Self-Employed"]:
        return "Other"  # General category for non-graduate workers
    else:
        return "Other"  # Default category

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
    st.title('మీ వివరాలను నవీకరించండి')
    st.write('దయచేసి మీ వివరాలను క్రింద నవీకరించండి.')
    # Extracting user data
    user_data = get_user_by_email(st.session_state.get('user', ['', 'Unknown', 'Unknown'])[2])
    col1,col2,col3=st.columns(3)
    weight = col1.number_input('బరువు (కిలోలు) నమోదు చేయండి',min_value=10,value=user_data[4])
    disease_mapping = { "ఏమీ లేను": "NoDisease", "ఎపిలెప్సీ": "Epilepsy", "కళ్ల వ్యాధి": "EyeDisease", "అల్జీమర్స్": "Alzheimer", "ఆర్థరైటిస్": "Arthritis", "హృదయ వ్యాధి": "HeartDisease", "డయాబెటిస్": "Diabetes", "క్యాన్సర్": "Cancer", "అధిక రక్తపోటు": "High BP", "ఓబేసిటీ": "Obesity" }
    hereditary_disease = col2.selectbox("ఏదైనా వంశపారంపర్య వ్యాధి ఉందా?", list(disease_mapping.keys()))
    age = col3.slider('వయస్సును నమోదు చేయండి',min_value=1,value=user_data[6])
    col1,col2,col3,col4=st.columns(4)
    smoking = col1.selectbox('మీరు ధూమపానం చేస్తారా?',['Yes','No'])
    regular_bp_level = col2.number_input('సాధారణ రక్తపోటు స్థాయి',value=user_data[8])
    diabetes = col3.selectbox('మీకు మధుమేహం ఉందా?',['Yes','No'])
    regular_exercise = col4.selectbox('మీరు క్రమం తప్పకుండా వ్యాయామం చేస్తారా?',['Yes','No'])
    col1,col2,col3,col4=st.columns(4)
    marital_status = col1.selectbox('వైవాహిక స్థితిని ఎంచుకోండి',['Married','Unmarried','Divorced','Widowed'])
    no_of_dependents = col2.number_input('ఆధారపడిన వారి సంఖ్య',min_value=0,value=user_data[12])
    education = col3.selectbox('విద్యను ఎంచుకోండి',['Graduate','Non Graduate'])
    employment = col4.selectbox('ఉపాధిని ఎంచుకోండి',['Salaried', 'Self-Employed', 'Freelancer', 'Student', 'Unemployed'])
    col1,col2,col3,col4=st.columns(4)
    property_status = col1.selectbox('ఆస్తి స్థితిని ఎంచుకోండి',['Rural','Urban','Semi Urban'])
    credit_score = col2.number_input('క్రెడిట్ స్కోర్‌ను నమోదు చేయండి',min_value=0,value=user_data[16])
    credit_history = col3.selectbox('క్రెడిట్ చరిత్రను ఎంచుకోండి',['Good','Bad','Average'])
    annual_income = col4.number_input('వార్షిక ఆదాయాన్ని నమోదు చేయండి (K)',min_value=0,value=user_data[18])
    col1,col2,col3,col4=st.columns(4)
    co_applicant_annual_income = col1.number_input('సహ-దరఖాస్తుదారు ఆదాయం (K)',min_value=0,value=user_data[19])
    loan_amount = col2.number_input('రుణ మొత్తాన్ని నమోదు చేయండి (K)',min_value=0,value=user_data[20])
    loan_duration = col3.number_input('లోన్ వ్యవధిని నమోదు చేయండి(సంవత్సరాలు)',min_value=1,value=user_data[21],step=1)
    existing_loan = col4.selectbox('ఇప్పటికే ఉన్న రుణాన్ని ఎంచుకోండి',['Yes','No'])
    col1,col2,col3,col4=st.columns(4)
    existing_loan_amount = col1.number_input('ఇప్పటికే ఉన్న లోన్ మొత్తం',min_value=0,value=user_data[23])
    existing_loan_duration = col2.number_input('ఇప్పటికే ఉన్న లోన్ వ్యవధి (సంవత్సరాలు)',min_value=1,value=user_data[24],step=1)
    existing_loan_type=col3.selectbox('ఇప్పటికే ఉన్న లోన్ రకాన్ని ఎంచుకోండి',['Home Loan','Personal Loan','Car Loan','Bank Loan','Others'],index=0 if user_data[25]=='Home Loan' else 1 if user_data[25]=='Personal Loan' else 2 if user_data[25]=='Car Loan' else 3 if user_data[25]=='Education Loan' else 4)
    language = col4.selectbox("ఎన్నుకోబడిన భాష", ["English", "Telugu"],index=0 if user_data[26]=='English' else 1 if user_data[26]=='Telugu' else 2)
    if st.button('నవీకరించు',type='primary',key='update'):
        hereditary_disease=disease_mapping[hereditary_disease]
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

def telugu_page():
    # Navigation menu for user dashboard
    
    with st.sidebar:
        col1,col2,col3=st.columns([1,4,1])
        col2.image('https://cdn-icons-png.flaticon.com/512/1177/1177568.png',use_column_width=True)
        name=translate_to_telugu(st.session_state['user'][1])
        st.markdown(f"<h1 style='text-align: center; color: black;'><b>{name} డాష్‌బోర్డ్</b></h1>", unsafe_allow_html=True)
        selected_tab = option_menu(
            menu_title=None,
            options=["ప్రొఫైల్", "నవీకరణలు", "రుణాలు",'విభజన','మోసం గుర్తింపు','లాగ్అవుట్'],
            icons=['person','bar-chart','bank','collection','bank','power'], menu_icon="cast", default_index=0,
        styles={
        "nav-link-selected": {"background-color": "red", "color": "white", "border-radius": "30px"},
        }
        )
    if selected_tab == "ప్రొఫైల్":
        user_profile()
    elif selected_tab == "రుణాలు":
        loan_page()
    elif selected_tab == "నవీకరణలు":
        visualizations_page()
    elif selected_tab=='లాగ్అవుట్':
        # Logout functionality
        st.session_state.clear()  # Clear session state to "log out"
        st.experimental_rerun()
    elif selected_tab=='విభజన':
        st.markdown('<h1 style="color: #9c0399; text-align: center;">కస్టమర్ సెగ్మెంటేషన్</h1>', unsafe_allow_html=True)
        st.markdown(" ")
        # Load project descriptions
        with open("descriptions.json") as f:
            segment_descriptions = json.load(f)

        segment_descriptions = pd.DataFrame(segment_descriptions.values(), index=segment_descriptions.keys(), columns=["description"])

        # Load the model and scaler
        model = joblib.load("model.joblib")
        scaler = MinMaxScaler()
        scaler.min_, scaler.scale_ = np.load('minmax_scaler_params.npy')

        # Encoding mappings
        encodings = {
            'Married': {'Yes': 1, 'No': 0},
            'Gender': {"Female": 0, "Male": 1},
            'Profession': {'Artist': 0, 'Doctor': 1, 'Engineer': 2, 'Entertainment': 3, 'Executive': 4, 'Healthcare': 5, "Lawyer": 6, "Other": 7},
        }

        # List of features and column names
        num_features = ['Family Size', 'Age', 'Work Experience']
        cat_features = ['Spending Score', 'Profession', 'Gender', 'Graduated', 'Married']
        columns = ['Family_Size', 'Age', 'Work_Experience', 'Spending_Score',
                'Profession_Artist', 'Profession_Doctor', 'Profession_Engineer',
                'Profession_Entertainment', 'Profession_Executive',
                'Profession_Healthcare', 'Profession_Lawyer', 'Profession_Other',
                'Gender', 'Graduated', 'Ever_Married']

        # Streamlit UI
        user_data = get_user_by_email(st.session_state.get('user', ['', 'Unknown', 'Unknown'])[2])
        name = [1]
        family_size = user_data[12]
        age = user_data[6]
        married = 'Yes' if user_data[11]=='Married' else 'No'
        work_experience = 1
        graduated = 1 if user_data[13]=='Graduate' else 0
        work_profession = classify_profession(user_data[13],user_data[14],user_data[18],user_data[5],user_data[7],user_data[10],user_data[16])
        gender= 'Male' if user_data[3]=='Male' else 'Female'
        spending_score = user_data[16]

        # Prepare input dictionary
        inputs = {
            'Family Size': family_size,
            'Age': age,
            'Work Experience': work_experience,
            'Spending Score': spending_score,
            'Profession': work_profession,
            'Gender': gender,
            'Graduated': graduated,
            'Married': married
        }

        # Preprocess numerical inputs
        num_inputs = {k: v for k, v in inputs.items() if k in num_features}
        num_df = pd.DataFrame.from_dict(num_inputs, orient='index').T
        scaled_inputs = scaler.transform(num_df)
        num_df = pd.DataFrame(scaled_inputs)

        # Process categorical inputs
        num_professions = len(set(encodings['Profession'].values()))
        num_onehot_encoded_features = 1
        cat_df = np.zeros((1, len(cat_features) - num_onehot_encoded_features + num_professions))

        for i, feature in enumerate(cat_features):
            if feature == 'Profession':
                profession = np.zeros(num_professions)
                profession[encodings[feature][inputs[feature]]] = 1
                cat_df[:, i:i+num_professions] = profession.reshape(1, num_professions)
            elif feature in ['Married', 'Gender']:
                cat_df[0, i+num_professions-num_onehot_encoded_features] = encodings[feature][inputs[feature]]
        
        cat_df = pd.DataFrame(cat_df)
        predict_df = pd.concat([num_df, cat_df.add_suffix('_2')], axis=1)
        predict_df.columns = columns

        # Make the prediction
        prediction = model.predict(predict_df)
        predicted_segment = prediction[0]
        if predicted_segment=='A':
            seg='స్టార్టర్'
        elif predicted_segment=='B':
            seg='బిల్డర్'
        elif predicted_segment=='C':
            seg='ఎలైట్'
        elif predicted_segment=='D':
            seg='అన్వేషి'
        description = segment_descriptions.loc[predicted_segment]['description']
        dec=translate_to_telugu(description)
        st.markdown(
            f"""
            <style>
                .description-box {{
                    background-image:url(https://png.pngtree.com/thumb_back/fh260/background/20230415/pngtree-hd-pastel-pink-gold-marble-background-image_2440700.jpg);
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    background-color:rgba(255,255,255,0.1);
                    background-blend-mode: overlay;
                    padding: 15px;
                    border-radius: 10px;
                    border: 2px solid #ddd;  /* Light border */
                    text-align: center;
                    font-size: 20px;
                    font-family: 'Arial', sans-serif;
                    font-weight: bold;
                    color: black;  /* Default text color */
                    box-shadow: 2px 2px 10px rgba(2, 0, 0, 0.1);
                }}
                .segment {{
                    color: red;  /* Customer segment in red */
                    font-size: 22px;
                }}
                .desc {{
                    color: black;  /* Remaining description in black */
                }}
            </style>
            <div class="description-box">
                <span class="segment">మీ వర్గం చెందినది {seg}</span><br><br>
                <span class="desc">{dec}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Predict probabilities
        probabilities = model.predict_proba(predict_df)[0]
        probabilities = np.round(probabilities, 2)
        segment_labels = ['స్టార్టర్', 'బిల్డర్', 'ఎలైట్', 'అన్వేషి']

        df = pd.DataFrame({"Segment": segment_labels, "Probability": probabilities})

        # Create Plotly bar chart
        fig = px.bar(
            df,
            x="Segment",
            y="Probability",
            color="Segment",  # Different colors for each segment
            text="Probability",
            labels={"Segment": "వృత్తి విభాగాలు", "Probability": "సంభావ్యత"},
            color_discrete_sequence=px.colors.qualitative.Plotly,  # Nice color palette
        )

        # Customize layout
        fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
        fig.update_layout(
            xaxis_tickangle=-45, 
            plot_bgcolor="white",
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, zeroline=False)
        )

        # Display
        st.plotly_chart(fig, use_container_width=True)
    elif selected_tab=='మోసం గుర్తింపు':
        st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://i0.wp.com/bisonbank.com/wp-content/uploads/2024/07/Picture1-800x450.jpg?fit=960%2C540&ssl=1');
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
        st.markdown('<h1 style="color: #9c0399; text-align: center;">మోసం గుర్తింపు</h1>', unsafe_allow_html=True)
        st.write("")
        st.write("")
        loaded_model = joblib.load("fraud_detection_model.sav")
        # Sidebar Description
        user_data = get_user_by_email(st.session_state.get('user', ['', 'Unknown', 'Unknown'])[2])
        # Input Fields
        age = user_data[6]
        step = 1
        customer = 1
        gender = 'Male' if user_data[3]=='Male' else 'Female'
        merchant = 1
        col1,col2,col3=st.columns(3)
        mode=col1.selectbox('లావాదేవీ విధానాన్ని ఎంచుకోండి',['ఆన్‌లైన్','ఆఫ్‌లైన్'])
        if mode=='ఆన్‌లైన్':
            category = 1
        else:
            category=0
        portal=col2.selectbox('పోర్టల్‌ని ఎంచుకోండి',['బ్యాంక్ బదిలీ','క్రెడిట్ కార్డ్','డెబిట్ కార్డ్','ఈ-వాలెట్','UPI','నగదు'])
        amount = col3.number_input("లావాదేవీ మొత్తం", min_value=0.0, step=0.01)

        # Submit Button
        col1,col2,col3=st.columns([2,2,1])
        if col2.button("మోసాన్ని గుర్తించండి",type='primary'):
            if portal=='UPI' and amount>5000 and mode=='ఆన్‌లైన్':
                st.error('మోసానికి అధిక అవకాశాలు')
            elif portal=='క్రెడిట్ కార్డ్' and amount>10000 and mode=='ఆన్‌లైన్':
                st.error('మోసానికి అధిక అవకాశాలు')
            elif portal=='డెబిట్ కార్డ్' and amount>5000 and mode=='ఆన్‌లైన్':
                st.error('మోసానికి అధిక అవకాశాలు')
            elif mode=='ఆఫ్‌లైన్' and (portal=='క్రెడిట్ కార్డ్' or portal=='డెబిట్ కార్డ్' or portal=='ఈ-వాలెట్' or portal=='బ్యాంక్ బదిలీ' or portal=='UPI'):
                st.error('ఆఫ్‌లైన్ మోడ్‌లో మోసాన్ని గుర్తించలేకపోయాము')
            elif mode=='ఆఫ్‌లైన్' and portal=='నగదు' and amount>100000:
                st.error('మోసానికి అధిక అవకాశాలు')
            elif mode=='ఆఫ్‌లైన్' and amount<100000:
                st.success('ఏ మోసం గుర్తించబడలేదు')
            elif mode=='ఆన్‌లైన్' and portal=='నగదు':
                st.error('ఆన్‌లైన్ మోడ్‌లో మోసాన్ని గుర్తించడం సాధ్యం కాలేదు.')
            else:
                # Create dataframe from user inputs
                new_data = pd.DataFrame([[step, customer, age, gender, merchant, category, amount]], 
                                        columns=['step', 'customer', 'age', 'gender', 'merchant', 'category', 'amount'])
                
                # Data transformation
                col_categorical = new_data.select_dtypes(include=['object']).columns
                for col in col_categorical:
                    new_data[col] = new_data[col].astype('category')

                # Categorical to numeric conversion
                new_data[col_categorical] = new_data[col_categorical].apply(lambda x: x.cat.codes)

                # Prediction
                result = loaded_model.predict(new_data)

                # Display Results
                if result == 1:
                    prediction = "🚨 మోసానికి అధిక అవకాశాలు"
                    st.error(prediction)
                else:
                    prediction = "✅ మోసపూరితం కాని చెల్లింపు"
                    st.success(prediction)