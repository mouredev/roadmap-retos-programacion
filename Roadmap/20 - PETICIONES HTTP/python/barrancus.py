# 20 - Python
# 
# EJERCICIO:
# Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
# una petición a la web que tú quieras, verifica que dicha petición
# fue exitosa y muestra por consola el contenido de la web.
# 
# DIFICULTAD EXTRA (opcional):
# Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
# terminal al que le puedas solicitar información de un Pokémon concreto
# utilizando su nombre o número.
# - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
# - Muestra el nombre de su cadena de evoluciones
# - Muestra los juegos en los que aparece
# - Controla posibles errores
# 

import requests
from bs4 import BeautifulSoup as bs
import json

class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

def serparacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena * 20}')

def ejercicio() -> None:
    serparacion("_:_")
    web = requests.get("https://www.as.com")
    if web.status_code == 200:
        testweb = bs(web.text, features="lxml")
        print(testweb)

def extra() -> None:
    serparacion("_:_")
    # Busqueda recurente fases evolucion
    def rev_poke_chain(chain) -> list:
        test = []
        if type(chain) == list:
            for menta in chain:
                chain = menta
        if "evolves_to" in chain.keys() and len(chain["evolves_to"]) != 0:
            test = rev_poke_chain(chain["evolves_to"])
        test.append(chain["species"]["name"])
        return test
    
    while True:
        print("\nPor favor inserta el nº o el nombre del Pokemon que quieres buscar.\nInserta 0 para salir.")
        search_pokemon = input("ID/Nombre: ")
        if search_pokemon == "0":
            break
        pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search_pokemon}/")
        if pokeapi.status_code == 200:
            search_pokemon_info = json.loads(pokeapi.text)
            poke_form = search_pokemon_info["forms"]
            for element in poke_form:
                try:
                    poke_name = element["name"]
                except:
                    pass
            poke_number = search_pokemon_info["id"]
            poke_height = search_pokemon_info["height"]
            poke_weight = search_pokemon_info["weight"]
            poke_game_indices = search_pokemon_info["game_indices"]
            poke_game_name=[]
            for element in poke_game_indices:
                version = element["version"]
                poke_game_name.append(version["name"])

            poke_weight = (poke_weight * 0.453592)
            poke_height = (poke_height * 2.54)
            print(f'\nEl Pokemon {poke_name.upper()} es el id {poke_number}, tiene una altura de {poke_height:n} cm y un peso de {poke_weight:n} kilos.')
            print(f'El Pokemon {poke_name.upper()} aparede en los juegos {poke_game_name}')
            pokeapi2 = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{search_pokemon}/")
            search_pokemon_info2 = json.loads(pokeapi2.text)
            evol_chain = search_pokemon_info2["evolution_chain"]
            pokeapi3 = requests.get(evol_chain["url"])
            search_pokemon_evol = json.loads(pokeapi3.text)
            poke_chain = search_pokemon_evol["chain"]
            chain = rev_poke_chain(poke_chain)
            print(f'El Pokemon {poke_name.upper()} tiene la siguiente cadena de evolucion {chain}.\n')

        elif pokeapi.status_code >= 400 and pokeapi.status_code <= 499:
            print('\nProbablemente el Pokemon no existe o no está registrado, prueba con otro.')
        elif pokeapi.status_code >= 500 and pokeapi.status_code <= 599:
            print('\nNo se puede proceder con la solicitud por problemas con el servidor.')
        else:
            print('\nError desconocido, prueba con otro.')

def main() -> None:
    ejercicio()
    extra()

contador = iter(Counter())
if __name__ == "__main__":
    main()
