# GPIOFlaskGateway
Flask-based REST API for interacting with a Raspberry PI GPIO pins

Tool used to read and update the Raspberry PI GPIO pins using HTTP request from a remote computer.

## Pre-requisites

Install python3, flask and pytho3-RPo-GPIO

```
sudo apt-get install python3-dev python3-rpi.gpio
pip install flask
```

## How to run

```
export FLASK_APP=flask_app.py
flask run -h 0.0.0.0 -p 5000
```

# Available enpoints
GET /pin : Get a JSON will all the pins (up to 20) statuses.

GET /pin/[pin id]: Get a JSON with the status of a specific pin.

GET /pin/[pin id]/[0|1]: Activate or deactivate a pin given its id.




