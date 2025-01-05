import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
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
    user_data = st.session_state.get('user', ['', 'Unknown', 'Unknown'])
    name = user_data[1]
    email = user_data[2]
    
    # General image link
    image_link = "https://cdn-icons-png.flaticon.com/512/4042/4042356.png"  # Replace with your image URL

    # CSS Styling
    profile_css = """
    <style>
        .profile-container {
            background-color: #f8f9fa;
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
            color: #333;
        }
        .profile-item {
            font-size: 18px;
            margin-bottom: 10px;
            color: #555;
        }
        .profile-image {
            flex-shrink: 0;
            margin-left: 20px;
        }
        .profile-image img {
            border-radius: 50%;
            max-width: 200px;
            max-height: 200px;
        }
    </style>
    """

    # HTML Structure
    profile_html = f"""
    <div class="profile-container">
        <div class="profile-details">
            <div class="profile-header">User Profile</div>
            <div class="profile-item"><strong>Name:</strong> {name}</div>
            <div class="profile-item"><strong>Email:</strong> {email}</div>
        </div>
        <div class="profile-image">
            <img src="{image_link}" alt="User Image">
        </div>
    </div>
    """

    # Display styled content
    st.markdown(profile_css + profile_html, unsafe_allow_html=True)

def loan_page():
    with st.form(key='loan_form'):
        st.subheader('Select the values from the dropdown menu to get the bank loan prediction')
        model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))
        ## Account No
        account_no = st.text_input('Account number')

        ## Full Name
        fn=st.session_state['user'][1]
        col1, col2 = st.columns(2)
        with col1:
            ## For gender
            gen_display = ('Female','Male')
            gen_options = list(range(len(gen_display)))
            gen = col1.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])
        with col2:
            ## For Marital Status
            mar_display = ('No','Yes')
            mar_options = list(range(len(mar_display)))
            mar = col2.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])
        with col1:
            ## No of dependets
            dep_display = ('No','One','Two','More than Two')
            dep_options = list(range(len(dep_display)))
            dep = col1.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])
        with col2:
            ## For edu
            edu_display = ('Not Graduate','Graduate')
            edu_options = list(range(len(edu_display)))
            edu = col2.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])
        with col1:
            ## For emp status
            emp_display = ('Job','Business')
            emp_options = list(range(len(emp_display)))
            emp = col1.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])
        with col2:
            ## For Property status
            prop_display = ('Rural','Semi-Urban','Urban')
            prop_options = list(range(len(prop_display)))
            prop = col2.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])
        with col1:
            ## For Credit Score
            cred_display = ('Between 300 to 500','Above 500')
            cred_options = list(range(len(cred_display)))
            cred = col1.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])
        with col2:
            ## Applicant Monthly Income
            mon_income = col2.number_input("Applicant's Monthly Income($)",value=0)
        with col1:
            ## Co-Applicant Monthly Income
            co_mon_income = col1.number_input("Co-Applicant's Monthly Income($)",value=0)
        with col2:
            ## Loan AMount
            loan_amt = col2.number_input("Loan Amount",value=0)
        ## loan duration
        dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
        dur_options = range(len(dur_display))
        dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])
        submitted=st.form_submit_button("Submit")
    if submitted:
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
    if ans == 0:
        st.markdown(
            f"""
            <div style='
                background-color:#f8d7da;
                padding:15px;
                border-radius:5px;
                border:1px solid #f5c2c7;
                color:#842029;
                font-size:16px;
                font-weight:bold;
            '>
                Hello: {fn}->Account number: {account_no} <br>
                According to our Calculations, you will <b>not</b> get the loan from the Bank.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='
                background-color:#d1e7dd;
                padding:15px;
                border-radius:5px;
                border:1px solid #badbcc;
                color:#0f5132;
                font-size:16px;
                font-weight:bold;
            '>
                Hello: {fn} ->Account number: {account_no} <br>
                Congratulations!! You will get the loan from the Bank.
            </div>
            """,
            unsafe_allow_html=True
        )


def visualizations_page():
    data=pd.read_csv('Loan_Data/train.csv')
    st.title('Visualizations')
    #place option for the user to see the EDA and model plots
    menu=st.selectbox('Select the type of visualization',['EDA','Model'])
    if menu=='EDA':
        st.write('This is the data used for the visualization')
        st.write(data)
        st.write('The following are the visualizations of the data')
        col1, col2 = st.columns(2)
        with col1:
            st.write('1. Applicant Income')
            st.line_chart(data['ApplicantIncome'])
            st.write('3. Loan Amount')
            st.line_chart(data['LoanAmount'])
            st.write('5. Credit History')
            st.line_chart(data['Credit_History'])
            st.write('7. Count of Loan Status')
            st.bar_chart(data['Loan_Status'].value_counts())
            st.write('9. Count of Gender')
            st.bar_chart(data['Gender'].value_counts(), color=(175, 238, 238))  # RGB equivalent of 'paleturquoise'
            st.write('11. Count of Education')
            st.bar_chart(data['Education'].value_counts(), color=(255, 192, 203))  # RGB equivalent of 'pink'
            st.write('13. Count of Married')
            st.bar_chart(data['Married'].value_counts(), color=(0, 0, 255))  # RGB equivalent of 'blue'
            st.write('15. Gender vs Loan Status')
            st.scatter_chart(data, x='Gender', y='Loan_Status')
            st.write('17. Married vs Loan Status')
            st.line_chart(data, x='Married', y='Loan_Status')

        with col2:
            st.write('2. Co-Applicant Income')
            st.line_chart(data['CoapplicantIncome'])
            st.write('4. Loan Amount Term')
            st.line_chart(data['Loan_Amount_Term'])
            st.write('6. Count of Dependents')
            st.bar_chart(data['Dependents'].value_counts(), color=(0, 255, 0))
            st.write('8. Count of Credit History')
            st.bar_chart(data['Credit_History'].value_counts(), color=(255, 255, 0))  # RGB equivalent of 'yellow'
            st.write('10. Count of Property Area')
            st.bar_chart(data['Property_Area'].value_counts(), color=(255, 165, 0))  # RGB equivalent of 'orange'
            st.write('12. Count of Self Employed')
            st.bar_chart(data['Self_Employed'].value_counts(), color=(255, 0, 0))  # RGB equivalent of 'red'
            st.write('14. Count of Dependents')
            st.bar_chart(data['Dependents'].value_counts(), color=(0, 255, 0))  # RGB equivalent of 'lime'
            st.write('16. Education vs Loan Status')
            st.line_chart(data, x='Education', y='Loan_Status')
            st.write('18. Property Area vs Loan Status')
            st.scatter_chart(data, x='Property_Area', y='Loan_Status')
    if menu=='Model':
        st.write('This is the graph of the model training')
        models= st.radio('Select the model',['Logistic Regression','Random Forest','Decision Tree','Linear Discriminant Analysis','Support Vector Classifier','K- Neirest Neighbour','Naive Bayes'])
        st.markdown('----')
        if models=='Logistic Regression':
            #info about the model
            st.write('Logistic Regression is a classification algorithm used to assign observations to a discrete set of classes. Unlike linear regression which outputs continuous number values, logistic regression transforms its output using the logistic sigmoid function to return a probability value which can then be mapped to two or more discrete classes.')
            #image of the model
            st.image("https://images.spiceworks.com/wp-content/uploads/2022/04/11040521/46-4-e1715636469361.png")
            #confusion matrix
            st.write('Confusion Matrix')
            st.image("Model/1.png")
        if models=='Random Forest':
            #info about the model
            st.write('Random Forest is a supervised learning algorithm. The "forest" it builds, is an ensemble of decision trees, usually trained with the “bagging” method. The general idea of the bagging method is that a combination of learning models increases the overall result.')
            #image of the model
            st.image("https://images.javatpoint.com/tutorial/machine-learning/images/random-forest-algorithm.png")
            st.image('Model/2.png')
        if models=='Decision Tree':
            #info about the model
            st.write('A decision tree is a flowchart-like tree structure where an internal node represents a feature(or attribute), the branch represents a decision rule, and each leaf node represents the outcome. The topmost node in a decision tree is known as the root node.')
            #image of the model
            st.image("https://images.javatpoint.com/tutorial/machine-learning/images/decision-tree-classification-algorithm.png")
            st.image('Model/3.png')
        if models=='Linear Discriminant Analysis':
            #info about the model
            st.write('Linear Discriminant Analysis (LDA) is a dimensionality reduction technique used as a pre-processing step in Machine Learning and pattern classification applications. The goal of LDA is to project a feature space (a dataset n-dimensional samples) onto a smaller subspace k (where k≤n−1) while maintaining the class-discriminatory information.')
            #image of the model
            st.image("https://media.licdn.com/dms/image/v2/C4D12AQHnj8ho2kN_qQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1613927657941?e=2147483647&v=beta&t=8p-MS_99xloplyq5p2UHip1DMQ9siXdqNKw9dkOuec8")
            st.image('Model/4.png')
        if models=='Support Vector Classifier':
            #info about the model
            st.write('Support Vector Machine (SVM) is a supervised machine learning algorithm that can be employed for both classification and regression purposes. SVMs are more commonly used in classification problems and as such, this is what we will focus on in this post.')
            #image of the model
            st.image("https://images.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm.png")
            st.image('Model/5.png')
        if models=='K- Neirest Neighbour':
            #info about the model
            st.write('The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and regression problems.')
            #image of the model
            st.image("https://images.javatpoint.com/tutorial/machine-learning/images/k-nearest-neighbor-algorithm-for-machine-learning2.png")
            st.image('Model/6.png')
        if models=='Naive Bayes':
            #info about the model
            st.write('Naive Bayes is a simple technique for constructing classifiers: models that assign class labels to problem instances, represented as vectors of feature values, where the class labels are drawn from some finite set.')
            #image of the model
            st.image("https://miro.medium.com/v2/resize:fit:1200/0*0sObCvaI0oijvekS.png")
            st.image('Model/7.png')
def user_home_page():
    # Navigation menu for user dashboard
    with st.sidebar:
        selected_tab = option_menu(
            menu_title=None,
            options=["User Profile", "Visualizations", "Bank Loan",'Logout'],
            icons=['person','bar-chart','bank'], menu_icon="cast", default_index=0,
        styles={
        "nav-link-selected": {"background-color": "skyblue", "color": "black", "border-radius": "5px"},
        }
        )
    if selected_tab == "User Profile":
        user_profile()
    elif selected_tab == "Bank Loan":
        loan_page()
    elif selected_tab == "Visualizations":
        visualizations_page()
    elif selected_tab=='Logout':
        # Logout functionality
        st.session_state.clear()  # Clear session state to "log out"
        st.experimental_rerun()
