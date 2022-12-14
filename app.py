import streamlit as st
import pandas as pd
import pickle
st.write("""
# My Graded Assignment
""")
st.header('User Input Parameters')
with st.form(key = '1div'):
    col1,col2,col3 =st.columns([3,2,1])
    with col1:
        number1 = st.number_input("NUMERATOR")
    with col2:
        number2 = st.number_input("DENOMINATOR")
    with col3:
        st.text("Answer")
        submit =st.form_submit_button(label='Calculate')
st.write("""
# Division
""")        
if submit:
    with st.expander("Results"):
        ans = (number1 / number2)
        st.write(" Answer ===>",ans)
       
