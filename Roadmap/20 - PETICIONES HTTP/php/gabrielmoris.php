<?php
/*
 * EXERCISE:
 * Using an HTTP request mechanism in your language, make
 * a request to the website of your choice, verify that the request
 * was successful, and display the website content in the console.
 */

// $url = 'https://ai-coverletters.vercel.app/en';
// // simplest way to get contents: Only works with GET requests and it is not safe (Requires allow_url_fopen enabled)
// try {
//     $context = stream_context_create(['https' => ['method' => 'GET']]);
//     $content = file_get_contents('https://ai-coverletters.vercel.app/en/', false, $context);
//     // echo $content . "\n";
// } catch (Exception $e) {
//     echo "Error: $e";
// }

// cURL Is a library for making http requests in PHP
// try {
//     $ch = curl_init("https://ai-coverletters.vercel.app/en");
//     curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
//     $content = curl_exec($ch);
//     // echo $content . "\n";
//     curl_close($ch);
// } catch (Exception $e) {
//     echo "Error: $e";
// }


/*
 * EXTRA DIFFICULTY (optional):
 * Using the PokéAPI (https://pokeapi.co), create a terminal program
 * where you can request information about a specific Pokémon
 * using its name or number.
 * - Display the name, id, weight, height, and type(s) of the Pokémon
 * - Display the name of its evolution chain
 * - Display the games it appears in
 * - Handle potential errors
 */

function pokemon()
{
    echo "
    ===== Welcome to the Pokemon Database =====
     1.- Check Pokemon Data
     2.- Check which games show the Pokemon 
     3.- Check Pokemon Evolutions
     4.- Exit
    ============================================
     \n";

    while (true) {
        $selection = readline("Select an option\n");
        switch ($selection) {
            case 1:
                $pokemon =  readline("Pokemon Name or Number: \n");
                $info = apiCall($pokemon, "pokemon");
                if (!json_decode($info, true) || !$info) {
                    echo "Invalid JSON string or API not working";
                    break;
                }
                $jsonObject = json_decode($info, true);

                $name = $jsonObject['species']['name'];
                $height = $jsonObject['height'];
                $weight = $jsonObject['weight'];
                $id = $jsonObject['id'];

                $types = array_map(function ($type) {
                    return $type['type']['name'];
                }, $jsonObject['types']);

                echo "ID: $id\nName: $name\nHeight: $height m\nWeight: $weight Kg\nTypes: " . implode(', ', $types)  . "\n";
                break;
            case 2:
                $pokemon = readline("Pokemon Name or Number \n");
                $info = apiCall($pokemon, "generation");
                if (!json_decode($info, true) || !$info) {
                    echo "Invalid JSON string or API not working";
                    break;
                }
                $jsonObject = json_decode($info, true);

                $games = array_map(function ($version) {
                    return $version['name'];
                },  $jsonObject['version_groups']);

                echo "Games:" . implode(', ', $games)  . "\n";
                break;
            case 3:
                $pokemon =  readline("Pokemon Name or Number: \n");
                $info = apiCall($pokemon, "evolution-chain");
                if (!json_decode($info, true) || !$info) {
                    echo "Invalid JSON string or API not working";
                    break;
                }
                $jsonObject = json_decode($info, true);


                $evolutionChain = $jsonObject['chain'];
                getEvolutions($evolutionChain);
                break;
            case 4:
                echo "\033c";
                echo "Good bye 👋 \n";
                exit;
            default:
                echo "This option doesn't exist.\n";
        }
    }
}

function apiCall($pokemon, $information)
{
    try {
        $ch = curl_init("https://pokeapi.co/api/v2/$information/$pokemon");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $content = curl_exec($ch);
        return $content;
        curl_close($ch);
    } catch (Exception $e) {
        echo "Error: $e";
    }
}

function getEvolutions($data)
{
    if (!empty($data['evolves_to'])) {
        $evolution = $data['evolves_to'][0]['species']['name'];
        echo "Evolves to: $evolution\n";
        getEvolutions($data['evolves_to'][0]);
    }
}

pokemon();
