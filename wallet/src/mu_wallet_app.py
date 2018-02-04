import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import requests

from muWallet import MUContractWallet

app = Flask(__name__)
CORS(app, support_credentials=True)

wallet = MUContractWallet('http://127.0.0.1:8545', 'keys.txt', 0)



@app.route('/wallet/balance', methods=['GET'])
@cross_origin(supports_credentials=True)
def getBalance():
    response = {
        'balance' : str(wallet.getBalance())
    }
    return jsonify(response), 200

# Create a new contract
# {
#   'machineID': ID,
#   'value': amount # (in ether),
#   'providerAddr': provAddr
# }
@app.route('/contract/new', methods=['POST'])
@cross_origin(supports_credentials=True)
def newContract():
    data = request.get_json()

    contractAddr, contractAbi = wallet.createContract(data['providerAddr'], data['value'])

    requests.post(data['providerUrl'] + '/contract/new', json = {
        'contractAddr' : contractAddr,
        'contractAbi' : contractAbi,
        'value' : data['value'],
        'machineID' : data['machineID'],
        'muAddr' : wallet.publicKey
    })

    return jsonify({ 'contractAddr': contractAddr, 'contractAbi': contractAbi}), 200

# Transfer euro to contract
# {
#   'contractAddr': addr,
#   'value': amount # (in euro)
# }
@app.route('/contract/transfer/euro', methods = ['POST'])
@cross_origin(supports_credentials=True)
def transferEuros():
    data = request.get_json()
    wallet.sendEurosToContract(data['contractAddr'], data['value'])
    return getBalance()

# Transfer ether to contract
# {
#   'contractAddr': addr,
#   'value': amount # (in ether)
# }
@app.route('/contract/transfer/ether', methods = ['POST'])
@cross_origin(supports_credentials=True)
def transferEther():
    data=request.get_json()
    wallet.sendEtherToContract(data['contractAddr'], data['value'])
    return getBalance()

# Withdraw
# {
#   'contractAddr': addr
# }
@app.route('/contract/finished', methods = ['POST'])
@cross_origin(supports_credentials=True)
def withdraw():
    data = request.get_json()
    wallet.withdraw(data['contractAddr'])
    return getBalance()

#
# {
#   'contractAddr': addr
# }
@app.route('/contract/ackRepair', methods = ['POST'])
@cross_origin(supports_credentials=True)
def ackRepair():
    data = request.get_json()
    wallet.ackRepair(data['contractAddr'])

    # requests.post(data['providerUrl'] + '/contract/finished', json = {
    #     'contractAddr' : data['contractAddr'],
    # })

    return getBalance()


if __name__ == '__main__':
  app.run('127.0.0.1', 5000)

