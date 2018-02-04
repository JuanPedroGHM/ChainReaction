from wallet import Wallet
from web3 import Web3

import requests
import time

class MUContractWallet(Wallet):

    def createContract(self, providerAddr, euros):

        contractFilePath = "../contracts/chainReaction1_0.sol"
        contractName = "ChainReaction"
        ether = euros / self.getCurrentEtherPrice()
        contractAddr, contractAbi = self.deployContract(contractFilePath, contractName, ether, providerAddr)
        currentContract =  self.getContract(contractAddr, contractAbi)

        self.openContracts[contractAddr] = {
            'provider' : providerAddr,
            'contractAddress' : contractAddr,
            'euros' :  euros,
            'instance': currentContract
        }

        # eventFilter = currentContract.eventFilter('ProviderResponse')

        # self.eventWatcher(eventFilter, threading.Event())
        # print('Waiting for ack')
        return contractAddr, contractAbi

    def sendProviderAddr(self, contractAddr, providerAddr):
        self.openContracts[contractAddr].setProviderAddr(providerAddr)

    def sendEurosToContract(self, contractAddr , euros):
        ether = euros / self.getCurrentEtherPrice()
        self.sendEtherToContract(contractAddr, ether)

    def sendEtherToContract(self, contractAddr , ether):
        self.openContracts[contractAddr].transact({'from' : self.publicKey, 'value' : self.w3.toWei(ether, 'ether')
        }).sendMoney()

    def ackRepair(self, contractAddr):
        self.openContracts[contractAddr]['instance'].transact({'from' : self.publicKey}).acknowledgeRepair()
    
    def withdraw(self, contractAddr):
        self.openContracts[contractAddr]['instance'].transact({'from' : self.publicKey}).withdraw()

        self.closedContracts[contractAddr] = self.openContracts[contractAddr]
        del self.openContracts[contractAddr]

    def getContractBalance(self, contractAddr):
        return self.openContracts[contractAddr].getBalance()

    # def eventWatcher(self, eventFilter, stop):
    #     events = eventFilter.get_new_entries()
    #     print(events)
    #     if len(events) > 0:
    #         stop.set()

    #     if not stop.is_set():
    #         threading.Timer(10, self.eventWatcher, [eventFilter, stop]).start()

if __name__ == '__main__':
    myWallet = MUContractWallet('http://127.0.0.1:8545', 'muKeys.txt', 0)
    print(myWallet.getBalance())


    contractAddr, contractAbi = myWallet.createContract(myWallet.w3.eth.accounts[1], 1000)

    requests.post("http://127.0.0.1:5001/contract/new", json = {
        "contractAddr" : contractAddr,
        'muAddr' : myWallet.publicKey,
        'contractAbi' : contractAbi,
        'value' : 1000,
        'valid' : True
    })

    print(myWallet.getBalance())

    time.sleep(10)

    myWallet.ackRepair(contractAddr)
    requests.post("http://127.0.0.1:5001/contract/finished", json = {
        "contractAddr" : contractAddr
        })

    myWallet.withdraw(contractAddr)
    print(myWallet.getBalance())

