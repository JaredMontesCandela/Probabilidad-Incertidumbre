# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:04:50 2024

@author: jared
"""
"""
Supongamos que tenemos un brazo robótico con dos articulaciones, cada una con un ángulo de rotación θ1 y θ2 respectivamente
Queremos encontrar las coordenadas (x, y) del extremo del brazo (punta) 
dadas las longitudes de los segmentos del brazo (L1 y L2) y las posiciones de las articulaciones
"""

"""
En este ejemplo, la función calcular_cinemática_inversa toma las coordenadas (x, y) del extremo del brazo y las
longitudes de los segmentos del brazo (L1 y L2) como entrada, y devuelve los ángulos θ1 y θ2 
de las articulaciones en radianes. Luego, convertimos los ángulos a grados y los imprimimos.
"""

import math

def calcular_cinemática_inversa(x, y, L1, L2):
    # Calcular la distancia desde el origen al punto (x, y)
    distancia = math.sqrt(x**2 + y**2)
    
    # Calcular el ángulo θ2
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    sin_theta2 = math.sqrt(1 - cos_theta2**2)
    theta2 = math.atan2(sin_theta2, cos_theta2)
    
    # Calcular el ángulo θ1
    alpha = math.atan2(y, x)
    beta = math.acos((x**2 + y**2 + L1**2 - L2**2) / (2 * L1 * distancia))
    theta1 = alpha - beta
    
    return theta1, theta2

# Definir las longitudes de los segmentos del brazo
L1 = 5
L2 = 4

# Definir las coordenadas (x, y) del extremo del brazo
x = 7
y = 2

# Calcular la cinemática inversa para encontrar los ángulos de las articulaciones
theta1, theta2 = calcular_cinemática_inversa(x, y, L1, L2)

# Imprimir los resultados
print("Ángulo θ1:", math.degrees(theta1), "grados")
print("Ángulo θ2:", math.degrees(theta2), "grados")
