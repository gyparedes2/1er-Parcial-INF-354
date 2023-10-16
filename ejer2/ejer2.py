import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
df = pd.read_csv('wine-quality-white-and-red.csv')

# Seleccionar solo las columnas numéricas
columnas_numericas = df.select_dtypes(include=[np.number])

# Agrupar por el tipo de vino (blanco y rojo) y calcular las estadísticas
grouped = columnas_numericas.groupby(df['type'])

# Calcular la media (promedio) por tipo de vino
media = grouped.mean()
print("Media (Promedio) por tipo de vino:")
print(media)
print()

# Calcular la moda (valor más frecuente) por tipo de vino
moda = grouped.apply(lambda x: x.mode().iloc[0])
print("Moda (Valor más frecuente) por tipo de vino:")
print(moda)
print()

# Calcular los cuartiles (25%, 50%, 75%) por tipo de vino
cuartiles = grouped.quantile([0.25, 0.50, 0.75])
print("Cuartiles por tipo de vino:")
print(cuartiles)
print()

# Calcular los percentiles (por ejemplo, 10%, 90%) por tipo de vino
percentiles = grouped.quantile([0.10, 0.90])
print("Percentiles por tipo de vino:")
print(percentiles)
print()
