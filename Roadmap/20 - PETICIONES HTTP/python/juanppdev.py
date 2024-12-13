"""
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""

import requests

# URL de la página web a la que quieres hacer la petición
url = 'https://www.example.com'

try:
    # Realizar la petición HTTP
    response = requests.get(url)
    
    # Verificar si la petición fue exitosa (código de estado 200)
    if response.status_code == 200:
        print("Petición exitosa!")
        # Mostrar el contenido de la web
        print(response.text)
    else:
        print(f"Error en la petición: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error en la petición: {e}")


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

import requests

def get_pokemon_info(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la petición fue exitosa
        data = response.json()

        # Información básica del Pokémon
        name = data['name']
        id = data['id']
        weight = data['weight']
        height = data['height']
        types = [t['type']['name'] for t in data['types']]

        print(f"Nombre: {name}")
        print(f"ID: {id}")
        print(f"Peso: {weight}")
        print(f"Altura: {height}")
        print(f"Tipo(s): {', '.join(types)}")

        # Obtener la cadena de evoluciones
        species_url = data['species']['url']
        species_response = requests.get(species_url)
        species_data = species_response.json()
        evolution_chain_url = species_data['evolution_chain']['url']
        evolution_response = requests.get(evolution_chain_url)
        evolution_data = evolution_response.json()

        print("Cadena de evoluciones:")
        chain = evolution_data['chain']
        while chain:
            print(chain['species']['name'])
            if chain['evolves_to']:
                chain = chain['evolves_to'][0]
            else:
                chain = None

        # Obtener los juegos en los que aparece
        games = [game['version']['name'] for game in data['game_indices']]
        print(f"Juegos: {', '.join(games)}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    pokemon = input("Introduce el nombre o número del Pokémon: ").lower()
    get_pokemon_info(pokemon)
