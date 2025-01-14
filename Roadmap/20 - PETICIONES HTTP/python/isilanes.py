import requests


def main():
    url = "https://isilanes.org"
    response = requests.get(url)
    assert response.status_code == 200
    print(response.text)


def extra(name_or_pid: str | int | None = None):
    name_or_pid = name_or_pid or input("Introduce el nombre o el ID del Pokémon: ")

    if not name_or_pid:
        print("Error: no has especificado qué Pokémon quieres.")
        return

    pokemon = get_pokemon_by_name_or_id(name_or_pid)
    pokemon_types = [t["type"]["name"] for t in pokemon.get("types", [])]
    name: str = pokemon.get('name')

    if not name:
        print("Error. No pudimos encontrar ese Pokemon.")
        return

    evolution_chain = get_evolution_chain(pokemon)
    games = get_games(pokemon)

    print(f"Nombre:              {name}")
    print(f"ID:                  {pokemon.get('id')}")
    print(f"Altura:              {pokemon.get('height')}")
    print(f"Peso:                {pokemon.get('weight')}")
    print(f"Tipos:               {', '.join(pokemon_types)}")
    print(f"Cadena de evolución: {' -> '.join(evolution_chain)}")
    print(f"Juegos:              {', '.join(games)}")


def get_games(pokemon: dict | None = None) -> list[str]:
    return [g["version"]["name"] for g in pokemon["game_indices"]]


def get_evolution_chain(pokemon: dict | None = None) -> list[str]:
    if not pokemon:
        return []

    species_url = pokemon["species"]["url"]
    species_data = requests.get(species_url).json()
    chain_url = species_data.get("evolution_chain", {}).get("url")

    if not chain_url:
        return []

    chain_data = requests.get(chain_url).json().get("chain")

    if not chain_data:
        return []

    chain = []
    while chain_data:
        name = chain_data["species"]["name"]
        if not name:
            break

        chain.append(name)

        sub_chain = chain_data["evolves_to"]
        if not sub_chain:
            break

        chain_data = sub_chain[0]

    return chain


def get_pokemon_by_name_or_id(name_or_pid: str | int | None = None) -> dict:
    if not name_or_pid:
        return {}

    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_pid}"
    response = requests.get(url)

    if response.status_code != 200:
        return {}

    return response.json()


if __name__ == "__main__":
    main()
    extra()
