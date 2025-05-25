import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open("randomforest.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Chronic Kidney Disease Prediction")
st.write("Enter patient details to predict classification.")

# Define input fields

age = st.number_input("Age", value=50)
bp = st.number_input("Blood Pressure", value=80)
sg = st.number_input("Specific Gravity", value=1.02)
al = st.number_input("Albumin", value=0)
su = st.number_input("Sugar", value=0)
rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["present", "not present"])
ba = st.selectbox("Bacteria", ["present", "not present"])
bgr = st.number_input("Blood Glucose Random", value=100)
bu = st.number_input("Blood Urea", value=30)
sc = st.number_input("Serum Creatinine", value=1.2)
sod = st.number_input("Sodium", value=135)
pot = st.number_input("Potassium", value=4.5)
hemo = st.number_input("Hemoglobin", value=15)
pcv = st.number_input("Packed Cell Volume", value=40)
wc = st.number_input("White Blood Cell Count", value=8000)
rc = st.number_input("Red Blood Cell Count", value=5.2)
htn = st.selectbox("Hypertension", ["yes", "no"])
dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
appet = st.selectbox("Appetite", ["good", "poor"])
pe = st.selectbox("Pedal Edema", ["yes", "no"])
ane = st.selectbox("Anemia", ["yes", "no"])

# Convert categorical values to numerical format
mapping = {"normal": 1, "abnormal": 0, "present": 1, "not present": 0, "yes": 1, "no": 0, "good": 1, "poor": 0}

rbc = mapping[rbc]
pc = mapping[pc]
pcc = mapping[pcc]
ba = mapping[ba]
htn = mapping[htn]
dm = mapping[dm]
cad = mapping[cad]
appet = mapping[appet]
pe = mapping[pe]
ane = mapping[ane]

# Create an input array
input_data = np.array([[ age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])

# Prediction Button
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.error(f"Prediction: Chronic Kidney Disease Found {prediction[0]}")
    else:
        st.success(f"Prediction: Not Chronic Kidney Disease Not Found {prediction[0]}")

# import pickle
# import streamlit as st
 
# # loading the trained model
# pickle_in = open('randomforest.pkl', 'rb') 
# classifier = pickle.load(pickle_in)
 
# @st.cache()
  
# # defining the function which will make the prediction using the data which the user inputs 
# def prediction(age, wc, htn, dm):   
 
#     # Pre-processing user input    
#     if htn == "no":
#         htn = 0
#     else:
#         htn = 1
 
#     if dm == "no":
#         dm = 0
#     else:
#         dm = 1
 
      
#     # Making predictions 
#     prediction = classifier.predict( 
#         [[age, wc, htn, dm]])
     
#     if prediction == 0:
#         pred = 'Kidney Disease not detected'
#     else:
#         pred = 'Kidny Disease found'
#     return pred
      
  
# # this is the main function in which we define our webpage  
# def main():       
#     # front end elements of the web page 
#     html_temp = """ 
#     <div style ="background-color:cyan;padding:13px"> 
#     <h1 style ="color:black;text-align:center;">Kidney Disease Prediction</h1> 
#     </div> 
#     """
      
#     # display the front end aspect
#     st.markdown(html_temp, unsafe_allow_html = True) 
      
#     # following lines create boxes in which user can enter data required to make prediction 
#     htn = st.selectbox('htn',("no","yes"))
#     dm = st.selectbox('dm Status',("no","yes")) 
#     age = st.number_input("AGE") 
#     wc = st.number_input("WC")
#     result =""
      
#     # when 'Predict' is clicked, make the prediction and store it 
#     if st.button("Predict"): 
#         result = prediction(age, wc, htn, dm) 
#         st.success('Report Results: {}'.format(result))
        
     
# if __name__=='__main__': 
#     main()