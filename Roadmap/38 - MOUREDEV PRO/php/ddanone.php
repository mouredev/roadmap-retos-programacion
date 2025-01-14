<?php
// Cargar el csv en un array
$file  		= file( dirname(__FILE__)."/fichero.csv", FILE_IGNORE_NEW_LINES|FILE_SKIP_EMPTY_LINES);

// Nos quedamos sólo con los activos
$file  		= array_filter($file, function($k) { return explode(',',$k)[2] == 'activo'; });

// Seleccionamos 3 registros al azar
$winners 	= array_rand($file, 3);

// Los imprimimos
foreach($winners as $k=>$v){ echo sprintf("Winner %d: %s (%d) <br>", $k+1, explode(',',$file[$v])[1], explode(',',$file[$v])[0]); }

// 4 líneas de código !! ;)
