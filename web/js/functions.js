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
	/*$("#MachineA").click(function(){*/
	$(".MUButton").click(function(event){
		var pos1=$(event.target).offset();
		var pos2=$("#cout").offset();
		var alert=$(".sprite")
		alert.css({'top' : pos1.top, 'left' : pos1.left});
		alert.css({'visibility':'visible'});
		alert.animate({
			left:pos2.left,
			top:pos2.top},
			3000
		);

		print()
		demo.sendContractInfoToMU(event.target.id,0,true);
	});

	$(".MUButton").click(function(event){

		console.log(event.target)
		var pos1=$(event.target).offset();
		var pos2=$("#cout").offset();
		console.log(pos1)
		var alert=$(".sprite")
		alert.css({'top' : pos1.top, 'left' : pos1.left});
		alert.css({'visibility':'visible'});
		alert.animate({
			left:pos2.left,
			top:pos2.top},
			3000
		);
	});
});

