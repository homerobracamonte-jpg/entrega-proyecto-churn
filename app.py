import streamlit as st
import pandas as pd
import joblib

model = joblib.load("modelo_final (2).pkl")

# Mostrar las variables que espera el modelo
st.write("Variables esperadas por el modelo:")
st.write(model.feature_names_in_)

st.title("Predicción de Churn")

internet = st.selectbox(
    "Tipo de Internet",
    [0, 1, 2]
)

input_data = pd.DataFrame(
    [[internet]],
    columns=["InternetService"]
)

if st.button("Predecir"):
    pred = model.predict(input_data)

    if pred[0] == 1:
        st.error("El cliente se va ❌")
    else:
        st.success("El cliente se queda ✔")
