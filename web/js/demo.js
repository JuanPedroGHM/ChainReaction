var contractData;

class Demo{

    constructor(){
        
        this.MU = {
            url : 'http://localhost:5000',
            pubk : '0xcCd25d5aC5d960B257Ea80b3740361C54b75f956'
        };

        this.providers = [{
            'url' : 'http://localhost:5001',
            'pubk' : '0x49c38B6bcb4f0bA108Dabe254Fd8c196998cB30a'
        },{
            'url' : 'http://localhost:5002',
            'pubk' : '0xFd7B465f9Cc0E5fB919599F6CC84f5676Ee4a909'
        }];
    }

    // MU will forward the info to the provider
    sendContractInfoToMU(machineID, providerIndex, valid){
        var data = {
            'providerAddr': this.providers[providerIndex].pubk,
            'providerUrl' : this.providers[providerIndex].url,
            'value': 1000,
            'machineID' : machineID
        }

        $.ajax({
            url : this.MU.url + '/contract/new',
            type: 'POST',
            data : JSON.stringify(data),
            contentType: 'application/json',
            success : function(data){
                contractData = data;
            }
        });
    }

    answerContractRequest(accept, providerIndex){

        var data = {
            'contractAddr' : contractData['contractAddr'],
            'valid' : accept
        }
        console.log(data);
        $.ajax({
            url: this.providers[providerIndex].url + '/contract/validate',
            type : 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success : function(data){
                contractData.accepted = data['accepted']
            }
        })
    }

    acknowledgeRepair(){

        var data = {
            'contractAddr' : contractData.contractAddr
        };

        $.ajax({
            url : this.MU.url + '/contract/ackRepair',
            type: 'POST',
            data : JSON.stringify(data),
            contentType: 'application/json',
            async: false,
            success : function(data){
                console.log(data);
            }
        });
    }

    withdraw(name){
        var url;
        if (name  == 'mu'){
            url = this.MU.url;
        }else if(name == 'provider0'){
            url = this.providers[0].url;

        }else{
            url = this.providers[1].url;
        }

        var data = {
            'contractAddr' : contractData.contractAddr,
        }
        $.ajax({
            url: url + '/contract/finished',
            type : 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success : function(data){
                console.log(data);
            }
        }) 
    }

    getBalance(walletUrl) {
        $.ajax({
            url : walletUrl + '/wallet/balance',
            type: 'GET',
            success : function(data){
                console.log(data);
            }
        });
    }
}