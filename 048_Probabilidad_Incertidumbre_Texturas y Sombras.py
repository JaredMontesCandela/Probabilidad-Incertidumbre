# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:52:28 2024

@author: jared
"""

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('lambo.jpg')

# Crear una matriz de sombra
sombra = np.zeros_like(imagen, dtype=np.uint8)

# Definir el desplazamiento de la sombra
desplazamiento = (50, 50)

# Aplicar la sombra desplazada
for y in range(imagen.shape[0]):
    for x in range(imagen.shape[1]):
        sombra[y, x] = imagen[(y + desplazamiento[1]) % imagen.shape[0], (x + desplazamiento[0]) % imagen.shape[1]]

# Combinar la imagen original con la sombra
imagen_con_sombra = cv2.addWeighted(imagen, 0.7, sombra, 0.3, 0)

# Mostrar la imagen original y la imagen con sombra
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen con Sombra', imagen_con_sombra)
cv2.waitKey(0)
cv2.destroyAllWindows()
