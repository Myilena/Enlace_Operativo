import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import openpyxl

# Carga el archivo de Excel
archivo_excel = "Ejercicio_Datos_PythonV2.xlsx"

# Reemplaza con la ruta correcta
try:
    wb = openpyxl.load_workbook(archivo_excel)
    hoja = wb['Hoja2']  # Reemplaza con el nombre de tu hoja

    # Inicializa listas para almacenar datos
    meses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   

    # Accede a los datos y recopila información
    for n in range(1, hoja.max_row + 1):
        mes = hoja['A' + str(n)].value
        
        string= isinstance (mes,str)
        if string :
            continue
        datob = hoja['B' + str(n)].value
        cliente_valor = hoja['C' + str(n)].value
        meses[mes-1] = meses[mes-1] + datob
       
        # Crea un modelo de regresión lineal
    model = LinearRegression()

    meses2=[1,2,3,4,5,6,7,8,9,10,11,12] 
    X = np.array(meses2).reshape(-1, 1)
    y = np.array(meses)  # Convierte la lista de ventas en una matriz 1D

    model.fit(X, y)

    # Imprime los coeficientes del modelo
    print("Coeficientes del modelo:")
    print("Intercepto:", model.intercept_)
    print("Coeficientes:", model.coef_)

    # Realizar predicciones
    prediccion = model.predict(np.array([[6]]))
    print(prediccion)

    # Graficar la regresión lineal
    plt.scatter(X, y, color='blue', label='Datos reales')
    plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regresión lineal')
    plt.xlabel('Mes')
    plt.ylabel('Datos')
    plt.title('Regresión Lineal')
    plt.legend()
    plt.show()

except FileNotFoundError:
    print("El archivo Excel no se encuentra en la ruta especificada.")
   