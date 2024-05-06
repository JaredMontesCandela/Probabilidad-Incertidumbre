# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:03:26 2024

@author: jared
"""

import numpy as np

def hebb_rule(X):
    return np.dot(X.T, X)

# Ejemplo de uso
X = np.array([[1, -1, 1],
              [1, 1, -1],
              [-1, -1, -1]])

weights = hebb_rule(X)
print("Pesos según la regla de Hebb:")
print(weights)
