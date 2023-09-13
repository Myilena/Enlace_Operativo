import pandas as pd
import random

# Listas de posibles valores aleatorios
nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Raúl', 'Luis']
clases = ['A', 'B', 'C']
orientaciones = ['Ciencias', 'Artes']

# Generar datos aleatorios para 500 alumnos
data = {
    'Nombre': [random.choice(nombres) for _ in range(500)],
    'Clase': [random.choice(clases) for _ in range(500)],
    'Orientación': [random.choice(orientaciones) for _ in range(500)],
    'Nota Final': [round(random.uniform(5.0, 10.0), 1) for _ in range(500)]
}

df = pd.DataFrame(data)

# Hallar la nota media de los alumnos
nota_media_total = df['Nota Final'].mean()

# Hallar la nota máxima obtenida
nota_maxima = df['Nota Final'].max()

# Hallar la nota más baja obtenida
nota_minima = df['Nota Final'].min()

# Contar el número de alumnos participantes
numero_alumnos = len(df)

# Hallar la nota media para cada orientación académica
nota_media_por_orientacion = df.groupby('Orientación')['Nota Final'].mean()

# Hallar la nota media para cada clase
nota_media_por_clase = df.groupby('Clase')['Nota Final'].mean()

# Encontrar la clase y nota de un alumno específico (por ejemplo, Raúl)
alumno_buscado = df[df['Nombre'] == 'Raúl'][['Clase', 'Nota Final']]

# Contar el número de personas que han sacado una nota igual o superior a 7
alumnos_aprobados = df[df['Nota Final'] >= 7]
numero_aprobados = len(alumnos_aprobados)

# Guardar el resultado en un archivo Excel
with pd.ExcelWriter('resultados.xlsx', engine='openpyxl', mode='w') as writer:
    df.to_excel(writer, sheet_name='Alumnos', index=False)
    nota_media_por_orientacion.to_excel(writer, sheet_name='Media por Orientación')
    nota_media_por_clase.to_excel(writer, sheet_name='Media por Clase')
    alumno_buscado.to_excel(writer, sheet_name='Alumno Buscado', index=False)
    writer.save()

# Imprimir los resultados
print(f'Nota Media Total: {nota_media_total}')
print(f'Nota Máxima: {nota_maxima}')
print(f'Nota Mínima: {nota_minima}')
print(f'Número de Alumnos: {numero_alumnos}')
print('Nota Media por Orientación:')
print(nota_media_por_orientacion)
print('Nota Media por Clase:')
print(nota_media_por_clase)
print('Clase y Nota de Raúl:')
print(alumno_buscado)
print(f'Número de Personas con Nota >= 7: {numero_aprobados}')

