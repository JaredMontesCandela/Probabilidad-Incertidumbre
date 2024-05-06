"""
El objetivo de este ejemplo es ilustrar cómo utilizar un Modelo Oculto de Markov para predecir el clima basado en observaciones
"""
"""
Supongamos que queremos modelar el clima como un HMM con tres estados: soleado (S), nublado (N) y lluvioso (L).
Utilizaremos un HMM para predecir el clima basado en observaciones del estado del cielo durante varios días.
"""


import random

# Definimos la matriz de transición del HMM para el clima
matriz_transicion = {
    'S': {'S': 0.7, 'N': 0.2, 'L': 0.1},
    'N': {'S': 0.3, 'N': 0.5, 'L': 0.2},
    'L': {'S': 0.2, 'N': 0.4, 'L': 0.4}
}

# Definimos la matriz de emisión del HMM para las observaciones del estado del cielo
matriz_emision = {
    'S': {'soleado': 0.6, 'nublado': 0.3, 'lluvioso': 0.1},
    'N': {'soleado': 0.3, 'nublado': 0.4, 'lluvioso': 0.3},
    'L': {'soleado': 0.1, 'nublado': 0.2, 'lluvioso': 0.7}
}

# Función para simular el clima utilizando el HMM
def simular_clima(num_dias):
    clima = []
    estado_actual = random.choice(['S', 'N', 'L'])
    for _ in range(num_dias):
        clima.append(estado_actual)
        estado_actual = random.choices(list(matriz_transicion[estado_actual].keys()), 
                                        weights=matriz_transicion[estado_actual].values())[0]
    return clima

# Función para simular observaciones del estado del cielo basadas en el clima
def simular_observaciones(clima):
    observaciones = []
    for estado in clima:
        observaciones.append(random.choices(list(matriz_emision[estado].keys()), 
                                             weights=matriz_emision[estado].values())[0])
    return observaciones

# Simulamos el clima y las observaciones durante 7 días
clima_simulado = simular_clima(7)
observaciones_simuladas = simular_observaciones(clima_simulado)

# Imprimimos los resultados
print("Simulación del Clima:")
print(clima_simulado)
print("\nObservaciones del Estado del Cielo:")
print(observaciones_simuladas)
