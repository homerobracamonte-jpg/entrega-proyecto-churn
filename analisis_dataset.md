# Análisis Cualitativo del Dataset

## Descripción general
El proyecto utiliza el dataset "Telco Customer Churn", obtenido de Kaggle. Este conjunto de datos captura información demográfica y de servicios de 7,043 clientes de una empresa de telecomunicaciones, con el fin de analizar el fenómeno de abandono (churn).

## Estructura y Variables
El dataset cuenta con 21 variables, incluyendo datos de servicios (Internet, telefonía), tipo de contrato, cargos mensuales y la variable objetivo 'Churn'.

## Calidad y Pertinencia
Tras una revisión exploratoria, el dataset es pertinente para responder a la pregunta analítica, ya que contiene la información necesaria para clasificar el riesgo de abandono. No se detectaron inconsistencias graves. Las principales limitaciones son el desbalance de clases (hay más clientes que se quedan que los que se van), lo cual será gestionado mediante métricas de evaluación como el F1-score.