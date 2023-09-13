import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Ejercicio 2: Datos de muestra con ruido
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.2, 3.7, 4.5, 5.1, 6.8, 8.0])

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

# Predecir valores y obtener la pendiente y la intersección
predicted_y = model.predict(x.reshape(-1, 1))
slope = model.coef_[0]
intercept = model.intercept_

# Graficar los datos y la línea de regresión
plt.scatter(x, y, label='Datos de muestra con ruido')
plt.plot(x, predicted_y, label='Regresión lineal', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

print(f"Pendiente: {slope}")
print(f"Intersección: {intercept}")
