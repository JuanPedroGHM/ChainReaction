import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from muWallet import MUContractWallet

app = Flask(__name__)
CORS(app, support_credentials=True)

wallet = MUContractWallet('http://127.0.0.1:8545', 'keys.txt', 0)

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
    print(request)
    contractAddr, contractAbi = wallet.createContract(data['providerAddr'], data['value'])

    return jsonify({ 'contractAddr': contractAddr, 'contractAbi': contractAbi}), 200

# Transfer euro to contract
# {
#   'contractAddr': addr,
#   'value': amount # (in euro)
# }
@app.route('/contract/transfer/euro', methods = ['POST'])
def transferEuros(contractAddr, amount):
    data = request.get_json()
    wallet.sendEurosToContract(data['contractAddr'], data['value'])
    return jsonify('OK')

# Transfer ether to contract
# {
#   'contractAddr': addr,
#   'value': amount # (in ether)
# }
@app.route('/contract/transfer/ether', methods = ['POST'])
def transferEther(contractAddr, amount):
    data=request.get_json()
    wallet.sendEtherToContract(data['contractAddr'], data['value'])
    return jsonify({ 'OK' })

# Withdraw
# {
#   'contractAddr': addr
# }
@app.route('/contract/withdraw', methods = ['POST'])
def withdraw(contractAddr):
    data = request.get_json()
    wallet.withdraw(data['contractAddr'])
    return createBalanceResponse(wallet)

#
# {
#   'contractAddr': addr
# }
@app.route('/contract/ackRepair', methods = ['POST'])
def ackRepair(contractAddr):
    data = request.get_json()
    wallet.ackRepair(data['contractAddr'])
    response = {
        'balance': createBalanceResponse(wallet)
    }
    return jsonify(response)


@app.route('/wallet/balance', methods = ['GET'])
def getContractBalance():
    response = {
        'balance': createBalanceResponse(wallet)
    }
    return jsonify(response)


if __name__ == '__main__':
  app.run('127.0.0.1', 5000)

