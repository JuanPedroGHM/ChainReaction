

class Demo{

    constructor(){
        
        this.MU = {
            url : 'http://localhost:5000',
            pubk : '0xa7eb704d22d02302be513804cf01f17f65bda653'
        };

        this.providers = [{
            'url' : 'http://localhost:5001',
            'pubk' : '0x9ab4361184baf905ea5134d2ff31f2d48aba1916'
        },{
            'url' : 'http://localhost:5002',
            'pubk' : '0x6df43ceccffebcdcaefdaea5f73430949f0638bd'
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