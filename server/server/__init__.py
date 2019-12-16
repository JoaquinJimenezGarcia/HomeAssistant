from flask import Flask,jsonify
#import RPi.GPIO as GPIO

app = Flask(__name__)

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7, GPIO.OUT)

@app.route('/')
def index():
    return jsonify({"message":"This is your home assistant from the net"})

@app.route('/apagar')
def apagar():
#    GPIO.output(7, False)
    return jsonify({"destinatario":1,"mensaje":"Todo apagado"})

@app.route('/encender')
def encender():
#    GPIO.output(7, True)
    return jsonify({"destinatario":1,"mensaje":"Todo encendido"})

@app.route('/buenos-dias')
def buenosdias():
    return jsonify({"destinatario":1,"mensaje":""})
