#!/bin/bash


# * EJERCICIO:
# * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
# * una peticion a la web que tu quieras, verifica que dicha peticion
# * fue exitosa y muestra por consola el contenido de la web.

echo -e "\n\n=======================================EJERCICIO=======================================\n\n"


url="https://github.com/mouredev"

response=$(curl -s -w "%{http_code}" -o response.txt "$url")

if [ "$response" -eq 200 ]; then
    echo -e "\nEl codigo de salida es 200\n"
    cat -n response.txt | head -n25
else
    echo "Error: No se pudo realizar la peticion, codigo de respuesta: $response"
fi


rm response.txt



# * DIFICULTAD EXTRA (opcional):
# * Utilizando la PokeAPI (https://pokeapi.co), crea un programa por
# * terminal al que le puedas solicitar informacion de un Pokemon concreto
# * utilizando su nombre o numero.
# * - Muestra el nombre, id, peso, altura y tipo(s) del Pokemon
# * - Muestra el nombre de su cadena de evoluciones
# * - Muestra los juegos en los que aparece
# * - Controla posibles errores



echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"



read -p "Escribe el identificador o el nombre del pokemon que quieras conocer (hay 1025 pokemon): " pokemon

find_pokemon() {
    local name_or_id=$1
    local url="https://pokeapi.co/api/v2/pokemon/$name_or_id"
    
    response=$(curl -s -w "%{http_code}" -o response.json "$url")
    
    if [ "$response" -eq 200 ]; then
        name=$(jq -r '.name' response.json | tr '[:lower:]' '[:upper:]')
        id=$(jq -r '.id' response.json)
        weight=$(jq -r '.weight' response.json)
        height=$(jq -r '.height' response.json)
        types=$(jq -r '[.types[].type.name] | join(", ")' response.json)
        games=$(jq -r '[.game_indices[].version.name] | join(", ")' response.json)
        
        echo "======================================="
        echo "El pokemon elegido es: $name"
        echo "El id del pokemon $name: es $id"
        echo "El peso del pokemon $name: es $weight"
        echo "La altura del pokemon $name: es $height"
        echo "$name es un pokemon de tipo: $types"
        echo "$name participa en los juegos: $games"
        echo "======================================="
    else
        echo "Error: No se pudo encontrar el pokemon, codigo de respuesta: $response"
    fi
}

find_pokemon "$pokemon"

rm response.json
