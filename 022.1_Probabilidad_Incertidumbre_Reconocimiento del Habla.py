# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:53:39 2024

@author: jared
"""
"""
pip install pyaudio- necesitas intalar esta libreria para grabar el audio

"""
import pyaudio
import wave

def grabar_audio(nombre_archivo, duracion_segundos):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = duracion_segundos

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Grabando...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Grabación finalizada.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(nombre_archivo, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Nombre del archivo a grabar y duración en segundos
nombre_archivo = 'audio.wav'
duracion_segundos = 3

# Llamamos a la función para grabar audio
grabar_audio(nombre_archivo, duracion_segundos)
