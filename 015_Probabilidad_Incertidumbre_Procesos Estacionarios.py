"""
Supongamos que estamos modelando la llegada de clientes a un banco durante el día utilizando un proceso de Poisson.
"""
"""

Supongamos que estamos modelando la llegada de clientes a un banco durante el día.
Utilizaremos un proceso de Poisson para modelar esta llegada de clientes
Un proceso de Poisson es un ejemplo de proceso estacionario donde los eventos ocurren de manera independiente y a una tasa constante en el tiempo.
"""

import random
import math

# Función para simular llegadas de clientes en un proceso de Poisson
def simular_llegadas_poisson(tasa_llegadas, duracion_simulacion):
    tiempo = 0
    llegadas = []
    while tiempo < duracion_simulacion:
        tiempo += tiempo_entre_llegadas(tasa_llegadas)
        if tiempo < duracion_simulacion:
            llegadas.append(tiempo)
    return llegadas

# Función para generar el tiempo entre llegadas en un proceso de Poisson
def tiempo_entre_llegadas(tasa_llegadas):
    return -math.log(1.0 - random.random()) / tasa_llegadas

# Definimos la tasa de llegadas de clientes por hora
tasa_llegadas = 10

# Duración de la simulación en horas
duracion_simulacion = 8

# Simulamos llegadas de clientes durante la duración de la simulación
llegadas = simular_llegadas_poisson(tasa_llegadas, duracion_simulacion)

# Imprimimos las llegadas de clientes
print("Llegadas de Clientes (Tiempo en horas):")
print("No persona - Hora")
for i, llegada in enumerate(llegadas):
    print(f"Llegada {i+1}: {llegada:.2f}")
