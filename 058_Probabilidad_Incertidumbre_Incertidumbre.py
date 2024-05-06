# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:08:29 2024

@author: jared
"""

import random

# Definir la incertidumbre sobre si la moneda está trucada o no
probabilidad_trucada = 0.3  # Probabilidad de que la moneda esté trucada

# Lanzar la moneda
if random.random() < probabilidad_trucada:
    # Si la moneda está trucada, la probabilidad de obtener cara es 0.8
    probabilidad_cara = 0.8
else:
    # Si la moneda no está trucada, la probabilidad de obtener cara es 0.5 (moneda justa)
    probabilidad_cara = 0.5

# Imprimir la probabilidad de obtener cara
print("La probabilidad de obtener cara es:", probabilidad_cara)
