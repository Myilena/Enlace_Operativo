# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import openpyxl

# Carga el archivo de Excel
archivo_excel = "cuanti_cuali.xlsx"

# Reemplaza con la ruta correcta

# Intenta cargar el archivo Excel
try:
    wb = openpyxl.load_workbook(archivo_excel)
    hoja = wb['Hoja1']  # Reemplaza con el nombre de tu hoja

    # Crear un DataFrame con los datos de la hoja de Excel
    data = {
        'Cantidad clientes': [],
        'Ciudad': [],
        'tipo_letra': []
    }

    # Iterar sobre las filas de la hoja de Excel y agregar los datos al DataFrame
    for row in hoja.iter_rows(min_row=2, values_only=True):
        data['Cantidad clientes'].append(row[0])
        data['Ciudad'].append(row[1])
        data['tipo_letra'].append(row[2])

    df = pd.DataFrame(data)

    # Identificar variables cuantitativas y cualitativas
    variables_cuantitativas = ['Cantidad clientes']  # Columna 'Cantidad clientes' es cuantitativa
    variables_cualitativas = ['Ciudad', 'tipo_letra']  # Columnas 'Ciudad' y 'tipo_letra' son cualitativas

    # Convertir la variable 'Ciudad' a numérica mediante etiquetado numérico
    df['Ciudad'] = pd.Categorical(df['Ciudad'])
    df['Ciudad'] = df['Ciudad'].cat.codes

    # Codificar la variable 'tipo_letra' utilizando one-hot encoding
    df_encoded = pd.get_dummies(df, columns=['tipo_letra'], prefix=['tipo_letra'])

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X = df_encoded[variables_cuantitativas + list(df_encoded.columns[df_encoded.columns.str.startswith('tipo_letra_')])]
    y = df_encoded.drop(variables_cuantitativas, axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear un modelo de regresión múltiple
    reg_model = LinearRegression()
    reg_model.fit(X_train, y_train)

    # Realizar predicciones en el conjunto de prueba
    y_pred = reg_model.predict(X_test)

    # Calcular métricas de evaluación
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Imprimir las métricas de evaluación
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    # Graficar las predicciones contra los valores reales
    plt.scatter(X_test['Cantidad clientes'], y_test.values, color='blue', label='Valores reales')
    plt.scatter(X_test['Cantidad clientes'], y_pred.flatten(), color='red', marker='x', label='Predicciones')
    plt.xlabel('Cantidad clientes')
    plt.ylabel('tipo_letra')
    plt.legend(loc='upper left')
    plt.title('Regresión Múltiple')
    plt.show()

except FileNotFoundError:
    print("El archivo Excel no se encuentra en la ruta especificada.")
