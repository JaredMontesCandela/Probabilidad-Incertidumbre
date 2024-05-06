# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:03:52 2024

@author: jared
"""

import numpy as np

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, X):
        for x in X:
            self.weights += np.outer(x, x)
        np.fill_diagonal(self.weights, 0)

    def predict(self, x):
        return np.sign(np.dot(x, self.weights))

# Ejemplo de uso
X_train = np.array([[1, -1, 1],
                    [1, 1, -1],
                    [-1, -1, -1]])

hopfield_net = HopfieldNetwork(size=X_train.shape[1])
hopfield_net.train(X_train)

x_test = np.array([1, -1, 1])
prediction = hopfield_net.predict(x_test)
print("Predicción de la red de Hopfield:", prediction)
