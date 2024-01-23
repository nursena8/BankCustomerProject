import streamlit as st
import pandas as pd
import joblib
import numpy as np
from streamlit.components.v1 import html
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(current_directory, "gbm_model_production.joblib")

st.set_page_config(page_title="Customer Churn Prediction App", page_icon=":bar_chart:")

class_report_path = os.path.join(current_directory, "class_report.html")
data_quality_report_path = os.path.join(current_directory, "data_quality_report.html")
general_report_path = os.path.join(current_directory, "report.html")
image_path = os.path.join(current_directory, "machine.jpg")
st.sidebar.markdown("---")
st.sidebar.markdown("# Navigation")
page = st.sidebar.radio("Select a report", ["Prediction","Class Report", "Data Quality Report", "General Report"])
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by Nursena")
st.sidebar.markdown("---")


if page == "Prediction":
    st.markdown("## Customer Churn Prediction")
    st.write("Enter customer information to get predictions.")
    credit_score = st.text_input("Credit score 300-850", "850")
    tenure = st.selectbox("Choose year amount of the spent at the bank", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    age = st.slider("Choose age", 18, 92)
    balance = st.slider("Choose amount of account", 0.0, 200000.0)
    estimated_salary = st.slider("Choose amount of estimated_salary", 0.0, 200000.0)
    products_number = st.slider("Choose number of products", 0, 4)


    if st.button("Predict"):
        loaded_model  = joblib.load(model_file_path)
        row = np.array([credit_score, tenure, age, balance, estimated_salary, products_number]).reshape(1, -1)
        prediction = loaded_model.predict(row)
        if prediction[0] == 1:
            st.success("This customer is likely to leave. :thumbsup:")
        elif prediction[0] == 0:
            st.success("This customer is likely to stay. :thumbsup:")
        else:
            st.error("Try again later")
        
elif page == "Class Report":
    st.markdown("## Class Report")
    with open(class_report_path, "r") as file:
        class_html_content = file.read()
    st.components.v1.html(class_html_content, height=3000)

elif page == "Data Quality Report":
    st.markdown("## Data Quality Report")
    with open(data_quality_report_path, "r") as file:
        data_quality_html_content = file.read()
    st.components.v1.html(data_quality_html_content, height=800)

elif page == "General Report":
    st.markdown("## General Report")
    with open(general_report_path, "r") as file:
        general_html_content = file.read()
    st.components.v1.html(general_html_content, height=2000)
#!wget -q -O - ipv4.icanhazip.com
#!streamlit run app.py & npx localtunnel --port 8501
# if you want to run this on your local you can learn first ipv4 adress