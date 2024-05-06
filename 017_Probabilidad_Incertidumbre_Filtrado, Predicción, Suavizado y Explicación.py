"""

"""
import numpy as np

# Función para simular la medición del sensor de posición
def medir_posicion(verdadera_posicion, error_medicion):
    return verdadera_posicion + np.random.normal(0, error_medicion)

# Implementación del filtro de Kalman
class FiltroKalman:
    def __init__(self, x0, P0, A, Q, H, R):
        self.x = x0  # Estado inicial estimado
        self.P = P0  # Covarianza del estado inicial estimado
        self.A = A    # Matriz de transición del estado
        self.Q = Q    # Covarianza del proceso de transición
        self.H = H    # Matriz de observación
        self.R = R    # Covarianza de la observación

    def filtrar(self, medicion):
        # Predicción
        x_prediccion = np.dot(self.A, self.x)
        P_prediccion = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        # Actualización
        y = medicion - np.dot(self.H, x_prediccion)
        S = np.dot(np.dot(self.H, P_prediccion), self.H.T) + self.R
        K = np.dot(np.dot(P_prediccion, self.H.T), np.linalg.inv(S))
        self.x = x_prediccion + np.dot(K, y)
        self.P = P_prediccion - np.dot(np.dot(K, self.H), P_prediccion)

    def predecir(self):
        # Predicción
        self.x = np.dot(self.A, self.x)
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

    def suavizar(self, filtro_anterior):
        # Paso de suavizado de Kalman
        J = np.dot(np.dot(self.P, self.A.T), np.linalg.inv(filtro_anterior.P))
        self.x = self.x + np.dot(J, filtro_anterior.x - np.dot(self.A, self.x))
        self.P = self.P + np.dot(np.dot(J, filtro_anterior.P - self.P), J.T)

# Parámetros del problema
x0 = np.array([0])  # Estado inicial estimado
P0 = np.array([[1]])  # Covarianza del estado inicial estimado
A = np.array([[1]])   # Matriz de transición del estado (movimiento rectilíneo)
Q = np.array([[0.01]])  # Covarianza del proceso de transición
H = np.array([[1]])   # Matriz de observación (medición de la posición)
R = np.array([[0.1]])  # Covarianza de la observación (error de medición)

# Creamos un filtro de Kalman
filtro = FiltroKalman(x0, P0, A, Q, H, R)

# Simulación de movimiento del objeto y mediciones del sensor
num_pasos = 20
verdadera_posicion = np.linspace(0, 10, num_pasos)
posiciones_medidas = [medir_posicion(pos, 0.1) for pos in verdadera_posicion]

# Filtrado y predicción
for medicion in posiciones_medidas:
    filtro.filtrar(medicion)
    filtro.predecir()

# Suavizado
filtros_suavizados = []
filtro_actual = filtro
for medicion in reversed(posiciones_medidas):
    filtro_actual.suavizar(filtro)
    filtros_suavizados.append(filtro_actual)
    filtro_actual = filtro

# Imprimimos los resultados
print("Resultados del Filtro de Kalman:")
for i, medicion in enumerate(posiciones_medidas):
    print(f"Medición {i+1}: Posición medida = {medicion:.2f}, Posición estimada = {filtro.x[0]:.2f}")

# Imprimimos los resultados del suavizado
print("\nResultados del Suavizado de Kalman:")
for i, filtro_suavizado in enumerate(reversed(filtros_suavizados)):
    print(f"Medición {num_pasos-i}: Posición suavizada = {filtro_suavizado.x[0]:.2f}")
