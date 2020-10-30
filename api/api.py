import flask
from flask_cors import CORS, cross_origin
from patients import Patient
from patientrepository import patientrepositry
from bedsrepository import BedsRepositry

from flask import jsonify

from flask import request

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1>"


@app.route('/addBeds', methods=['POST'])
def addBedsRepository():
    numberofbeds = request.json['numberofbeds']
    message = BedsRepositry.addBeds(numberofbeds)
    return jsonify(message)


@app.route('/patient', methods=['POST'])
def patiententry():
    name = request.json['name']
    age = request.json['age']
    patientdetails = Patient(name, age)
    message = patientrepositry.addPatient(patientdetails)
    return jsonify(message)


@app.route('/alertonpatientstatus', methods=['GET'])
def alertonpatientstatus():
    message = patientrepositry.patientCheckVitals()
    return jsonify(message)


@app.route('/resetPatientStatus', methods=['POST'])
def ResetPatientStatus():
    bedid = request.json['bedid']
    message = patientrepositry.resetPatientVitals(bedid)
    return jsonify(message)


@app.route('/dischargePatient', methods=['POST'])
def dischargePatient():
    bedid = request.json['bedid']
    message = patientrepositry.dischargePatient(bedid)
    return jsonify(message)


app.run()
