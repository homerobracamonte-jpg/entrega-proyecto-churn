import streamlit as st
import pandas as pd
import joblib

model = joblib.load("modelo_final.pkl")

st.title("Predicción de Churn")

tenure = st.number_input("Meses de contrato", 0, 100)
monthly = st.number_input("Pago mensual", 0, 200)

input_data = pd.DataFrame([[tenure, monthly]],
                          columns=["tenure", "MonthlyCharges"])

if st.button("Predecir"):
    pred = model.predict(input_data)

    if pred[0] == 1:
        st.error("El cliente se va ❌")
    else:
        st.success("El cliente se queda ✔")
