pragma solidity ^0.4.18;

contract ChainReaction {
    
    bool payment;
    bool rejected;
    bool accepted;
    bool aRepair;
    bool finish;
    
    address mgmtUnit;
    address trustedProvider;
    
    uint amount4MU;
    uint amount4TP;
    
    //Only TP can call these
    event ProviderResponse(bool accepted);
    //only MU can call this 
    event AckRepair(bool aRepair);
    
    function ChainReaction(address provider) public payable {
        payment = true;
        mgmtUnit = msg.sender;
        require(msg.sender != provider);
        require(msg.value > 0);
        trustedProvider = provider;
        amount4TP = msg.value;
        amount4MU = 0;
    }
    
    function getAMU() public view returns (uint) {
      return amount4MU;
    }
    
    function getATP() public view returns (uint) {
      return amount4TP;
    }    
    
    function() public payable {
        
    }
    
    function getBalance() public view returns (uint) {
      return this.balance;
    }
    
    function acceptContract() public {
        require(trustedProvider == msg.sender);
        accepted = true;
        ProviderResponse(true);
    }
    
    function rejectContract() public {
        require(trustedProvider==msg.sender);
        rejected = true;
        amount4MU = amount4TP;
        amount4TP = 0;
        ProviderResponse(false);
    }
    
    function sendMoney() public payable {
        amount4TP += msg.value;
    }
    
    function acknowledgeRepair() public {
        require(accepted == true);
        require(mgmtUnit == msg.sender);
        aRepair = true;
        AckRepair(aRepair);
    }
    
    modifier canWithdraw() {
        bool allowed = false;
        if ((payment==true&&rejected==true)||(payment==true&&accepted==true&&aRepair==true)){
            allowed = true;
        }
        require(allowed);
        _;
    }
    
    function withdraw() public canWithdraw {
        if(msg.sender == mgmtUnit) {
            uint varo = amount4MU;
            msg.sender.send(varo);
            amount4MU = 0;
        }
        if(msg.sender == trustedProvider) {
            uint pavos = amount4TP;
            msg.sender.send(pavos);
            amount4TP = 0;
        }
    }
}