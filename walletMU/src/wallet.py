from web3 import HTTPProvider, Web3
from web3.contract import ConciseContract

from ethereum import utils

import os

import pdb

class Wallet:

    def __init__(self, url, filename):
        self.w3 = self.connectToBlockchain(url)
        
        self.importAccount(filename)
        if self.publicKey == '':
            self.createAccount()
            self.saveAccount(filename)


        print('Public Key : {}'.format(self.publicKey))


    def connectToBlockchain(self, url):

        http_provider = HTTPProvider(url)
        return Web3(http_provider)


    def createAccount(self):
        self.privateKey = utils.sha3(os.urandom(4096))
        raw_address = utils.privtoaddr(self.privateKey)
        self.publicKey = utils.checksum_encode(raw_address)

    def saveAccount(self, filename):
        file = open(filename, 'w')
        file.write('{}\n{}\n'.format(self.privateKey, self.publicKey))
        file.close()


    def importAccount(self, filename):
        try:
            with open(filename) as file:
                self.privateKey = file.readline().strip()
                self.publicKey = file.readline().strip()
        except IOError:
            self.publicKey = 0

    
    def getBalance(self):
        return self.w3.fromWei(self.w3.eth.getBalance(self.publicKey), 'ether')


    def deployContract(self, filename, contractName, addrProvider):
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
            transaction = {'from' : self.publicKey},
            args= [addrProvider]
        )

        transaction_receipt = self.w3.eth.getTransactionReceipt(transaction_hash)
        contract_address = transaction_receipt['contractAddress']
        return contract_address, contract_abi


    def getContract(self, contractAbi, contractAddr):
        return self.w3.eth.contract(
            abi=contractAbi,
            address=contractAddr,
            ContractFactoryClass=ConciseContract,
        )


if __name__ == '__main__':
    myWallet = Wallet('http://127.0.0.1:7545', 'keys.txt')
    print(myWallet.getBalance())

    myWallet.w3.eth.sendTransaction({
        'from' : '0x627306090abaB3A6e1400e9345bC60c78a8BEf57',
        'to' : myWallet.publicKey,
        'value' : myWallet.w3.toWei(5, 'ether')
    })

    print(myWallet.getBalance())