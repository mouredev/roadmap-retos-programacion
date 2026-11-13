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

# response = requests.get("https://google.com")

# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f"Error con código {response.status_code} al realizar la petición")

"""
Extra
"""
pokemon = input("introduce un nombre o pokemon a buscar").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if response.status_code == 200:
    data = response.json()
    print(f"Los datos don pokemon son Nombre :{data["name"]}")
    print(f"ID :{data["id"]}")
    print(f"Peso:{data["weight"]}")
    print(f"Altura:{data["height"]}")
    for type in data["types"]:
        print(f"Tipo:{type["type"]["name"]}")
    print("Juegos: ")
    for game in data["game_indices"]:
        print(game["version"]["name"])


    

    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]

        response = requests.get(url)

        if response.status_code == 200:
            data=response.json()
            print("Cadena de evolución:")
            

            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])
                
        else:
            print(f"Error pokemon no encontrado, código de error {response.status_code} al realizar la petición")        

    else:
        print(f"Error pokemon no encontrado, código de error {response.status_code} al realizar la petición")       




else:
    print(f"Error pokemon no encontrado, código de error {response.status_code} al realizar la petición")