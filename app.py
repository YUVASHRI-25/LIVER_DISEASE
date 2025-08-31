import pickle
import streamlit as st
import numpy as np

# Load the model and scaler from the pickle file
scaler, model = pickle.load(open("best_rf_model_and_scaler.pkl", "rb"))

# Streamlit app title
st.title("🍷 Liver Disease Classification App")
st.write("Enter patient details to predict liver disease risk")

# Collect user inputs
Age = st.number_input("Age", min_value=1, max_value=100, value=45)
Gender = st.selectbox("Gender", ["Male", "Female"])
Total_Bilirubin = st.number_input("Total Bilirubin", min_value=0.0, value=2.4)
Direct_Bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, value=1.1)
Alkaline_Phosphotase = st.number_input("Alkaline Phosphotase", min_value=0, value=168)
Alamine_Aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0, value=33)
Aspartate_Aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0, value=50)
Total_Protiens = st.number_input("Total Proteins", min_value=0.0, value=5.1)
Albumin = st.number_input("Albumin", min_value=0.0, value=2.6)
AG_Ratio = st.number_input("Albumin/Globulin Ratio", min_value=0.0, value=1.0)

# Convert gender to numeric (Male=1, Female=0)
Gender_num = 1 if Gender == "Male" else 0

# Collect all features into a numpy array
features = np.array([[Age, Gender_num, Total_Bilirubin, Direct_Bilirubin,
                      Alkaline_Phosphotase, Alamine_Aminotransferase,
                      Aspartate_Aminotransferase, Total_Protiens,
                      Albumin, AG_Ratio]])

# Scale the features using the loaded scaler
features_scaled = scaler.transform(features)

# Make predictions when the user clicks the button
if st.button("🔍 Predict"):
    proba = model.predict_proba(features_scaled)[0][1]  # Get the probability for the positive class
    
    if proba >= 0.55:  # If the probability is greater than 0.55, classify as high risk
        st.error(f"⚠️ High Risk of Liver Disease(2)(Probability: {proba:.2f})")
    else:  # If the probability is less than 0.55, classify as low risk
        st.success(f"✅ Low Risk of Liver Disease (1)(Probability: {proba:.2f})")

