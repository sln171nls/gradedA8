import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle
st.write("""
# My Graded Assignment
""")
st.header('User Input Parameters')
def user_input_features():
    number1 = st.number_input("AMT_NUMERATOR",min_value=2000000.0,max_value=2000000.0)
    number2 = st.number_input("AMT_DENOMINATOR",min_value=2000000.0,max_value=2000000.0)
