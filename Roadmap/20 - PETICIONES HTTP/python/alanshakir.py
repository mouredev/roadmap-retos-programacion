"""
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
"""
import requests

url = "https://docs.python.org/es/3/tutorial/"
response = requests.get(url)
status = response.status_code

if status == 200:
    print("Peticion exitosa")
    print(response.text)
else:
    print(f"Peticion fallida, error: {status}")

#Extra

pokemon = input("introduce el codigo o nombre del pokemon: ")

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if response.status_code == 200:
    data_pokemon = response.json()
    print("Id: ", data_pokemon["id"])
    print("Name: ", data_pokemon["name"])
    print("Weight: ", data_pokemon["weight"])
    print("Height: ", data_pokemon["height"])
    for type in data_pokemon["types"]:
        print("Type(s): ", type["type"]["name"]) 
    print("Game(s): ")
    for game_index in data_pokemon["game_indices"]:
        print(game_index["version"]["name"])       
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        data_pokemon = response.json()["evolution_chain"]["url"]
        response = requests.get(data_pokemon)
        if response.status_code == 200:
            evolution_pokemon = response.json()
            print("Cadena de evoluciones: ")
            def evolutions(evolution_pokemon):
                print(evolution_pokemon["species"]["name"])
                if "evolves_to" in evolution_pokemon:
                    for evolution in evolution_pokemon["evolves_to"]:
                        evolutions(evolution)
            evolutions(evolution_pokemon["chain"])
        else:
            print(f"No se encuentran cadena evoluciones para este pokemon, error: {response.status_code}")
    else:
        print(f"No se encuentran evoluciones para este pokemon, error: {response.status_code}")
else:
    print(f"Peticion fallida, error: {response.status_code}")
