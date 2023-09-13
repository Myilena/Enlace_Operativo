import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generar datos ficticios
np.random.seed(0)
num_students = 100
hours_studied = np.random.rand(num_students) * 10
true_coefficient = 3.5
true_intercept = 20
noise = np.random.randn(num_students) * 2
grades = true_coefficient * hours_studied + true_intercept + noise

# Crear un DataFrame con los datoscd 
data = pd.DataFrame({'HoursStudied': hours_studied, 'Grades': grades})

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data[['HoursStudied']], data['Grades'], test_size=0.2, random_state=0)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Visualizar los resultados
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regresión lineal')
plt.xlabel('Horas de estudio')
plt.ylabel('Notas')
plt.title('Regresión Lineal: Notas de Alumnos')
plt.legend()
plt.show()
