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
def switch_off():
    switch_pin(pin_luces, False)
    return_answer(1, "Everything is off.")

@app.route('/switch_on')
def switch_on():
    switch_pin(pin_luces, True)
    return_answer(1, "Everything is on.")

@app.route('/morning')
def good_morning():
    return {"destiny":"1", "message":"Good morning, Joaquin"}

@app.route('/search/<term>')
def search_wikipedia(term):
    description = wikipedia.summary(term, sentences=1)

    return_answer(1, description)

def return_answer(destiny, message):
    return jsonify({"destiny":destiny, "message":message})

@app.route('/<path:data>')
def get_message(data):
    return_message = 'Error parsing the response in the server.'

    if 'hello' in data:
        return_message = good_morning()
        return jsonify(return_message)

    else:
        return jsonify(return_message)

def switch_pin(pin, state):
    GPIO.output(pin, state)