import json
from flask import Flask, jsonify, request
from wallet import MUContractWallet

app = Flask(__name__)

wallet = MUContractWallet('http://127.0.0.1:7545', 'keys.txt')

@app.route('/')




@app.route('/contract', methods=['POST'])
def newContract():
    data = request.get_json()

@app.route('/contract/transfer/euro', methods = ['POST'])
def transferEuros():

@app.route('/contract/tranfer/ether', methods = ['POST'])
def transferEther():

@app.route('/contract/withdraw', methods = ['POST'])
def withdraw():

@app.route('/contract/ackRepair', methods = ['POST'])
def ackRepair():

@app.route('/contract/balance', methods = ['POST'])
def getContractBalance():
