# Arquitectura de la Solución: Churn en Telecomunicaciones

El sistema se organiza en tres capas:
1. Capa de Datos: Contiene los datos originales (data/raw) y procesados (data/processed).
2. Capa de Modelado: Contiene el modelo serializado (models/modelo_final.pkl) y sus métricas (models/model_metadata.json).
3. Capa de Visualización: Aplicación en Streamlit (app_final.py) que carga el modelo para realizar predicciones.

Flujo: El usuario ingresa datos en la app, la app consulta el modelo, y se muestra si el cliente es probable que abandone el servicio.
