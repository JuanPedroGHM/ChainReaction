# Blockchain Hackathon Stuttgart (1/2018)

## How to use this project

## Requirements

Have Ganache2 installed and running
##### Install further requirements

    pip install flask py-solc "web3" ethereum

# Import dependencies


#### Run it

Run a python shell and import the wallet:

    from src import wallet

#### Create a new local wallet

    mywallet = wallet
    mywallet = wallet.Wallet('http://127.0.0.1:7545', 'keys.txt')
    mywallet.getBalance()
    
#### Go to Ganache2 and get a adress
    

    mywallet.w3.eth.sendTransaction({'from': '0xf17f52151EbEF6C7334FAD080c5704D77216b732' 'value': mywallet.w3.toWei(5, 'ether'), 'to': mywallet.publicKey})
    mywallet.getBalance()