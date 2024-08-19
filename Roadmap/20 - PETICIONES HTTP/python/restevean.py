"""
Exercise
"""
import requests


def request_url(url):
    # Realizar la petición GET
    response = requests.get(url)

    # Verificar si la petición fue exitosa
    if response.status_code == 200:
        return "Petición exitosa."
    else:
        return f"Error en la petición: {response.status_code},"


"""
Extra
"""


def get_pokemon_data(pokemon_identifier):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    url = f"{base_url}{pokemon_identifier.lower()}"

    response = requests.get(url)

    if response.status_code != 200:
        print(
            f"Error: No se pudo obtener información para {pokemon_identifier}. Código de estado: {response.status_code}")
        return

    data = response.json()
    print(f"Name: {data['name'].capitalize()}")
    print(f"ID: {data['id']}")
    print(f"Weight: {data['weight']/10} kg")
    print(f"Height: {data['height']*10} cm")

    types = [type_info['type']['name'] for type_info in data['types']]
    print(f"Tipe(s): {', '.join(types).capitalize()}")

    # Obtener cadena de evoluciones
    species_url = data['species']['url']
    species_response = requests.get(species_url)
    species_data = species_response.json()
    evolution_chain_url = species_data['evolution_chain']['url']

    evolution_chain_response = requests.get(evolution_chain_url)
    evolution_chain_data = evolution_chain_response.json()

    evolution_chain = []
    current_evolution = evolution_chain_data['chain']

    while current_evolution:
        evolution_chain.append(current_evolution['species']['name'].capitalize())
        if current_evolution['evolves_to']:
            current_evolution = current_evolution['evolves_to'][0]
        else:
            current_evolution = None

    print(f"Evolutions chain: {', '.join(evolution_chain)}")

    # Obtener juegos en los que aparece
    games = [game_info['version']['name'] for game_info in data['game_indices']]
    print(f"Games where it appears: {', '.join(games).capitalize()}")


if __name__ == '__main__':
    print("Exercise")
    url = "https://retosdeprogramacion.com/roadmap/"
    print("GET to", url, request_url(url))
    url = "https://retosdeprogramacion.com/roadmap/1"
    print("GET to",url, request_url(url))

    print("Extra")
    pokemon_name = input("Type pokemon's name or number: ")
    get_pokemon_data(pokemon_name)
