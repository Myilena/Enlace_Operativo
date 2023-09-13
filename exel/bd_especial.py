import random
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Genera datos de ejemplo con 100 registros
data = {
    "Nombre": [f"Persona_{i}" for i in range(1, 101)],
    "Tipo_EPS": [random.choice(["A", "B", "C"]) for _ in range(100)],
    "Estrato": [random.randint(1, 6) for _ in range(100)],
    "Trabajo": [random.choice([0, 1]) for _ in range(100)],
    "Sueldo": [random.randint(20000, 100000) for _ in range(100)]
}

# Crea un DataFrame de pandas
df = pd.DataFrame(data)

# Separar los datos en características (X) y variable objetivo (y)
X = df[["Tipo_EPS", "Estrato", "Trabajo"]]
y = df["Sueldo"]

# Codificar las variables categóricas (Tipo_EPS) usando one-hot encoding
X = pd.get_dummies(X, columns=["Tipo_EPS"], drop_first=True)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo (por ejemplo, con el error cuadrático medio)
mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio: {mse}")

# Exportar el DataFrame a un archivo Excel
df.to_excel("datos_regresion_con_nombre.xlsx", index=False)
