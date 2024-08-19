"""
* EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""

from requests import get
from time import sleep

url = "https://retosdeprogramacion.com"
response = get(url)
if response.status_code == 200:
    print(response.text.replace(">",">\n")) #doy formato a la respuesta
else:
    print(f"Error, código: {response.status_code}")

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

def is_there_evolutions(json): #busca las evoluciones de manera recursiva y las almacena en una lista
    evolutions = list()
    if len(json["evolves_to"])!= 0:
        evolutions.append(json["species"]["name"])
        for index in range(0,(len(json["evolves_to"]))):
            evolutions.extend(is_there_evolutions(json["evolves_to"][index]))
    else:
        evolutions.append(json["species"]["name"])
    return evolutions

def find_evolution(url):
    evolutions = list()
    response = get(url)
    response_json = response.json()
    evolutions = is_there_evolutions(response_json["chain"])
    return evolutions

def find_pokemon(response):
    response_json = response.json()
    response_species = get(response_json["species"]["url"])
    response_species_json = response_species.json()
    response_evolution_url = response_species_json["evolution_chain"]["url"]
    evolutions = find_evolution(response_evolution_url)
    name = response_json["forms"][0]["name"]
    id = response_json["id"]
    weight = response_json["weight"]
    height = response_json["height"]
    types = list()
    for element in response_json["types"]:
        types.append(element["type"]["name"])
    games = list()
    for element in response_json["game_indices"]:
        games.append(element["version"]["name"])
    return name,id,height,weight,types,evolutions,games

def make_http_request(data):
    url = f"https://pokeapi.co/api/v2/pokemon/{data}"
    response = get(url)
    return response

def pokemon():
    print("\nTE DOY LA BIENVENIDA AL SISTEMA DE BÚSQUEDA DE POKEMONS - basado en la PokeAPI®")
    while True:
        data = input("\nDime el nombre del Pokemon que buscas o su número: ")
        try:
            pokemon = int(data)
        except ValueError:
            pokemon = data
        response = make_http_request(pokemon)
        if response.status_code == 200:
            name,id,height,weight,types,evolutions,games = find_pokemon(response)
            print(f"\nNombre: {name.title()}")
            print(f"Número: {id}")
            print(f"Altura: {float(height/10)} m")
            print(f"Peso: {float(weight/10)} kg\n")
            print("Elementos:")
            for type in types:
                print(f" - {type.title()}")
            print("\nCadena de Evolución: ")
            for evolution in evolutions:
                print(f" - {evolution.title()}")
            print(f"\nJuegos en los que aparece el pokemon {name.title()}")
            if len(games) == 0:
                print(f"Vaya parece que no tenemos registrado ningún juego en el que aparezca {name.title()}")
            else:
                for game in games:
                    print(f" - {game.title()}")
        else:
            print("No hay resultados para tu búsqueda")
        sleep(1)
        print("\n")
        option = input("¿Quieres buscar más pokemon?\n - Si(S)\n - No(N)\n---> ").lower()
        if option == "n":
            print("Gracias por usar este sistema de búsqueda. Hasta Pronto")
            break

pokemon()
