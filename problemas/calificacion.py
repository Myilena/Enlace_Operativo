import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de horas de estudio y calificación promedio
horas_estudio = np.array([2, 3, 4, 5, 6]).reshape(-1, 1)
calificaciones = np.array([70, 75, 80, 85, 90])

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(horas_estudio, calificaciones)

# Predecir las calificaciones para diferentes cantidades de horas de estudio
horas_prediccion = np.array([2.5, 4.5, 7]).reshape(-1, 1)
calificaciones_predichas = modelo.predict(horas_prediccion)

# Imprimir las predicciones
for horas, calificacion in zip(horas_prediccion, calificaciones_predichas):
    print(f"Horas de estudio: {horas[0]}, Calificación estimada: {calificacion:.2f}")

# Graficar los datos y la línea de regresión
plt.scatter(horas_estudio, calificaciones, color='blue', label='Datos reales')
plt.plot(horas_prediccion, calificaciones_predichas, color='red', label='Regresión lineal')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación Promedio')
plt.title('Predicción de Rendimiento de Estudiantes vs. Horas de Estudio')
plt.legend()
plt.show()
