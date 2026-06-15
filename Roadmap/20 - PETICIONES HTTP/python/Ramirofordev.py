'''
Ejercicio: 
utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza una peticion a la web que tu quieras y verifica que dicha peticion fue exitosa y muestra por consola el contenido de la web.
'''

import requests as rq
import json

response = rq.get("https://www.google.com/webhp?hl=es&ictx=0&sa=X&ved=0ahUKEwiGlJDw_pSRAxVbLPsDHcdLJaEQpYkNCAs&zx=1764337949585&no_sw_cr=1")

if response.status_code == 200:
    print(response.text)

'''
Dificultad extra:
Utilizando la PokeAPI, crea un programa por terminal al que le puedas solicitar informacion de un Pokemon concreto utilizando su nombre o numero.
    * Muestra el nombre, id, peso, altura, y tipo(s) del pokemon
    * Muestra el nombre de su cadena de evoluciones.
    * Muestra los juegos en los que aparece
    * Controla posibles errores.
'''

def menu():
    while True:
        try:
            option = int(input("""Elige una de las siguientes opciones: 
                        1. Datos del pokemon.
                        2. Evoluciones del pokemon.
                        3. Juegos en los que aparece
                        4. Salir. """))
        except ValueError:
            print("Por favor ingresa un numero valido.")
        
        if option in [1, 2, 3]:
            options(option)
        elif option == 4:
            print("Saliendo de la pokedex!")
            break
        else:
            print("Opcion invalida, por favor ingresa una opcion.")

def show_pokemon_data():
    # Preguntamos al usuario por el nombre del pokemon
    pokemon_name = input("Inserte el nombre del pokemon: ")
    try:
        # Obtenemos la informacion del pokemon
        response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")

        if response.status_code != 200:
            print("El pokemon no existe.")
            return
        
        pokemon_data = response.json()
    
        # Imprimimos el nombre, peso, altura, tipo(s)
        print(f"Nombre: {pokemon_data['name']}")
        print(f"ID: {pokemon_data['id']}")
        print(f"Peso: {pokemon_data['weight']}")
        print(f"Altura: {pokemon_data['height']}")
        
        for tipo in pokemon_data["types"]:
            print(f"Tipo(s): {tipo['type']['name']}\n")

    except rq.exceptions.RequestException as e:
        print(f"Ha surgido un error: {e}")
    

def show_pokemon_evo():
    # Le preguntamos al usuario del pokemon que desea saber sus evoluciones
    pokemon_name = input("Inserte el nombre del pokemon: ")

    try:
        response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")

        if response.status_code != 200:
            print("El pokemon no existe.")
            return

        pokemon_data = response.json()

        # Obtenemos la url de la especie del pokemon
        species_url = pokemon_data["species"]["url"]

        response = rq.get(species_url)
        species_data = response.json()

        # Obtenemos el url de la evolucion
        evolution_url = species_data["evolution_chain"]["url"]
        response = rq.get(evolution_url)

        evolution_data = response.json()

        names = []

        current = evolution_data["chain"]
        while current:
            names.append(current["species"]["name"])
            if current["evolves_to"]:
                current = current["evolves_to"][0]
            else:
                current = None
        
        print(names)
        
    except rq.exceptions.RequestException as e:
        print(f"Ha surgido un error: {e}")

    
def show_pokemon_in_game():
    # Preguntamos por el pokemon 
    pokemon_name = input("Inserte el nombre del pokemon: ")
    try:
        response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")

        if response.status_code != 200:
            print("El pokemon no existe.")
            return

        pokemon_data = response.json()

        # Loopeamos a travez de los datos obtenidos y despues extraemos los nombres de los juegos
        games = set()
        for game in pokemon_data["game_indices"]:
            games.add(game["version"]["name"])

        print(sorted(games))

    except rq.exceptions.RequestException as e:
        print(f"Ha surgido un error: {e}")


def options(o):
    dic = {
        1: show_pokemon_data,
        2: show_pokemon_evo,
        3: show_pokemon_in_game
    }
    return dic[o]()

menu()