""" /*
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
 */ """

import requests

#EJERCICIO

""" response = requests.get("http://www.google.es")
if response.status_code == 200:
    print(response.text)
    print(response)
else:
    (f"Error con código {response.status_code} al utilizar la petición.") """
    
#DIFICULTAD EXTRA

pokemon = input("Introduce el nombre o número del Pokemon a buscar:").lower()

response_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response_pokemon.status_code == 200:
    data = response_pokemon.json()
    print(f"\nID: ", data["id"])
    print(f"Nombre: ", data["name"])
    print(f"Peso: ", data["weight"])
    print(f"Altura: ", data["height"])
    for type in data["types"]:
        print("Tipo: ", type["type"]["name"])

    response_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response_pokemon.status_code == 200:
        url = response_pokemon.json()["evolution_chain"]["url"]

        response_pokemon = requests.get(url)

        if response_pokemon.status_code == 200:
            data = response_pokemon.json()

            print("\nCadena de evoluciones:")

            def get_evolves(data):
                
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])

        else:
            print("Error")
         
    else:
        print("Error.")

    print("\nListado de juegos:")
    response_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    if response_pokemon.status_code == 200:
        data = response_pokemon.json()
        for game in data["game_indices"]:
            print(game["version"]["name"])
    else:
        print("Error.")

else:
    print("Error, pokemon no encontrado.")