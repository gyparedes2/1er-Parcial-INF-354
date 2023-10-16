import csv
import random

# Cargar los datos desde el archivo CSV
data = []
with open('Iris.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Saltar la fila de encabezados
    for row in reader:
        data.append(row)

# Fijar la semilla aleatoria para reproducibilidad
random.seed(42)

# Definir el tamaño del conjunto de prueba (20%)
test_size = 0.20

# Calcular el número de ejemplos para el conjunto de prueba
test_size = int(len(data) * test_size)

# Generar índices aleatorios para el conjunto de prueba
test_indices = random.sample(range(len(data)), test_size)

# Crear índices para el conjunto de entrenamiento
train_indices = [i for i in range(len(data)) if i not in test_indices]

# Dividir los datos en conjuntos de entrenamiento y prueba
train_data = [data[i] for i in train_indices]
test_data = [data[i] for i in test_indices]

# Verificar la cantidad de datos en cada conjunto
print("Número de ejemplos en el conjunto de entrenamiento:", len(train_data))
print("Número de ejemplos en el conjunto de prueba:", len(test_data))
