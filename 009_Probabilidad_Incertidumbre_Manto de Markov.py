"""
Objetivo del código: Simular un modelo de Manto de Markov para predecir el clima durante varios días.
En este código, modelamos el clima como un proceso de Manto de Markov donde el clima en un día dado depende solo del clima del día anterior   
"""
import random


# Definimos los estados posibles del clima
estados_clima = ['soleado', 'nublado', 'lluvioso']

# Definimos la matriz de transición de estados
matriz_transicion = {
    'soleado': {'soleado': 0.7, 'nublado': 0.2, 'lluvioso': 0.1},
    'nublado': {'soleado': 0.3, 'nublado': 0.4, 'lluvioso': 0.3},
    'lluvioso': {'soleado': 0.1, 'nublado': 0.3, 'lluvioso': 0.6}
}

# Definimos una función para simular el clima durante varios días
def simular_clima(dias):
    clima_actual = random.choice(estados_clima)
    secuencia_clima = [clima_actual]
    for _ in range(dias - 1):
        clima_siguiente = random.choices(estados_clima, weights=[matriz_transicion[clima_actual][estado] for estado in estados_clima])[0]
        secuencia_clima.append(clima_siguiente)
        clima_actual = clima_siguiente
    return secuencia_clima

# Simulamos el clima durante 7 días
secuencia_7dias = simular_clima(7)

# Imprimimos los resultados
print("Secuencia del clima durante 7 días:", secuencia_7dias)
