from web3 import HTTPProvider, Web3
from web3.contract import ConciseContract

from ethereum import utils

import requests

import os

import pdb

from wallet import Wallet

from flask import Flask, request, jsonify

class PRWallet(Wallet):

    def saveContract(self, contractAddr, contractAbi):

        currentContract =  self.getContract(contractAddr, contractAbi)
        euros=currentContract.euros
        #MUAdress = currentContract. 

        self.openContracts[contractAddr] = {
            #'MUAdress' : MUAdress
            'contractAddress' : contractAddr,
            'euros' :  euros,
            'instance': currentContract
        }

    def closeContract(self, contractAddr, contractAbi):

        currentContract =  self.getContract(contractAddr, contractAbi)
        euros=currentContract.euros
        #MUAdress = currentContract.

        self.closedContracts[contractAddr] = {
            #'MUAdress' : MUAdress
            'contractAddress' : contractAddr,
            'euros' :  euros,
            'instance': currentContract
        }

    def ackRepair(self, contractAddr):
        self.openContracts[contractAddr].acknowledgeRepair({'from' : self.publicKey})
    
    def withdraw(self, contractAddr):
        self.openContracts[contractAddr].withdraw({'from' : self.publicKey})

        self.closedContracts[contractAddr] = self.openContracts[contractAddr]
        del self.openContracts[contractAddr]

    def getContractBalance(self, contractAddr):
        return self.openContracts[contractAddr].getBalance()

WalletProvider = PRWallet()

min_ether =  100


@app.route('/contract/accept', methods=['POST'])
def check_if_valid(automatic = True, contractAddr):

    if automatic :

        WalletProvider.getContractBalance(contractAddr)

    else:

        values = request.get_json()

        return values["Accept Contract"]

@app.route('/contract', methods=['POST', 'GET'])
def newContract():
    values = request.get_json() 

    contractAddr = values["contractAddr"]
    contractAbi = values["contractAbi"]

    if check_if_valid(contractAddr):

        WalletProvider.saveContract(contractAddr, contractAbi)

        response = {
            'acknowledge': 'True',
        }

    else :

        WalletProvider.closeContract(contractAddr, contractAbi)

        response = {
            'acknowledge': 'False',
        }

    return jsonify(response)

if __name__ == '__main__':
    myWallet = Wallet('http://127.0.0.1:7545', 'keys.txt')
    print(myWallet.getBalance())

    myWallet.w3.eth.sendTransaction({
        'from' : '0x627306090abaB3A6e1400e9345bC60c78a8BEf57',
        'to' : myWallet.publicKey,
        'value' : myWallet.w3.toWei(5, 'ether')
    })

    print(myWallet.getBalance())
