import streamlit as st
import pandas as pd
import pickle
import numpy as np


st.set_page_config(page_title="Asistente Salud IA", page_icon=None)
st.title(" Asistente Inteligente de Salud")
st.markdown("""
Analiza tu riesgo preventivo de diabetes basado en hábitos de vida. 
*Este modelo utiliza XGBoost con un 85% de precisión.*
""")

 
try:
    with open('asistente_salud_model.pkl', 'rb') as f:
        modelo = pickle.load(f)
except FileNotFoundError:
    st.error("No se encontró el archivo 'asistente_salud_model.pkl'. Asegúrate de haber corrido modelo.py primero.")

 
st.sidebar.header("Tus Datos de Salud")
bmi = st.sidebar.slider("Tu IMC (BMI)", 10.0, 60.0, 25.0)
gen_hlth = st.sidebar.slider("Salud General (1: Excelente - 5: Mala)", 1, 5, 2)
phys_activity = st.sidebar.radio("¿Haces actividad física?", [1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
age = st.sidebar.slider("Rango de Edad (Nivel 1-13)", 1, 13, 5)

# Botón de predicción
if st.button("Analizar Riesgo"):
    
    input_data = np.zeros((1, 21))
    input_data[0, 3] = bmi          
    input_data[0, 14] = gen_hlth     
    input_data[0, 8] = phys_activity 
    input_data[0, 18] = age          
    
    prediccion = modelo.predict(input_data)[0]
    
     
    st.subheader("Resultado:")
    if prediccion == 0:
        st.success(" **Riesgo Bajo:** Tus hábitos muestran un perfil saludable.")
    elif prediccion == 1:
        st.warning(" **Riesgo Moderado (Pre-diabetes):** Considera mejorar tu actividad física y alimentación.")
    else:
        st.error(" **Riesgo Alto:** Es importante que consultes a un médico para un chequeo preventivo.")