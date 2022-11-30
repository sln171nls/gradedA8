import streamlit as st
import pandas as pd
import pickle
st.write("""
# My Graded Assignment
""")
st.header('User Input Parameters')
def user_input_features():
    number1 = st.number_input("AMT_NUMERATOR",min_value=-2000000.0,max_value=2000000.0)
    number2 = st.number_input("AMT_DENOMINATOR",min_value=-2000000.0,max_value=2000000.0)
    
    data = {
            'AMT_NUMERATOR': number1,
            'AMT_DENOMINATOR': number2,
            'AMT': number1/number2
           }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
st.subheader('Division Answer')
st.write(df.to_dict())
