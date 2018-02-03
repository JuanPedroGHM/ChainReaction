import json
from flask import Flask, jsonify, request
from wallet import MUContractWallet, Wallet

app = Flask(__name__)

wallet = MUContractWallet('http://127.0.0.1:7545', 'keys.txt')
mywallet=Wallet('http://127.0.0.1:7545', 'keys.txt')



@app.route('/contract', methods=['POST'])
def newContract():
    data = request.get_json()

@app.route('/contract/transfer/euro', methods = ['POST'])
def transferEuros():
    return

@app.route('/contract/transfer/ether', methods = ['POST'])
def transferEther():
    return

@app.route('/contract/withdraw', methods = ['POST'])
def withdraw():
    return

@app.route('/contract/<contractid>/ackRepair', methods = ['POST'])
def ackRepair():
    return

@app.route('/contract/balance', methods = ['POST'])
def getContractBalance():
    response = createBalanceResponse(wallet)
    return response


def createBalanceResponse(wallet):
    response = {
        'balance': wallet.getBalance()
    }
    return jsonify(response)

if __name__ == '__main__':
  app.run('127.0.0.1',5000)

