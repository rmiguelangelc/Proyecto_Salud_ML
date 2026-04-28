import pandas as pd
import xgboost as xgb
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle # Para guardar el modelo después

 
engine = create_engine('sqlite:///salud_deportiva.db')
df = pd.read_sql("SELECT * FROM datos_pacientes", engine)

 
X = df.drop('Diabetes_012', axis=1)
y = df['Diabetes_012']

 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Iniciando entrenamiento con XGBoost...")

 
modelo_xgb = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    objective='multi:softmax',
    num_class=3,
    random_state=42,
    tree_method='hist'  
)

modelo_xgb.fit(X_train, y_train)
 
preds = modelo_xgb.predict(X_test)
accuracy = accuracy_score(y_test, preds)

print(f"\n--- RESULTADOS DEL MODELO ---")
print(f"Precisión (Accuracy): {accuracy:.4f}")
print("\nReporte de Clasificación:")
print(classification_report(y_test, preds))

 
with open('asistente_salud_model.pkl', 'wb') as f:
    pickle.dump(modelo_xgb, f)

print("\n Modelo guardado como 'asistente_salud_model.pkl'")