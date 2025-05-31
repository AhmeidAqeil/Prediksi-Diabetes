import streamlit as st
import numpy as np
import joblib
import tensorflow as tf

# Load model dan scaler
model = tf.keras.models.load_model("diabetes_model.h5")
scaler = joblib.load("scaler.pkl")

st.title("Prediksi Diabetes")

# Input form
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("Prediksi"):
    user_input = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    scaled_input = scaler.transform(user_input)
    pred = model.predict(scaled_input)
    result = int(pred[0] > 0.5)

    st.success("Hasil: Diabetes" if result == 1 else "Hasil: Tidak Diabetes")
