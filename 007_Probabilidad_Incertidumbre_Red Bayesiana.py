"""
Este código crea una red bayesiana simple con dos nodos (clima y lleva_paraguas) y sus 
probabilidades condicionales correspondientes. Luego, realizamos una predicción para 
determinar la probabilidad de que alguien lleve un paraguas dado que el clima es lluvioso.    

"""
# Definimos las probabilidades
prob_lluvia = 0.3
prob_sol = 0.7

prob_lleva_paraguas_dado_lluvia = 0.8
prob_lleva_paraguas_dado_sol = 0.2

# Calculamos la probabilidad de llevar un paraguas y no llevar un paraguas independientemente del clima
prob_lleva_paraguas = (prob_lluvia * prob_lleva_paraguas_dado_lluvia) + (prob_sol * prob_lleva_paraguas_dado_sol)
prob_no_lleva_paraguas = 1 - prob_lleva_paraguas

# Calculamos la probabilidad condicional de llevar un paraguas dado el clima
prob_lleva_paraguas_dado_lluvia = (prob_lluvia * prob_lleva_paraguas_dado_lluvia) / prob_lleva_paraguas
prob_lleva_paraguas_dado_sol = (prob_sol * prob_lleva_paraguas_dado_sol) / prob_lleva_paraguas

# Mostramos los resultados
print("Probabilidad de llevar un paraguas:", prob_lleva_paraguas)
print("Probabilidad de no llevar un paraguas:", prob_no_lleva_paraguas)
print("Probabilidad de llevar un paraguas dado que está lloviendo:", prob_lleva_paraguas_dado_lluvia)
print("Probabilidad de llevar un paraguas dado que hace sol:", prob_lleva_paraguas_dado_sol)

