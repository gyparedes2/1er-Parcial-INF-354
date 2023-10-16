#Escalamiento de Características: 
#Para muchas técnicas de aprendizaje automático, es importante que las características tengan la misma escala.
#El escalado estandariza las características, lo que puede mejorar el rendimiento de estos modelos.
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos
data = pd.read_csv("wine-quality-white-and-red.csv")

# Seleccionar todas las columnas numéricas
columnas_numericas = data.select_dtypes(include=['number'])

# Escalamiento de Características para todas las columnas numéricas
#El escalado estándar (StandardScaler) reescala las características de tal manera que 
# tengan una media igual a 0 y una desviación estándar igual a 1. 
scaler = StandardScaler()
data[columnas_numericas.columns] = scaler.fit_transform(columnas_numericas)

# Imprimir el resultado
print(data.head())
