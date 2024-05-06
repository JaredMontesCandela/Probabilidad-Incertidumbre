# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:31:00 2024

@author: jared
"""
"""
Ejemplo: Supongamos que tenemos un conjunto de datos que representa el clima de una región
durante varios días, donde las observaciones son el tipo de clima (soleado, nublado, lluvioso) y los 
estados ocultos son las estaciones del año (verano, otoño, invierno, primavera). 
Utilizaremos un HMM para modelar este proceso y predecir el tipo de clima para los próximos días.
"""

import numpy as np

class HiddenMarkovModel:
    def __init__(self, n_states, n_obs):
        self.n_states = n_states
        self.n_obs = n_obs
        self.transition_matrix = np.random.rand(n_states, n_states)
        self.transition_matrix /= np.sum(self.transition_matrix, axis=1, keepdims=True)
        self.emission_matrix = np.random.rand(n_states, n_obs)
        self.emission_matrix /= np.sum(self.emission_matrix, axis=1, keepdims=True)
        self.initial_state_probs = np.ones(n_states) / n_states

    def forward(self, observations):
        n_obs = len(observations)
        alpha = np.zeros((n_obs, self.n_states))

        # Inicialización
        alpha[0] = self.initial_state_probs * self.emission_matrix[:, observations[0]]

        # Inducción
        for t in range(1, n_obs):
            alpha[t] = np.dot(alpha[t - 1], self.transition_matrix) * self.emission_matrix[:, observations[t]]

        return alpha

# Datos de ejemplo
observations = [0, 1, 2, 0, 1]  # Ejemplo simplificado de tipos de clima (0 - Soleado, 1 - Nublado, 2 - Lluvioso)

# Construir y entrenar el modelo HMM
model = HiddenMarkovModel(n_states=4, n_obs=3)  # 4 estados ocultos para las 4 estaciones del año
alpha = model.forward(observations)

# Mapeo de estados ocultos a estaciones del año
estaciones = {0: 'Verano', 1: 'Otoño', 2: 'Invierno', 3: 'Primavera'}
predicted_states = np.argmax(alpha, axis=1)
predicted_estaciones = [estaciones[s] for s in predicted_states]

print("Predicción de estaciones del año para los próximos días:")
print(predicted_estaciones)
