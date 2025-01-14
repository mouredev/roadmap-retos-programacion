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


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"{response.status_code} Error")


fetch_data()
""" prints:
{
  userId: 1,
  id: 1,
  title: 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
  body: 'quia et suscipit\n' +
    'suscipit recusandae consequuntur expedita et cum\n' +
    'reprehenderit molestiae ut ut quas totam\n' +
    'nostrum rerum est autem sunt rem eveniet architecto'
}
"""


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
"""


def get_pokemon(pokemon):
    try:
        URL = "https://pokeapi.co/api/v2/pokemon/"
        response = requests.get(f"{URL}{pokemon}")

        if response.status_code != 200:
            raise RuntimeError("Data not found.")

        data = response.json()
        return data
    except Exception as err:
        print(err)


def ask_pokemon():
    pokemon = input("Enter a Pokémon name or Id:\n> ")
    data = get_pokemon(pokemon)
    if not data:
        return

    print("\nName:", data["name"].capitalize())
    print("Pokémon Id:", data["id"])
    print("Pokémon weight:", data["weight"])
    print("Pokémon height:", data["height"])
    print("Pokémon type(s):")
    for type in data["types"]:
        print(f"  {type['slot']}.", type["type"]["name"])


ask_pokemon()
