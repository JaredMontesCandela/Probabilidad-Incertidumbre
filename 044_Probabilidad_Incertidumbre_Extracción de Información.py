# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:15:56 2024

@author: jared
"""

import re

# Texto que contiene información sobre productos y precios
texto = "El precio del producto A es $20. El producto B cuesta $15.99."

# Definir patrones de búsqueda para nombres de productos y precios
patron_producto = r'producto\s([A-Za-z]+)'
patron_precio = r'\$\d+(\.\d+)?'

# Función para extraer información sobre productos y precios
def extraer_informacion(texto):
    productos = re.findall(patron_producto, texto)
    precios = re.findall(patron_precio, texto)
    return list(zip(productos, precios))

# Ejemplo de uso
informacion_extraida = extraer_informacion(texto)
print("Información extraída:")
for producto, precio in informacion_extraida:
    print("Producto:", producto, "- Precio:", precio)
