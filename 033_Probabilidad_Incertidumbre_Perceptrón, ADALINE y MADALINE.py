# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:49:38 2024

@author: jared
"""
import numpy as np

class Perceptron:
    def __init__(self, num_inputs):
        self.weights = np.random.rand(num_inputs)
        self.bias = np.random.rand()

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        return 1 if summation > 0 else 0

    def train(self, inputs, targets, learning_rate=0.1, epochs=100):
        for _ in range(epochs):
            for input, target in zip(inputs, targets):
                prediction = self.predict(input)
                error = target - prediction
                self.weights += learning_rate * error * input
                self.bias += learning_rate * error

class Adaline:
    def __init__(self, num_inputs):
        self.weights = np.random.rand(num_inputs)
        self.bias = np.random.rand()

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        return 1 if summation > 0 else 0

    def train(self, inputs, targets, learning_rate=0.1, epochs=100):
        for _ in range(epochs):
            for input, target in zip(inputs, targets):
                prediction = self.predict(input)
                error = target - prediction
                self.weights += learning_rate * error * input
                self.bias += learning_rate * error

class Madaline:
    def __init__(self, num_inputs, num_layers):
        self.weights = [np.random.rand(num_inputs) for _ in range(num_layers)]
        self.biases = np.random.rand(num_layers)

    def predict(self, inputs):
        summations = [np.dot(inputs, weights) + bias for weights, bias in zip(self.weights, self.biases)]
        return [1 if summation > 0 else 0 for summation in summations]

    def train(self, inputs, targets, learning_rate=0.1, epochs=100):
        for _ in range(epochs):
            for input, target in zip(inputs, targets):
                predictions = self.predict(input)
                errors = [target - prediction for prediction in predictions]  # Corrección aquí
                for i in range(len(self.weights)):
                    self.weights[i] += learning_rate * errors[i] * input
                    self.biases[i] += learning_rate * errors[i]


# Ejemplo de uso
if __name__ == "__main__":
    # Datos de entrenamiento (inputs)
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # Objetivos (targets)
    targets = np.array([0, 1, 1, 1])

    # Instanciar el Perceptrón
    perceptron = Perceptron(num_inputs=2)
    # Entrenar el Perceptrón
    perceptron.train(inputs, targets)

    # Instanciar el Adaline
    adaline = Adaline(num_inputs=2)
    # Entrenar el Adaline
    adaline.train(inputs, targets)

    # Instanciar el Madaline
    madaline = Madaline(num_inputs=2, num_layers=2)
    # Entrenar el Madaline
    madaline.train(inputs, targets)

    # Imprimir resultados
    print("Perceptrón:")
    for input in inputs:
        print(perceptron.predict(input))

    print("Adaline:")
    for input in inputs:
        print(adaline.predict(input))

    print("Madaline:")
    for input in inputs:
        print(madaline.predict(input))

