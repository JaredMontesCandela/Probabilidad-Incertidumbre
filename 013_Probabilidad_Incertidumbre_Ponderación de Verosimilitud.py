"""
El objetivo de este ejemplo es aplicar la ponderación de verosimilitud en un modelo bayesiano
que describe la probabilidad de un evento de interés dado un conjunto de observaciones."""

# Definimos la red bayesiana
red_bayesiana_spam = {
    'Spam': {'prob': 0.2, 'padres': [], 'hijos': ['Palabra1', 'Palabra2', 'Palabra3']},
    'Palabra1': {'prob': {'Spam': {True: 0.8, False: 0.1}}, 'padres': ['Spam'], 'hijos': []},
    'Palabra2': {'prob': {'Spam': {True: 0.6, False: 0.2}}, 'padres': ['Spam'], 'hijos': []},
    'Palabra3': {'prob': {'Spam': {True: 0.7, False: 0.3}}, 'padres': ['Spam'], 'hijos': []}
}

# Definimos la función para realizar ponderación de verosimilitud
def ponderacion_de_verosimilitud(red_bayesiana, evidencia):
    # Inicializamos la probabilidad conjunta
    prob_conjunta = 1
    # Iteramos sobre las variables en la evidencia
    for variable, valor in evidencia.items():
        # Obtenemos la probabilidad condicional de la variable dado su valor
        prob_condicional = red_bayesiana[variable]['prob'][red_bayesiana[variable]['padres'][0]][valor]
        # Multiplicamos la probabilidad condicional a la probabilidad conjunta
        prob_conjunta *= prob_condicional
    return prob_conjunta

# Definimos la evidencia (presencia de palabras clave en el correo electrónico)
evidencia = {'Palabra1': True, 'Palabra2': True, 'Palabra3': False}

# Realizamos ponderación de verosimilitud para calcular la probabilidad de spam dado las palabras clave observadas
probabilidad_spam = ponderacion_de_verosimilitud(red_bayesiana_spam, evidencia)

# Imprimimos el resultado
print("La probabilidad de que el correo electrónico sea spam dado las palabras clave observadas es:", probabilidad_spam)
