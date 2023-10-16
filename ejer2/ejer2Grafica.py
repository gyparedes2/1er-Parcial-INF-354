import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carga el archivo CSV en un DataFrame de pandas
df = pd.read_csv('wine-quality-white-and-red.csv')

# Filtra el DataFrame para "white" y "red"
df_white = df[df['type'] == 'white']
df_red = df[df['type'] == 'red']

# Define las columnas de interés
columns_of_interest = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
    'density', 'pH', 'sulphates', 'alcohol', 'quality'
]

# Configura el diseño de los subplots
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 10))
fig.subplots_adjust(hspace=0.5)

for i, column in enumerate(columns_of_interest):
    ax = axes[i // 3, i % 3]

    if column == 'quality':
        # Calcula el promedio de calidad para "white" y "red" usando NumPy
        avg_quality_white = np.mean(df_white['quality'])
        avg_quality_red = np.mean(df_red['quality'])

        # Crea un gráfico de barras para mostrar la puntuación promedio de calidad
        ax.bar(["Blanco", "Rojo"], [avg_quality_white, avg_quality_red], color=["blue", "red"])
        ax.set_title("Calidad Promedio")
        ax.set_ylabel('Calificación Promedio')
    else:
        # Crea histogramas para "white" y "red"
        ax.hist(df_white[column], alpha=0.5, label="Blanco", color="blue", bins=15)
        ax.hist(df_red[column], alpha=0.5, label="Rojo", color="red", bins=15)
        
        # Calcula los promedios usando NumPy
        avg_white = np.mean(df_white[column])
        avg_red = np.mean(df_red[column])
        
        # Dibuja líneas verticales para los promedios usando NumPy
        ax.axvline(avg_white, color='blue', linestyle='dashed', linewidth=2, label='Promedio Blanco')
        ax.axvline(avg_red, color='red', linestyle='dashed', linewidth=2, label='Promedio Rojo')
        
        ax.set_title(column.replace('_', ' ').capitalize())
        ax.set_xlabel(column)
        ax.set_ylabel('Frecuencia')
        ax.legend()

plt.tight_layout()
plt.show()
