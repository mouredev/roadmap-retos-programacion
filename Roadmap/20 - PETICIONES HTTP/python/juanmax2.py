import requests

"""
Ejercicio
"""

response = requests.get("https://google.com")

# Mostrar por consola el contenido de la web
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error con codigo {response.status_code} al realizar la petición")

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

pokemon = input("Introduce el nombre o numero de un pokemon: ").lower()

poke_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if poke_response.status_code == 200:
    data = poke_response.json()
    print(f"Nombre: {data["name"]}")
    print(f"Peso: {data["weight"]}")
    print(f"ID: {data["id"]}")
    print(f"Altura: {data["height"]}")
    print("Tipo(s):")
    for type in data["types"]:
        print(f"{type["type"]["name"]}")
    print("Juegos en los que aparece:")
    for game in data["game_indices"]:
        print(game["version"]["name"])
        
    poke_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if poke_response.status_code == 200:
        url = poke_response.json()["evolution_chain"]["url"]
        
        poke_response = requests.get(url)
        if poke_response.status_code == 200:
            data = poke_response.json()
            
            print("Cadena de evolución:")
            
            
            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)
                
            get_evolves(data["chain"])
                       
        else:
            print(f"Error {poke_response.status_code} al realizar la petición.")
    else:
        print(f"Error {poke_response.status_code} al realizar la petición.")
    

else:
    print(f"Error con código {response.status_code} al realizar la petición")
    
    