$(document).ready(function(){

	var demo = new Demo();

	$(".bulb").click(function(){
		id=$(this).attr("id");
		id_str="#"+(id);
		$(id_str).css("background-color", "red");
	});
	/* same but for state = True */
	$(".bulb").click(function(){
		id=$(this).attr("id");
		id_str="#"+(id);
		$(id_str).css("background-color", "green");
	});
	/*send notification from A to B*/
	/*MachineA to cout*/
	$("#MachineA").click(function(event){
		var pos1=$(event.target).offset();
		var pos2=$("#cout").offset();
		var alert=$(".sprite")
		alert.css({'top' : pos1.top, 'left' : pos1.left});
		alert.css("visibility","visible");
		alert.animate({
			left:pos2.left,
			top:pos2.top},
			3000
		);

		setTimeout(function() {
  			$("#msg1").css("visibility","visible")
  			setTimeout(function() {
				$("#msg2").css("visibility","visible");
				demo.sendContractInfoToMU(event.target.id,0,true);

				pos2=$("#P1").offset();
				$("#alert").attr("src","./images/smart-contract.svg");
				alert.animate({
					left:pos2.left,
					top:pos2.top},
					3000
				);
				setTimeout(function() {
					$("#notif1").css("visibility","visible")
					$(".Contract1").css("visibility","visible")
				}, 3500);
			}, 2000);
		}, 3000);
	});
	$(".Contract1").click(function(event){
		if (event.target.id == "Acc1"){
			
		}
		else{

		}

	})


	$("#MachineB").click(function(event){
		var pos1=$(event.target).offset();
		var pos2=$("#cout").offset();
		var alert=$(".sprite")
		alert.css({'top' : pos1.top, 'left' : pos1.left});
		alert.css("visibility","visible");
		alert.animate({
			left:pos2.left,
			top:pos2.top},
			3000
		);
		demo.sendContractInfoToMU(event.target.id,0,false);
	});

	$("#MachineC").click(function(event){
		var pos1=$(event.target).offset();
		var pos2=$("#cout").offset();
		var alert=$(".sprite")
		alert.css({'top' : pos1.top, 'left' : pos1.left});
		alert.css("visibility","visible");
		alert.animate({
			left:pos2.left,
			top:pos2.top},
			3000
		);
		demo.sendContractInfoToMU(event.target.id,0,true);
	});
});

