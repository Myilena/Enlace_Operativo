import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt

URL = r'C:\Users\yilena.mosquera\Downloads\cuanti_cuali.xlsx'
data = pd.read_excel(URL)

# Explora tus datos
print(data.head())
# Codificación one-hot encoding para variables cualitativas
data = pd.get_dummies(data, columns=['Ciudad', 'tipo_letra'], drop_first=True)
print(data.head())
# Define las variables independientes (X) y la variable dependiente (y)
X = data.drop('Cantidad clientes', axis=1)
y = data['Cantidad clientes']

# Inicializa y ajusta el modelo de regresión
model = LinearRegression()
model.fit(X, y)

# Imprime los coeficientes y el intercepto
print('Coeficientes:', model.coef_)
print('Intercepto:', model.intercept_)
print("/////")
# Filtra las columnas que contienen "Cantidad clientes"
columnas_cantidad_clientes = [
    col for col in data.columns if 'Cantidad clientes' in col]

# Crea una gráfica con las columnas filtradas
for col in columnas_cantidad_clientes:
    plt.scatter(data[col], data['Cantidad clientes'], label=col)

# Personaliza la gráfica (títulos, etiquetas, leyenda, etc.)
plt.title('Gráfica de Cantidad de Clientes vs. Variable Dependiente')
plt.xlabel('Cantidad de Clientes')
plt.ylabel('Variable Dependiente')
plt.legend()
plt.show()

# También puedes volver a ajustar el modelo aquí si es necesario
