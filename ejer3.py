import pandas as pd

# Carga el archivo CSV en un DataFrame de pandas
df = pd.read_csv('wine-quality-white-and-red.csv')

# Verifica si hay valores faltantes en el DataFrame
missing_values = df.isnull().sum()

# Itera a través de las columnas con valores faltantes
for column, count in missing_values.items():
    if count > 0:
        # Calcula la media de la columna
        mean_value = df[column].mean()
        
        # Imputa los valores faltantes con la media
        df[column].fillna(mean_value, inplace=True)

# Guarda los datos imputados en un nuevo archivo CSV
df.to_csv('wine-quality-white-and-red-imputed.csv', index=False)
