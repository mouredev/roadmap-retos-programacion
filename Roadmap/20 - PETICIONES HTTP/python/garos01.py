import requests


def obtener_contenido_web(url):
    # Realizar la solicitud HTTP
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Mostrar el contenido de la web por consola
        print(respuesta.text)
    else:
        print("La solicitud no fue exitosa. Código de estado:", respuesta.status_code)


# URL de ejemplo
url_ejemplo = "https://www.ejemplo.com"

# Llamar a la función con la URL deseada
obtener_contenido_web(url_ejemplo)


# Ejercicio extra


def obtener_informacion_pokemon(pokemon):
    try:
        # Realizar la solicitud a la PokéAPI
        respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")
        respuesta.raise_for_status()  # Levanta una excepción si la solicitud no fue exitosa
        datos = respuesta.json()

        # Obtener y mostrar la información básica del Pokémon
        nombre = datos["name"]
        id_pokemon = datos["id"]
        peso = datos["weight"]
        altura = datos["height"]
        tipos = [tipo["type"]["name"] for tipo in datos["types"]]

        print(f"Nombre: {nombre.capitalize()}")
        print(f"ID: {id_pokemon}")
        print(f"Peso: {peso}")
        print(f"Altura: {altura}")
        print(f"Tipo(s): {', '.join(tipos)}")

        # Obtener la URL de la especie del Pokémon para más detalles
        url_especie = datos["species"]["url"]
        respuesta_especie = requests.get(url_especie)
        respuesta_especie.raise_for_status()
        datos_especie = respuesta_especie.json()

        # Obtener y mostrar la cadena de evoluciones
        url_evoluciones = datos_especie["evolution_chain"]["url"]
        respuesta_evoluciones = requests.get(url_evoluciones)
        respuesta_evoluciones.raise_for_status()
        datos_evoluciones = respuesta_evoluciones.json()

        cadena_evoluciones = []
        actual = datos_evoluciones["chain"]
        while actual:
            cadena_evoluciones.append(actual["species"]["name"].capitalize())
            actual = actual["evolves_to"][0] if actual["evolves_to"] else None

        print(f"Cadena de Evoluciones: {', '.join(cadena_evoluciones)}")

        # Obtener y mostrar los juegos en los que aparece
        juegos = [
            juego["version"]["name"].capitalize() for juego in datos["game_indices"]
        ]
        print(f"Juegos: {', '.join(juegos)}")

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print(f"El Pokémon '{pokemon}' no se encontró.")
        else:
            print(f"Error en la solicitud: {err}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    pokemon = input("Introduce el nombre o número del Pokémon: ")
    obtener_informacion_pokemon(pokemon)
