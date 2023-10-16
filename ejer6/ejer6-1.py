# Tratamiento de Valores Nulos:
# Garantiza que no haya valores faltantes en las características para evitar errores
# o sesgos en el análisis y la construcción de modelos.

import pandas as pd
from sklearn.impute import SimpleImputer

# Cargar el conjunto de datos
data = pd.read_csv("wine-quality-white-and-red.csv")

# Tratamiento de Valores Nulos con most_frecuent (valores mas frecuentes)
imputer = SimpleImputer(strategy='most_frequent')
data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Imprimir el resultado
print(data.head())
