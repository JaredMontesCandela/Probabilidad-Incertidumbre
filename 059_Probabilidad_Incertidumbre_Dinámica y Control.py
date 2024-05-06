# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:20:44 2024

@author: jared
"""

import numpy as np

# Parámetros del sistema
masa = 1.0  # kg
constante_resorte = 10.0  # N/m
constante_amortiguador = 1.0  # Ns/m
posicion_deseada = 0.0  # m

# Condiciones iniciales
posicion_inicial = 1.0  # m
velocidad_inicial = 0.0  # m/s

# Tiempo de simulación
tiempo_total = 10.0  # s
paso_tiempo = 0.1  # s
num_pasos = int(tiempo_total / paso_tiempo)

# Controlador proporcional
ganancia_proporcional = 10.0

# Simulación del sistema
tiempo = np.arange(0, tiempo_total, paso_tiempo)
posicion = np.zeros(num_pasos)
velocidad = np.zeros(num_pasos)

posicion[0] = posicion_inicial
velocidad[0] = velocidad_inicial

for i in range(1, num_pasos):
    # Error
    error = posicion_deseada - posicion[i-1]
    
    # Ley de control proporcional
    fuerza_control = ganancia_proporcional * error
    
    # Ecuaciones de movimiento del sistema
    aceleracion = (fuerza_control - constante_resorte * posicion[i-1] - constante_amortiguador * velocidad[i-1]) / masa
    velocidad[i] = velocidad[i-1] + aceleracion * paso_tiempo
    posicion[i] = posicion[i-1] + velocidad[i] * paso_tiempo

# Imprimir resultados en la consola
for t, p in zip(tiempo, posicion):
    print("Tiempo: {:.2f} s, Posición: {:.2f} m".format(t, p))
