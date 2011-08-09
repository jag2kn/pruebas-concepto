<?php
if (isset($_POST["cargar"])){
	$d=rand(0,1000);
	file_put_contents("dato.dat", $d);
	echo "registrado [".$d."]";
}else{
	?>

	<html>
	<head>
	  <script src="http://code.jquery.com/jquery-latest.js"></script>


	<script>

	function cargar (){
		$.ajax({
			type: "POST",
			url: "senal.php",
			data: "cargar=true",
			success: function(msg){
				$("#resultado").html(msg);
			}
		});
	}
	$(document).ready(function(){
		$("#boton").click(function () { 
			cargar();
		});
	});
	</script>

	</head>
	<body>
	<button id="boton">Generar</button><hr/>
	<div id="resultado"></div>

	</body>
	</head>
	<?php
}
?>
