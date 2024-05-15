<?php

$ch = curl_init();

// Configurar la URL a la que se hará la petición
curl_setopt($ch, CURLOPT_URL, "https://retosdeprogramacion.com/");

// Configurar cURL para devolver el resultado en lugar de imprimirlo directamente
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

// Configurar cURL para usar el archivo de certificados descargado
curl_setopt($ch, CURLOPT_CAINFO, 'cacert.pem');

// Ejecutar la petición
$output = curl_exec($ch);

// Verificar si hubo algún error durante la ejecución de la petición
if($output === false) {
    echo "cURL Error: " . curl_error($ch);
} else {
    // Obtener el código de estado HTTP de la respuesta
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Mostrar el código de estado HTTP
    echo "HTTP Status Code: " . $http_code . "\n\n";

    // Mostrar el contenido de la respuesta
    echo $output;
}

// Cerrar la sesión cURL
curl_close($ch);



// EXTRA

echo "\n\n DIFICULTAD EXTRA \n\n";



