"""
Objetivo del código: Realizar inferencia por enumeración para calcular la probabilidad de un evento dado un conjunto de evidencia.
En este código, modelamos el clima como un proceso de Manto de Markov donde el clima en un día dado depende solo del clima del día anterior   
"""
import itertools

# Definimos la red bayesiana
red_bayesiana = {
    'Enfermedad': {'prob': 0.1, 'padres': [], 'hijos': ['Prueba_A', 'Prueba_B']},
    'Prueba_A': {'prob': {'Enfermedad': {True: 0.9, False: 0.05}}, 'padres': ['Enfermedad'], 'hijos': []},
    'Prueba_B': {'prob': {'Enfermedad': {True: 0.85, False: 0.1}}, 'padres': ['Enfermedad'], 'hijos': []}
}

# Definimos la función para realizar inferencia por enumeración
def inferencia_por_enumeracion(red_bayesiana, evidencia):
    # Obtenemos la lista de todas las variables en la red bayesiana
    variables = list(red_bayesiana.keys())
    # Obtenemos la lista de variables no observadas (ocultas)
    ocultas = [v for v in variables if v not in evidencia]
    # Inicializamos la probabilidad total
    prob_total = 0
    # Iteramos sobre todas las combinaciones posibles de valores para las variables ocultas
    for valores_posibles in itertools.product([True, False], repeat=len(ocultas)):
        # Creamos un diccionario con las asignaciones de valores a las variables ocultas
        asignaciones = dict(zip(ocultas, valores_posibles))
        # Inicializamos la probabilidad conjunta
        prob_conjunta = 1
        # Iteramos sobre todas las variables en la red bayesiana
        for variable in variables:
            if variable in evidencia:
                # Si la variable está en la evidencia, multiplicamos la probabilidad por la probabilidad de la evidencia
                prob_conjunta *= red_bayesiana[variable]['prob'] if evidencia[variable] else (1 - red_bayesiana[variable]['prob'])
            else:
                # Si la variable no está en la evidencia, calculamos la probabilidad condicional
                padres = red_bayesiana[variable]['padres']
                prob_condicional = red_bayesiana[variable]['prob'][padres[0]][asignaciones[padres[0]]]
                prob_conjunta *= prob_condicional if asignaciones[variable] else (1 - prob_condicional)
        # Sumamos la probabilidad conjunta a la probabilidad total
        prob_total += prob_conjunta
    # Devolvemos la probabilidad total
    return prob_total

# Definimos la evidencia (ambas pruebas son positivas)
evidencia = {'Prueba_A': True, 'Prueba_B': True}

# Realizamos inferencia por enumeración
probabilidad_enfermedad = inferencia_por_enumeracion(red_bayesiana, evidencia)

# Imprimimos el resultado
print("La probabilidad de tener la enfermedad dado que ambas pruebas son positivas es:", probabilidad_enfermedad)
