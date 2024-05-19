# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * PETICIONES HTTP
# -----------------------------------
# Mas info: https://www.datacamp.com/es/tutorial/making-http-requests-in-python

# pip install requests
# https://requests.readthedocs.io/en/latest/

import requests
import textwrap

"""
* EJERCICIO #1:
* Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
* una petición a la web que tú quieras, verifica que dicha petición
* fue exitosa y muestra por consola el contenido de la web.
"""

def get_user(user_id: int) -> dict:
    try:
        url = "https://jsonplaceholder.typicode.com/users/{userId}"
        response = requests.get(url.format(userId=user_id))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Id: {user_id} No encontrado")
            print("status_code: ", response.status_code)
            return {}

    except requests.ConnectionError as error:
        #print(error)
        print("error_de conexión")
        return {}

def print_user(user_data: dict):
    if user_data:
        print(textwrap.dedent(f"""\
        Usuario con id: '{user_data['id']}':
        Nombre:  {user_data['name']}
        Usuario:" {user_data['username']}
        Email:, {user_data['email']}
        Teléfono: {user_data['phone']}
        \
        """))

print("\nEJERCICIO #1:\n")
u1 = get_user(1)
print_user(u1)

u2 = get_user(2)
print_user(u2)

u3 = get_user(777) # xD-error
print_user(u3)
 
"""
* EJERCICIO #2:
* Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar información de un Pokémon concreto
* utilizando su nombre o número.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
"""

class GetPokemon:
    def __init__(self, id: str | int):
        base_url = "https://pokeapi.co/api/v2/pokemon/{id_or_name}"
        url = base_url.format(id_or_name = id)
        response = requests.get(url)
        self._pokemon: dict = response.json()
        print(f"\nPokémon '{id}' ha sido cargado.")
       
    def info(self):
        print(textwrap.dedent(f"""\
        Información Básica
        * Id:      {self._pokemon["id"]}
        * Nombre:  {self._pokemon["name"]}
        * Peso:    {self._pokemon["weight"]} kg
        * Altura:  {self._pokemon["height"]} m
        * Tipo(s):\
        """))
        for t in self._pokemon.get("types", []):
            type_name = t.get("type", {}).get("name", "")
            print(f"{' ' * 9}- {type_name}")
    
    def evolution_chain(self):
        species_url = self._pokemon['species']['url']
        species_data = requests.get(species_url).json()
        evolution_chain_url = species_data['evolution_chain']['url']

        evolution_chain_data = requests.get(evolution_chain_url).json()
        current_evolution = evolution_chain_data['chain']

        if "species" in current_evolution:
            print("\nCadena de evoluciones:")
            print("-", current_evolution["species"]["name"])
            while current_evolution.get("evolves_to"):
                current_evolution = current_evolution["evolves_to"][0]
                print("- ", current_evolution["species"]["name"])
        else:
            print("Este Pokémon no tiene cadena de evolución.")

    def show__games(self):
        print("\nJuegos en los que aparece:")
        if self._pokemon['game_indices']:
            for game_info in self._pokemon['game_indices']:
                print("-", game_info['version']['name'])
        else:
            print("No aparece en ninguno.")

    @staticmethod
    def handle_exceptions(e: Exception):
        if isinstance(e, requests.exceptions.ConnectionError):
            print("Error de conexión:", e)
        elif isinstance(e, requests.exceptions.Timeout):
            print("Tiempo de espera agotado:", e)
        elif isinstance(e, requests.exceptions.RequestException):
            print("Error durante la solicitud:", e)
        else:
            print("Error inesperado:", e)

print("\nEJERCICIO #2:\n")

try:
    p1 = GetPokemon(1)
    p1.info()
    p1.evolution_chain()
    p1.show__games()

    p2 = GetPokemon("ivysaur")
    p2.info()
    p2.evolution_chain()
    p2.show__games()

except Exception as e:
    GetPokemon.handle_exceptions(e)

