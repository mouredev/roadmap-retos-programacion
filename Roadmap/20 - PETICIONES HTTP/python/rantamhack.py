'''
* EJERCICIO:
* Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
* una peticion a la web que tu quieras, verifica que dicha peticion
* fue exitosa y muestra por consola el contenido de la web.
'''
print("\n\n=======================================EJERCICIO=======================================\n\n")

import requests

response = requests.get("https://www.github.com/mouredev", timeout=5)


web = response.content.decode('utf8')

print(web)

print("=======================================")
print(response)
print("=======================================")


'''
* DIFICULTAD EXTRA (opcional):
* Utilizando la PokeAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar informacion de un Pokemon concreto
* utilizando su nombre o numero.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokemon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
'''


print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")



pokemon = input("Escribe el identificador o el nombre del pokemon que quieras conocer\n(Si pones el identificador ten en cuenta que hay 1025 pokemon): ")

 
def find_pokemon(name_or_id):
        
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name_or_id}", timeout=5)
    response.raise_for_status()
    pokemon_data = response.json()
        
    print("=======================================")
    print(response)
    print("=======================================")
        
                    
    name = pokemon_data["name"].capitalize()
    id = pokemon_data["id"]
    weight = pokemon_data["weight"]
    height = pokemon_data["height"]
    pokemon_type = [type["type"]["name"] for type in pokemon_data["types"]]

        
    pokemon_games = [game["version"]["name"] for game in pokemon_data["game_indices"]]     

    
    print(f"El pokemon elegido es {name}")
    print(f"El id del pokemon {name} es {id}")
    print(f"El peso del pokemon {name} es de {weight}")
    print(f"La altura del pokemon {name} es de {height}")
    print(f"{name} es un pokemon de tipo {pokemon_type}")
    print(f"{name} participa en los juegos: {pokemon_games}")
        
        
        


    
find_pokemon(pokemon)
