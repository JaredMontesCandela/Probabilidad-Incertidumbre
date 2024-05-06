# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:32:03 2024

@author: jared
"""

import numpy as np

# Definición de las entradas (features) y los pesos (weights)
entrada = np.array([1.0, 2.0, 3.0])  # Vector de entrada con 3 características
pesos = np.array([0.2, 0.8, -0.5])    # Vector de pesos asociados a cada característica

# Computación neuronal: multiplicación de las entradas por los pesos y suma ponderada
activacion = np.dot(entrada, pesos)

# Aplicación de una función de activación (opcional)
def relu(x):
    return max(0, x)

activacion_relu = relu(activacion)

# Impresión de resultados
print("Activación antes de la función de activación:", activacion)
print("Activación después de la función de activación (ReLU):", activacion_relu)
