import requests
from flask import Flask
app = Flask(__name__)


wallet_ip='localhost'
wallet_port='5000'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/request/transfer_money/<amount>', methods=['GET','POST'])
def request_money(amount):
  print(amount)
  return amount


@app.route('/request/withdraw_money/<amount>', methods=['POST'])
def withdraw_funds(amount):
  return requests.get('http://example.com').content



#@app.route('/test_post',  methods=['POST'])
#def create_smart_contract():
#    print("This works!")
#    print(requests.post('http://localhost:5000/request/transfer_money/5000').content)


@app.route('/receive/sensordata/<sensor_id>/<sensor_value>', methods=['POST'])
def receive_sensordata(sensor_id, sensor_value):
  print('Id and data')
  return 'Id and data'

@app.route('/receive/diagnostics/report/<machine>/<report>', methods=['POST'])
def receive_diagnostics(machine, report):
  print('Diagnostics Report')
  return 'Diagnostics Report'


def notify_wallet(status=working, machine_id = 1):
  Request = requests.post('http://localhost:5001/update/machine/' + machine_id + '/status/' + working)
  return Request