<html>
<head>
  <script src="http://code.jquery.com/jquery-latest.js"></script>


<script>
var time=0;

function cargar (){
	$.ajax({
		type: "POST",
		url: "servidor.php",
		success: function(msg){
			if (msg!=""){
				$("#resultado").html(msg);
			}else{
				$("#resultado").html($("#resultado").html()+".");
			}
			setTimeout("cargar()", 100);
		}
	});
}
$(document).ready(function(){
	$("#boton").click(function () {
		$("#resultado").html("Cargando");
		cargar();
	});
});
</script>

</head>
<body>
<button id="boton">Boton</button><hr/>

<div id="resultado"></div>

</body>
</head>

