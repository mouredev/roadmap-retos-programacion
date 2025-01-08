# pylint: disable=pointless-string-statement,broad-exception-caught,missing-module-docstring,missing-function-docstring

from typing import TypedDict

import requests

"""
    HTTP request...
"""

print("HTTP request...")

DogFactAttributes = TypedDict(
    "DogFactAttributes",
    {
        "body": str,
    },
)

DogFact = TypedDict(
    "DogFact",
    {
        "id": str,
        "type": str,
        "attributes": DogFactAttributes,
    },
)

DogRequest = TypedDict(
    "DogRequest",
    {"data": list[DogFact]},
)

try:
    response: requests.Response = requests.get(
        url="https://dogapi.dog/api/v2/facts", timeout=1000
    )

    if response.status_code == 200:
        random_dog_fact: DogRequest = response.json()
        print(f"\nRandom dog fact: {random_dog_fact["data"][0]["attributes"]["body"]}")
    else:
        raise RuntimeError(f"{response.status_code} {response.text}")

except Exception as error:
    print(f"\n{error}")


print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")

TypeAttributes = TypedDict("TypeAttributes", {
    "name": str
})

Type = TypedDict("Type", {
    "type": TypeAttributes
})

Version = TypedDict("Version", {
    "name": str
})

GameIndex = TypedDict("GameIndex", {
    "game_index": int,
    "version": Version,
})

Pokemon = TypedDict("Pokemon", {
    "game_indices": list[GameIndex],
    "height": int,
    "id": int,
    "name": str,
    "types": list[Type],
})

def get_pokemon(*,query: int | str) -> Pokemon:
    __response: requests.Response = requests.get(
        url=f"https://pokeapi.co/api/v2/pokemon/{query}",
        timeout=1000
    )

    if __response.status_code == 200:
        pokemon_data: Pokemon = __response.json()
        return pokemon_data

    raise RuntimeError(f"{__response.status_code} {__response.text}")


print("\nPokemon with id number three...")

try:
    third_pokemon: Pokemon = get_pokemon(query=3)
    print(f"\nid: {third_pokemon["id"]}")
    print(f"name: {third_pokemon["name"]}")
    print(f"height: {third_pokemon["height"]}")
    print(f"types: {[type["type"]["name"] for type in third_pokemon["types"]]}")
    print(f"games: {[game["version"]["name"] for game in third_pokemon["game_indices"]]}")

except Exception as error:
    print(f"\n{error}")

print("\nPokemon with 'Lugia' name...")

try:
    third_pokemon: Pokemon = get_pokemon(query="lugia")
    print(f"\nid: {third_pokemon["id"]}")
    print(f"name: {third_pokemon["name"]}")
    print(f"height: {third_pokemon["height"]}")
    print(f"types: {[type["type"]["name"] for type in third_pokemon["types"]]}")
    print(f"games: {[game["version"]["name"] for game in third_pokemon["game_indices"]]}")

except Exception as error:
    print(f"\n{error}")
