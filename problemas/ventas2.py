import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos de publicidad (TV) y ventas
publicidad = np.array([100, 200, 300, 400, 500])
ventas = np.array([550, 620, 720, 850, 980])  # Cambia los valores de ventas

# Definir una función exponencial
def funcion_exponencial(x, a, b, c):
    return a * np.exp(b * x) + c

# Ajustar la función exponencial a los datos
parametros, _ = curve_fit(funcion_exponencial, publicidad, ventas)

# Crear un rango de valores de publicidad para la predicción
publicidad_prediccion = np.linspace(0, 600, 100)
ventas_predichas = funcion_exponencial(publicidad_prediccion, *parametros)

# Imprimir los parámetros ajustados
a, b, c = parametros
print(f"Parámetros de la función exponencial: a = {a}, b = {b}, c = {c}")

# Graficar los datos y la función exponencial ajustada
plt.scatter(publicidad, ventas, color='blue', label='Datos reales')
plt.plot(publicidad_prediccion, ventas_predichas, color='red', label='Ajuste exponencial')
plt.xlabel('Inversión en Publicidad (TV)')
plt.ylabel('Ventas')
plt.title('Ajuste de una Función Exponencial a los Datos')
plt.legend()
plt.show()
