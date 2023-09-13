import numpy as np
import pandas as pd
import openpyxl
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generar 400 datos de ejemplo
np.random.seed(0)  # Fijar la semilla para reproducibilidad
X = np.random.rand(400) * 100  # Valores numéricos en un rango de 0 a 100
y = 2.5 * X + np.random.randn(400) * 10  # Ecuación lineal con ruido

# Crear un DataFrame con los datos
data = {'X': X, 'y': y}
df = pd.DataFrame(data)

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
X = X.reshape(-1, 1)  # Ajustar la forma de los datos
modelo.fit(X, y)

# Realizar predicciones
y_pred = modelo.predict(X)

# Graficar los datos y la línea de regresión
plt.scatter(X, y, color='purple', label='Datos reales')
plt.plot(X, y_pred, color='pink', label='Regresión lineal')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()

# Imprimir los coeficientes del modelo
print("Coeficiente (pendiente):", modelo.coef_[0])
print("Término independiente (intercepto):", modelo.intercept_)

# Exportar el DataFrame a un archivo Excel con openpyxl
with pd.ExcelWriter('datos_regresion_lineal.xlsx', engine='openpyxl') as writer:
    writer.book = openpyxl.Workbook()
    df.to_excel(writer, sheet_name='Hoja1', index=False)

