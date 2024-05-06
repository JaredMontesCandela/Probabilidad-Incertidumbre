"""
El objetivo de la práctica es aprender sobre la inferencia probabilística y cómo aplicar diferentes 
técnicas para realizar inferencias en modelos bayesianos."""

# Definimos la red bayesiana
red_bayesiana_enfermedades = {
    'Gripe': {'prob': 0.05, 'padres': [], 'hijos': ['Fiebre', 'Congestion_Nasal']},
    'Resfriado': {'prob': 0.1, 'padres': [], 'hijos': ['Fiebre', 'Congestion_Nasal']},
    'Fiebre': {'prob': {'Gripe': {True: 0.9, False: 0.1}, 'Resfriado': {True: 0.7, False: 0.3}}, 'padres': ['Gripe', 'Resfriado'], 'hijos': []},
    'Congestion_Nasal': {'prob': {'Gripe': {True: 0.5, False: 0.5}, 'Resfriado': {True: 0.8, False: 0.2}}, 'padres': ['Gripe', 'Resfriado'], 'hijos': []}
}

# Definimos la función para realizar eliminación de variables
def eliminacion_de_variables(red_bayesiana, variables_ocultas, evidencia):
    # Inicializamos la probabilidad conjunta
    prob_conjunta = 1
    # Iteramos sobre las variables ocultas
    for variable_oculta in variables_ocultas:
        # Obtenemos los padres de la variable oculta
        padres = red_bayesiana[variable_oculta]['padres']
        # Obtenemos la probabilidad condicional de la variable oculta dado los padres
        prob_condicional = red_bayesiana[variable_oculta]['prob']
        for padre in padres:
            prob_condicional = prob_condicional[padre][evidencia[padre]]
        # Multiplicamos la probabilidad condicional a la probabilidad conjunta
        prob_conjunta *= prob_condicional
    return prob_conjunta

# Definimos la evidencia (el estudiante tiene fiebre)
evidencia = {'Fiebre': True}

# Realizamos eliminación de variables para calcular la probabilidad de gripe dado que el estudiante tiene fiebre
probabilidad_gripe = eliminacion_de_variables(red_bayesiana_enfermedades, ['Gripe'], evidencia)

# Imprimimos el resultado
print("La probabilidad de que el estudiante tenga gripe dado que tiene fiebre es:", probabilidad_gripe)
