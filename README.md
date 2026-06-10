Proyecto Integrador: Predicción de Churn de Clientes
Descripción del Proyecto

El objetivo de este proyecto es analizar y predecir la fuga de clientes (Churn) utilizando técnicas de Ciencia de Datos y Machine Learning.

La predicción de Churn permite identificar clientes con mayor probabilidad de abandonar el servicio, facilitando la toma de decisiones para mejorar la retención de clientes.

Dataset

Se utilizó el dataset Telco Customer Churn, que contiene información demográfica, contractual y de consumo de clientes de una empresa de telecomunicaciones.

Variables relevantes utilizadas en el proyecto:

tenure: meses de permanencia del cliente.
MonthlyCharges: cargo mensual del servicio.
InternetService: tipo de servicio de internet.
Churn: variable objetivo que indica si el cliente abandona o permanece.
Metodología
1. Exploración de Datos
Análisis de dimensiones del dataset.
Identificación de valores faltantes.
Visualización de patrones de abandono.
Análisis descriptivo de variables.
2. Limpieza y Preparación
Conversión de variables categóricas.
Selección de variables relevantes.
Preparación de los datos para modelado.
3. Entrenamiento del Modelo

Se implementaron y compararon los siguientes modelos:

Random Forest Classifier
Decision Tree Classifier
4. Evaluación

La métrica principal utilizada fue F1-Score Macro.

Resultados obtenidos:

Random Forest: F1-Score = 0.42
Decision Tree: F1-Score = 0.42
Dashboard Streamlit

La aplicación permite ingresar datos del cliente y obtener una predicción de abandono utilizando el modelo entrenado.

Estructura del Repositorio
01_exploracion.ipynb
02_eda_limpieza.ipynb
03_modelado.ipynb
Proyecto_Churn_Final.ipynb
app.py
modelo_final.pkl
requirements.txt
README.md
Consideraciones Éticas

El modelo puede presentar errores de clasificación y debe utilizarse únicamente como apoyo para la toma de decisiones. Los resultados no deben emplearse como criterio único para determinar acciones sobre los clientes.


Homero Bracamonte
