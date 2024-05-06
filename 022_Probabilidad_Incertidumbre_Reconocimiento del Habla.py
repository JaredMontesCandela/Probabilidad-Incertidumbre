"""
pip install SpeechRecognition necesitas descargar esta extension 
ademas esta otro codigo se llama 022.1_Probabilidad_Incertidumbre_Reconocimiento del Habla.py
con este codigo puedes grabar tu el audio
"""


import speech_recognition as sr

# Función para realizar el reconocimiento del habla
def reconocimiento_habla(archivo_audio):
    # Inicializamos el reconocedor de voz
    reconocedor = sr.Recognizer()
    
    # Cargamos el archivo de audio
    with sr.AudioFile(archivo_audio) as audio:
        # Escuchamos el audio y realizamos el reconocimiento
        try:
            audio_data = reconocedor.record(audio)
            texto_transcrito = reconocedor.recognize_google(audio_data, language='es-ES')  # Reconocimiento utilizando la API de Google
            return texto_transcrito
        except sr.UnknownValueError:
            return "No se pudo entender el audio"
        except sr.RequestError as e:
            return f"No se pudo completar la solicitud: {e}"

# Archivo de audio a transcribir (debe estar en formato compatible)
archivo_audio = "audio.wav"

# Realizamos el reconocimiento del habla
texto_transcrito = reconocimiento_habla(archivo_audio)

# Imprimimos el resultado
print("Texto Transcrito:")
print(texto_transcrito)
