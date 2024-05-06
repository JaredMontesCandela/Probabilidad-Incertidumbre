"""
Objetivo del código: Calcular y mostrar si dos eventos son independientes dado un tercer evento específico.
En este ejemplo, supongamos que estamos lanzando dos dados y queremos determinar si los 
 resultados de los dados son independientes dado que la suma de los resultados es igual a 7. 
"""

# Definimos una función para calcular si dos eventos son independientes dado un tercer evento
def independencia_condicional():
    # Contamos la cantidad total de lanzamientos de dados
    total_lanzamientos = 0
    # Contamos la cantidad de lanzamientos que cumplen la condición (suma de los resultados igual a 7)
    condicion_cumplida = 0
    # Contamos la cantidad de lanzamientos que cumplen la condición y ambos dados muestran un número par
    condicion_y_pares = 0
    
    # Realizamos los lanzamientos de los dados
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            total_lanzamientos += 1
            # Verificamos si la suma de los resultados es igual a 7
            if dado1 + dado2 == 7:
                condicion_cumplida += 1
                # Verificamos si ambos dados muestran un número par
                if dado1 % 2 == 0 and dado2 % 2 == 0:
                    condicion_y_pares += 1
    
    # Calculamos las probabilidades de los eventos
    probabilidad_condicion = condicion_cumplida / total_lanzamientos
    probabilidad_condicion_y_pares = condicion_y_pares / total_lanzamientos
    
    # Verificamos si los eventos son independientes
    if probabilidad_condicion_y_pares == probabilidad_condicion * probabilidad_condicion:
        return True
    else:
        return False

# Verificamos si los eventos son independientes dado un tercer evento
if independencia_condicional():
    print("Los eventos son independientes dado un tercer evento específico.")
else:
    print("Los eventos no son independientes dado un tercer evento específico.")
