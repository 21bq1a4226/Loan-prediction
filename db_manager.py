import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    #drop table
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            gender TEXT,
            weight INTEGER,
            hereditary_disease TEXT,
            age INTEGER,
            smoking TEXT,
            regular_bp_level INTEGER,
            diabetes TEXT,
            regular_exercise TEXT,
            marital_status TEXT,
            no_of_dependents INTEGER,
            education TEXT,
            employment TEXT,
            property_status TEXT,
            credit_score INTEGER,
            credit_history TEXT,
            annual_income INTEGER,
            co_applicant_annual_income INTEGER,
            loan_amount INTEGER,
            loan_duration INTEGER,
            existing_loan TEXT,
            existing_loan_amount INTEGER,
            existing_loan_duration INTEGER,
            existing_loan_type TEXT,
            language TEXT,
            otp INTEGER,
            password TEXT 
        )
    """)
    conn.commit()
    conn.close()

# Register a new user
def register_user(name, email, gender, weight, hereditary_disease, age, smoking, regular_bp_level, diabetes, regular_exercise, marital_status, no_of_dependents, education, employment, property_status, credit_score, credit_history, annual_income, co_applicant_annual_income, loan_amount, loan_duration, existing_loan, existing_loan_amount, existing_loan_duration, existing_loan_type, language,otp, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, gender, weight, hereditary_disease, age, smoking, regular_bp_level, diabetes, regular_exercise, marital_status, no_of_dependents, education, employment, property_status, credit_score, credit_history, annual_income, co_applicant_annual_income, loan_amount, loan_duration, existing_loan, existing_loan_amount, existing_loan_duration, existing_loan_type, language,otp, password) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, email, gender, weight, hereditary_disease, age, smoking, regular_bp_level, diabetes, regular_exercise, marital_status, no_of_dependents, education, employment, property_status, credit_score, credit_history, annual_income, co_applicant_annual_income, loan_amount, loan_duration, existing_loan, existing_loan_amount, existing_loan_duration, existing_loan_type, language,otp, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Validate login credentials
def validate_user(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Get user by email
def get_user_by_email(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user(user_id, weight, hereditary_disease, age, smoking, regular_bp_level, 
                diabetes, regular_exercise, marital_status, no_of_dependents, education, employment, 
                property_status, credit_score, credit_history, annual_income, co_applicant_annual_income, 
                loan_amount, loan_duration, existing_loan, existing_loan_amount, existing_loan_duration, 
                existing_loan_type, language):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL update query using the user_id to update the user's details
    cursor.execute("""
        UPDATE users
        SET weight = ?, 
            hereditary_disease = ?, 
            age = ?, 
            smoking = ?, 
            regular_bp_level = ?, 
            diabetes = ?, 
            regular_exercise = ?, 
            marital_status = ?, 
            no_of_dependents = ?, 
            education = ?, 
            employment = ?, 
            property_status = ?, 
            credit_score = ?, 
            credit_history = ?, 
            annual_income = ?, 
            co_applicant_annual_income = ?, 
            loan_amount = ?, 
            loan_duration = ?, 
            existing_loan = ?, 
            existing_loan_amount = ?, 
            existing_loan_duration = ?, 
            existing_loan_type = ?, 
            language = ?
        WHERE id = ?  -- This ensures that we update the record corresponding to the correct user_id
    """, (weight, hereditary_disease, age, smoking, regular_bp_level, diabetes, regular_exercise, marital_status, 
          no_of_dependents, education, employment, property_status, credit_score, credit_history, annual_income, 
          co_applicant_annual_income, loan_amount, loan_duration, existing_loan, existing_loan_amount, 
          existing_loan_duration, existing_loan_type, language, user_id))
    
    conn.commit()
    conn.close()
    return True

def update_otp(email,otp):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET otp = ? WHERE email = ?", (otp, email))
    conn.commit()
    conn.close()
    return True

def get_otp(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT otp FROM users WHERE email = ?", (email,))
    otp = cursor.fetchone()
    conn.close()
    return otp

def valid_user(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False
    
def update_password(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE email = ?", (password, email))
    conn.commit()
    conn.close()
    return True

def fetch_password(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    password = cursor.fetchone()
    conn.close()
    return password
    
