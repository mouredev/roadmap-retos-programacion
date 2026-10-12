"""
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
"""

import requests

response = requests.get("https://moure.dev/2342J")
print(response)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error con código {response.status_code} al realizar la petición.")


pokemon = input("Introduce un nombre o número del Pokémon a buscar: ").lower().strip()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    print(response.text)
else:
    print("Pokémon no encontrado.")
print()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json()
    name = data["name"]
    id = data["id"]
    peso = data["weight"]
    altura = data["height"]
    tipos = "| "
    for type in data["types"]:
        tipos += f"{type["type"]["name"]} | "
    print("Juegos: ")
    for game in data["game_indices"]:
        print(game["version"]["name"])

    print("="*30)
    print(" Nombre: {}\n Identificador: {}\n Peso: {}\n Altura: {}\n Tipos: {}".format(name.upper(), id, peso, altura, tipos))
    print("="*30)

    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/"
    )

    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Cadena de evolución: ")

            def get_envolves(data):
                data["species"]["name"]
                if "envolves_to" in data:
                    for evolve in data["envolves_to"]:
                        get_envolves(evolve)

            get_envolves(data["chain"])
        else:
            print("No se pueden obtener las evoluciones del pokemón.")
    else:
        print("No se pueden obtener las evoluciones del pokemón.")

else:
    print("Pokémon no encontrado.")



