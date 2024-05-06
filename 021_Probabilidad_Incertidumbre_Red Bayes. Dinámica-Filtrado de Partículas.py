
"""
El objetivo de este ejemplo es ilustrar cómo usar el algoritmo de filtrado de partículas para estimar el estado oculto en una red bayesiana dinámica.
"""
"""
Supongamos que queremos estimar la posición de un objeto en movimiento utilizando un modelo de red bayesiana dinámica y el algoritmo de filtrado de partículas.
"""

import numpy as np
import random

class Particula:
    def __init__(self, x, peso):
        self.x = x        # Estado de la partícula
        self.peso = peso  # Peso de la partícula

# Función de transición del estado
def transicion_estado(x_anterior):
    # Modelo de movimiento del objeto: movimiento rectilíneo con velocidad constante
    return x_anterior + random.normalvariate(0, 0.1)

# Función de observación
def observacion(x):
    # Modelo de observación del sensor: medición de la posición con ruido gaussiano
    return x + random.normalvariate(0, 0.1)

# Algoritmo de filtrado de partículas
def filtrado_de_particulas(num_particulas, observaciones):
    # Inicializamos las partículas
    particulas = [Particula(random.uniform(0, 1), 1/num_particulas) for _ in range(num_particulas)]
    
    for observacion in observaciones:
        # Predicción: transición del estado de cada partícula
        for particula in particulas:
            particula.x = transicion_estado(particula.x)
        
        # Actualización: ajuste de los pesos basado en la verosimilitud de la observación
        peso_total = 0
        for particula in particulas:
            verosimilitud = observacion - particula.x
            particula.peso *= np.exp(-0.5 * (verosimilitud ** 2) / 0.1)
            peso_total += particula.peso
        
        # Normalización de los pesos
        for particula in particulas:
            particula.peso /= peso_total
    
    # Estimación del estado oculto (posición) como el promedio ponderado de las partículas
    estado_estimado = sum(particula.x * particula.peso for particula in particulas)
    
    return estado_estimado

# Simulamos las observaciones del sensor (mediciones de la posición con ruido)
observaciones_simuladas = [observacion(pos) for pos in np.arange(0, 1, 0.1)]

# Aplicamos el algoritmo de filtrado de partículas para estimar la posición del objeto
posicion_estimada = filtrado_de_particulas(1000, observaciones_simuladas)

# Imprimimos el resultado
print("Posición Estimada del Objeto:")
print(posicion_estimada)
