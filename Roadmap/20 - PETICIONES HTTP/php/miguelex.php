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

function getPokemonData($pokemon) {
    $data = file_get_contents("https://pokeapi.co/api/v2/pokemon/$pokemon");
    $data = json_decode($data);

    echo "Nombre: " . $data->name . "\n";
    echo "ID: " . $data->id . "\n";
    echo "Peso: " . $data->weight . "\n";
    echo "Altura: " . $data->height . "\n";
    echo "Tipos: ";
    foreach ($data->types as $type) {
        echo $type->type->name . " ";
    }
    echo "\n";

    $speciesData = file_get_contents($data->species->url);
    $speciesData = json_decode($speciesData);

    echo "Cadena de evolución: " . $speciesData->evolution_chain->url . "\n";

    echo "Juegos: ";
    foreach ($data->game_indices as $game) {
        echo $game->version->name . " ";
    }
    echo "\n";
}

try {
    while (true) {
        echo "Introduce el nombre o número del Pokémon (o 'salir' para terminar): ";
        $pokemon = trim(fgets(STDIN));
        if ($pokemon == 'salir') {
            break;
        }
        getPokemonData($pokemon);
    }
} catch (Exception $e) {
    echo "Ha ocurrido un error: " . $e->getMessage();
}
?>

