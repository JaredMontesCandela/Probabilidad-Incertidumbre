# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:31:04 2024

@author: jared
"""
"""
El objetivo de este ejemplo es ilustrar cómo realizar el aprendizaje bayesiano para estimar los parámetros de un modelo lineal simple.
"""

"""
Supongamos que tenemos un conjunto de datos que representa la relación entre la temperatura (en grados Celsius) 
y la cantidad de helados vendidos en una heladería. Queremos estimar los parámetros de un modelo lineal simple
y=mx+b, donde 
-y- es la cantidad de helados vendidos y  -x- es la temperatura.
"""

import numpy as np

# Datos observados
temperatura = np.array([20, 25, 30, 35, 40])  # Temperatura en grados Celsius
helados_vendidos = np.array([50, 60, 70, 80, 90])  # Cantidad de helados vendidos

# Definimos las funciones de verosimilitud y prior
def likelihood(m, b):
    y_pred = m * temperatura + b
    error = helados_vendidos - y_pred
    likelihood = np.exp(-0.5 * np.sum(error**2))
    return likelihood

def prior(m, b):
    prior_m = 1  # Prior uniforme para m
    prior_b = 1  # Prior uniforme para b
    return prior_m * prior_b

# Creamos una cuadrícula de valores para m y b
m_values = np.linspace(0, 5, 100)
b_values = np.linspace(0, 100, 100)

# Calculamos la densidad posterior para cada combinación de m y b
posterior_values = np.zeros((len(m_values), len(b_values)))
for i, m in enumerate(m_values):
    for j, b in enumerate(b_values):
        posterior_values[i, j] = likelihood(m, b) * prior(m, b)

# Normalizamos la densidad posterior
posterior_values /= np.sum(posterior_values)

# Encontramos los valores de m y b que maximizan la densidad posterior
indice_max = np.argmax(posterior_values)
indice_m, indice_b = np.unravel_index(indice_max, posterior_values.shape)
m_estimado = m_values[indice_m]
b_estimado = b_values[indice_b]

# Imprimimos los resultados
print("Parámetros estimados:")
print(f"m: {m_estimado}")
print(f"b: {b_estimado}")
