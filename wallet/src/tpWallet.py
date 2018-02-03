from wallet import Wallet
from web3 import Web3

class PRWallet(Wallet):

    def newContract(self, contractAddr, contractAbi, muAddr, value, valid):

        currentContract = self.getContract(contractAddr, contractAbi)

        self.openContracts[contractAddr] = {
            'muAddr' : muAddr,
            'contractAddress' : contractAddr,
            'euros' :  value,
            'instance': currentContract
        }
        
        if not valid:
            currentContract.call().rejectContract()
            self.closeContract(contractAddr)
        
        else: 
            currentContract.transact({'from' : self.publicKey}).acceptContract()

            money = Web3.toInt(self.getAssignedAmount(contractAddr))
            print('Money : {}'.format(self.w3.fromWei(money, 'ether')))

    def closeContract(self, contractAddr):
        self.closedContracts[contractAddr] = self.openContracts[contractAddr]
        del self.openContracts[contractAddr]
    
    def withdraw(self, contractAddr):
        balance = Web3.toInt(self.getContractBalance(contractAddr))
        print('Balance Contrato : {}'.format(self.w3.fromWei(balance, 'ether')))

        money = Web3.toInt(self.getAssignedAmount(contractAddr))
        print('Money : {}'.format(self.w3.fromWei(money, 'ether')))

        self.openContracts[contractAddr]['instance'].transact({'from' : self.publicKey}).withdraw()
        self.closeContract(contractAddr)

    def getContractBalance(self, contractAddr):
        return self.openContracts[contractAddr]['instance'].call().getBalance()
    
    def getAssignedAmount(self, contractAddr):
        return self.openContracts[contractAddr]['instance'].call().getATP()
    
