# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:31:39 2024

@author: jared
"""
# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Generar datos sintéticos
X, y = datasets.make_circles(n_samples=100, noise=0.05, random_state=42)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear un clasificador SVM con un kernel no lineal (por ejemplo, un kernel RBF)
svm_classifier = SVC(kernel='rbf', C=1, gamma='auto')  # C es el parámetro de regularización

# Entrenar el clasificador
svm_classifier.fit(X_train, y_train)

# Función para visualizar los resultados
def plot_decision_boundary(clf, X, y):
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=20)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision Boundary')

# Visualizar el límite de decisión
plt.figure(figsize=(10, 6))
plot_decision_boundary(svm_classifier, X_train, y_train)
plt.show()
