import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
import requests
import json
from gtts import gTTS
from settings import *


def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Waiting...")
        audio = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(audio, language="es-ES")
        print(data)
        if data == 'Asistente':
            escucha()
    except sr.UnknownValueError:
        print("Error on value")
    except sr.RequestError as e:
        print("No se ha obtenido respuesta desde los servicios de Google Speech Recognition: " + e)


def escucha():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hearing...")
        audio = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(audio, language="es-ES")
        print("You've said: " + data)
        jarvis(data)
    except sr.UnknownValueError:
        print("Hearing...")
    except sr.RequestError as e:
        print("No se ha obtenido respuesta desde los servicios de Google Speech Recognition: " + e)

    recordAudio()


def jarvis(data):
    if "hola" in data:
        request = requests.get(ip_server+"encender")
        respuesta = json.loads(request.text)
        
        speech = gTTS(text=respuesta["mensaje"],lang='es',slow=False)
        speech.save("voz.mp3")
        
        os.system("mpg321 voz.mp3")

    elif "adiós" in data:
        request = requests.get(ip_server+"apagar")
        respuesta = json.loads(request.text)
        
        speech = gTTS(text=respuesta["mensaje"],lang='es',slow=False)
        speech.save("voz.mp3")
        
        os.system("mpg321 voz.mp3")
        

while 1:
    recordAudio()