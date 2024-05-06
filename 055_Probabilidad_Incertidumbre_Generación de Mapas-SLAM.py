# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:57:33 2024

@author: jared
"""

"""
En este ejemplo:

Generamos un mapa aleatorio que representa un entorno binario (ocupado o libre).
Simulamos la trayectoria de un robot en este entorno, con ruido en los movimientos.
El robot realiza mediciones en cada paso, que consisten en la suma de los valores del mapa en una vecindad alrededor de su posición actual, con ruido añadido.
Aplicamos el algoritmo SLAM para estimar el mapa a partir de las mediciones y la trayectoria del robot.
Visualizamos el verdadero mapa y el mapa estimado.
"""
import numpy as np

# Definir parámetros del entorno
tamano_entorno = 20
num_pasos = 1000
desviacion_estimacion = 2
desviacion_medida = 5

# Generar datos simulados del entorno y del robot
verdadero_mapa = np.random.randint(2, size=(tamano_entorno, tamano_entorno))
posicion_inicial = [tamano_entorno // 2, tamano_entorno // 2]
trayectoria = [posicion_inicial]
for _ in range(num_pasos):
    movimiento = np.random.normal(0, desviacion_estimacion, 2)
    nueva_posicion = [int(round(trayectoria[-1][0] + movimiento[0])),
                      int(round(trayectoria[-1][1] + movimiento[1]))]
    if 0 <= nueva_posicion[0] < tamano_entorno and 0 <= nueva_posicion[1] < tamano_entorno:
        trayectoria.append(nueva_posicion)
    else:
        trayectoria.append(trayectoria[-1])

# Simular mediciones del robot
mediciones = []
for paso in trayectoria:
    medida = np.sum(verdadero_mapa[paso[0] - 1:paso[0] + 2, paso[1] - 1:paso[1] + 2]) + np.random.normal(0, desviacion_medida)
    mediciones.append(medida)

# Aplicar algoritmo SLAM para generar el mapa
mapa_estimado = np.zeros_like(verdadero_mapa)
for i, paso in enumerate(trayectoria):
    mapa_estimado[paso[0], paso[1]] = mediciones[i]

# Imprimir el verdadero mapa y el mapa estimado
print("Verdadero Mapa:")
print(verdadero_mapa)
print("\nMapa Estimado (SLAM):")
print(mapa_estimado)
