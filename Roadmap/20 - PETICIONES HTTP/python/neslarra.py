"""
 EJERCICIO:
 Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 una petición a la web que tú quieras, verifica que dicha petición
 fue exitosa y muestra por consola el contenido de la web.

 DIFICULTAD EXTRA (opcional):
 Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 terminal al que le puedas solicitar información de un Pokémon concreto
 utilizando su nombre o número.
 - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 - Muestra el nombre de su cadena de evoluciones
 - Muestra los juegos en los que aparece
 - Controla posibles errores
"""
import requests


print(f"##  Explicación  {'#' * 30}\n")
print(r"""
El módulo "requests" permite hacer envío y recepción de solicitudes HTML a través de métodos GET, POST, PUT y DELETE.
Para el caso, vamos a usat "get" para consumir una API que nos entregará una cantidad "c" de palabras en español (útil,
por ejemplo, para hacer una partida de "ahoracado" -o adivina la palabra-).

Es importante conocer qué estaría devolviendo la API para poder explotarla correctamente (viendo la doc específica o
usando herramientas como "postman" o, si no, yendo a la "url" y ver qué trae).

import requests

response = requests.get(url="https://clientes.api.greenborn.com.ar/public-random-word", params={"c": 10}, timeout=5)
status = response.status_code
if status == 200:
    palabras = response.json()
    print(f"Palabras para usar: {palabras}")
else:
    print(f"Error HTTP: {status}")
""")
response = requests.get(url="https://clientes.api.greenborn.com.ar/public-random-word", params={"c": 10}, timeout=5)
status = response.status_code
if status == 200:
    palabras = response.json()
    print(f"Palabras para usar: {palabras}", end="\n\n")
else:
    print(f"Error HTTP: {status}", end="\n\n")

print(f"##  Dificultad extra  {'#' * 30}")

URL_BASE = "https://pokeapi.co/api/v2/"


def query_api(url: str, params=None) -> dict:
    data = dict()
    try:
        req = requests.get(url, params, timeout=2)
        if req.status_code == 200:
            data = req.json()
        else:
            print(f"{url} devolvió RC={req.status_code}")
    except requests.exceptions.Timeout:
        print(f"{url} NO respondió a tiempo. Intente más tarde.")
    return data


def get_pokemon_id(name: str, count: int) -> str:
    def get_id(url: str) -> str:
        fields = url[:-1].split("/")
        return fields.pop()

    data = query_api(URL_BASE + "pokemon/", {"offset": 0, "limit": str(count)})

    for pokemones in data.items():
        if pokemones[0] == "results":
            for p in pokemones[1]:
                if p['name'].lower() == name.lower():
                    return get_id(p['url'])
    return ""


def get_pokemon_data(pok_id: str) -> tuple:
    def pokemon_evol_chain(pok_id: str) -> list:
        evolves_chain = []
        data = query_api(URL_BASE + "pokemon-species/" + pok_id + "/")
        try:
            evolves_to_url = data["evolution_chain"]["url"]
            evol_to_data = query_api(evolves_to_url)
            evolves_chain.append(evol_to_data["chain"]["species"]["name"])
            evolves_chain.append(evol_to_data["chain"]["evolves_to"][0]["species"]["name"])
            evolves_chain.append(evol_to_data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"])
        except Exception:
            pass
        finally:
            return evolves_chain

    games = []
    data = query_api(URL_BASE + "pokemon/" + pok_id + "/")
    type_ = data["types"][0]["type"]["name"]
    height = data["height"]
    weight = data["weight"]
    for game in data["game_indices"]:
        games.append(game["version"]["name"])
    form_url = data["forms"][0]["url"]
    form_data = query_api(form_url)
    image_url = form_data["sprites"]["front_default"]
    evolves_chain = pokemon_evol_chain(pok_id)
    return type_, height, weight, games, image_url, evolves_chain


def show_profile(name, id_, data):
    print(f"""
    Pokemon name: {name}  (id: {id_})
    Type: {data[0]}
    Height: {data[1]}
    Weight: {data[2]}
    Games:
""", end="")
    for g in data[3]:
        print(f"\t\t{g}")
    print(f"\tEvolution chain:")
    for ec in data[5]:
        print(f"\t\t{ec}")
    print(f"\tImage: {data[4]}")


def main():
    pokemon = ""
    pokemon_count = 0
    data = query_api(URL_BASE + "pokemon/", {"offset": 0, "limit": 1})
    if data:
        pokemon = "_"
        pokemon_count = data["count"]
    while pokemon:
        pokemon = input("\nEnter pokemon name (empty to exit): ")
        pokemon_id = get_pokemon_id(pokemon, pokemon_count)
        if pokemon_id:
            pokemon_data = get_pokemon_data(pokemon_id)
            show_profile(pokemon, pokemon_id, pokemon_data)


if __name__ == "__main__":
    main()
