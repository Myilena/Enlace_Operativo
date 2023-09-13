import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression # Generar datos ficticios

np.random.seed(0)
X = np.random.rand(50, 1) * 10 # Característica (variable independiente)
y = 2 * X + 1 + np.random.randn(50, 1) * 2 # Variable dependiente con algo de ruido # Crear el modelo de regresión lineal 
model= LinearRegression() 
model.fit(X, y) # Realizar predicciones utilizando el modelo 
y_pred = model.predict(X) # Graficar los datos y la línea de regresión
plt.scatter(X, y, label='Datos reales') 
plt.plot(X, y_pred, color='red', label='Regresión lineal')
plt.xlabel('X') 
plt.ylabel('y')
plt.title('Regresión Lineal') 
plt.legend() 
plt.show()