#etiquetado simple y binario, ya que clasifica las filas 
#en dos categorías ("bueno" y "malo") en función de un umbral numérico.
import pandas as pd

# Carga el archivo CSV en un DataFrame de pandas
df = pd.read_csv('wine-quality-white-and-red.csv')

# Define el umbral para clasificar como "buenos" o "malos" (calidad >= 7)
umbral_calidad = 7

# Crea una nueva columna llamada 'etiqueta' y asigna "bueno" a las filas con calidad >= umbral_calidad y "malo" a las demás
df['etiqueta'] = df['quality'].apply(lambda x: 'bueno' if x >= umbral_calidad else 'malo')

# Guarda el DataFrame con las etiquetas en un nuevo archivo CSV
df.to_csv('wine-quality-labeled.csv', index=False)
