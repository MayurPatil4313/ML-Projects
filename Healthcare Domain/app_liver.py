import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open("Liver_classifer.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Chronic Liver Disease Prediction")
st.write("Enter patient details to predict classification.")

# Define input fields

age = st.number_input("Age", value=50)
gender = st.selectbox("Gender ", ["Male", "Female"])
Total_Bilirubin = st.number_input("Total_Bilirubin", value=3.321754)
Direct_Bilirubin = st.number_input("Direct_Bilirubin", value=1.497544)
Alkaline_Phosphotase = st.number_input("Alkaline_Phosphotase", value=291.750877)
Alamine_Aminotransferase = st.number_input("Alamine_Aminotransferase", value=79.728070)
Aspartate_Aminotransferase = st.number_input("Aspartate_Aminotransferase", value=109.380702)
Albumin = st.number_input("Albumin", value=3.148947)

Total_Protiens = st.number_input("Total_Protiens", value=6.496316)
Albumin_and_Globulin_Ratio = st.number_input("Albumin_and_Globulin_Ratio", value=0.948004)


# Convert categorical values to numerical format
mapping = {"Male": 1, "Female": 0}

gender = mapping[gender]


# Create an input array
input_data = np.array([[ age, gender, Total_Bilirubin ,Direct_Bilirubin , Alkaline_Phosphotase , Alamine_Aminotransferase , 
                        Aspartate_Aminotransferase , Albumin  , Total_Protiens , Albumin_and_Globulin_Ratio]])

# Prediction Button
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.error(f"Prediction: Chronic Liver Disease Found {prediction[0]}")
    else:
        st.success(f"Prediction: Chronic Liver Disease Not Found {prediction[0]}")

