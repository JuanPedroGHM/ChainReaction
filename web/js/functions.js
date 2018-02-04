$(document).ready(function(){

	function setContractState(created, paid, rejected, accepted, repaired, finished){
		if(!created){
			$('.bulb').each(function(element){
				$(element).css("background-color", "gray")
			})
		}else{
			$('#P').css("background-color", (paid) ? "green" : "red")
			$('#A').css("background-color", (accepted) ? "green" : "red")
			$('#R').css("background-color", (rejected) ? "green" : "red")
			$('#AR').css("background-color", (repaired) ? "green" : "red")
			$('#F').css("background-color", (finished) ? "green" : "red")
		}
		
	}

	var currentMsgId = '';

	function changeConsoleMsg(msgId){
		if(currentMsgId != ''){
			$(currentMsgId).css('visibility', "hidden");
		}
		if(msgId != '') $(msgId).css("visibility","visible")
		currentMsgId = msgId;
	}

	function reset(){
		changeConsoleMsg('');
		// setContractState(false, false, false, false, false, false);
		$(".Contract1").css('visibility', "hidden");
		$(".Contract2").css('visibility', "hidden");
		$("#muWithdraw").css('visibility', "hidden");
	}

	$("#muWithdraw").on('click', function(event){
		demo.withdraw('mu')
		changeConsoleMsg('msg6')
		setContractState(true, false, false,false, false, true)

		var pos1 = $('#lights').offset();
		var alert = $('.sprite')
		alert.css({'top' : pos1.top, 'left' : pos1.left})
		var pos2 = $('#cout').offset();
		$("#alert").attr("src","./images/ether.png");
		$('#muAddr').html('MU : ');
		$('#providerAddr').html('Provider : ');
		$('#contractAddr').html('Contract : ');
		$('#amount').html('Euros : ');
		alert.animate({
			left:pos2.left,
			top:pos2.top},
			3000, function(event){
				alert.css('visibility', "hidden");
				$('#muWithdraw').css('visibility', 'hidden');
			}
		);
	})

	setContractState(false, false, false, false, false, false);

	var demo = new Demo();

	/*send notification from A to B*/
	/*MachineA to cout*/
	$(".MUButton").click(function(event){

		var pos1=$(event.target).offset();
		var pos2=$("#cout").offset();
		var alert=$(".sprite")
		$('#alert').attr('src', './images/notification.png')
		alert.css({'top' : pos1.top, 'left' : pos1.left});
		alert.css("visibility","visible");
		alert.animate({
			left:pos2.left,
			top:pos2.top},
			3000
		);

		setTimeout(function() {
			
			changeConsoleMsg("#msg1")
  			setTimeout(function() {
				changeConsoleMsg("#msg2")

				setContractState(true, true, false, false, false, false);
				demo.sendContractInfoToMU(event.target.id,0,true);

				pos2=$("#P1").offset();
				$("#alert").attr("src","./images/smart-contract.svg");
				alert.animate({
					left:pos2.left,
					top:pos2.top},
					3000
				);
				setTimeout(function() {
					$("#notif1").css("visibility","visible");
					$(".Contract1").css("visibility","visible");
				}, 3500);
			}, 2000);
		}, 3000);
	});
	$(".Contract1").click(function(event){
		pos2=$("#cout").offset();
		$(".sprite").animate({
					left:pos2.left,
					top:pos2.top},
					3000
		);
		$('.Contract1').css('visibility', 'hidden');
		if (event.target.id == "Acc1"){
			setContractState(true, true, false, true, false, false);
			demo.answerContractRequest(true,0);
			$("#alert").attr("src","./images/tick.svg");
			changeConsoleMsg("#msg52")
			setTimeout(function() {
				changeConsoleMsg("#msg511")
				setTimeout(function() {
					changeConsoleMsg("#msg512")
					demo.acknowledgeRepair()
					setContractState(true, true, false, true, true, false);
					$('#notif1').css('background-color', 'green');
					// $('#notif1').css('round-color', 'green');
					$('#notif1').html('Withdraw');
					$('#notif1').click(function(event){
						console.log('Withdrawing provider 1 funds')
						demo.withdraw("provider0")

						$('#muAddr').html('MU : ');
						$('#providerAddr').html('Provider : ');
						$('#contractAddr').html('Contract : ');
						$('#amount').html('Euros : ');
						changeConsoleMsg('msg6')

						setContractState(true, false, false,false, false, true)
						var pos1 = $('#lights').offset();
						var alert = $('.sprite');
						alert.css({'top' : pos1.top, 'left' : pos1.left})
						var pos2 = $('#P1').offset();
						$("#alert").attr("src","./images/ether.png");
						alert.animate({
							left:pos2.left,
							top:pos2.top},
							3000,function(event){
								alert.css('visibility', "hidden")
							}
						);

						$('#notif1').css('background-color', 'rgba(0,0,0,0)');
						$('#notif1').html('New Contract Offer!');
						$('#notif1').css('visibility', 'hidden');
					});
				}, 5000);
			}, 2000);
		}
		else{

			setContractState(true, true, true, false, false, false);
			demo.answerContractRequest(false,0)
			$("#alert").attr("src","./images/cross.svg");
			changeConsoleMsg("#msg51")	
			$("#muWithdraw").css('visibility', 'visible');
			var pos1 = $('#lights').offset();
			alert.css({'top' : pos1.top, 'left' : pos1.left})
			var pos2 = $('#cout').offset();
			$("#alert").attr("src","./images/smart-contract.svg");
			alert.animate({
				left:pos2.left,
				top:pos2.top},
				3000
			);
		}
	})
});

