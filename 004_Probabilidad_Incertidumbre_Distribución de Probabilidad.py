"""
Objetivo del código: Generar una distribución de probabilidad uniforme para simular el 
lanzamiento de un dado de seis caras.    
"""

# Definimos una función para generar una distribución de probabilidad uniforme para un dado de n caras
def distribucion_uniforme(num_lados):
    # Calculamos la probabilidad de cada resultado (1/n para una distribución uniforme)
    probabilidad = 1 / num_lados
    # Creamos un diccionario para almacenar las probabilidades de cada resultado
    distribucion = {i: probabilidad for i in range(1, num_lados + 1)}
    return distribucion

# Definimos el número de lados del dado
num_lados_dado = 6

# Generamos la distribución de probabilidad uniforme para un dado de seis caras
distribucion = distribucion_uniforme(num_lados_dado)

# Imprimimos la distribución de probabilidad
print("Distribución de Probabilidad para un Dado de 6 Caras:")
for resultado, probabilidad in distribucion.items():
    print("Resultado:", resultado, "- Probabilidad:", probabilidad)
