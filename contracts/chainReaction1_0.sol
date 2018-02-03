pragma solidity ^0.4.0;

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
    event ContractRejected;
    event ackContract;
    event MissingFundsEvent(uint money);
    //only MU can call this 
    event ackRepair(bool aRepair);
    
    function ChainReaction(address provider) public payable {
        payment = true;
        mgmtUnit=msg.sender;
        require(msg.sender!=provider);
        require(msg.value>0);
        trustedProvider = provider;
        amount4TP = msg.value;
        amount4MU=0;
    }
    
    function getAMU() public view returns (uint) {
      return amount4MU;
    }
    
    function getATP() public view returns (uint) {
      return amount4TP;
    }    
    
    function() public payable{
        
    }
    
    function getBalance() public view returns (uint) {
      return this.balance;
    }
    
    function acceptContract() public{
        require(trustedProvider==msg.sender);
        accepted = true;
        ackContract();
    }
    
    function rejectContract() public{
        require(trustedProvider==msg.sender);
        rejected = true;
        amount4MU = amount4TP;
        amount4TP = 0;
        ContractRejected();
    }
    
    function sendMoney() public payable {
        amount4TP+=msg.value;
    }
    
    function acknowledgeRepair() public {
        require(accepted == true);
        require(mgmtUnit == msg.sender);
        aRepair = true;
        ackRepair(aRepair);
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
        address requester;
        requester = msg.sender;
        if(requester==mgmtUnit && amount4MU > 0) {
            uint varo = amount4MU;
            msg.sender.transfer(varo);
            amount4MU = 0;
        }
        if(requester==trustedProvider && amount4TP > 0){
            uint pavos = amount4TP;
            msg.sender.transfer(pavos);
            amount4TP = 0;
        }
    }
}