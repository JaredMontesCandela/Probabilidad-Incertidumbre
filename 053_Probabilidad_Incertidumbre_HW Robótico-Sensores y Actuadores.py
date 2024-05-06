# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:17:32 2024

@author: jared
"""

import RPi.GPIO as GPIO
import time

# Definir los pines GPIO para los sensores infrarrojos
pin_sensor_izquierdo = 17
pin_sensor_derecho = 18

# Definir los pines GPIO para los motores DC
pin_motor_izquierdo_avance = 22
pin_motor_izquierdo_retroceso = 23
pin_motor_derecho_avance = 24
pin_motor_derecho_retroceso = 25

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_sensor_izquierdo, GPIO.IN)
GPIO.setup(pin_sensor_derecho, GPIO.IN)
GPIO.setup(pin_motor_izquierdo_avance, GPIO.OUT)
GPIO.setup(pin_motor_izquierdo_retroceso, GPIO.OUT)
GPIO.setup(pin_motor_derecho_avance, GPIO.OUT)
GPIO.setup(pin_motor_derecho_retroceso, GPIO.OUT)

# Función para avanzar
def avanzar():
    GPIO.output(pin_motor_izquierdo_avance, GPIO.HIGH)
    GPIO.output(pin_motor_derecho_avance, GPIO.HIGH)

# Función para retroceder
def retroceder():
    GPIO.output(pin_motor_izquierdo_retroceso, GPIO.HIGH)
    GPIO.output(pin_motor_derecho_retroceso, GPIO.HIGH)

# Función para girar a la izquierda
def girar_izquierda():
    GPIO.output(pin_motor_izquierdo_retroceso, GPIO.HIGH)
    GPIO.output(pin_motor_derecho_avance, GPIO.HIGH)

# Función para girar a la derecha
def girar_derecha():
    GPIO.output(pin_motor_izquierdo_avance, GPIO.HIGH)
    GPIO.output(pin_motor_derecho_retroceso, GPIO.HIGH)

# Función para detenerse
def detener():
    GPIO.output(pin_motor_izquierdo_avance, GPIO.LOW)
    GPIO.output(pin_motor_izquierdo_retroceso, GPIO.LOW)
    GPIO.output(pin_motor_derecho_avance, GPIO.LOW)
    GPIO.output(pin_motor_derecho_retroceso, GPIO.LOW)

try:
    while True:
        # Leer los valores de los sensores infrarrojos
        valor_sensor_izquierdo = GPIO.input(pin_sensor_izquierdo)
        valor_sensor_derecho = GPIO.input(pin_sensor_derecho)

        # Tomar decisiones basadas en los valores de los sensores
        if valor_sensor_izquierdo == 0 and valor_sensor_derecho == 0:
            avanzar()
        elif valor_sensor_izquierdo == 1 and valor_sensor_derecho == 0:
            girar_derecha()
        elif valor_sensor_izquierdo == 0 and valor_sensor_derecho == 1:
            girar_izquierda()
        else:
            retroceder()

except KeyboardInterrupt:
    detener()
    GPIO.cleanup()
