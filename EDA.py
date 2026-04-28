import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

 
engine = create_engine('sqlite:///salud_deportiva.db')
df = pd.read_sql("SELECT * FROM datos_pacientes", engine)

 
print("Columnas detectadas:", df.columns.tolist())

 
target = 'Diabetes_012' 

 
plt.figure(figsize=(10, 12))
 
correlaciones = df.corr()[target].sort_values(ascending=False).to_frame()
sns.heatmap(correlaciones, annot=True, cmap='magma')
plt.title(f"Impacto de los Factores en: {target}")
plt.show()

 
plt.figure(figsize=(10, 6))
sns.boxplot(x='PhysActivity', y='BMI', hue=target, data=df)
plt.title("Relación entre Actividad Física, IMC y Diabetes")
plt.xlabel("Realiza Actividad Física (0=No, 1=Sí)")
plt.show()

 
resumen = df.groupby(target)[['BMI', 'Age', 'PhysActivity']].mean()
print("\n--- Promedios por Categoría de Salud ---")
print(resumen)