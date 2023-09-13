import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de publicidad (TV) y ventas
publicidad = np.array([77, 52, 65, 250, 302]).reshape(-1, 1)
ventas = np.array([563, 655, 734, 823,930])

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
modelo.fit(publicidad, ventas)

# Predecir las ventas para un rango de valores de publicidad
publicidad_prediccion = np.array([[563], [655], [734], [823], [930]])
ventas_predichas = modelo.predict(publicidad_prediccion)

# Imprimir las predicciones
for i in range(len(publicidad_prediccion)):
    print(f"Inversión en publicidad: {publicidad_prediccion[i][0]} - Predicción de ventas: {ventas_predichas[i]}")

# Graficar los datos y la línea de regresión
plt.scatter(publicidad, ventas, color='blue', label='Datos reales')
plt.plot(publicidad_prediccion, ventas_predichas, color='red', label='Regresión lineal')
plt.xlabel('Inversión en Publicidad (TV)')
plt.ylabel('Ventas')
plt.title('Predicción de Ventas basada en Publicidad en TV')
plt.legend("")
plt.show()


