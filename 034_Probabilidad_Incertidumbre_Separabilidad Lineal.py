# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:23:56 2024

@author: jared
"""
"""

El objetivo de este código es generar y visualizar datos que sean linealmente separables en un espacio bidimensional.
La función principal del código es crear dos conjuntos de datos que representan dos clases diferentes, 
distribuidas alrededor de dos centros diferentes en el espacio bidimensional. Luego, estos conjuntos de datos se 
visualizan en un gráfico de dispersión, donde cada clase se representa con un color diferente.

La utilidad de este código radica en mostrar un ejemplo práctico de datos que son linealmente separables. 
"""


import numpy as np
import matplotlib.pyplot as plt

# Generar datos linealmente separables en dos dimensiones
np.random.seed(0)
num_samples = 100
mean_class_1 = [2, 2]
cov_class_1 = [[1, 0], [0, 1]]
mean_class_2 = [6, 6]
cov_class_2 = [[1, 0], [0, 1]]

class_1_data = np.random.multivariate_normal(mean_class_1, cov_class_1, num_samples)
class_2_data = np.random.multivariate_normal(mean_class_2, cov_class_2, num_samples)

# Visualizar los datos
plt.scatter(class_1_data[:, 0], class_1_data[:, 1], color='blue', label='Clase 1')
plt.scatter(class_2_data[:, 0], class_2_data[:, 1], color='red', label='Clase 2')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Datos Linealmente Separables')
plt.legend()

# Guardar la figura en un archivo
plt.savefig('separabilidad_lineal.png')

# Mostrar la figura
plt.show('separabilidad_lineal.png')

