'''
EJERCICIO:
* Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
* una petición a la web que tú quieras, verifica que dicha petición
* fue exitosa y muestra por consola el contenido de la web.
'''

import re
import requests     # It's not a built-in function, need "python3.14 -m pip install requests" for Ubuntu

def lee(url:str):
    validar = bool(re.match(r"^http[s]?://(w)*\.*[\w]+\.[\w\/\-]+$", url))
    if validar:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            if "application/json" in respuesta.headers.get("Content-Type"):    
                respuesta = respuesta.json()
            else:
                respuesta = respuesta.text
        else:
            print(f"{url} invalida, error con código {respuesta.status_code}!!!")        
    else:
        print(f"url: {url} invalida!!!")
        raise UnboundLocalError("No hay respuesta")     
    return(respuesta)
           

print("*"*60)

direccion = input("Escribe la url: ")
try: 
    print(lee(direccion))
except UnboundLocalError as e:
    print(e)



'''
* DIFICULTAD EXTRA (opcional):
* Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar información de un Pokémon concreto
* utilizando su nombre o número.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
'''

direccion = "https://pokeapi.co/api/v2/pokemon/1"
info = lee(direccion)
print("-"*60)
print("Nombre: " + info["name"])
print(f"Id: {info["id"]}")
print(f"Peso: {info["weight"]}")
print("Tipo:")
for type in info["types"]:
    print(type["type"]["name"])
print("-"*60)

direccion = "https://pokeapi.co/api/v2/pokemon-species/1/"
info = lee(direccion)
direccion = info["evolution_chain"]["url"]
info = lee(direccion)

def get_evolves(info):
    print(info["species"]["name"])
    if "evolves_to" in info:
        for evolucion in info["evolves_to"]:
            get_evolves(evolucion)

print("Evolución: ")
get_evolves(info["chain"])

print("-"*60)

direccion = "https://pokeapi.co/api/v2/pokemon/1"
info = lee(direccion)
print("Juegos:")
for juego in info["game_indices"]:
    print(juego["version"]["name"])