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
from english import english_page
from telugu import telugu_page
def user_home_page():
    # Navigation menu for user dashboard
    user_data = st.session_state.get('user', ['', 'Unknown', 'Unknown'])
    user_data=get_user_by_email(user_data[2])
    language=user_data[26]
    if language=='English':
        english_page()
    if language=='Telugu':
        telugu_page()