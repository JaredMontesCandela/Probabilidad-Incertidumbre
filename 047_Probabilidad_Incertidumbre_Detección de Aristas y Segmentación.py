# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:49:38 2024

@author: jared
"""

import cv2

# Cargar la imagen en escala de grises
imagen = cv2.imread('lambo.jpg', 0)

# Aplicar el detector de bordes Canny
bordes = cv2.Canny(imagen, 100, 200)

# Mostrar la imagen original y los bordes detectados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Bordes Detectados', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
