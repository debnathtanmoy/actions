import requests
from flask import jsonify

url = 'http://127.0.0.1:5000/addBeds'
myobj = {"numberofbeds": "10"}

x = requests.post(url, json=myobj)
print(x.text)

url = 'http://127.0.0.1:5000/patient'
myobj = {"name": "Suresh", "age": "70"}

y = requests.post(url, json=myobj)
print(y.text)

url = 'http://127.0.0.1:5000//alertonpatientstatus'
x = requests.get(url)
print(x.text)

url = 'http://127.0.0.1:5000/dischargePatient'
myobj = {"bedid": "1"}
x = requests.post(url, json=myobj)
print(x.text)
