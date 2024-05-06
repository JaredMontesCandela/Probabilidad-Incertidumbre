# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:43:01 2024

@author: jared
"""

# Diccionario de traducción inglés-español
diccionario_traduccion = {
    'cat': 'gato',
    'dog': 'perro',
    'apple': 'manzana'
}

# Función para realizar la traducción de una palabra de inglés a español
def traducir_palabra(palabra_ingles):
    return diccionario_traduccion.get(palabra_ingles, 'No se encontró la traducción')

# Ejemplo de uso
palabra_ingles = 'dog'
traduccion = traducir_palabra(palabra_ingles)
print(f'Traducción de "{palabra_ingles}" a español:', traduccion)
