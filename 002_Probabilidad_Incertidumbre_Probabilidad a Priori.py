import random
"""
Calcular la probabilidad a priori de obtener un número par al lanzar un dado.
"""

# Definimos una función para calcular la probabilidad a priori de obtener un número par al lanzar un dado
def probabilidad_a_priori(num_lados):
    # Contamos la cantidad total de resultados posibles (número de lados del dado)
    total_posibilidades = num_lados
    # Contamos la cantidad de resultados favorables (números pares en un dado de 6 caras)
    favorables = num_lados // 2
    
    # Calculamos la probabilidad a priori
    probabilidad = favorables / total_posibilidades
    
    return probabilidad

# Definimos el número de lados del dado
num_lados_dado = 6


# Calculamos la probabilidad a priori de obtener un número par al lanzar el dado
probabilidad_par = probabilidad_a_priori(num_lados_dado)

# Imprimimos el resultado
print("Probabilidad a priori de obtener un número par al lanzar un dado de {} caras:".format(num_lados_dado))
print(probabilidad_par)
