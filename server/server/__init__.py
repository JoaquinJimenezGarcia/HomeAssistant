__author__ = 'JJGDevelopment'

from flask import Flask,jsonify
import RPi.GPIO as GPIO
from gtts import gTTS
import yaml
import wikipedia

app = Flask(__name__)

with open("server/server/config.yaml", "r") as f:
    config = yaml.load(f)

pin_luces = config['pin_lights']

wikipedia.set_lang("en")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_luces, GPIO.OUT)

@app.route('/')
def status():
    return {"destiny":"1", "message":"This is your home assistant from the net."}

@app.route('/switch_off')
def switch_off():
    switch_pin(pin_luces, False)
    
    return {"destiny":"1", "message":"Everything is off."}

@app.route('/switch_on')
def switch_on():
    switch_pin(pin_luces, True)

    return {"destiny":"1", "message":"Everything is on."}

@app.route('/morning')
def good_morning():
    return {"destiny":"1", "message":"Good morning, Joaquin"}

@app.route('/search/<term>')
def search_wikipedia(term):
    description = wikipedia.summary(term, sentences=1)

    return {"destiny":"1", "message":description}

@app.route('/<path:data>')
def get_message(data):
    return_message = 'Error parsing the response in the server.'

    if 'hello' in data:
        return_message = good_morning()
    elif 'what is' in data:
        term = data.replace("what is ", "")
        return_message = search_wikipedia(term)
    elif 'bye' in data:
        return_message = switch_off()
    elif 'turn on' in data:
        return_message = switch_on()

    return jsonify(return_message)

def switch_pin(pin, state):
    GPIO.output(pin, state)