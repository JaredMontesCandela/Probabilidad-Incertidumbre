# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:13:28 2024

@author: jared
"""

# Definir una lista de datos
data = [
    {'id': 1, 'nombre': 'Juan', 'edad': 25},
    {'id': 2, 'nombre': 'María', 'edad': 30},
    {'id': 3, 'nombre': 'Pedro', 'edad': 35},
    {'id': 4, 'nombre': 'Ana', 'edad': 28}
]

# Función para recuperar datos por ID
def recuperar_por_id(data, id):
    for item in data:
        if item['id'] == id:
            return item
    return None

# Función para recuperar datos por nombre
def recuperar_por_nombre(data, nombre):
    for item in data:
        if item['nombre'] == nombre:
            return item
    return None

# Ejemplo de uso
print("Recuperación por ID:")
print(recuperar_por_id(data, 2))

print("\nRecuperación por nombre:")
print(recuperar_por_nombre(data, 'Ana'))
