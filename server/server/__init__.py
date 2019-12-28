from flask import Flask,jsonify
import RPi.GPIO as GPIO
from settings import *

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_luces, GPIO.OUT)

@app.route('/')
def index():
    return jsonify({"message":"This is your home assistant from the net"})

@app.route('/apagar')
def apagar():
    GPIO.output(pin_luces, False)
    return jsonify({"destinatario":1,"mensaje":"Todo apagado"})

@app.route('/encender')
def encender():
    GPIO.output(pin_luces, True)
    return jsonify({"destinatario":1,"mensaje":"Todo encendido"})

@app.route('/buenos-dias')
def buenosdias():
    return jsonify({"destinatario":1,"mensaje":"Buenos días, Joaquín"})
