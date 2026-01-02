#!/usr/bin/bash
: '
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */
'

#imprimiendo el menu principal

menu() {
    clear
    echo "-------------------------------------"
    echo "1. obtener html de un sitio web"
    echo "2. consultar informacion de pokemon"
    echo "3. salir"
    echo "-------------------------------------"
}


#obneter html de una url

obtener_html() {
    read -p "introduce la url: " url
    echo "realizando peticion a $url..."
    codigo=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [ "$codigo" -eq 200 ]; then #verificar que el protocolo http sea existoso
        echo "-------------------------------------"
        curl -s "$url" | head -n 15
        echo "recortando contenido..."
        echo "-------------------------------------"
    else
        echo "error!!!! >.< codigo de estado: $codigo"
    fi
    read -p "presiona enter para continuar..."
}


#obtener datos de pokemon con jq

pokemon_info() {
    if ! command -v jq &> /dev/null; then
        echo "necesitas instalar jq para usar esta opcion!!"
        echo "instala con: sudo apt install jq o sudo pacman -S jq ^_^"
        read -p "presiona enter para continuar..."
        return
    fi
    
    read -p "nombre o numero del pokemon: " pokemon
    url="https://pokeapi.co/api/v2/pokemon/$pokemon"
    codigo=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [ "$codigo" -ne 200 ]; then
        echo "pokemon no encontrado! :c"
        read -p "presiona enter para continuar..."
        return
    fi
    
    datos=$(curl -s "$url")
    especie_url=$(curl -s "$url" | jq -r '.species.url')
    cadena_evo=$(curl -s "$especie_url" | jq -r '.evolution_chain.url')
    evoluciones=$(curl -s "$cadena_evo" | jq -r '.chain | recurse(.evolves_to[]) | .species.name')
    
    echo "-------------------------------------"
    echo "nombre:   $(echo "$datos" | jq -r '.name')"
    echo "id:       $(echo "$datos" | jq -r '.id')"
    echo "peso:     $(echo "$datos" | jq -r '.weight/10') kg"  # Convertir a kg
    echo "altuar:   $(echo "$datos" | jq -r '.height/10') m"   # Convertir a metros
    echo "tipos:    $(echo "$datos" | jq -r '.types[].type.name')"
    echo "evoluciones: ${evoluciones%, }"
    echo "-------------------------------------"
    read -p "presiona enter para continuar..."
}


# delarar el bucle principal

while true; do
    menu
    read -p "eilge una opcion: " opcion
    case $opcion in
        1) obtener_html ;;
        2) pokemon_info ;;
        3) exit ;;
        *) echo "opcion no valida" ;;
    esac
done