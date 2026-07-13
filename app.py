import streamlit as st
import joblib
import pandas as pd

# Load saved model and feature names
model = joblib.load("breast_cancer_model.jb")
feature_names = joblib.load("feature_names.jb")

st.title("Breast Cancer Detection")
st.write("Enter the diagnostic values below to predict whether the tumor is benign or malignant.")

# Create input fields
user_data = {}

for feature in feature_names:
    user_data[feature] = st.slider(
        feature,
        min_value=1,
        max_value=10,
        value=5
    )

# Convert input to DataFrame
input_data = pd.DataFrame([user_data])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 2:
        st.success("The tumor is predicted as Benign.")
    elif prediction[0] == 4:
        st.error("The tumor is predicted as Malignant.")
    else:
        st.info(f"Predicted Class: {prediction[0]}")