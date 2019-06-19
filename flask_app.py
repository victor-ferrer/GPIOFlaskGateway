from flask import Flask, jsonify, request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

# Get the status of a GPIO pin by its ID
@app.route('/pin/<pin>', methods=['GET'])
def getPinStatus(pin):
    try:
       GPIO.setup(int(pin), GPIO.IN)
       status = GPIO.input(int(pin))
    except:
       status = -1

    data = {'pin' :  pin, 'status' : response }

    return jsonify(data), 200

# Get all pins statuses
@app.route('/pin', methods=['GET'])
def getAllPinStatuses():

    data = []
    for pin in list(range(20)):
         GPIO.setup(int(pin), GPIO.IN)
         data.append({'pin' : pin, 'status' : GPIO.input(int(pin))})

    return jsonify(data), 200

# Modify (negate) the status of a pin, given its ID
@app.route('/pin/<pin>', methods=['POST'])
def setPinStatus(pin):
    try:
       GPIO.setup(int(pin), GPIO.IN)
       status = GPIO.input(int(pin))
       GPIO.setup(int(pin), GPIO.OUT)
       GPIO.output(int(pin), not status)

       data = {'pin' :  pin, 'status' : not status
       }

    except:
       return jsonify('Error'), 500
    
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



