# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:56:03 2024

@author: jared
"""

import cv2

# Cargar el clasificador de Haar para la detección de caras
clasificador_cara = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar la imagen
imagen = cv2.imread('people.jpg')

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar caras en la imagen
caras = clasificador_cara.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar rectángulos alrededor de las caras detectadas
for (x, y, w, h) in caras:
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con las caras detectadas
cv2.imshow('Caras Detectadas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
