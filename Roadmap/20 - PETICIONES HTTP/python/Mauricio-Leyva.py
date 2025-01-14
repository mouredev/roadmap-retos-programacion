## Ejercicio

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"

response = requests.get(url)

if response.status_code == 200:
    print("La petición fue exitosa!")

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify())
else:
    print(f"La petición falló con el código de estado: {response.status_code}")




## Dificultad extra


import requests

def get_pokemon_info(pokemon_name_or_id):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}")
        response.raise_for_status() 

        pokemon_data = response.json()

        name = pokemon_data["name"].capitalize()
        pokemon_id = pokemon_data["id"]
        weight = pokemon_data["weight"] / 10 
        height = pokemon_data["height"] / 10 
        types = [t["type"]["name"].capitalize() for t in pokemon_data["types"]]
        evolution_chain_url = pokemon_data["species"]["url"]  
        game_appearances = [entry["version"]["name"] for entry in pokemon_data["game_indices"]]

        evolution_chain_response = requests.get(evolution_chain_url)
        evolution_chain_response.raise_for_status()
        evolution_chain_data = evolution_chain_response.json()

        if "chain" in evolution_chain_data and evolution_chain_data["chain"]:
            evolution_chain = [pokemon["species"]["name"].capitalize() for pokemon in evolution_chain_data["chain"]["evolves_to"]]
        else:
            evolution_chain = [name]

        print(f"Nombre: {name}")
        print(f"ID: {pokemon_id}")
        print(f"Peso: {weight} kg")
        print(f"Altura: {height} m")
        print(f"Tipo(s): {', '.join(types)}")
        print(f"Cadena de evolución: {' -> '.join(evolution_chain)}")
        print(f"Aparece en los juegos: {', '.join(game_appearances)}")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición: {e}")
    except ValueError:
        print("El valor proporcionado no es un nombre o número de Pokémon válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Solicitar al usuario el nombre o número del Pokémon
pokemon_name_or_id = input("Ingresa el nombre o número del Pokémon: ").lower()

# Llamar a la función para obtener la información del Pokémon
get_pokemon_info(pokemon_name_or_id)
