# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:15:00 2024

@author: jared
"""

import cv2

# Capturar el primer fotograma de la secuencia de vídeo
captura = cv2.VideoCapture(0)
_, primer_fotograma = captura.read()
gris_primer_fotograma = cv2.cvtColor(primer_fotograma, cv2.COLOR_BGR2GRAY)

# Configurar el detector de movimiento
detector_movimiento = cv2.createBackgroundSubtractorMOG2()

while True:
    # Capturar el siguiente fotograma de la secuencia de vídeo
    ret, fotograma = captura.read()
    if not ret:
        break

    # Convertir el fotograma a escala de grises
    gris_fotograma = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)

    # Aplicar el detector de movimiento para obtener la máscara de movimiento
    mascara_movimiento = detector_movimiento.apply(gris_fotograma)

    # Mostrar la máscara de movimiento
    cv2.imshow('Máscara de Movimiento', mascara_movimiento)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar la captura
captura.release()

# Cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()