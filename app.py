import streamlit as st
import joblib

model = joblib.load("modelo_final (2).pkl")

st.write("Tipo de modelo:", type(model))

if hasattr(model, "feature_names_in_"):
    st.write("Columnas esperadas:")
    st.write(list(model.feature_names_in_))
else:
    st.write("El modelo no tiene feature_names_in_")
