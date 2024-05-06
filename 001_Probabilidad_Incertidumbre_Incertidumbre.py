import random
"""
Objetivo del código: Generar una simulación de lanzamiento de moneda para entender el 
concepto de incertidumbre en probabilidad.
"""

# Definimos una función para simular el lanzamiento de una moneda
def lanzamiento_moneda():
    # Generamos un número aleatorio entre 0 y 1
    resultado = random.random()
    # Si el número es menor que 0.5, consideramos cara (probabilidad 0.5)
    if resultado < 0.5:
        return "cara"
    # Si el número es mayor o igual a 0.5, consideramos cruz (probabilidad 0.5)
    else:
        return "cruz"

# Definimos la cantidad de lanzamientos que queremos simular
num_lanzamientos = 10

# Creamos una lista para almacenar los resultados de los lanzamientos
resultados = []

# Realizamos los lanzamientos y almacenamos los resultados
for _ in range(num_lanzamientos):
    resultado_actual = lanzamiento_moneda()
    resultados.append(resultado_actual)

# Contamos cuántas veces obtuvimos cara y cuántas veces obtuvimos cruz
num_caras = resultados.count("cara")
num_cruces = resultados.count("cruz")

# Calculamos las probabilidades de cara y cruz
probabilidad_cara = num_caras / num_lanzamientos
probabilidad_cruz = num_cruces / num_lanzamientos

# Imprimimos los resultados
print("Resultados de los lanzamientos:")
print("Caras:", num_caras)
print("Cruces:", num_cruces)
print("Probabilidad de cara:", probabilidad_cara)
print("Probabilidad de cruz:", probabilidad_cruz)
