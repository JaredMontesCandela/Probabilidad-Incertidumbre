# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:54:56 2024

@author: jared
"""

"""

"""

import numpy as np

class EMAlgorithm:
    def __init__(self, n_clusters, max_iter=100, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, X):
        # Inicialización de parámetros
        n_samples, n_features = X.shape
        self.means = X[np.random.choice(n_samples, self.n_clusters, replace=False)]
        self.covariances = [np.eye(n_features)] * self.n_clusters
        self.weights = np.ones(self.n_clusters) / self.n_clusters

        # Algoritmo EM
        for _ in range(self.max_iter):
            # Expectation step
            responsibilities = self.expectation(X)

            # Maximization step
            self.maximization(X, responsibilities)

    def expectation(self, X):
        n_samples = X.shape[0]
        responsibilities = np.zeros((n_samples, self.n_clusters))
        for k in range(self.n_clusters):
            responsibilities[:, k] = self.weights[k] * self.multivariate_normal(X, self.means[k], self.covariances[k])
        responsibilities /= np.sum(responsibilities, axis=1)[:, np.newaxis]
        return responsibilities

    def maximization(self, X, responsibilities):
        n_samples = X.shape[0]
        for k in range(self.n_clusters):
            nk = np.sum(responsibilities[:, k], axis=0)
            self.weights[k] = nk / n_samples
            self.means[k] = np.sum(X * responsibilities[:, k][:, np.newaxis], axis=0) / nk
            self.covariances[k] = np.dot((responsibilities[:, k][:, np.newaxis] * (X - self.means[k])).T,
                                          (X - self.means[k])) / nk

    def multivariate_normal(self, X, mean, covariance):
        n_features = X.shape[1]
        det = np.linalg.det(covariance)
        norm_const = 1.0 / ((2 * np.pi) ** (n_features / 2) * np.sqrt(det))
        inv_cov = np.linalg.inv(covariance)
        exp_term = np.exp(-0.5 * np.sum((X - mean) @ inv_cov * (X - mean), axis=1))
        return norm_const * exp_term

# Generar datos de ejemplo
np.random.seed(0)
X = np.concatenate([np.random.normal(loc=0, scale=1, size=(100, 2)),
                    np.random.normal(loc=4, scale=1, size=(100, 2))])

# Crear y entrenar el modelo de mezcla gaussiana utilizando EM
n_clusters = 2
em = EMAlgorithm(n_clusters=n_clusters)
em.fit(X)

# Imprimir los parámetros estimados del modelo
print("Parámetros del modelo:")
for k in range(n_clusters):
    print(f"Cluster {k+1}:")
    print("Media:", em.means[k])
    print("Covarianza:", em.covariances[k])
    print("Peso:", em.weights[k])
