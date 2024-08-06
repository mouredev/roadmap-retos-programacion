import requests
import sys

#  EJERCICIO:
#  Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  una petición a la web que tú quieras, verifica que dicha petición
#  fue exitosa y muestra por consola el contenido de la web.

def exercise() -> str:
    url = "https://retosdeprogramacion.com/"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error {response.status_code} al conectar con la API"
    return response.text
        

#  DIFICULTAD EXTRA (opcional):
#  Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  terminal al que le puedas solicitar información de un Pokémon concreto
#  utilizando su nombre o número.
#  - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  - Muestra el nombre de su cadena de evoluciones
#  - Muestra los juegos en los que aparece
#  - Controla posibles errores



def api_response(pokemon: str) -> dict:
    
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
      
    if response.status_code == 200:
        return response.json()
    else:
        if response.status_code == 404:
            return None
        else:
            print(f"Error {response.status_code} al conectar con la API")
            sys.exit()

def filtering_data(pokemon_dict: dict) -> dict:
    data = pokemon_dict
    leaked_pokemon_dict = {
        "name": data["name"].capitalize(),
        "id": data["id"],
        "weight": data["weight"] / 10,
        "height": data["height"] / 10,
        "types": {t["type"]["name"].capitalize() for t in data["types"]},
        "games": [g["version"]["name"].capitalize() for g in data["game_indices"]]
        }
    
    return leaked_pokemon_dict
        
def get_evolution_chain(pokemon_id: int) -> dict:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}")
    if response.status_code != 200:
        return f"Error {response.status_code} al conectar con la API"
    else:
        evolution_url = response.json()["evolution_chain"]["url"]
        response = requests.get(evolution_url)
        if response.status_code != 200:
            return f"Error {response.status_code} al conectar con la API"
        else:
            data = response.json()["chain"]
            leaked_chain = []

            def get_evolves(data):
                leaked_chain.append(data["species"]["name"].capitalize())
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)
            get_evolves(data)
            return leaked_chain
            
def read_user_pokemon() -> str:
    return input("Ingresa el nombre o número del pokémon: ").lower()

if __name__=='__main__':
    print(exercise(), "\n\n\n\n")
    while True:
        pokemon = read_user_pokemon()
        api = api_response(pokemon)
        
        if api is not None:
            data = filtering_data(api)
            evolutions = get_evolution_chain(data["id"])

            print(
                f"\nNombre: {data['name']}\n"
                f"ID: {data['id']}\n"
                f"Peso: {data['weight']} kg\n"
                f"Altura: {data['height']} m\n"
            )

            print("Tipo(s):")
            for type in data["types"]:
                print(type)
            
            print("\nCadena de Evolución:")
            for evolution in evolutions:
                print(evolution)

            print("\nJuegos en los que aparece:")
            for game in data["games"]:
                print(game)
            break
        else:
            print("\nPokémon no encontrado, por favor ingresa un nombre o id válido.\n")