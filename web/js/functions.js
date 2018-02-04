$(document).ready(function(){
	$("#MachineA").click(function(){

	});
	/* if one object of class="bulb" 
	changes state (signalised here 
	as being clicked, it's color x 
	changes to red given it's id
	if state==False*/
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
	$(".bulb").click(function(){
		var pos1=$("#MachineA").offSet();
		var pos2=$("#P1").offSet();
		alert(pos1)
		/*x=pos2.right - pos1.right;
		y=pos2.top - pos1.top;
		$("sprite").prepend('<img id="alert" src="/images/notification.png" style="height:20px" />');
		var alert=$("#alert");
		alert.css("position",pos1.toString());
		alert.fadeIn();
		alert.animate({
			backgroundPositionX:x;
			backgroundPositionY:y;
			speed:slow;
		});*/
	});
});
