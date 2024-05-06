# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:57:57 2024

@author: jared
"""

import numpy as np

def hamming_distance(x, y):
    return np.sum(x != y)

# Ejemplo de uso
x = np.array([0, 1, 0, 1])
y = np.array([1, 1, 0, 0])
distance = hamming_distance(x, y)
print("Distancia de Hamming:", distance)
