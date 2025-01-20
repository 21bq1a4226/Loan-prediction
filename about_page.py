import streamlit as st

def about_page():
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://i.pinimg.com/736x/11/38/c3/1138c346b9129c95708bd3bcc22cf1dd.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Center the registration form container using Streamlit form layout
    # Title
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 1px; background-color: white; border-radius: 1px; border: 1.5px solid black; margin-bottom: 20px;">
            <p style="color: black; font-size: 20px;"><b>The Loan Prediction System aims to assist financial institutions in determining the eligibility of loan applicants by analyzing their financial and personal details. The challenge lies in accurately predicting whether a loan should be approved or rejected based on key factors such as income, credit history, employment type, loan amount, and repayment capacity. The system needs to minimize the risk for the lender while ensuring an efficient and fair approval process for the applicants.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="text-align: center; padding: 1px; background-color: white; border-radius: 1px; border: 1.5px solid black; margin-bottom: 20px;">
            <p style="color: black; font-size: 20px;"><b>The Loan Prediction System leverages machine learning algorithms to streamline the loan approval process by automating the evaluation of applicants' eligibility. By analyzing historical loan data, the system identifies patterns and critical factors that influence loan approval decisions. The model predicts the likelihood of approval based on attributes such as income, credit history, and loan tenure. This solution not only enhances the speed and accuracy of decision-making but also reduces human bias, enabling financial institutions to make data-driven, reliable, and consistent decisions.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="text-align: center; padding: 1px; background-color: white; border-radius: 1px; border: 1.5px solid black; margin-bottom: 20px;">
            <p style="color: black; font-size: 20px;"><b>The system employs various machine learning techniques, including Logistic Regression, Decision Trees, Random Forest, Gradient Boosting (XGBoost, LightGBM), and Support Vector Machines (SVM). Data preprocessing involves handling missing values, feature encoding (e.g., One-Hot Encoding or Label Encoding), and scaling of numerical features. Feature selection techniques are used to identify the most influential variables. Performance is evaluated using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC. The final model is fine-tuned using hyperparameter optimization methods like Grid Search or Random Search.   
        </div>
        """,
        unsafe_allow_html=True
    )
