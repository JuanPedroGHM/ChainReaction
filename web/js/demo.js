

class Demo{

    constructor(muUrl, p1url, p2url, chainUrl){
        this.muUrl = muUrl;
        this.p1url = p1url;
        // this.p2url = p2url;
        
        // this.w3 = new Web3(new Web3.providers.HttpProvider(chainUrl));

    }

    example1(){
        // 1. Tell mu machine A needs to be repaired

        // breakMachine('A');
        
        // 2. mu creates contract, selects provider 1, sends info
        
        var data = {
            'providerAddr': this.p1url,
            'value': 1000,
            'machineID' : 'A',
        }
        $.ajax({
            url : this.muUrl + '/contract/new',
            type: 'POST',
            data : JSON.stringify(data),
            contentType: 'application/json',
            success : function(data){
                Console.log(data);
            }
        })

        // 3. provider 1 takes contract (done automatic)
        // acceptContract(1);

        // 4. provider 1 repairs machine A
        // 5. machine A informs managment unit
        // repairMachine('A');

        // 6. managment unit ackRepair on contract
        // $.post(this.muUrl + '/contract/ackRepair',
        //         contract, function(data){
        //             Console.log(data);
        //         });

        // // 7. managment unit and provider 1 withdraw funds from contract
        // $.post(this.muUrl + '/contract/widthdraw',
        //         contract, function(data){
        //             Console.log(data);
        //         });

        // $.post(this.p1url + '/contract/widthdraw',
        // contract, function(data){
        //     Console.log(data);
        // });
    }

    example2(){
        // 1. Tell mu machine B needs to be repaired
        
        // 2. mu creates contract, selects provider 1, sends info

        // 3. provider 2 takes contract

        // 4. provider 2 repairs machine B within a time limit, gets rewarded

        // 5. machine B informs managment unit

        // 6. managment unit ackRepair on contract

        // 7. managment unit and provider 2 withdraw funds from contract
    }

    example3(){
        // 1. Tell mu machine C needs to be repaired
        
        // 2. mu creates contract, selects provider 1, sends info

        // 3. provider 1 rejects contract

        // 4. mu send contract 2 provider 2, it takes the contract

        // 4. provider 2 repairs machine C

        // 5. machine C informs managment unit

        // 6. managment unit ackRepair on contract

        // 7. managment unit and provider 1 withdraw funds from contract
    }
}