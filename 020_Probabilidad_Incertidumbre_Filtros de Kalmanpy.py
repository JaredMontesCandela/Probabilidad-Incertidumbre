"""
El objetivo de este ejemplo es ilustrar cómo utilizar el filtro de Kalman para estimar la posición de un objeto en movimiento en una dimensión.
"""
"""
Supongamos que tenemos un objeto que se mueve en línea recta con una velocidad constante y queremos estimar su posición utilizando un filtro de Kalman.

En este ejemplo, utilizamos el filtro de Kalman para estimar la posición de un objeto en movimiento en una dimensión.
Las mediciones del sensor están sujetas a ruido, y el filtro de Kalman se utiliza para combinar las mediciones con el modelo
de movimiento del objeto para proporcionar una estimación precisa de la posición del objeto. 
La salida son las posiciones reales del objeto, las mediciones del sensor (con ruido) y las posiciones estimadas por el filtro de Kalman.
"""

import random

class FiltroKalman:
    def __init__(self, x0, P0, A, Q, H, R):
        self.x = x0  # Estado inicial estimado
        self.P = P0  # Covarianza del estado inicial estimado
        self.A = A    # Matriz de transición del estado
        self.Q = Q    # Covarianza del proceso de transición
        self.H = H    # Matriz de observación
        self.R = R    # Covarianza de la observación

    def predecir(self):
        # Predicción del estado siguiente
        self.x = self.A * self.x
        # Predicción de la covarianza del estado siguiente
        self.P = self.A * self.P * self.A + self.Q

    def actualizar(self, z):
        # Residual (diferencia entre la observación real y la predicción)
        y = z - self.H * self.x
        # Ganancia de Kalman
        K = self.P * self.H / (self.H * self.P * self.H + self.R)
        # Actualización del estado estimado
        self.x = self.x + K * y
        # Actualización de la covarianza del estado estimado
        self.P = (1 - K * self.H) * self.P

# Parámetros del problema
x0 = 0      # Posición inicial estimada
P0 = 1      # Covarianza del estado inicial estimado
A = 1       # Matriz de transición del estado (movimiento rectilíneo)
Q = 0.01    # Covarianza del proceso de transición (ruido del proceso)
H = 1       # Matriz de observación (medición de la posición)
R = 0.1     # Covarianza de la observación (error de medición)

# Creamos un filtro de Kalman
filtro = FiltroKalman(x0, P0, A, Q, H, R)

# Simulamos la posición real del objeto (movimiento rectilíneo con velocidad constante)
posicion_real = [i * 0.5 for i in range(20)]

# Simulamos las mediciones del sensor (con ruido)
mediciones = [pos + random.normalvariate(0, 0.1) for pos in posicion_real]

# Aplicamos el filtro de Kalman para estimar la posición del objeto
posiciones_estimadas = []
for z in mediciones:
    filtro.predecir()
    filtro.actualizar(z)
    posiciones_estimadas.append(filtro.x)

# Imprimimos los resultados
print("Posición Real del Objeto:")
print(posicion_real)
print("\nMediciones del Sensor (con ruido):")
print(mediciones)
print("\nPosiciones Estimadas por el Filtro de Kalman:")
print(posiciones_estimadas)
