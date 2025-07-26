# app.py

import streamlit as st # type: ignore
import pandas as pd
import joblib
model = joblib.load("C:/Users/ASUS/Desktop/ml-streamlit-deployment/notebooks/ML_STREAMLIT_DEPLOYMENT_model.pkl")

# App title
st.title("🍷 Wine Quality Prediction App")

# Sidebar inputs
st.sidebar.header("Input Wine Characteristics")

# Define feature inputs
def user_input_features():
    fixed_acidity = st.sidebar.slider("Fixed Acidity", 4.0, 16.0, 8.0)
    volatile_acidity = st.sidebar.slider("Volatile Acidity", 0.1, 1.5, 0.5)
    citric_acid = st.sidebar.slider("Citric Acid", 0.0, 1.0, 0.3)
    residual_sugar = st.sidebar.slider("Residual Sugar", 0.5, 15.0, 2.5)
    chlorides = st.sidebar.slider("Chlorides", 0.01, 0.2, 0.05)
    free_sulfur_dioxide = st.sidebar.slider("Free Sulfur Dioxide", 1, 72, 15)
    total_sulfur_dioxide = st.sidebar.slider("Total Sulfur Dioxide", 6, 289, 46)
    density = st.sidebar.slider("Density", 0.9900, 1.0050, 0.9960)
    pH = st.sidebar.slider("pH", 2.5, 4.5, 3.2)
    sulphates = st.sidebar.slider("Sulphates", 0.3, 2.0, 0.6)
    alcohol = st.sidebar.slider("Alcohol", 8.0, 15.0, 10.0)

    data = {
        'fixed acidity': fixed_acidity,
        'volatile acidity': volatile_acidity,
        'citric acid': citric_acid,
        'residual sugar': residual_sugar,
        'chlorides': chlorides,
        'free sulfur dioxide': free_sulfur_dioxide,
        'total sulfur dioxide': total_sulfur_dioxide,
        'density': density,
        'pH': pH,
        'sulphates': sulphates,
        'alcohol': alcohol
    }

    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Show input values
st.subheader("Wine Features Provided:")
st.write(input_df)

# Prediction
if st.button("Predict Quality"):
    prediction = model.predict(input_df)
    st.subheader("Predicted Wine Quality Score:")
    st.success(f"{int(prediction[0])} / 10")
