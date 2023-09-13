import openpyxl
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Carga el archivo de Excel
archivo_excel = "Ejercicio_Datos_PythonV2.xlsx"

# Reemplaza con la ruta correcta
def new_func(ciudad):
    return ciudad

try:
    wb = openpyxl.load_workbook(archivo_excel)
    hoja = wb['Hoja2']  # Reemplaza con el nombre de tu hoja

    # Inicializa un diccionario para almacenar datos por ciudad
    datos_ciudades = {}

    # Accede a los datos y recopila información
    for n in range(1, hoja.max_row + 1):
        datoa = hoja['A' + str(n)].value
        datob = hoja['B' + str(n)].value
        cliente = hoja['C' + str(n)].value
        ciudad = hoja['D' + str(n)].value

        # Verifica si la ciudad ya está en el diccionario
        if ciudad not in datos_ciudades:
            datos_ciudades[ciudad] = {'meses': [], 'ventas': [], 'clientes': []}

        # Agrega los datos a la ciudad correspondiente
        datos_ciudades[ciudad]['meses'].append(datoa)
        datos_ciudades[ciudad]['ventas'].append(datob)
        datos_ciudades[ciudad]['clientes'].append(cliente)

    # Realiza el análisis para cada ciudad
    for ciudad, datos in datos_ciudades.items():
        meses_ciudad = datos['meses']
        ventas_ciudad = datos['ventas']
        clientes_ciudad = datos['clientes']

        # Comprueba si tienes suficientes datos para hacer una regresión lineal en esta ciudad
        if len(meses_ciudad) < 2:
            print(f"No hay suficientes datos para realizar una regresión lineal en la ciudad {ciudad}.")
        else:
            # Crea un modelo de regresión lineal
            model = LinearRegression()

            # Ajusta el modelo a tus datos
            X_ciudad = [[mes, venta, cliente] for mes, venta, cliente in zip(meses_ciudad, ventas_ciudad, clientes_ciudad)]
            y_ciudad = ventas_ciudad
            model.fit(X_ciudad, y_ciudad)

            # Imprime los coeficientes del modelo para esta ciudad
            print(f"Coeficientes del modelo para la ciudad {ciudad}:")
            print("Intercepto:", model.intercept_)
            print("Coeficientes:", model.coef_)

            # Realizar predicciones para esta ciudad
            y_pred_ciudad = model.predict(X_ciudad)

            # Realizar predicciones
            y_pred = model.predict(X_ciudad)

            # Calcular predicciones para la variable "meses"
            meses_pred = np.linspace(min(meses_ciudad), max(meses_ciudad), 100)  # Valores para "meses"
            ventas_pred = [model.predict([[mes, venta, cliente]])[0] for mes, venta, cliente in zip(meses_pred, ventas_ciudad, clientes_ciudad)]

            # Crear un diccionario para almacenar las ciudades y sus clientes correspondientes
            ciudad_clientes = {}
            for ciudad, cliente, venta_pred in zip(ciudad, clientes_ciudad, ventas_pred):
                if ciudad not in ciudad_clientes:
                    ciudad_clientes[ciudad] = []
                ciudad_clientes[ciudad].append(cliente)

            # Calcular la cantidad de clientes en cada ciudad
            ciudad_cantidad_clientes = {ciudad: len(clientes) for ciudad, clientes in ciudad_clientes.items()}

            # Imprimir la cantidad de clientes en cada ciudad
            for ciudad, cantidad_clientes in ciudad_cantidad_clientes.items():
                print(f"Ciudad: {ciudad}, Cantidad de Clientes: {cantidad_clientes}")

            # Crear un gráfico de barras que muestra la cantidad de clientes por ciudad
            plt.bar(ciudad_cantidad_clientes.keys(), ciudad_cantidad_clientes.values())
            plt.xlabel("Ciudad")
            plt.ylabel("Cantidad de Clientes")
            plt.title("Cantidad de Clientes por Ciudad")
            plt.xticks(rotation=45)
            plt.show()

except FileNotFoundError:
    print("El archivo Excel no se encuentra en la ruta especificada.")
