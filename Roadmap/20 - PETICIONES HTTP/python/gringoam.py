import requests

"""
Ejercicio
"""

respuesta= requests.get("https://www.google.com")
print(respuesta.status_code)
if respuesta.status_code== 200:
    print(respuesta.text)
    
else:
    print(f"Error con codigo {respuesta.status_code} al realizar la petición")


"""
Extra
"""

pokemon = input("Introduce un nombre o número del Pokémon a buscar: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if response.status_code == 200:
    data = response.json()
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["height"])
    print("Tipo(s): ")
    for type in data["types"]:
        print(type["type"]["name"])
    print("Juegos:")
    for game in data["game_indices"]:
        print(game["version"]["name"])

    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("Cadena de evolución:")

            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])

        else:
            print(f"Error {response.status_code} obteniendo las evoluciones.")
    else:
        print(f"Error {response.status_code} obteniendo las evoluciones.")
else:
    print(f"Error {response.status_code}: Pokémon no encontrado")
