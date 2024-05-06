"""
El objetivo de este ejemplo es calcular la probabilidad de una secuencia de observaciones en un Modelo Oculto de Markov utilizando el algoritmo hacia adelante-atrás.
"""
"""
Supongamos que tenemos un HMM que modela el clima con tres estados: soleado (S), nublado (N) y lluvioso (L). 
Queremos calcular la probabilidad de una secuencia de observaciones del estado del cielo durante varios días
"""

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

# Función para calcular la probabilidad de una secuencia de observaciones en un HMM usando el algoritmo hacia adelante-atrás
def calcular_probabilidad_hmm(observaciones):
    # Inicializamos las variables forward y backward
    forward = [{}]
    backward = [{}]

    # Paso hacia adelante: calcular las probabilidades forward
    for estado in matriz_transicion.keys():
        forward[0][estado] = matriz_emision[estado][observaciones[0]] * 1 / len(matriz_transicion)
    
    for t in range(1, len(observaciones)):
        forward.append({})
        for estado_destino in matriz_transicion.keys():
            forward[t][estado_destino] = sum(forward[t-1][estado_origen] * matriz_transicion[estado_origen][estado_destino] * matriz_emision[estado_destino][observaciones[t]] for estado_origen in matriz_transicion.keys())

    # Paso hacia atrás: calcular las probabilidades backward
    for estado in matriz_transicion.keys():
        backward[-1][estado] = 1
    
    for t in reversed(range(len(observaciones)-1)):
        backward.insert(0, {})
        for estado_origen in matriz_transicion.keys():
            backward[0][estado_origen] = sum(matriz_transicion[estado_origen][estado_destino] * matriz_emision[estado_destino][observaciones[t+1]] * backward[1][estado_destino] for estado_destino in matriz_transicion.keys())

    # Calcular la probabilidad total de la secuencia de observaciones
    probabilidad_total = sum(forward[t][estado] * backward[t][estado] for t in range(len(observaciones)) for estado in matriz_transicion.keys())
    
    return probabilidad_total

# Secuencia de observaciones del estado del cielo
observaciones = ['soleado', 'nublado', 'lluvioso']

# Calcular la probabilidad de la secuencia de observaciones en el HMM
probabilidad = calcular_probabilidad_hmm(observaciones)

# Imprimir el resultado
print(f"La probabilidad de la secuencia de observaciones {observaciones} en el HMM es: {probabilidad:.6f}")
