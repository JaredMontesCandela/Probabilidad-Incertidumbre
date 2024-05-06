# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:01:46 2024

@author: jared
"""
"""
En este ejemplo, utilizo una matriz de caracteres para representar el espacio de configuración en la consola. 
 Cada punto se marca como 'O' si está libre y 'X' si está ocupado por un obstáculo.
"""
# Definir los parámetros del espacio de configuración
rango_x = (-10, 10)
rango_y = (-10, 10)
resolucion = 1

# Definir los obstáculos como círculos (centro_x, centro_y, radio)
obstaculos = [(0, 0, 5), (3, 3, 2), (-5, -6, 3)]

# Crear una cuadrícula en el espacio de configuración
x = range(rango_x[0], rango_x[1] + resolucion, resolucion)
y = range(rango_y[0], rango_y[1] + resolucion, resolucion)

# Verificar si cada punto en la cuadrícula está dentro de un obstáculo
espacio_libre = [['O' for _ in range(len(x))] for _ in range(len(y))]
for i, yi in enumerate(y):
    for j, xj in enumerate(x):
        for obstaculo in obstaculos:
            distancia = ((xj - obstaculo[0])**2 + (yi - obstaculo[1])**2)**0.5
            if distancia < obstaculo[2]:
                espacio_libre[i][j] = 'X'

# Imprimir el espacio de configuración en la consola
for fila in espacio_libre:
    print(' '.join(fila))
