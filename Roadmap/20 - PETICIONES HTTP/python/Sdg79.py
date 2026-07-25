
import requests

url = "https://www.bna.com.ar/Personas"

respuesta = requests.get(url)

estado = respuesta.status_code
print(estado)

contenido = respuesta.content
#print(contenido)


# DIFICULTAD EXTRA:

url = "https://pokeapi.co/api/v2/pokemon"

pokemon = input("Introduce el nombre o número del Pokemon a consultar: ").lower()
response = requests.get(f"{url}/{pokemon}/")
if response.status_code == 200:
    datos = response.json()
    print(f"Nombre: {datos["name"]}")
    print(f"Id: {datos["id"]}")
    print(f"Peso: {datos["weight"]}")
    print(f"Altura: {datos["height"]}")
    for type in datos["types"]:
        print(f"Tipos: {type["type"]["name"]}")
    print("Juegos: ")
    for juego in datos["game_indices"]:
        print(juego["version"]["name"])

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            print("Cadena de Evolución: ")
            
            def evoluciones(datos):
                print(datos["species"]["name"])
                if "evolves_to" in datos:
                    for evolucion in datos["evolves_to"]:
                        evoluciones(evolucion)
                                
            evoluciones(datos["chain"])

        else:
            print("Error {response.status_code}, no se ha encontrado la evolucion del Pokemon")
    else:
        print("Error {response.status_code}, no se ha encontrado la evolucion del Pokemon")
    
else:
    print(f"Error {response.status_code}, no se ha encontrado el Pokemon ")
