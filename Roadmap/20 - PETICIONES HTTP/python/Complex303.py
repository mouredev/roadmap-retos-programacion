"""
Peticiones HTTP
"""

"""una petición HTTP es una solicitud que un cliente (como un navegador o una app) 
envía a un servidor para pedir o enviar información a través de la web. 
Se compone de un método (como GET, POST, PUT o DELETE), una URL, y opcionalmente cabeceras y datos."""

# Importamos la librería requests, que permite hacer peticiones HTTP en Python.
import requests
import json
# Realizamos una petición GET a la URL indicada (en este caso, el sitio de eBay)
# response = requests.get("https://www.ebay.com/")

# # Verificamos si el código de estado de la respuesta es 200 (lo que significa que la petición fue exitosa)
# if response.status_code == 200:
#     # Si la respuesta fue exitosa, imprimimos el contenido de la página (en texto HTML)
#     print(response.text)
# else:
#     # Si la respuesta no fue exitosa, mostramos un mensaje de error con el código de estado recibido
#     print(f"Error con codigo {response.status_code} al realizar la peticion")




""" * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores"""

#un endpoint es una URL específica dentro de una API o servicio web a la que se puede enviar una petición para obtener o enviar datos.

# Pedimos al usuario que escriba el nombre o número del Pokémon
# Usamos .lower() para convertir todo a minúsculas y evitar errores por mayúsculas
pokemon = input("Introduce el nombre o el numero del pokemon a buscar: ").lower()

# Realizamos una petición GET a la API de Pokémon para obtener información básica
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

# Verificamos si la respuesta de la API fue exitosa (código 200 = OK)
if response.status_code == 200: 
    # Convertimos la respuesta JSON en un diccionario de Python
    pokemon_data = response.json()

    # Mostramos algunos datos del Pokémon en consola
    print("Nombre: ", pokemon_data["name"])       # Nombre del Pokémon
    print("ID: ", pokemon_data["id"])             # ID del Pokémon en la Pokédex
    print("Peso: ", pokemon_data["weight"])       # Peso del Pokémon
    print("Altura: ", pokemon_data["height"])     # Altura del Pokémon

    # Mostramos los tipos del Pokémon (pueden ser 1 o 2)
    print("Tipo(s): ", end="") 
    print(", ".join(tipo["type"]["name"] for tipo in pokemon_data["types"]))

    # Mostramos los juegos en los que ha aparecido ese Pokémon
    print("Juegos: ", end="")
    print(", ".join(juego["version"]["name"] for juego in pokemon_data["game_indices"]))

    # Hacemos otra petición para obtener información de la especie (donde está la cadena evolutiva)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    # Si la respuesta fue exitosa
    if response.status_code == 200:
        # Obtenemos la URL de la cadena de evolución desde la respuesta
        url = response.json()["evolution_chain"]["url"]

        # Hacemos otra petición a esa URL para obtener la cadena de evolución
        response = requests.get(url)

        # Si la respuesta fue exitosa
        if response.status_code == 200:
            # Convertimos la respuesta JSON en un diccionario
            data = response.json()

            # Mostramos el encabezado de la sección de evoluciones
            print("Cadena de evolucion: ")

            # Definimos una función recursiva para recorrer la cadena evolutiva
            def get_evolves(data):
                # Imprimimos el nombre de la especie actual
                print(data["species"]["name"])
                # Verificamos si hay evoluciones en "evolves_to"
                if "evolves_to" in data:
                    # Por cada evolución encontrada, llamamos recursivamente a la función
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            # Llamamos a la función con la raíz de la cadena evolutiva
            get_evolves(data["chain"])
        else:
            # Si hubo error al obtener las evoluciones
            print(f"Error {response.status_code} obteniendo evoluciones")
    else:
        # Si hubo error al obtener la especie del Pokémon
        print(f"Error {response.status_code} obteniendo evoluciones")

    # Creamos un diccionario con los datos resumidos del Pokémon
    info_resumida = {
        "Nombre": pokemon_data["name"],
        "ID": pokemon_data["id"],
        "Peso": pokemon_data["weight"],
        "Altura": pokemon_data["height"],
        "Tipos": [tipo["type"]["name"] for tipo in pokemon_data["types"]],
        "Juegos": [juego["version"]["name"] for juego in pokemon_data["game_indices"]]
    }

    # Abrimos (o creamos) un archivo JSON para guardar el resumen
    with open(f"{pokemon}_resumen.json", "w", encoding="utf-8") as archivo:
        # Guardamos el diccionario en el archivo con indentación de 4 espacios
        json.dump(info_resumida, archivo, indent=4)

else:
    # Si la primera petición falla (el Pokémon no existe o error en la API)
    print(f"Error: {response.status_code} pokemon no encontrado")

