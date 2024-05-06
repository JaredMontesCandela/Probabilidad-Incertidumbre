# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:41:42 2024

@author: jared
"""
"""

El objetivo de este código es implementar el algoritmo de retropropagación del error (backpropagation) para entrenar una red
neuronal de una sola capa oculta. La función principal del código es realizar el proceso de entrenamiento de la red neuronal
ajustando iterativamente los pesos y sesgos de la red para minimizar la diferencia entre las predicciones de la red y las salidas deseadas (objetivo). 
"""

 
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Inicialización de pesos y sesgos
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        # Paso hacia adelante
        self.hidden_output = self.sigmoid(np.dot(X, self.weights_input_hidden) + self.bias_hidden)
        self.predictions = self.sigmoid(np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output)
        return self.predictions

    def backward(self, X, y):
        # Paso hacia atrás
        error = y - self.predictions
        output_delta = error * self.sigmoid_derivative(self.predictions)
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)

        # Actualización de pesos y sesgos
        self.weights_hidden_output += np.dot(self.hidden_output.T, output_delta) * self.learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
        self.weights_input_hidden += np.dot(X.T, hidden_delta) * self.learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            # Paso hacia adelante
            predictions = self.forward(X)
            # Paso hacia atrás
            self.backward(X, y)
            # Calcular y mostrar la pérdida
            loss = np.mean(np.square(y - predictions))
            if epoch % 1000 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de entrada y salida
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Crear y entrenar la red neuronal
    nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)
    nn.train(X, y, epochs=10000)

    # Hacer predicciones
    predictions = nn.forward(X)
    print("Predicciones finales:")
    print(predictions)

