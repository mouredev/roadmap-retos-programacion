#! /bin/python3.11
# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23 
import http.client
import json

'''
* EJERCICIO
* Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
* una petición a la web que tú quieras, verifica que dicha petición
* fue exitosa y muestra por consola el contenido de la web.
*
* DIFICULTAD EXTRA (opcional):
* Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar información de un Pokémon concreto
* utilizando su nombre o número.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
'''

##################################################
################## EJERCICIO #####################
##################################################

HOSTNAME = 'www.python.org'

# Se crea una instancia de HTTPSConnection
connection = http.client.HTTPSConnection(
    host = HOSTNAME,  # Pagina de la documentacion de Python
)

# Se realiza la peticion al servidor
connection.request(method='GET', url="/")

# Se obtiene el resultado de la peticion
response = connection.getresponse()

#   Devuelve '+' si el status code se encuentra entre el rango 200 - 299 los cuales son códigos de exito   
print(f"[{ '+' if 200 <= response.code < 300  else '-'}] Peticion al servidor { HOSTNAME } retornó un código { response.code }")
print("Respuesta en binario: \n")
if 200 <= response.code < 300: print(response.read())


##################################################
################ EJERCICIO EXTRA #################
##################################################

import http.client

poke_name_id = input("\nIngrese el nombre/id de tu pokemon favorito: ").lower()

poke_conn = http.client.HTTPSConnection("pokeapi.co")
poke_conn.request("GET", f"/api/v2/pokemon/{ poke_name_id }")
poke_resp = poke_conn.getresponse()
poke_data = poke_resp.read().decode("utf-8")

if poke_resp.code == 200:
    poke_json = json.loads(poke_data)
    poke_name = poke_json["name"].upper()
    poke_id = poke_json["id"]
    poke_weight = poke_json["weight"] / 10 
    poke_height = poke_json["height"] / 10 
    poke_types = [typ["type"]["name"].capitalize() for typ in poke_json["types"]]
    poke_evo_url = poke_json["species"]["url"]  
    poke_games = [entry["version"]["name"] for entry in poke_json["game_indices"]]

    poke_conn.request("GET", poke_evo_url)
    evo_resp = poke_conn.getresponse()
    evo_data = evo_resp.read().decode("utf-8")

    if evo_resp.code == 200:
        evo_json = json.loads(evo_data)
        if "chain" in evo_json and evo_json["chain"]:
            poke_evo_chain = [evo_poke["species"]["name"].capitalize() for evo_poke in evo_json["chain"]["evolves_to"]]
        else:
            poke_evo_chain = [poke_name]

        print(f"Nombre del pokemom: { poke_name }")
        print(f"ID: { poke_id }")
        print(f"Peso del pokemon: { poke_weight } kg")
        print(f"Altura: { poke_height } mts")
        print(f"Tipo(s): {', '.join(poke_types)}")
        print(f"Cadena de evolución: {' -> '.join(poke_evo_chain)}")
        print(f"Aparece en los juegos: {', '.join(poke_games)}")
    else:
        print("Error al obtener datos de la cadena de evolución")
else:
    print("Error al obtener datos del Pokémon")