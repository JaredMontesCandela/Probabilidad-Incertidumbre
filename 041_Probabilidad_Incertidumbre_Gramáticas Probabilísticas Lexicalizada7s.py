# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:01:08 2024

@author: jared
"""

import random

# Definir una gramática probabilística lexicalizada (PGL)
grammar = {
    'S': [['NP VP', 0.9], ['VP', 0.1]],
    'NP': [['Det N', 0.6], ['NP PP', 0.4]],
    'VP': [['V NP', 0.7], ['VP PP', 0.3]],
    'PP': [['P NP', 1.0]],
    'Det': {'el': 0.4, 'un': 0.6},
    'N': {'gato': 0.7, 'perro': 0.3},
    'V': {'persigue': 0.5, 'muerde': 0.5},
    'P': {'a': 0.7, 'con': 0.3}
}

# Función para generar una oración utilizando la PGL
def generate_sentence(grammar, start_symbol='NP'):
    sentence = []
    expansions = grammar[start_symbol]
    for expansion in expansions:
        if isinstance(expansion[0], str):
            sentence.extend(expansion[0].split())
        else:
            symbol = random.choices(list(expansion[0].keys()), weights=list(expansion[0].values()))[0]
            sentence.extend(generate_sentence(grammar, symbol))
    return sentence

# Generar una oración utilizando la PGL
sentence = generate_sentence(grammar)
print(' '.join(sentence))
