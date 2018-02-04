var contractData;
var MU = {
    url : 'http://localhost:5000',
    pubk : '0x6D60c2e9ee6EcA2C29848b796dD10DCfAC63dC49'
};

var providers = [{
    'url' : 'http://localhost:5001',
    'pubk' : '0x252b7F9E6104E6EcC332e38954c33CFDa2Af6E54'
},{
    'url' : 'http://localhost:5002',
    'pubk' : '0xFd7B465f9Cc0E5fB919599F6CC84f5676Ee4a909'
}];

class Demo{

    constructor(){
        
        
    }

    // MU will forward the info to the provider
    sendContractInfoToMU(machineID, providerIndex, valid){
        var data = {
            'providerAddr': providers[providerIndex].pubk,
            'providerUrl' : providers[providerIndex].url,
            'value': 1000,
            'machineID' : machineID
        }


        $.ajax({
            url : MU.url + '/contract/new',
            type: 'POST',
            data : JSON.stringify(data),
            contentType: 'application/json',
            success : function(response){
                contractData = response;
                $('#muAddr').html($('#muAddr').html() + MU.pubk);
                $('#providerAddr').html($('#providerAddr').html() + providers[0].pubk);
                $('#contractAddr').html($('#contractAddr').html() + contractData['contractAddr']);
                $('#amount').html($('#amount').html() + '1000.00');
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
            url: providers[providerIndex].url + '/contract/validate',
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
            url : MU.url + '/contract/ackRepair',
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
            url = MU.url;
        }else if(name == 'provider0'){
            url = providers[0].url;

        }else{
            url = providers[1].url;
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