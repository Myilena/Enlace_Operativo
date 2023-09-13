import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de entrenamiento
areas = np.array([1200, 1500, 1800, 2000, 2200]).reshape(-1, 1)
precios = np.array([250, 300, 350, 400, 450])

# Imprimir los datos de entrenamiento
print("Áreas (pies cuadrados):")
print(areas)
print("Precios ($1000):")
print(precios)

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(areas, precios)

# Áreas para las que queremos predecir precios
areas_prediccion = np.array([1700, 1900, 2100]).reshape(-1, 1)

# Imprimir las áreas para predicción
print("Áreas para predicción:")
print(areas_prediccion)

# Realizar predicciones
precios_predichos = modelo.predict(areas_prediccion)

# Imprimir las predicciones
print("Predicciones de precios ($1000):")
for area, precio_predicho in zip(areas_prediccion, precios_predichos):
    print(f"Área: {area[0]} pies cuadrados, Precio estimado: ${precio_predicho:.2f} mil")

# Visualización del gráfico de dispersión y línea de regresión
plt.scatter(areas, precios, color='blue', label='Datos reales')
plt.plot(areas, modelo.predict(areas), color='red', label='Regresión lineal')
plt.scatter(areas_prediccion, precios_predichos, color='green', label='Predicciones')
plt.xlabel('Área (pies cuadrados)')
plt.ylabel('Precio ($1000)')
plt.title('Predicción de Precio de Viviendas')
plt.legend()
plt.grid(True)
plt.show()



