###############################################################################
### EJERCICIO
###############################################################################
import requests

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print('Respuesta exitosa!')
    content = response.json()
    for line in content:
        print(f'\n{line} : {content[line]}')
else:
    print('Error')


###############################################################################
### DIFICULTAD EXTRA
###############################################################################


def pokemon_info(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
    r = requests.get(url)
    content = r.json()
    
    print('Nombre: ',content['name'].capitalize())
    print('Id: ', content['id'])
    print('Peso: ',content['weight'])
    print('Altura: ',content['height'])
    
    types = []
    for indice in range(0, len(content['types'])):
        types.append(content['types'][indice]['type']['name'].capitalize())
    print('Tipo: ', ', '.join(types))

    url_species = content['species']['url']
    r_species = requests.get(url_species)
    species = r_species.json()

    url_evolution_chain = species['evolution_chain']['url']
    r_evolution = requests.get(url_evolution_chain)
    evolution_chain = r_evolution.json()

    current_chain = evolution_chain['chain']
    evolves = []
    while current_chain:
        evolves_to = current_chain['evolves_to']
        if evolves_to:
            for evolution in evolves_to:
                evolves.append(evolution['species']['name'].capitalize())
            current_chain = evolves_to[0]
        else:
            break
    print('Evoluciones:', ", ".join(evolves))

    games = []
    for indice in range(0, len(content['game_indices'])):
        games.append(content['game_indices'][indice]['version']['name'])
    print('Juegos en los que aparece: ', ', '.join(games))



pokemon = input('Introduce un pokemon: ')
pokemon_info(pokemon)