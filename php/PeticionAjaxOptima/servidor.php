<?php
function noCache() {
  header("Expires: Tue, 01 Jul 2001 06:00:00 GMT");
  header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
  header("Cache-Control: no-store, no-cache, must-revalidate");
  header("Cache-Control: post-check=0, pre-check=0", false);
  header("Pragma: no-cache");
}

function file_size($size){
	$filesizename = array(" Bytes", " KB", " MB", " GB", " TB", " PB", " EB", " ZB", " YB");
	return $size ? round($size/pow(1024, ($i = floor(log($size, 1024)))), 2) . $filesizename[$i] : '0 Bytes';
}


$contenido="";
$true=true;
$contador=0;
while($true){
	if(file_exists("dato.dat")){
		$contenido=file_get_contents("dato.dat");
	}
	if (strlen($contenido)>0){
		file_put_contents("dato.dat", "");
		echo $contenido."<br/>".
		"Mem Used	=> ".file_size(memory_get_usage())."/".file_size(memory_get_peak_usage())."<br/>".
		"Max Mem Used	=> ".file_size(memory_get_usage(true))."/".file_size(memory_get_peak_usage(true));
		$true=false;
	}else{
		//echo ",";
		usleep(500000);
		$contador++;
	}
	if ($contador>5){
		$true=false;
	}
}

