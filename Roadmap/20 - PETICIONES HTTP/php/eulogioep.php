<?php

/**
 * Ejercicio de peticiones HTTP en PHP
 * 
 * Teoría sobre peticiones HTTP en PHP:
 * PHP ofrece varias formas de realizar peticiones HTTP:
 * 1. cURL - Una biblioteca potente para transferir datos con varios protocolos
 * 2. file_get_contents() - Función simple para peticiones GET (requiere allow_url_fopen)
 * 3. Bibliotecas de terceros como Guzzle
 * 
 * En este ejemplo usamos cURL por su flexibilidad y robustez.
 * 
 * Conceptos clave:
 * - cURL: Cliente URL library, permite hacer peticiones HTTP
 * - JSON: Formato de intercambio de datos, decodificado con json_decode()
 * - CLI: Command Line Interface, interfaz por línea de comandos
 */

/**
 * Realiza una petición HTTP GET
 * 
 * @param string $url La URL a la que realizar la petición
 * @return string El contenido de la respuesta
 * @throws Exception Si hay un error en la petición
 */
function realizarPeticionHttp($url)
{
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    if ($httpCode !== 200) {
        $error = curl_error($ch);
        curl_close($ch);
        throw new Exception("Error en la petición HTTP (código $httpCode): $error");
    }

    curl_close($ch);
    return $response;
}

/**
 * Muestra la cadena de evolución de forma recursiva
 * 
 * @param object $chain Objeto JSON con la información de evolución
 * @param int $nivel Nivel de indentación para la visualización
 */
function mostrarCadenaEvolucion($chain, $nivel = 0)
{
    $indentacion = str_repeat("  ", $nivel);
    echo "{$indentacion}- " . $chain->species->name . PHP_EOL;

    if (!empty($chain->evolves_to)) {
        foreach ($chain->evolves_to as $evolucion) {
            mostrarCadenaEvolucion($evolucion, $nivel + 1);
        }
    }
}

// Ejemplo básico de petición HTTP
echo "=== Ejemplo básico de petición HTTP ===" . PHP_EOL;
try {
    $contenido = realizarPeticionHttp('https://www.example.com');
    echo "Petición exitosa a example.com" . PHP_EOL;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}

// Programa principal para buscar información de Pokémon
while (true) {
    echo PHP_EOL . "=== Búsqueda de Pokémon ===" . PHP_EOL;
    echo "Ingrese el nombre o número del Pokémon (o 'salir' para terminar): ";
    $entrada = trim(strtolower(fgets(STDIN)));

    if ($entrada === 'salir') {
        break;
    }

    try {
        // Obtener datos básicos del Pokémon
        $pokemonJson = realizarPeticionHttp("https://pokeapi.co/api/v2/pokemon/{$entrada}");
        $pokemon = json_decode($pokemonJson);

        echo PHP_EOL . "Información del Pokémon:" . PHP_EOL;
        echo "Nombre: " . $pokemon->name . PHP_EOL;
        echo "ID: " . $pokemon->id . PHP_EOL;
        echo "Peso: " . ($pokemon->weight / 10) . " kg" . PHP_EOL;
        echo "Altura: " . ($pokemon->height / 10) . " m" . PHP_EOL;

        // Mostrar tipos
        echo "Tipos:" . PHP_EOL;
        foreach ($pokemon->types as $tipo) {
            echo "- " . $tipo->type->name . PHP_EOL;
        }

        // Obtener y mostrar cadena de evolución
        $especieJson = realizarPeticionHttp($pokemon->species->url);
        $especie = json_decode($especieJson);

        $evolucionJson = realizarPeticionHttp($especie->evolution_chain->url);
        $evolucion = json_decode($evolucionJson);

        echo PHP_EOL . "Cadena de evolución:" . PHP_EOL;
        mostrarCadenaEvolucion($evolucion->chain);

        // Mostrar juegos
        echo PHP_EOL . "Juegos en los que aparece:" . PHP_EOL;
        foreach ($pokemon->game_indices as $juego) {
            echo "- " . $juego->version->name . PHP_EOL;
        }
    } catch (Exception $e) {
        echo "Error: No se pudo encontrar el Pokémon. Asegúrese de escribir el nombre o número correctamente." . PHP_EOL;
    }
}

echo "¡Gracias por usar el buscador de Pokémon!" . PHP_EOL;
