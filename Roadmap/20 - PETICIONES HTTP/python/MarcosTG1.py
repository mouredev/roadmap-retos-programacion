"""
* EJERCICIO:
* Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
* una petición a la web que tú quieras, verifica que dicha petición
* fue exitosa y muestra por consola el contenido de la web.
"""

from requests import request
import json

req = request("GET", "https://pokeapi.co/api/v2/pokemon/pikachu")

print(req.status_code)

"""
* DIFICULTAD EXTRA (opcional):
* Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar información de un Pokémon concreto
* utilizando su nombre o número.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
"""

def contruir_endpoint_data_basic() -> str:
    pokemon_name = str(input("Introduce el nombre o id del pokemon a consultar: ")).strip().lower()
    print("\n")
    endpoint = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name

    if request("GET", endpoint).status_code != 200:
        print("El nombre del pokemon es incorrecto.")
        return contruir_endpoint_data_basic()

    return endpoint, pokemon_name

def contruir_endpoint_evolution_chain(pokemon_name: str) -> str:
    endpoint = (f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}")
    return endpoint

def realizar_peticion(endpoint: str) -> dict:
    req = request("GET", endpoint)
    json_response = req.json()
    return json_response
    
def show_pokemon_data_basic(json_response: dict):
    name = json_response["name"]
    identifier = json_response["id"]
    weight = json_response["weight"]
    peso_kg = weight / 10
    height = json_response["height"]
    altura_cm = height * 10
    types = json_response["types"]

    print(f"Tu pokemos es {name}, con el id {identifier}, pesa {peso_kg}kg y mide {altura_cm}cm, además es de tipo {types[0]['type']['name']}.")

def get_evolve(data):
    """
    Importante pasarle la data ya con data["chain"]
    """
    print(data["species"]["name"])
    if "evolves_to" in data:
        for evolve in data["evolves_to"]:
            get_evolve(evolve)


def show_pokemon_evolution_chain(json_response: dict):
    data = json_response["chain"]
    get_evolve(data)


def get_pokemon_evolution_chain_id(json_response: dict) -> str:
    evolution_chain_endpoint = json_response["evolution_chain"]['url']
    return evolution_chain_endpoint

def show_games(json_response, pokemon_name: str):
    games_list = json_response["game_indices"]
    print("\n")
    print(f"{pokemon_name.title()} aparece en estos juegos.")
    for game in games_list:
        print(game["version"]["name"])
    print("\n")
    








def main():

    url, pokemon_name = contruir_endpoint_data_basic()
    json_file = realizar_peticion(url)

    show_pokemon_data_basic(json_file)

    show_games(json_file, pokemon_name)

    endpoint = contruir_endpoint_evolution_chain(pokemon_name)
    json_file = realizar_peticion(endpoint)
    endpoint_evolution_chain = get_pokemon_evolution_chain_id(json_file)
    json_evolution_chain = realizar_peticion(endpoint_evolution_chain)
    print("Esta es la cadena de evolución: ")
    show_pokemon_evolution_chain(json_evolution_chain)

if __name__ =="__main__":
    main()