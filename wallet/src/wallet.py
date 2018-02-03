from web3 import HTTPProvider, Web3

from ethereum import utils

from solc import compile_source

import requests

import os

import pdb

class Wallet:

    def __init__(self, url, filename, index):
        self.w3 = self.connectToBlockchain(url)

        self.openContracts = {}
        self.closedContracts = {}
        self.createAccount(index)

        print('Public Key : {}'.format(self.publicKey))

    def connectToBlockchain(self, url):
        http_provider = HTTPProvider(url)
        return Web3(http_provider)


    def createAccount(self, index):
        self.publicKey = self.w3.eth.accounts[index]
    
    def getBalance(self):
        return self.w3.fromWei(self.w3.eth.getBalance(self.publicKey), 'ether')

    def sendTransactionInEther(self, addr, ether):
        sendTransaction(addr, ether)

    def sendTransactionInEuros(self, addr, euros):
        ether = euros / self.getCurrentEtherPrice()
        sendTransaction(addr, ether)

    def sendTransaction(self, addr, ether):
        w3.eth.sendTransaction({
            'from' : self.publicKey,
            'to' : addr,
            'value' : self.w3.toWei(ether, 'ether')
        })

    def deployContract(self, filename, contractName, ether, providerAddr):
        with open(filename) as file:
            source_code = file.readlines()

        compiled_code = compile_source(''.join(source_code))

        contract_bytecode = compiled_code[f'<stdin>:{contractName}']['bin']
        contract_abi = compiled_code[f'<stdin>:{contractName}']['abi']

        contract_factory = self.w3.eth.contract(
            abi=contract_abi,
            bytecode=contract_bytecode,
        )

        transaction_hash = contract_factory.deploy(
            transaction = {'from' : self.publicKey, 'value' : self.w3.toWei(ether, 'ether')},
            args = [providerAddr]
            )

        transaction_receipt = self.w3.eth.getTransactionReceipt(transaction_hash)
        contract_address = transaction_receipt['contractAddress']
        return contract_address, contract_abi


    def getContract(self, contractAddr, contractAbi):
        return self.w3.eth.contract(contractAddr, abi=contractAbi)

    def getCurrentEtherPrice(self):
        jsonData = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=EUR").json()
        return jsonData['EUR']