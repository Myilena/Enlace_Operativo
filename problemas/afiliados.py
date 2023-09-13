import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de los planes de afiliación
niveles_cobertura = np.array([1, 2, 3])  # Niveles de cobertura: Básico, Intermedio, Premium
costos_mensuales = np.array([50, 80, 120])  # Costos mensuales correspondientes

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
niveles_cobertura = niveles_cobertura.reshape(-1, 1)  # Ajustar la forma de los datos
modelo.fit(niveles_cobertura, costos_mensuales)

# Realizar predicciones para los niveles de cobertura
niveles_prediccion = np.array([1, 2, 3]).reshape(-1, 1)
costos_prediccion = modelo.predict(niveles_prediccion)

# Graficar los datos y la línea de regresión
plt.scatter(niveles_cobertura, costos_mensuales, color='blue', label='Datos reales')
plt.plot(niveles_prediccion, costos_prediccion, color='red', label='Regresión lineal')
plt.xlabel('Nivel de Cobertura')
plt.ylabel('Costo Mensual ($)')
plt.title('Regresión Lineal - Costo Mensual de Afiliación')
plt.legend()
plt.show()

# Imprimir los coeficientes del modelo
print("Coeficiente (pendiente):", modelo.coef_[0])
print("Término independiente (intercepto):", modelo.intercept_)
