"""
En este ejemplo, se implementan dos métodos de muestreo: muestreo directo y muestreo por rechazo. 
Ambos métodos generan muestras aleatorias de la red bayesiana proporcionada y calculan la probabilidad conjunta de las muestras
En el muestreo por rechazo, algunas muestras pueden ser rechazadas si no cumplen con ciertas condiciones de probabilidad conjunta. 
"""

import random

# Definimos la red bayesiana
red_bayesiana_enfermedad = {
    'Enfermedad': {'prob': 0.1, 'padres': [], 'hijos': ['Fiebre', 'Tos']},
    'Fiebre': {'prob': {'Enfermedad': {True: 0.9, False: 0.05}}, 'padres': ['Enfermedad'], 'hijos': []},
    'Tos': {'prob': {'Enfermedad': {True: 0.7, False: 0.2}}, 'padres': ['Enfermedad'], 'hijos': []}
}

# Función para realizar muestreo directo
def muestreo_directo(red_bayesiana, num_muestras):
    # Lista para almacenar las muestras
    muestras = []
    for _ in range(num_muestras):
        # Generamos una muestra aleatoria de la enfermedad
        enfermedad = random.random() < red_bayesiana['Enfermedad']['prob']
        # Generamos una muestra aleatoria de fiebre dado el estado de la enfermedad
        fiebre = random.random() < red_bayesiana['Fiebre']['prob']['Enfermedad'][enfermedad]
        # Generamos una muestra aleatoria de tos dado el estado de la enfermedad
        tos = random.random() < red_bayesiana['Tos']['prob']['Enfermedad'][enfermedad]
        # Agregamos la muestra a la lista de muestras
        muestras.append((enfermedad, fiebre, tos))
    return muestras

# Función para realizar muestreo por rechazo
def muestreo_por_rechazo(red_bayesiana, num_muestras):
    # Lista para almacenar las muestras aceptadas
    muestras_aceptadas = []
    # Contador de muestras rechazadas
    muestras_rechazadas = 0
    while len(muestras_aceptadas) < num_muestras:
        # Generamos una muestra aleatoria de la enfermedad
        enfermedad = random.random() < red_bayesiana['Enfermedad']['prob']
        # Generamos una muestra aleatoria de fiebre dado el estado de la enfermedad
        fiebre = random.random() < red_bayesiana['Fiebre']['prob']['Enfermedad'][enfermedad]
        # Generamos una muestra aleatoria de tos dado el estado de la enfermedad
        tos = random.random() < red_bayesiana['Tos']['prob']['Enfermedad'][enfermedad]
        # Calculamos la probabilidad conjunta de la muestra
        prob_conjunta = red_bayesiana['Enfermedad']['prob'] * red_bayesiana['Fiebre']['prob']['Enfermedad'][enfermedad] * red_bayesiana['Tos']['prob']['Enfermedad'][enfermedad]
        # Generamos un número aleatorio para determinar si aceptamos o rechazamos la muestra
        if random.random() < prob_conjunta:
            muestras_aceptadas.append((enfermedad, fiebre, tos))
        else:
            muestras_rechazadas += 1
    print(f"Número de muestras rechazadas: {muestras_rechazadas}")
    return muestras_aceptadas

# Realizamos muestreo directo y mostramos las muestras obtenidas
print("Muestreo Directo:")
muestras_directo = muestreo_directo(red_bayesiana_enfermedad, 5)
for muestra in muestras_directo:
    print(muestra)

# Realizamos muestreo por rechazo y mostramos las muestras obtenidas
print("\nMuestreo Por Rechazo:")
muestras_rechazo = muestreo_por_rechazo(red_bayesiana_enfermedad, 5)
for muestra in muestras_rechazo:
    print(muestra)
