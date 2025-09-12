"""
* EJERCICIO:
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
"""

import requests

response_one = requests.get(
    "https://dummyapi.io/data/v1/user/",
    headers= {
        "app-id": "62b0433d2dfd91d4bf56c584"
    }
)

if response_one.status_code == 200:    
    data = response_one.json()
    result = data["data"][0]
    print(result)
else:
    print("La solicitud no fue extisosa. Codigo de estado:", response_one.status_code)


############ -------------------------------- EXTRA ----------------------------------- ##############################

def info_pokemon(id_or_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_or_name}")

    if response.status_code == 200:        
        data = response.json()

        name = data["name"]
        id = data["id"]
        weight = data["weight"]
        height = data["height"]
        pokemon_type = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        
        # Obtener información sobre la cadena de evolución
        species_url = data["species"]["url"]
        species_response = requests.get(species_url)
        if species_response.status_code == 200:
            species_data = species_response.json()
            evolution_url = species_data.get("evolution_chain", {}).get("url")
            if evolution_url:
                evolution_response = requests.get(evolution_url)
                if evolution_response.status_code == 200:
                    evolution_data = evolution_response.json()
                    evolution_chain = [evolution_data.get("chain", {}).get("species", {}).get("name", "").capitalize()]
                    while evolution_data.get("chain", {}).get("evolves_to"):
                        evolution_data = evolution_data["chain"]["evolves_to"][0]
                        evolution_chain.append(evolution_data.get("species", {}).get("name", "").capitalize())
                else:
                    evolution_chain = ["No se encontro informacion de evolucion"]
            else:
                evolution_chain = ["No se encontro URL de cadena de evolucion"]
        else:
            evolution_chain = ["No se encontro informacion de la especie"]

        # Obtener los nombres de los juegos en los que aparece el Pokemon
        game_names = [game["version"]["name"].replace("-", " ").capitalize() for game in data["game_indices"]]

        print(f"Nombre del Pokemon: {name.capitalize()}")
        print(f"ID del Pokemon: {id}")
        print(f"Peso: {weight}")
        print(f"Altura: {height}")
        print(f"Tipo de Pokemon: {pokemon_type}")
        print(f"Cadena de evolucion: {', '.join(evolution_chain)}")
        print(f"Juegos en los que aparece: {', '.join(game_names)}")        
        
    else:
        print("La solicitud no fue exitosa. Codigo de estado:", response.status_code)

while True:
    informacion = input("Ingrese el nombre o ID del Pokemon o 'salir' para salir: ").lower()
    if informacion == "salir":
        break
    else:
        info_pokemon(informacion)
        print()

