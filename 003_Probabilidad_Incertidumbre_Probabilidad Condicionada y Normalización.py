"""
Objetivo del código: Calcular la probabilidad condicionada de obtener un número par en el
segundo lanzamiento de un dado, dado que el primer lanzamiento resultó en un número impar.    
"""

# Definimos una función para calcular la probabilidad condicionada
def probabilidad_condicionada(num_lados):
    # Definimos la probabilidad a priori de obtener un número impar en un dado de n caras
    probabilidad_impar = 0.5
    
    # Calculamos la probabilidad a priori de obtener un número par
    probabilidad_par = 1 - probabilidad_impar
    
    # Calculamos la probabilidad condicionada de obtener un número par en el segundo lanzamiento,
    # dado que el primer lanzamiento resultó en un número impar (normalizamos para asegurar que la suma de probabilidades sea 1)
    probabilidad_condicionada = (probabilidad_par * probabilidad_impar) / (probabilidad_par * probabilidad_impar + probabilidad_impar * probabilidad_par)
    
    return probabilidad_condicionada

# Definimos el número de lados del dado
num_lados_dado = 6

# Calculamos la probabilidad condicionada de obtener un número par en el segundo lanzamiento,
# dado que el primer lanzamiento resultó en un número impar
probabilidad_cond = probabilidad_condicionada(num_lados_dado)

# Imprimimos el resultado
print("Probabilidad condicionada de obtener un número par en el segundo lanzamiento, dado que el primer lanzamiento resultó en un número impar:")
print(probabilidad_cond)
