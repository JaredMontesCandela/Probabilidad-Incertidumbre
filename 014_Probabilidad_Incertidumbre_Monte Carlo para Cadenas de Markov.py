"""
El objetivo de este ejemplo es utilizar el algoritmo de Monte Carlo para Cadenas de Markov para 
predecir el clima en una región dada, basado en observaciones históricas.
"""
"""
Supongamos que queremos predecir el clima en una región que puede estar soleada (S), nublada (N) o lluviosa (L).
Tenemos datos históricos que indican las probabilidades de transición entre los diferentes estados del clima según el día anterior, 
y queremos utilizar estos datos para predecir el clima futuro.
"""

import random

# Definimos la matriz de transición de la cadena de Markov
matriz_transicion_clima = {
    'S': {'S': 0.8, 'N': 0.1, 'L': 0.1},
    'N': {'S': 0.2, 'N': 0.7, 'L': 0.1},
    'L': {'S': 0.4, 'N': 0.4, 'L': 0.2}
}

# Función para realizar el algoritmo de Monte Carlo para Cadenas de Markov
def mcmc_cadena_markov_clima(matriz_transicion, estado_inicial, num_pasos):
    # Inicializamos el estado actual
    estado_actual = estado_inicial
    # Lista para almacenar los estados generados
    estados_generados = [estado_actual]
    # Realizamos los pasos del algoritmo de Monte Carlo
    for _ in range(num_pasos):
        # Escogemos el próximo estado según la matriz de transición
        proximo_estado = random.choices(list(matriz_transicion.keys()), 
                                         weights=matriz_transicion[estado_actual].values())[0]
        # Agregamos el próximo estado a la lista de estados generados
        estados_generados.append(proximo_estado)
        # Actualizamos el estado actual al próximo estado
        estado_actual = proximo_estado
    return estados_generados

# Definimos el estado inicial
estado_inicial_clima = 'S'

# Realizamos el algoritmo de Monte Carlo para Cadenas de Markov con 7 días
prediccion_clima = mcmc_cadena_markov_clima(matriz_transicion_clima, estado_inicial_clima, 7)

# Imprimimos la predicción del clima
print("Predicción del Clima para los Próximos 7 Días:")
print("(S)= soleado")
print("(N)= nublado")
print("(L)= lluvioso")

for i, clima in enumerate(prediccion_clima):
    print(f"Día {i+1}: {clima}")
