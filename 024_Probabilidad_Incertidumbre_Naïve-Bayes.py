# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:27:01 2024

@author: jared
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.parameters = {}
        for c in self.classes:
            self.parameters[c] = {}
            # Calcular la probabilidad a priori de cada clase
            self.parameters[c]['prior'] = np.mean(y == c)
            # Calcular la media y la desviación estándar de cada característica para cada clase
            self.parameters[c]['mean'] = np.mean(X[y == c], axis=0)
            self.parameters[c]['std'] = np.std(X[y == c], axis=0)

    def predict(self, X):
        predictions = []
        for x in X:
            posteriors = []
            for c in self.classes:
                # Calcular la probabilidad posterior de cada clase dada la característica
                posterior = np.prod(
                    (1 / (np.sqrt(2 * np.pi) * self.parameters[c]['std'])) *
                    np.exp(-((x - self.parameters[c]['mean']) ** 2) / (2 * (self.parameters[c]['std'] ** 2))))
                # Multiplicar por la probabilidad a priori de la clase
                posterior *= self.parameters[c]['prior']
                posteriors.append(posterior)
            # Elegir la clase con la mayor probabilidad posterior
            predictions.append(self.classes[np.argmax(posteriors)])
        return predictions

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=50)

# Crear y entrenar el clasificador Naïve Bayes
nb = NaiveBayes()
nb.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = nb.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador Naïve Bayes:", accuracy)
