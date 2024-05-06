# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:04:29 2024

@author: jared
"""

import numpy as np

class BoltzmannMachine:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))
        self.bias = np.zeros(size)

    def train(self, X, learning_rate=0.1, epochs=100):
        for epoch in range(epochs):
            for x in X:
                h = np.dot(x, self.weights) + self.bias
                p = 1 / (1 + np.exp(-h))
                self.weights += learning_rate * np.outer(x, x) - learning_rate * np.outer(p, p)
                self.bias += learning_rate * (x - p)

# Ejemplo de uso
X_train = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])

boltzmann_machine = BoltzmannMachine(size=X_train.shape[1])
boltzmann_machine.train(X_train)

print("Pesos finales de la máquina de Boltzmann:")
print(boltzmann_machine.weights)
