import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open("Parkinosis_classifer.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Parkinosis Disease Prediction")
st.write("Enter patient details to predict classification.")

# Define input fields

MDVP_Fo_Hz = st.number_input("MDVP_Fo_Hz", value=154.228641)
MDVP_Fhi_Hz = st.number_input("MDVP_Fhi_Hz", value=197.104918)

MDVP_Flo_Hz = st.number_input("MDVP_Flo_Hz", value=116.324631)
MDVP_Jitter_perc = st.number_input("MDVP_Jitter_perc", value=0.006220)
MDVP_Jitter_Abs = st.number_input("MDVP_Jitter_Abs", value=0.000044)
MDVP_RAP = st.number_input("MDVP_RAP", value=0.003306)
MDVP_PPQ = st.number_input("MDVP_PPQ", value=0.003446)
Jitter_DDP = st.number_input("Jitter_DDP", value=0.009920)
MDVP_Shimmer = st.number_input("MDVP_Shimmer", value=0.029709)
MDVP_Shimmer_dB = st.number_input("MDVP_Shimmer_dB", value=0.282251)
Shimmer_APQ3 = st.number_input("Shimmer_APQ3", value=0.015664)

Shimmer_APQ5 = st.number_input("Shimmer_APQ5", value=0.017878)

MDVP_APQ = st.number_input("MDVP_APQ", value=0.024081)

Shimmer_DDA = st.number_input("Shimmer_DDA", value=0.046993)

NHR = st.number_input("NHR", value=0.024847)
HNR = st.number_input("HNR", value=21.885974)
RPDE = st.number_input("RPDE", value=0.498536)
DFA = st.number_input("DFA", value=0.718099)
spread1 = st.number_input("spread1", value=-5.684397)
spread2 = st.number_input("spread2", value=0.226510)

D2 = st.number_input("D2", value=2.381826)
PPE = st.number_input("PPE", value=0.206552)


# Create an input array
input_data = np.array(
    [
        [
            MDVP_Fo_Hz,
            MDVP_Fhi_Hz,
            MDVP_Flo_Hz,
            MDVP_Jitter_perc,
            MDVP_Jitter_Abs,
            MDVP_RAP,
            MDVP_PPQ,
            Jitter_DDP,
            MDVP_Shimmer,
            MDVP_Shimmer_dB,
            Shimmer_APQ3,
            Shimmer_APQ5,
            MDVP_APQ,
            Shimmer_DDA,
            NHR,
            HNR,
            RPDE,
            DFA,
            spread1,
            spread2,
            D2,
            PPE,
        ]
    ]
)

# Prediction Button
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.error(f"Prediction: Parkinosis Disease Found {prediction[0]}")
    else:
        st.success(f"Prediction: Parkinosis Disease Not Found {prediction[0]}")
