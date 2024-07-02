import requests

url = 'https://jsonplaceholder.typicode.com/posts/76'
response = requests.get(url)

data = response.json()
#print(data)

### Ejercicio Extra ###

def get_pokemon_data(pokemon_name_or_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id.lower()}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: No se pudo encontrar el Pokémon '{pokemon_name_or_id}'. Código de estado: {response.status_code}")
        return None
    return response.json()

def get_evolution_chain(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: No se pudo obtener la cadena de evoluciones. Código de estado: {response.status_code}")
        return None
    return response.json()

def print_pokemon_info(pokemon):
    print(f"Nombre: {pokemon['name'].capitalize()}")
    print(f"ID: {pokemon['id']}")
    print(f"Peso: {pokemon['weight']} hectogramos")
    print(f"Altura: {pokemon['height']} decímetros")

    types = [t['type']['name'] for t in pokemon['types']]
    print(f"Tipo(s): {', '.join(types).capitalize()}")

def print_evolution_chain(evolution_chain):
    chain = evolution_chain['chain']
    evolution_names = []

    while chain:
        evolution_names.append(chain['species']['name'].capitalize())
        if chain['evolves_to']:
            chain = chain['evolves_to'][0]
        else:
            chain = None
    
    print(f"Cadena de evoluciones: {', '.join(evolution_names)}")

def print_game_indices(pokemon):
    games = [game['version']['name'].capitalize() for game in pokemon['game_indices']]
    print(f"Juegos en los que aparece: {', '.join(games)}")

def main():
    pokemon_name_or_id = input("Introduce el nombre o número del Pokémon: ")
    
    pokemon = get_pokemon_data(pokemon_name_or_id)
    if pokemon is None:
        return

    print_pokemon_info(pokemon)
    
    species_url = pokemon['species']['url']
    species_data = requests.get(species_url).json()
    
    evolution_chain_url = species_data['evolution_chain']['url']
    evolution_chain = get_evolution_chain(evolution_chain_url)
    if evolution_chain:
        print_evolution_chain(evolution_chain)
    
    print_game_indices(pokemon)


main()
