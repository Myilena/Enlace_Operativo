import pandas as pd
import random

# Crear una matriz bidimensional de datos con más de 300 filas
data = [
    ["Nombre", "Edad", "Ciudad"]
]

# Generar 300 filas de datos ficticios
nombres = ["Juan", "María", "Luis", "Ana", "Carlos", "Laura", "Pedro", "Sofía", "Diego", "Elena"]
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Málaga", "Zaragoza", "Murcia", "Granada", "Alicante"]

for _ in range(300):
    nombre = random.choice(nombres)
    edad = random.randint(18, 60)
    ciudad = random.choice(ciudades)
    data.append([nombre, edad, ciudad])

# Convertir la matriz en un DataFrame de Pandas
df = pd.DataFrame(data[1:], columns=data[0])

# Crear un archivo de Excel y guardar el DataFrame en él
archivo_excel = "datos_ampliados.xlsx"
df.to_excel(archivo_excel, index=False)

print("Los datos se han guardado en el archivo Excel:", archivo_excel)
