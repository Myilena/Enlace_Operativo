import numpy as np
import matplotlib.pyplot as plt

# Valores de las variables independientes
x1_values = np.linspace(0, 5, 100)
x2_values = np.linspace(0, 5, 100)

# Coeficientes y término constante del modelo
coef_x1 = 0.1
coef_x2 = 0.2
constante = 1.25

# Generar ruido aleatorio con distribución N(0, 0.2)
ruido = np.random.normal(0, 0.2, 100)

# Calcular los valores de y utilizando el modelo
y_values = coef_x1 * x1_values + coef_x2 * x2_values + constante + ruido

# Crear un gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1_values, x2_values, y_values, c='b', marker='o')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt.title('Relación entre x1, x2 y y')
plt.show()
