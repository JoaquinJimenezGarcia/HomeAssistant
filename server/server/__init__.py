__author__ = 'JJGDevelopment'

from flask import Flask,jsonify
import RPi.GPIO as GPIO
from gtts import gTTS
import os
import wikipedia

app = Flask(__name__)

pin_luces = 7

wikipedia.set_lang("en")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_luces, GPIO.OUT)

@app.route('/')
def index():
    return_answer(1, "This is your home assistant from the net.")

@app.route('/switch_off')
def apagar():
    switch_pin(pin_luces, False)
    return_answer(1, "Everything is off.")

@app.route('/switch_on')
def encender():
    switch_pin(pin_luces, True)
    return_answer(1, "Everything is on.")

@app.route('/morning')
def buenosdias():
    return_answer(1, "Good morning, Joaquin")

@app.route('/search/<term>')
def search_wikipedia(term):
    description = wikipedia.summary(term, sentences=1)

    return_answer(1, description)

def return_answer(destiny, message):
    return jsonify({"destiny":destiny, "message":message})

def switch_pin(pin, state):
    GPIO.output(pin, state)