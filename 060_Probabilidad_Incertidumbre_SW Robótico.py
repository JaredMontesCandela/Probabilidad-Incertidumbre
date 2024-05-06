# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:23:13 2024

@author: jared
"""
"""
En este ejemplo, el robot tiene tres posibles acciones: avanzar, girar a la izquierda o girar a la derecha.
El algoritmo de seguimiento de paredes sigue la pared a su derecha en todo momento. Siempre que el robot
encuentre una pared a su derecha, avanzará; de lo contrario, girará a la izquierda.
Esta simulación muestra el movimiento del robot mientras explora el entorno utilizando este algoritmo.
la función time.sleep(0.5) introduce un retraso de 0.5 segundos entre cada acción del robot.
"""

import random
import time

# Definir las posibles acciones del robot
acciones = ['avanzar', 'girar_izquierda', 'girar_derecha']

# Simulación de movimiento del robot con retraso
def mover_robot(accion):
    if accion == 'avanzar':
        print("Avanzando")
    elif accion == 'girar_izquierda':
        print("Girando a la izquierda")
    elif accion == 'girar_derecha':
        print("Girando a la derecha")
    time.sleep(0.5)  # Retraso de 0.5 segundos entre cada acción

# Algoritmo de seguimiento de paredes con retraso
def seguimiento_paredes():
    while True:
        # Si hay una pared a la derecha, girar a la izquierda y avanzar
        if random.random() < 0.8:  # Probabilidad de seguir la pared
            accion = 'avanzar'
        else:
            accion = 'girar_izquierda'
        mover_robot(accion)

# Ejecutar el algoritmo de seguimiento de paredes
seguimiento_paredes()
