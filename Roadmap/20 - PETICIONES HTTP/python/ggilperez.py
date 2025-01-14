# 20 HTTP requests
from http import HTTPStatus

import requests  # It's not a built-in function, need "python -m pip install requests"

response = requests.get("https://pokeapi.co/api/v2/")
if response.status_code == HTTPStatus.OK:
    if "application/json" in response.headers.get("Content-Type"):
        print(response.json())
    else:
        print(response.text)


# Extra

def show_pokemon_info(pokemon_id: str | int) -> None:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")

    if response.status_code != HTTPStatus.OK:
        print(f"Pokemon {pokemon_id} not found")
        return

    if "application/json" not in response.headers.get("Content-Type"):
        print("Invalid response format")
        return

    pokemon_data = response.json()

    print(f"Name: {pokemon_data.get('name')}")
    print(f"ID: {pokemon_data.get('id')}")
    print(f"Weight: {pokemon_data.get('weight')}")
    print(f"Height: {pokemon_data.get('height')}")
    print(f"Types:")
    for pok_type in pokemon_data.get('types', []):
        print(f"\t{pok_type['type']['name']}")

    print("Games:")
    for pok_game in pokemon_data.get("game_indices", []):
        print(f"\t{pok_game['version']['name']}")

    evolves_url = pokemon_data["species"]["url"]

    response = requests.get(evolves_url)
    if response.status_code != HTTPStatus.OK:
        print(f"Error {response.status_code} {response.reason} getting species")
        return

    response = requests.get(response.json()["evolution_chain"]["url"])
    if response.status_code != HTTPStatus.OK:
        print(f"Error {response.status_code} {response.reason} getting evolution chain")
        return

    if "application/json" not in response.headers.get("Content-Type"):
        print("Invalid response format from evolves")
        return

    evolves_data = response.json()["chain"]

    def show_evolves(evo_data):
        print(f"\t{evo_data['species']['name']}")
        if "evolves_to" in evo_data:
            for evolve in evo_data["evolves_to"]:
                show_evolves(evolve)

    print("Evolve chain:")
    show_evolves(evolves_data)


show_pokemon_info("pikachu")
