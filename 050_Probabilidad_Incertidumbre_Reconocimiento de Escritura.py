# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:01:41 2024

@author: jared
"""

import cv2
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Cargar el conjunto de datos de dígitos escritos a mano
digits = datasets.load_digits()

# Dividir el conjunto de datos en datos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Crear y entrenar el clasificador de redes neuronales
clf = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
clf.fit(x_train, y_train)

# Continuar con el código para cargar la imagen y realizar la predicción

# Cargar la imagen
imagen = cv2.imread('mi_imagen4.jpg', cv2.IMREAD_GRAYSCALE)

# Redimensionar la imagen a 8x8 para que coincida con el tamaño de las imágenes en el conjunto de datos de dígitos
imagen = cv2.resize(imagen, (8, 8))

# Invertir los colores de la imagen (si es necesario)
imagen = cv2.bitwise_not(imagen)

# Aplanar la imagen para que sea un vector unidimensional
imagen = imagen.flatten()

# Crear y cargar el clasificador de redes neuronales entrenado previamente
clf = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
clf = clf.fit(x_train, y_train)

# Predecir el dígito en la imagen proporcionada
digito_predicho = clf.predict([imagen])

print("El dígito predicho es:", digito_predicho[0])
