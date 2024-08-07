"""
    Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
    una petición a la web que tú quieras, verifica que dicha petición
    fue exitosa y muestra por consola el contenido de la web.
"""
import requests
from bs4 import BeautifulSoup

# url = "https://espndeportes.espn.com/"
url = "https://www.google.com"
response = requests.get(url)

if response.status_code == 200:
    print("Petición Exitosa")
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
else:
    print(f"La petición falló codigo: {response.status_code}")

"""
    DIFICULTAD EXTRA (opcional):
    Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
    terminal al que le puedas solicitar información de un Pokémon concreto
    utilizando su nombre o número.
        - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
        - Muestra el nombre de su cadena de evoluciones
        - Muestra los juegos en los que aparece
        - Controla posibles errores
"""


def get_poke_info(poke_id):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_id}")
        response.raise_for_status()
        data = response.json()
        name = data["name"].capitalize()
        pokemon_id = data["id"]
        weight = data["weight"] / 10
        height = data["height"] / 10
        types = [t["type"]["name"].capitalize() for t in data["types"]]
        evolution_url = f"https://pokeapi.co/api/v2/pokemon-species/{poke_id}/"
        appearances1 = [entry["version"]["name"]
                        for entry in data["game_indices"]]

        """ evolution_response = requests.get(evolution_url)
        evolution_response.raise_for_status()
        evolution_data = evolution_response.json()#["evolution_chain"]["url"]
            
        if "evolution_chain" in evolution_data and evolution_data["evolution_chain"]:

            evolution = [pokemon["species"]["name"].capitalize()
                        for pokemon in evolution_data["evolves_to"]]
        else:
            evolution = [name]"""
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{poke_id}/")
        if response.status_code == 200:
            url = response.json()["evolution_chain"]["url"]
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                def get_evolves(data):
                    stack = [data]
                    stack1 = []
                    while stack:
                        current = stack.pop()
                        if "evolves_to" in current:
                            for evolve in current["evolves_to"]:
                                stack.append(evolve)
                                stack1.append(evolve)
                    return stack1
                evolution = get_evolves(data["chain"])
            else:
                print(
                    f"Error {response.status_code} obteniendo las evoluciones.")
        else:
            print(f"Error {response.status_code} obteniendo las evoluciones.")

        print(f"""  
    Nombre: {name}
    ID: {pokemon_id}
    Peso: {weight} kg
    Altura: {height} m
    Tipo(s): {', '.join(types)}
    Aparece en los juegos: {', '.join(appearances1)}
    """)
        print("Cadena de evolución:", end="")
        while evolution:
            c = evolution.pop()
            if isinstance(c, str):
                print(c, end=", ")
            else:
                print(c["species"]["name"], end=", ")

    except requests.exceptions.RequestException as error:
        print(f"Error en la petición: {error}")
    except ValueError:
        print("Nombre o Id del pokemon invalido")
    except Exception as error:
        print(f"Error inesperado: {error}")


name_id = input("Ingresa el nombre o número del pokémon: ").lower()

get_poke_info(name_id)
