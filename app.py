import streamlit as st
import pandas as pd
import joblib

# Cargamos el archivo del modelo
model = joblib.load("modelo_final (2).pkl")

st.title("Predicción de Churn")

tenure = st.number_input("Meses como cliente", min_value=0, value=12)
monthly_charges = st.number_input("Cargo mensual", min_value=0.0, value=50.0)

# El botón de predecir
if st.button("Predecir"):
    input_data = pd.DataFrame([[tenure, monthly_charges]], columns=["tenure", "MonthlyCharges"])
    pred = model.predict(input_data)
    
    if pred[0] == 1:
        st.error("El cliente se va ❌")
    else:
        st.success("El cliente se queda ✔")
