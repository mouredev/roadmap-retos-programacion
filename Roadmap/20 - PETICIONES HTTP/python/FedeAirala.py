 #20 PETICIONES HTTP

"""
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""
import requests
import json

respuesta = requests.get("https://google.com")

if respuesta.status_code == 200:
    print (respuesta.text)
else:
    print (f"Error {respuesta.status_code}, URL incorrecta")


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


def data_pokemon(data):
    name = data["name"]
    id = data["id"]
    weight = data["weight"]
    height = data["height"]
    types = data["types"]
    game = data["game_indices"]
    print (f"Nombre: {name}")
    print (f"ID: {id}")
    print (f"Peso: {weight}")
    print (f"Altura: {height}")
    print ("Tipos:")
    for d in types:
        x = d["type"]["name"]
        print (f"{x}",end = " ")
    print ("")
    print ("Juegos:")
    for d in game:
        x = d["version"]["name"]
        print (f"{x}",end=" / ")
    



def pokemon_data():
    pokemon = input ("Ingrese pokémon que desea buscar :").lower()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    data = response.json()
    if response.status_code == 200:
        data_pokemon(data)
    else:
        print (f"Error {response.status_code} , Pokemon no existe")

pokemon_data()

