__author__ = 'JJGDevelopment'

import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
import requests
import json
from gtts import gTTS
from flask import Flask,jsonify

app = Flask(__name__)

ip_server="http://localhost:5000/"

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Waiting...")
        audio = r.listen(source)

    data = ""
    
    try:
        data = r.recognize_google(audio, language="en-EN")
        print(data)
        if data == 'hello':
            speak('Tell me, Joaquin')
            listen()
    except sr.UnknownValueError as e:
        print("Error on value: " + str(e))
    except sr.RequestError as e:
        print("Request error.")


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hearing...")
        audio = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(audio, language="en")
        jarvis(data)
    except sr.UnknownValueError:
        print("Hearing...")
    except sr.RequestError:
        print("Error gathering info.")

    recordAudio()


def jarvis(data):
    response_text = server_request(data)

    try:
        speak(response_text)
    except:
        speak("Sorry, I cannot help you with that.")


def server_request(api_path):    
    try:
        request = requests.get(ip_server + api_path)
        respuesta = json.loads(request.text)
        
        return respuesta['message']
    except:
        return "Sorry, there was an error trying to connect to server."

def speak(text):
    speech = gTTS(text=text,lang='en',slow=False)
    speech.save("voice.mp3")
        
    os.system("mpg321 voice.mp3")

while 1:
    recordAudio()
