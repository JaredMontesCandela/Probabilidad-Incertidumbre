"""
El objetivo de este ejemplo es ilustrar el concepto de hipótesis de Markov utilizando un proceso de Markov para modelar cambios en el clima.
"""


"""Matematica
     S    N    L
S  0.8  0.1  0.1
N  0.3  0.4  0.3
L  0.2  0.3  0.5

"""


import random

# Definimos la matriz de transición del proceso de Markov para el clima
matriz_transicion_clima = {
    'S': {'S': 0.8, 'N': 0.1, 'L': 0.1},
    'N': {'S': 0.3, 'N': 0.4, 'L': 0.3},
    'L': {'S': 0.2, 'N': 0.3, 'L': 0.5}
}

# Función para simular cambios en el clima utilizando el proceso de Markov
def simular_cambios_clima(matriz_transicion, estado_inicial, num_dias):
    clima_actual = estado_inicial
    cambios_clima = [clima_actual]
    for _ in range(num_dias - 1):
        siguiente_clima = random.choices(list(matriz_transicion.keys()), 
                                          weights=matriz_transicion[clima_actual].values())[0]
        cambios_clima.append(siguiente_clima)
        clima_actual = siguiente_clima
    return cambios_clima

# Definimos el estado inicial del clima
estado_inicial_clima = 'S'

# Simulamos cambios en el clima durante 7 días
cambios_clima = simular_cambios_clima(matriz_transicion_clima, estado_inicial_clima, 7)

# Imprimimos los cambios en el clima
print("Cambios en el Clima durante 7 Días:")
print("soleado (S), nublado (N) y lluvioso (L)")
for dia, clima in enumerate(cambios_clima, start=1):
    print(f"Día {dia}: {clima}")
