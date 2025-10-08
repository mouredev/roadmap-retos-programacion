# @Author Mhayhem (Daniel Grande)
# @Github https://github.com/mhayhem

import requests
import json

# EJERCICIO:
# Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
# una petición a la web que tú quieras, verifica que dicha petición
# fue exitosa y muestra por consola el contenido de la web.

r = requests.get("https://www.python.org/")
succes = r.status_code # 200 la peticion fue exitosa

text = r.text # contenido dela web


# DIFICULTAD EXTRA (opcional):
# Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
# terminal al que le puedas solicitar información de un Pokémon concreto
# utilizando su nombre o número.
# - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
# - Muestra el nombre de su cadena de evoluciones
# - Muestra los juegos en los que aparece
# - Controla posibles errores

def get_pokemon_info():
    
    while True:
        option = input("Buscar por nombre (n) o id (i) salir (s): ").lower()
        match option:
            case "n":
                param = input("Nombre del pokemón: ").capitalize()
            case "i":
                param = input("Id del pokemón: ")
            case "s":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida, pruebe de nuevo.")
                continue
        print("Procesando.\n")
        url = f"https://pokeapi.co/api/v2/pokemon/{param}"
        
        try:
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                print("Pokemón encontrado.\n")
                extract_info(data)
            
            elif response.status_code == 404:
                print("Pokemón no encontrado, intentelo de nuevo.\n")
                continue
            else:
                print(f"Error en la petición HTTP: {response.status_code}\n")
                continue
            
        except requests.exceptions.Timeout:
            print("Excedido el tiempo de espera, pruebe de nuevo.\n")
            continue
        except requests.exceptions.RequestException as error:
            print(f"Error en la petición HTTP: {error}\n")
            continue
            
def print_info_pokemon(name, pokemon_id, height, weight, types, games, evolution_chain):
    while True:
        selection = input("¿Qué información quiere mostrar?\n"
                        "1. Informacion basica\n"
                        "2. Cadena de evoluciones\n"
                        "3. Juegos en los que aparece\n"
                        "4. Información completa\n"
                        "5. Salir\n")
        print("\n")
        match selection:
            case "1":
                print(f"Nombre: {name.capitalize()}, ID: {pokemon_id}, Altura: {height}, Peso: {weight}, Tipos: {", ".join(types)}")
            case "2":
                print(f"Cadena de evoluciones: {' -> '.join(evolution_chain) if evolution_chain else "Sin evoluciones."}")
            case "3":
                print(f"Juegos en los que aparece: {' - '.join(games)}")
            case "4":
                print(
                    f"Nombre: {name.capitalize()}, ID: {pokemon_id}, Altura: {height}, Peso: {weight}, Tipos: {", ".join(types)}\n"
                    f"Cadena de evoluciones: {' -> '.join(evolution_chain) if evolution_chain else "Sin evoluciones."}\n"
                    f"Juegos en los que aparece: {' - '.join(games)}"
                )
            case "5":
                return "Cerrando el programa."
            case _:
                print("Opción invalida, pruebe de nuevo.")
        print("\n")
                 
        
        
def extract_info(data):
    name = data["name"]
    pokemon_id = data["id"]
    height = data["height"]
    weight = data["weight"]
    types = [t["type"]["name"] for t in data["types"]]
    games = [g["version"]["name"] for g in data["game_indices"]]
    species_url = data["species"]["url"]
    species_data = requests.get(species_url).json()
    evolution_chain = species_data["evolution_chain"]["url"]
    evolution_chain_data = requests.get(evolution_chain).json()
    evolution_chain = get_evolution_chain(evolution_chain_data["chain"])
    
    return print_info_pokemon(name, pokemon_id, height, weight, types, games, evolution_chain)

def get_evolution_chain(chain):
    evolutions = [chain["species"]["name"].capitalize()]
      
    for evo in chain["evolves_to"]:
        evolutions.extend(get_evolution_chain(evo))
    
    return evolutions
            

get_pokemon_info()