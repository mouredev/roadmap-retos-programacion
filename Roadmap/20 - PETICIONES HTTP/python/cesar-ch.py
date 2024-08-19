"""
    * 20 PETICIONES HTTP 
"""

"""
    * DIFICULTAD EXTRA
"""

import requests


def get_pokemon_data(identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{identifier}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Pokémon no encontrado ({response.status_code})")
        return

    data = response.json()
    name = data["name"]
    id = data["id"]
    weight = data["weight"]
    height = data["height"]
    types = [type_info["type"]["name"] for type_info in data["types"]]

    print(f"Nombre: {name}")
    print(f"ID: {id}")
    print(f"Peso: {weight}")
    print(f"Altura: {height}")
    print(f'Tipos: {", ".join(types)}')

    get_evolution_chain(data["species"]["url"])
    get_game_appearances(data["game_indices"])


def get_evolution_chain(species_url):
    response = requests.get(species_url)

    if response.status_code != 200:
        print(f"Error al obtener la especie del Pokémon ({response.status_code})")
        return

    species_data = response.json()
    evolution_chain_url = species_data["evolution_chain"]["url"]

    response = requests.get(evolution_chain_url)
    if response.status_code != 200:
        print(f"Error al obtener la cadena de evoluciones ({response.status_code})")
        return

    chain = response.json()["chain"]
    evolution_names = []

    def get_evolution_names(evolution):
        evolution_names.append(evolution["species"]["name"])
        for evolves_to in evolution["evolves_to"]:
            get_evolution_names(evolves_to)

    get_evolution_names(chain)
    print(f'Cadena de Evoluciones: {", ".join(evolution_names)}')


def get_game_appearances(game_indices):
    games = [game["version"]["name"] for game in game_indices]
    print(f'Juegos en los que aparece: {", ".join(games)}')


if __name__ == "__main__":
    pokemon = input("Introduce el nombre o número del Pokémon: ").lower()
    get_pokemon_data(pokemon)
