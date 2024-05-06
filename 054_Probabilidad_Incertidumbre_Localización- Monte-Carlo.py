# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:22:36 2024

@author: jared
"""

import numpy as np
import random

# Definir el tamaño del área rectangular y el número de partículas
ancho_area = 10
alto_area = 10
num_particulas = 1000

# Función para inicializar las partículas de manera uniforme en el área
def inicializar_particulas():
    particulas = []
    for _ in range(num_particulas):
        x = random.uniform(0, ancho_area)
        y = random.uniform(0, alto_area)
        particulas.append((x, y))
    return particulas

# Función para mover las partículas según el comando del robot
def mover_particulas(particulas, comando):
    nuevas_particulas = []
    for (x, y) in particulas:
        # Simular el movimiento del robot con cierto ruido
        nuevo_x = min(max(x + random.gauss(comando[0], 0.1), 0), ancho_area)
        nuevo_y = min(max(y + random.gauss(comando[1], 0.1), 0), alto_area)
        nuevas_particulas.append((nuevo_x, nuevo_y))
    return nuevas_particulas

# Función para calcular la probabilidad de observar una medida dado un conjunto de partículas
def calcular_probabilidad_medida(medida, particulas):
    probabilidad = []
    for (x, y) in particulas:
        # Calcular la distancia entre la partícula y la pared en cada dirección
        distancia_arriba = alto_area - y
        distancia_abajo = y
        distancia_izquierda = x
        distancia_derecha = ancho_area - x
        # Calcular la probabilidad de observar la medida dada la distancia a la pared
        prob_arriba = np.exp(-abs(medida[0] - distancia_arriba))
        prob_abajo = np.exp(-abs(medida[1] - distancia_abajo))
        prob_izquierda = np.exp(-abs(medida[2] - distancia_izquierda))
        prob_derecha = np.exp(-abs(medida[3] - distancia_derecha))
        # La probabilidad total es el producto de las probabilidades en cada dirección
        prob_total = prob_arriba * prob_abajo * prob_izquierda * prob_derecha
        probabilidad.append(prob_total)
    # Normalizar las probabilidades para que sumen 1
    probabilidad = [p / sum(probabilidad) for p in probabilidad]
    return probabilidad

# Función para estimar la posición del robot a partir de las partículas
def estimar_posicion(particulas):
    # Calcular la posición promedio ponderada de las partículas
    x_estimado = sum(x for x, _ in particulas) / len(particulas)
    y_estimado = sum(y for _, y in particulas) / len(particulas)
    return x_estimado, y_estimado

# Comando de movimiento del robot (distancia a avanzar en x y y)
comando_movimiento = (1, 1)

# Inicializar las partículas
particulas = inicializar_particulas()

# Simular el movimiento del robot y la observación
particulas = mover_particulas(particulas, comando_movimiento)
medida = (alto_area - 5, 5, 5, ancho_area - 5)  # Distancias medidas desde el sensor

# Actualizar las probabilidades de las partículas basadas en la observación
probabilidad = calcular_probabilidad_medida(medida, particulas)

# Resampleo de partículas basado en la probabilidad
particulas_resampleadas = random.choices(particulas, weights=probabilidad, k=num_particulas)

# Estimar la posición del robot
posicion_estimada = estimar_posicion(particulas_resampleadas)

print("Posición estimada del robot:", posicion_estimada)
