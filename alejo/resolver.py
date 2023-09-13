import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Supongamos que tienes tus datos en un archivo CSV llamado 'datos.csv'
data = pd.read_csv('datos.csv')

# Divide tus datos en variables independientes (X) y la variable dependiente (y)
X = data[['Feature1', 'Feature2', 'Feature3', ...]]  # Coloca aquí las características que quieras usar
y = data['VariableObjetivo']
