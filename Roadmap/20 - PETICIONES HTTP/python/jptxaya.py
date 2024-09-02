# #20 PETICIONES HTTP
# /*
#  * EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores
#  */

import requests
import json

req = requests.get("https://duckduckgo.com")

if req.status_code == 200:
    print("Peticion Exitosa")
    print("Content:")
    print(req.content)
else:
    print("Peticion Erronea")
    
print("****************************************")
print("Dificultad Extra")
print("Información de Pokemon")
pokemon_id = input("Introduce el numero o nombre de Pokemon:")

def get_evolucion(chain):
    print("   -"+chain["species"]["name"])
    for evol in chain["evolves_to"]:
        get_evolucion(evol)

req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
if req.status_code == 200:
    pokemon_data = req.json()
    print(f"Nombre:{pokemon_data["name"]}")
    print(f"Id:{pokemon_data["id"]}")
    print(f"Altura:{pokemon_data["height"]}")
    print(f"Peso:{pokemon_data["weight"]}")
    print("Tipos:")
    for type_pokemon in pokemon_data["types"]:
        print("   *"+type_pokemon["type"]["name"])
    print("Juegos:")
    for game_pokemon in pokemon_data["game_indices"]:
         print("   *"+game_pokemon["version"]["name"])
    print("Evolution:")
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}")
    if req.status_code != 200:
        print("Error al obtener evolucion")
    else:
        url_evolution_chain = req.json()["evolution_chain"]["url"]
        #print(url_evolution_chain)
        req = requests.get(url_evolution_chain)
        get_evolucion(req.json()["chain"])
    
elif req.status_code == 404:
    print("Pokemon no Encontrado")  
else:
    print(f"Peticion Erronea. Status Code: {req.status_code}")
