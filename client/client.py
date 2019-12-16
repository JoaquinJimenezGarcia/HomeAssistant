import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
import requests
import json
from gtts import gTTS

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Waiting...")
        audio = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(audio, language="es-ES")
        print(data)
        if data == 'Mónica':
            escucha()
    except sr.UnknownValueError:
        print("Error on value")
    except sr.RequestError as e:
        print("No se ha obtenido respuesta desde los servicios de Google Speech Recognition: " + e)

    return data

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

    return data

def jarvis(data):
    if "hola" in data:
        '''speech = gTTS(text="Hola, Joaquin",lang='es',slow=False)
        speech.save("voz.mp3")
        
        os.system("mpg321 voz.mp3")'''
        request = requests.get("http://192.168.1.104:5000/encender")
        respuesta = json.loads(request.text)
        
        speech = gTTS(text=respuesta["mensaje"],lang='es',slow=False)
        speech.save("voz.mp3")
        
        os.system("mpg321 voz.mp3")

    elif "adiós" in data:
        request = requests.get("http://192.168.1.104:5000/apagar")
        respuesta = json.loads(request.text)
        
        speech = gTTS(text=respuesta["mensaje"],lang='es',slow=False)
        speech.save("voz.mp3")
        
        os.system("mpg321 voz.mp3")
        

while 1:
    data = recordAudio()
    jarvis(data)