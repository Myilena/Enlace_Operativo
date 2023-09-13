import pandas as pd
import random

# Crear una lista unidimensional de datos con más de 300 elementos
data = []

# Generar 300 elementos de datos ficticios y agregarlos a la lista
nombres = ["Juan", "María", "Luis", "Ana", "Carlos", "Laura", "Pedro", "Sofía", "Diego", "Elena"]
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Málaga", "Zaragoza", "Murcia", "Granada", "Alicante"]

for _ in range(300):
    nombre = random.choice(nombres)
    edad = random.randint(18, 60)
    ciudad = random.choice(ciudades)
    data.append([nombre, edad, ciudad])

# Crear un DataFrame de Pandas a partir de la lista unidimensional
df = pd.DataFrame(data, columns=["Nombre", "Edad", "Ciudad"])

# Crear un archivo de Excel y guardar el DataFrame en él
archivo_excel = "datos_unidimensionales.xlsx"
df.to_excel(archivo_excel, index=False)

print("Los datos se han guardado en el archivo Excel:", archivo_excel)
