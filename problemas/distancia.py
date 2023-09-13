import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de velocidad y distancia de frenado
velocidades = np.array([30, 40, 50, 60, 70]).reshape(-1, 1)
distancias_frenado = np.array([45, 80, 125, 180, 245])

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(velocidades, distancias_frenado)

# Predecir las distancias de frenado para diferentes velocidades
velocidades_prediccion = np.array([35, 55, 75]).reshape(-1, 1)
distancias_predichas = modelo.predict(velocidades_prediccion)

# Imprimir las predicciones
for velocidad, distancia in zip(velocidades_prediccion, distancias_predichas):
    print(f"Velocidad: {velocidad[0]} mph, Distancia de frenado estimada: {distancia:.2f} pies")

# Graficar los datos y la línea de regresión
plt.scatter(velocidades, distancias_frenado, color='blue', label='Datos reales')
plt.plot(velocidades_prediccion, distancias_predichas, color='red', label='Regresión lineal')
plt.xlabel('Velocidad (mph)')
plt.ylabel('Distancia de Frenado (pies)')
plt.title('Predicción de Distancia de Frenado vs. Velocidad')
plt.legend()
plt.grid(True)
plt.show()

