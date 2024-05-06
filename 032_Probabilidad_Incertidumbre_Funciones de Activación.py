# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:47:06 2024

@author: jared
"""
"""
Este código define una función capa_neuronal que crea una capa de una red neuronal con un número especificado de neuronas y una función 
de activación dada. Luego, se prueba esta función con diferentes funciones de activación (ReLU, Sigmoid, Tanh y Softmax) utilizando un conjunto de datos de entrada de ejemplo.
"""

import tensorflow as tf

# Definición de la capa de una red neuronal con diferentes funciones de activación
def capa_neuronal(input_data, num_neurons, activation_function):
    weights = tf.Variable(tf.random.normal([input_data.shape[1], num_neurons]))  # Pesos aleatorios
    biases = tf.Variable(tf.random.normal([num_neurons]))  # Sesgos aleatorios
    linear_output = tf.add(tf.matmul(input_data, weights), biases)  # Computación lineal

    if activation_function == 'relu':
        return tf.nn.relu(linear_output)  # ReLU activation
    elif activation_function == 'sigmoid':
        return tf.nn.sigmoid(linear_output)  # Sigmoid activation
    elif activation_function == 'tanh':
        return tf.nn.tanh(linear_output)  # Tanh activation
    elif activation_function == 'softmax':
        return tf.nn.softmax(linear_output)  # Softmax activation
    else:
        raise ValueError("Función de activación no válida")

# Ejemplo de uso de la capa neuronal con diferentes funciones de activación
input_data = tf.constant([[1.0, 2.0, 3.0]])  # Datos de entrada
num_neurons = 4  # Número de neuronas en la capa
activations = ['relu', 'sigmoid', 'tanh', 'softmax']  # Lista de funciones de activación

for activation in activations:
    output = capa_neuronal(input_data, num_neurons, activation)
    print(f'Activación {activation}: {output}')

