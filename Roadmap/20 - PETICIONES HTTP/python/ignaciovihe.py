"""
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""

import requests
import time

url = "https://www.python.org/"
answer = requests.get(url)
if answer.status_code == 200:
    print(answer.text)




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

import asyncio
import aiohttp #modulo para llamadas http asincronas

async def call_api(session, url): # Función asincrona para las llamadas a la api
    async with session.get(url) as answer: # La sesison creada por aiohttp funciona como el request.
        if answer.status != 200:
            return None
        else:
            return await answer.json() #Debe esperar porque sin el await devuelve una corutine(una promesa de los datos cuando termine la llamada)
        
def print_evolutions(evolutions_root, level=0): # Funcion recursiva que imprime laas evoluciones de los pokemon. le paso la raiz de la cadena de evolución.
    print("  " * level  + f"🔹{evolutions_root["species"]["name"]}")
    for evolution in evolutions_root["evolves_to"]:
        print_evolutions(evolution, level + 1)

async def main():
    id_pokemon = input("Intoduce el nombre o el numero de un pokemon: ").lower()
    inicio = time.perf_counter()
    url_info_pokemon = f" https://pokeapi.co/api/v2/pokemon/{id_pokemon}/" #genero los dos url que puedo llamar a la vez
    url_species = f"https://pokeapi.co/api/v2/pokemon-species/{id_pokemon}/"
    
    async with aiohttp.ClientSession() as session: #el session es como el request. Para llamadas http asincronas. Utilizamos solo una sesión.
        #Se hacen las dos primeras llamadas que no dependen entre si a la vez. Evolutions debe esperar a tener la url de especies.
        info_pokemon_json, species_json = await asyncio.gather(call_api(session, url_info_pokemon), call_api(session, url_species))

        if info_pokemon_json:
            print(f"Name: {info_pokemon_json["name"]}")
            print(f"Id: {info_pokemon_json["id"]}")
            print(f"Height: {info_pokemon_json["height"]}")
            print(f"Weight: {info_pokemon_json["weight"]}")
            print(f"Types: ")
            for type in info_pokemon_json["types"]:
                print(f"\t🔸{type["type"]["name"]}")
            print("Games: ")
            for game in info_pokemon_json["game_indices"]:
                print(f"\t{game["version"]["name"]}")
            
            if species_json:
                url_evolutions = species_json["evolution_chain"]["url"]
                evolutions_json = await call_api(session, url_evolutions) #aqui llamamos por tercera vez a la api y debemos esperar la respuesta.
                if evolutions_json:
                    print("\nEvolutions: ")
                    print_evolutions(evolutions_json["chain"])
                else:
                    print("Error en la llamada a evolutions.")    
            else:
                print("Error en la llamada a species.")
        else:
            print("Error el poquemon no existe.")
    fin = time.perf_counter()  #Finalizamos el cronómetro
    print(f"\n Tiempo total de ejecución: {fin - inicio:.2f} segundos")

asyncio.run(main())