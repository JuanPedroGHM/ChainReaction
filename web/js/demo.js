

class Demo{

    constructor(){
        
        this.MU = {
            url : 'http://localhost:5000',
            pubk : '0x689cce8D28D200F548f6D85F4250b02b90AD4531'
        };

        this.providers = [{
            'url' : 'http://localhost:5001',
            'pubk' : '0x67BA6Bbe1210bdDD457F8f27027737390Dda3821'
        }];
    }

    // MU will forward the info to the provider
    sendContactInfoToMU(machineID, providerIndex, valid){
        var data = {
            'providerAddr': this.providers[providerIndex].pubk,
            'providerUrl' : this.providers[providerIndex].url,
            'value': 1000,
            'machineID' : machineID
        }
        
        this.contractData;

        $.ajax({
            url : this.MU.url + '/contract/new',
            type: 'POST',
            data : JSON.stringify(data),
            contentType: 'application/json',
            success : function(data){
                this.contractData = data;
            }.bind(this)
        });
    }

    answerContractRequest(accept, providerIndex){

        data = {
            'contractAddr' : this.contractData.contractAddr,
            'accept' : accept
        }
        $.ajax({
            url: this.providers[providerIndex].url + '/contract/validate',
            type : 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success : function(data){
                this.contractData.accepted = data['accepted']
            }.bind(this)
        })
    }

    acknowledgeRepair(){

        var data = {
            'contractAddr' : this.contractData.contractAddr
        };

        if( this.contractData){
            $.ajax({
                url : this.MU.url + '/contract/ackRepair',
                type: 'POST',
                data : JSON.stringify(data),
                contentType: 'application/json',
                async: false,
                success : function(data){
                    console.log(data);
                }.bind(this)
            });
        }
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

        data = {
            'contractAddr' : this.contractData.contractAddr,
        }
        $.ajax({
            url: url + '/contract/finished',
            type : 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success : function(data){
                console.log(data);
            }.bind(this)
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