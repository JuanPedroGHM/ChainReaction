from tpWallet import PRWallet

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

myWallet = {}


@app.route('/wallet/balance', methods=['GET'])
@cross_origin(supports_credentials=True)
def getBalance():
    response = {
        'balance' : str(myWallet.getBalance())
    }
    return jsonify(response), 200


@app.route('/contract/new', methods=['POST'])
@cross_origin(supports_credentials=True)
def newContract():

    values = request.get_json() 
    print('New Contract with data : {}'.format(values))

    contractAddr = values["contractAddr"]
    contractAbi = values["contractAbi"]
    muAddr = values['muAddr']
    value = values['value']
    # valid = values["valid"]

    myWallet.newContract(contractAddr, contractAbi, muAddr, value)
    
    return jsonify({'Contract recieved' : contractAddr}), 200

@app.route('/contract/validate', methods=['POST'])
@cross_origin(supports_credentials=True)
def validate():
    values = request.get_json()

    myWallet.validateContract(values['contractAddr'], values['valid'])

    response = {
        'accepted' : values['valid'],
    }
    return jsonify(response), 200


@app.route('/contract/finished', methods = ['POST'])
@cross_origin(supports_credentials=True)
def finishContract():
    values = request.get_json()

    contractAddr = values['contractAddr']

    myWallet.withdraw(contractAddr)
    print(myWallet.getBalance())
    
    return jsonify({'Contract finished' : True}), 200

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    parser.add_argument('-i', '--index', default=1, type=int, help='wallet account')
    args = parser.parse_args()
    port = args.port
    index = args.index

    myWallet = PRWallet('http://127.0.0.1:8545', 'tpKeys.txt', index)

    print(myWallet.getBalance())
    app.run('127.0.0.1', port)
