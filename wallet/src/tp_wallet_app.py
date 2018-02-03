from tpWallet import PRWallet

from flask import Flask, jsonify, request

app = Flask(__name__)

myWallet = PRWallet('http://127.0.0.1:8545', 'tpKeys.txt', 1)

@app.route('/contract/new', methods=['POST'])
def newContract():

    values = request.get_json() 
    # print('New Contract with data : {}'.format(values))

    contractAddr = values["contractAddr"]
    contractAbi = values["contractAbi"]
    muAddr = values['muAddr']
    value = values['value']
    valid = values["valid"]

    myWallet.newContract(contractAddr, contractAbi, muAddr, value, valid)
    
    return jsonify({'Contract recieved' : valid}), 200

@app.route('/contract/finished', methods = ['POST'])
def finishContract():
    values = request.get_json()

    contractAddr = values['contractAddr']

    myWallet.withdraw(contractAddr)
    print(myWallet.getBalance())
    
    return jsonify({'Contract finished' : True}), 200

if __name__ == '__main__':
    print(myWallet.getBalance())
    app.run('127.0.0.1', 5001)
