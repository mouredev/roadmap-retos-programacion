"""EJERCICIO:
Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
una petición a la web que tú quieras, verifica que dicha petición
fue exitosa y muestra por consola el contenido de la web."""
import requests


def get_an_activity() -> dict:
    response = requests.get('https://www.boredapi.com/api/activity')
    if response.status_code == 200:
        return dict(response.json())
    else:
        print('Request failed')
        return {}


def show_the_activity():
    activity = get_an_activity()
    if activity is not {}:
        print('**** Bored API ****')
        print(f'Activity: {activity.get("activity")}')
        print(f'Type of activity: {activity.get("type")}')
        print(f'Participants: {activity.get("participants")}')
        print(f'Price: {activity.get("price")}')
    else:
        print('No activity to display')


"""DIFICULTAD EXTRA (opcional):
Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
terminal al que le puedas solicitar información de un Pokémon concreto
utilizando su nombre o número.
- Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
- Muestra el nombre de su cadena de evoluciones
- Muestra los juegos en los que aparece
- Controla posibles errores"""


def get_pokemon_by_name(pokemon_name: str) -> dict:
    pokemon_name = pokemon_name.lower()

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')
    if response.status_code == 200:
        return dict(response.json())
    else:
        return {}


def get_pokemon_evolution_chain(pokemon: dict) -> dict:
    species_url = pokemon.get('species', {}).get('url')

    if not species_url:
        print('Species URL not found in the provided Pokemon dictionary')
        return {}

    species_response = requests.get(species_url)
    if species_response.status_code != 200:
        print('Failed to retrieve species data')
        return {}

    species_dict = species_response.json()

    evolution_chain = species_dict.get('evolution_chain')
    if not evolution_chain or 'url' not in evolution_chain:
        print('Evolution chain URL not found in species data')
        return {}

    evolution_chain_url = evolution_chain['url']

    evolution_chain_response = requests.get(evolution_chain_url)
    if evolution_chain_response.status_code == 200:
        evolution_chain_dict = evolution_chain_response.json()
        return evolution_chain_dict
    else:
        print('Failed to retrieve evolution chain data')
        return {}


def show_basic_pokemon_information(pokemon: dict):
    print(f'Pokemon name: {pokemon.get("name")}')
    print(f'Pokemon id: {pokemon.get("id")}')
    print(f'Pokemon weight: {pokemon.get("weight")}')
    print(f'Pokemon height: {pokemon.get("height")}')
    print(f'Pokemon type: {pokemon.get("types")[0]["type"]["name"]}')


def show_pokemon_evolution_chain(pokemon_evolution: dict):
    try:
        print(pokemon_evolution.get('chain', {}).get('species', {}).get('name'))
    except IndexError as e:
        pass
    try:
        print(pokemon_evolution.get('chain', {}).get('evolves_to', {})[0]['species']['name'])
    except IndexError as e:
        pass
    try:
        print(pokemon_evolution.get('chain', {}).get('evolves_to', {})[0]['evolves_to'][0]['species']['name'])
    except IndexError as e:
        pass


print('**** Exercise ****')
show_the_activity()
print('**** ****')
while True:
    pokemon_input = input('Enter the pokemon name or ID to search: ')
    pokemon_info = get_pokemon_by_name(pokemon_name=pokemon_input)
    if pokemon_info == {}:
        print('That pokemon was not found, try again')
    else:
        print('\n**** Pokemon basic information ****')
        show_basic_pokemon_information(pokemon=pokemon_info)

        print('\n**** Pokemon evolution chain ****')
        evolution_chain = get_pokemon_evolution_chain(pokemon=pokemon_info)
        show_pokemon_evolution_chain(pokemon_evolution=evolution_chain)
