"""
Objetivo del código: Aplicar la Regla de Bayes para calcular la probabilidad de que un paciente 
tenga una enfermedad, dado el resultado positivo de una prueba, utilizando las probabilidades de 
la enfermedad y la precisión de la prueba. 
"""
# Definimos una función para aplicar la Regla de Bayes
def regla_de_bayes(prob_enfermedad, prob_positivo_dado_enfermedad, prob_positivo_dado_no_enfermedad):
    # Calculamos la probabilidad de tener la enfermedad dado un resultado positivo de la prueba
    prob_no_enfermedad = 1 - prob_enfermedad
    prob_positivo = (prob_enfermedad * prob_positivo_dado_enfermedad) + (prob_no_enfermedad * prob_positivo_dado_no_enfermedad)
    prob_enfermedad_dado_positivo = (prob_enfermedad * prob_positivo_dado_enfermedad) / prob_positivo
    return prob_enfermedad_dado_positivo

# Definimos las probabilidades de la enfermedad y la precisión de la prueba
prob_enfermedad = 0.01  # Probabilidad de que un paciente tenga la enfermedad
prob_positivo_dado_enfermedad = 0.95  # Probabilidad de un resultado positivo de la prueba dado que el paciente tiene la enfermedad
prob_positivo_dado_no_enfermedad = 0.05  # Probabilidad de un resultado positivo de la prueba dado que el paciente no tiene la enfermedad

# Aplicamos la Regla de Bayes para calcular la probabilidad de tener la enfermedad dado un resultado positivo de la prueba
probabilidad = regla_de_bayes(prob_enfermedad, prob_positivo_dado_enfermedad, prob_positivo_dado_no_enfermedad)

# Imprimimos el resultado
print("La probabilidad de que un paciente tenga la enfermedad dado un resultado positivo de la prueba es:", probabilidad)
