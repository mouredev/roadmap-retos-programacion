import requests
import sys
from typing import List, Any

# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
print(response.status_code) # 200

if response.status_code == 200:
    print(response.json()) # Type dict
    print(response.text) # Type str

else:
    print(f"Error al hacer la petición. Código de estado: {response.status_code}")


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */
"""

def get_evolutions(chain) -> List[str]:
    evolutions = [chain['species']['name']]
    for evolution in chain['evolves_to']:
        evolutions.extend(get_evolutions(evolution))
    return evolutions

def get_data_pokemon(pokemon_name: str) -> dict[str, Any] | Any:
    """ Obtiene los datos de un pokémon a partir de su nombre o id
    :param pokemon_name: Nombre o id del pokémon
    :type pokemon_name: str
    :return: Datos del pokémon
    :rtype: dict
    """
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            url_species = pokemon_data['species']['url']
            species_data = requests.get(url_species).json()['evolution_chain']['url']

            # url_evolution_chain = species_data['evolution_chain']['url']
            evolution_data = requests.get(species_data).json()

            evolutions = list(dict.fromkeys(get_evolutions(evolution_data['chain'])))
            games = [game['version']['name'] for game in pokemon_data['game_indices']]

            return {
                'name': pokemon_data['name'].capitalize(),
                'id': pokemon_data['id'],
                'height': pokemon_data['height'],
                'weight': pokemon_data['weight'],
                'types': [pokemon_type['type']['name'].capitalize() for pokemon_type in pokemon_data['types']],
                'evolutions': evolutions,
                'games': games
            }

        else:
            raise Exception(f"Fallo en recuperar los datos. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        return None

    

def main():
    print("=" * 5, "Bienvenido a la PokéAPI", "=" * 5)
    while True:
        pokemon = input("Ingresa el nombre o id del pokémon, salir para terminar el programa: ").lower().strip()

        if pokemon == "salir":
            print("¡Hasta luego!")
            return
        
        if not pokemon:
            print("Debes ingresar un nombre o id de un pokémon valido!")
            continue

        try:
            data = get_data_pokemon(pokemon)
            if data:
                data = get_data_pokemon(pokemon) 
                print(f"Name: {data['name']}")
                print(f"Id: {data['id']}")
                print(f"Height: {data['height']}")
                print(f"Weight: {data['weight']}")
                print(f"Type: {', '.join(data['types'])}")
                print(f"Evolutions: {' → '.join(data['evolutions'])}")
                print(f"Games: {', '.join(data['games'])}")
        except Exception as e:
            print(f"Error: {e}")



if "__main__" == __name__:
    main()