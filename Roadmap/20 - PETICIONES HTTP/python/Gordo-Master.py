# 20 - Peticiones HTTP

import requests

url = "https://moure.dev"

response = requests.get(url)
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error con código {response.status_code} al realizar la petición")

"""
Ejercicio extra
"""

session = requests.Session()

name = input("Introduce un nombre o número del pokemon a buscar: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

response = session.get(url)

data = response.json()
if response.status_code == 200:
    
    name = data["name"]
    id = data["id"]
    weight = data["weight"]
    height = data["height"]
    type_pokemon = []
    for i in data["types"]:
        type_pokemon.append(i["type"]["name"])

    response = session.get(data["species"]["url"])
    if response.status_code == 200:

        url_2 = response.json()["evolution_chain"]["url"]

        response = session.get(url_2)

        if response.status_code == 200:

            data = response.json()
            evolution = []

            def create_the_total_list(data, all_evolves, actual_evolves = []):

                actual_evolves.append(data["species"]["name"])

                if data["evolves_to"] == []:
                    all_evolves.append(list(actual_evolves))
                else:
                    for evolves in data["evolves_to"]:
                        create_the_total_list(evolves,all_evolves,actual_evolves)
                
                actual_evolves.pop()

            
            create_the_total_list(data["chain"],evolution)


    url_3 = f"https://pokeapi.co/api/v2/pokemon/{id}/encounters"

    game_where_apear = []
    for i in session.get(url_3).json():
        game_where_apear.append(i["version_details"][0]["version"]["name"])
    game_where_apear = set(game_where_apear)

    print(f"Nombre: {name}")
    print(f"ID: {id}")
    print(f"Peso: {weight}")
    print(f"Altura: {height}")
    print(f"Tipos: {type_pokemon}")
    print(f"Linea evolutiva: ")
    for i in evolution:
        print(i)
    print(f"Juegos donde aparece: {game_where_apear}")

else:
    print(f"Nombre incorrecto, con error de {response.status_code}")

session.close()