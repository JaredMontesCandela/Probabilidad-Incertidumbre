# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:06:20 2024

@author: jared
"""
# Definir un corpus de ejemplo
corpus = [
    "Este es un ejemplo de texto",
    "El texto puede contener varias oraciones",
    "Cada oración puede tener palabras diferentes",
    "Ejemplo es una palabra común en este corpus",
    "Texto es una palabra común también"
]

# Tokenizar el corpus en palabras
words = [word.lower() for sentence in corpus for word in sentence.split()]

# Calcular la frecuencia de cada palabra en el corpus
word_freq = {}
total_words = len(words)
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Calcular la probabilidad de cada palabra
word_prob = {word: freq / total_words for word, freq in word_freq.items()}

# Ejemplo de uso
print("Probabilidad de la palabra 'ejemplo':", word_prob['ejemplo'])
print("Probabilidad de la palabra 'texto':", word_prob['texto'])
