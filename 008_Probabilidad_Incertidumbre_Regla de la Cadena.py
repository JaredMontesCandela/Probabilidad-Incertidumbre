"""
En este ejemplo, estamos calculando la probabilidad conjunta de tres eventos A, B y C utilizando 
la regla de la cadena. Se asumen las probabilidades condicionales de los eventos B y C dados los 
eventos anteriores A y B, respectivamente.    
"""

# Definimos las probabilidades de los eventos A, B y C
prob_A = 0.6
prob_B_dado_A = 0.8
prob_C_dado_A_B = 0.9

# Calculamos la probabilidad conjunta utilizando la regla de la cadena
prob_conjunta = prob_A * prob_B_dado_A * prob_C_dado_A_B

# Imprimimos el resultado
print("La probabilidad conjunta de los eventos A, B y C es:", prob_conjunta)
