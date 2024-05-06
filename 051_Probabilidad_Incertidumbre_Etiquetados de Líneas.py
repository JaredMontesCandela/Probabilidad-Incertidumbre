# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:11:06 2024

@author: jared
"""

import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('lambo.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización para binarizar la imagen
_, umbralizada = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)

# Encontrar los contornos en la imagen binarizada
contornos, _ = cv2.findContours(umbralizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
imagen_contornos = cv2.cvtColor(umbralizada, cv2.COLOR_GRAY2BGR)
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos detectados
cv2.imshow('Contornos', imagen_contornos)
cv2.waitKey(0)
cv2.destroyAllWindows()
