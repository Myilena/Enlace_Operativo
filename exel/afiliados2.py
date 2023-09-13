import pandas as pd
import random
import string

# Función para generar nombres aleatorios
def generar_nombre():
    nombres = ["Carlos", "María", "Luis", "Ana", "Pedro", "Laura", "Juan", "Sofía", "Andrés", "Valentina"]
    apellidos = ["Gómez", "Rodríguez", "López", "Martínez", "Fernández", "Pérez", "García", "Vargas", "Torres", "Díaz"]
    return random.choice(nombres) + " " + random.choice(apellidos)

# Función para generar datos ficticios
def generar_datos(num_datos):
    datos = []
    for _ in range(num_datos):
        nombre = generar_nombre()
        plan = random.choice(["Básico", "Intermedio", "Premium"])
        costo_mensual = random.randint(50, 150)
        nivel_cobertura = random.randint(1, 3)
        datos.append([nombre, plan, costo_mensual, nivel_cobertura])
    return datos

# Generar más de 400 datos ficticios
num_datos = 500  # Puedes ajustar este número según tus necesidades
datos_ficticios = generar_datos(num_datos)

# Crear un DataFrame con los datos ficticios
df = pd.DataFrame(datos_ficticios, columns=["Nombre", "Plan", "Costo Mensual", "Nivel de Cobertura"])

# Exportar el DataFrame a un archivo Excel
df.to_excel("datos_afiliacion_eps.xlsx", index=False)
