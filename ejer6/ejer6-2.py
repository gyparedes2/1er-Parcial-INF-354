# Codificación de Variables Categóricas
# En caso de tener características categóricas como el tipo de vino, es importante convertirlas en valores 
# numéricos para que los modelos puedan procesarlas.
import pandas as pd

# Cargar el conjunto de datos
data = pd.read_csv("wine-quality-white-and-red.csv")

# Cambiar la codificación de la columna "type" a 0 para "red" y 1 para "white"
data['type'] = data['type'].map({'red': 0, 'white': 1})

# Imprimir el resultado
print(data.head())
