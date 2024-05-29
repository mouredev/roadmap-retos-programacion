# #20 PETICIONES HTTP
"""
/*
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
 */
"""

import requests

# Realiza una solicitud HTTP GET a la página de inicio de Twitter
r = requests.get("https://twitter.com/home")  # Regresa el estado de la web

# Verifica si la solicitud fue exitosa
if r.status_code == 200:  # 200 indica que la solicitud fue exitosa
    print("exitosa: \n")
    print(r.text)  # Muestra el HTML de la página web
else:
    print("fallido")  # Indica que la solicitud falló

# Solicita al usuario que introduzca el nombre o número de un Pokémon
pokemon = input("introduce el nombre o numero de un pokemon : ").lower()

# Realiza una solicitud HTTP GET a la API de PokeAPI para obtener información del Pokémon
pokemones = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

# Verifica si la solicitud fue exitosa
if pokemones.status_code == 200:
    info = pokemones.json()  # Convierte la respuesta JSON en un diccionario de Python
    print("NOMBRE : ", info["name"])  # Imprime el nombre del Pokémon
    print("ID : ", info["id"])  # Imprime el ID del Pokémon
    print("PESO: ", info["weight"])  # Imprime el peso del Pokémon
    print("ALTURA: ", info["height"])  # Imprime la altura del Pokémon

    # Imprime los tipos del Pokémon
    for tipo in info["types"]:
        print("TIPO(S) : ", tipo["type"]["name"])

    print("Juegos: ")

    # Imprime los juegos en los que aparece el Pokémon
    for juego in info["game_indices"]:
        print(juego["version"]["name"], end=" , ")

    # Realiza una solicitud HTTP GET a la API de PokeAPI para obtener la cadena de evolución del Pokémon
    evoluciones = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    # Verifica si la solicitud fue exitosa
    if evoluciones.status_code == 200:
        url = evoluciones.json()["evolution_chain"]["url"]

        evoluciones = requests.get(url)

        # Verifica si la solicitud fue exitosa
        if evoluciones.status_code == 200:
            info = evoluciones.json()

            print("\nCadena de evolución:")

            # Función recursiva para imprimir la cadena de evolución
            def get_evolves(info):
                print(info["species"]["name"], end=" , ")
                if "evolves_to" in info:
                    for evolucion in info["evolves_to"]:
                        get_evolves(evolucion)

            get_evolves(info["chain"])
        else:
            print(f"no tiene evolucion el pokemon {pokemon}")
    else:
        print(f"Error : {evoluciones.status_code} , hay problema en las evoluciones")
else:
    print(f"Error : no hay un pokemos del nombre {pokemon} o te dio el erro {pokemones.status_code}")
