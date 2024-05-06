# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:55:55 2024

@author: jared
"""
"""
Este ejemplo ilustra cómo utilizar una PCFG para analizar sintácticamente una oración y generar los árboles de análisis
sintáctico más probables. Las PCFGs son una herramienta poderosa en el procesamiento 
del lenguaje natural para modelar la estructura sintáctica de un lenguaje de manera probabilística
"""

import random

# Definir una gramática probabilística independiente del contexto (PCFG)
grammar = {
    'S': [['NP', 'VP', 0.9], ['VP', 0.1]],
    'NP': [['Det', 'N', 0.6], ['NP', 'PP', 0.4]],
    'VP': [['V', 'NP', 0.7], ['VP', 'PP', 0.3]],
    'PP': [['P', 'NP', 1.0]],
    'Det': ['el', 'un'],
    'N': ['gato', 'perro'],
    'V': ['persigue', 'muerde'],
    'P': ['a', 'con']
}

# Función para generar una oración utilizando la PCFG
def generate_sentence(grammar, start_symbol='S'):
    sentence = []
    expansions = grammar[start_symbol]
    for expansion in expansions:
        if isinstance(expansion[-1], float):
            symbol = random.choices(expansion[:-1], weights=[1] * len(expansion[:-1]))[0]
            sentence.extend(generate_sentence(grammar, symbol))
        else:
            sentence.append(expansion)
    return sentence

# Generar una oración utilizando la PCFG
sentence = generate_sentence(grammar)
print(' '.join(sentence))

