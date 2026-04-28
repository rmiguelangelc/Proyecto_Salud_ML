import pandas as pd
import os
from sqlalchemy import create_engine


ruta_actual = os.path.dirname(__file__)

file_name = os.path.join(ruta_actual, "diabetes_012_health_indicators_BRFSS2015.csv")

try:
    #CSV
    df = pd.read_csv(file_name)
    print("--- REPORTE DE INGESTA ---")
    print(f" Archivo encontrado y cargado.")
    print(f" Total de registros: {len(df)}") 
    print(f" Columnas detectadas: {len(df.columns)}") 
    
    engine = create_engine('sqlite:///salud_deportiva.db')
    df.to_sql('datos_pacientes', engine, if_exists='replace', index=False)
    
    print(" Base de datos SQL creada .")

except FileNotFoundError:
    print(f" Error: No se encontró el archivo en la ruta: {file_name}")
    print("Asegurar de que el archivo tenga la extensión .csv al final.")