# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:34:11 2024

@author: jared
"""
"""
El objetivo de este código es crear y entrenar una red neuronal de múltiples capas (MLP) para clasificación binaria utilizando la biblioteca 
scikit-learn en Python. La red neuronal se entrena con un conjunto de datos sintéticos y se evalúa su precisión en un conjunto de prueba.
"""
"""
En este ejemplo:

Generamos un conjunto de datos sintético usando la función make_classification de scikit-learn.
Dividimos el conjunto de datos en conjuntos de entrenamiento y prueba usando train_test_split.
Creamos una red neuronal de múltiples capas (MLP) utilizando MLPClassifier de scikit-learn.
Especificamos dos capas ocultas con 100 y 50 neuronas respectivamente,
y utilizamos la función de activación ReLU y el optimizador Adam.
Entrenamos la red neuronal utilizando los datos de entrenamiento.
Realizamos predicciones en el conjunto de prueba y calculamos la precisión utilizando la métrica de precisión.
"""
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar un conjunto de datos sintético
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar la red neuronal de múltiples capas
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', random_state=42)
mlp.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = mlp.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del MLP: {:.2f}%".format(accuracy * 100))
