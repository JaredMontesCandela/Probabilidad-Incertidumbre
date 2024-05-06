# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:47:41 2024

@author: jared
"""

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('lambo.jpg')

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar el filtro de suavizado (filtro de media)
kernel_size = 5  # Tamaño del kernel del filtro de media
suavizado = cv2.blur(gris, (kernel_size, kernel_size))

# Mostrar la imagen original y la imagen suavizada
cv2.imshow('Imagen Original', gris)
cv2.imshow('Imagen Suavizada', suavizado)
cv2.waitKey(0)
cv2.destroyAllWindows()
