'''
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
'''

'''
Ejercicio
'''

import requests

# # Peticion
# response = requests.get("https://moure.dev/asdasdas")
# # Check
# if response.status_code == 200: ## Estado
#     print(response.text) ## Contenido
# else:
#     print(f"Error con código {response.status_code} al realizar la petición.")

'''
Extra
'''

input_pokemon = input("Introduce el nombre o número del Pokémon: ").lower()
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{input_pokemon}")
if response.status_code == 200:
    # print(response.text)
    data = response.json()
    print(f"Nombre: {data['name'].capitalize()}") ## Nombre
    print(f"ID: {data['id']}") ## ID
    print(f"Peso: {data['weight']} [hg]") ## Peso
    print(f"Altura: {data['height']} [dm]") ## Altura
    tipos = []
    for tipo in data['types']:
        tipos.append(tipo['type']['name'])
    print(f"Tipo(s): {', '.join(tipos)}") ## Tipo(s)

    ## Cadenas de evolución
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{input_pokemon}"
    )
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            evolutions = []
            def get_evolves(data):
                evolutions.append(data["species"]["name"].capitalize())
                # print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)
        
            get_evolves(data["chain"])
            print(f"Cadena de evolución: {' -> '.join(evolutions)}")
        else:
            print(f"Error {response.status_code}: evoluciones no encontrada.")    
    else:
        print(f"Error {response.status_code}: evoluciones no encontrada.")
    
    ## Juegos
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{input_pokemon}"
    )
    if response.status_code == 200:
        data = response.json()
        games = []
        for game in data["game_indices"]:
            games.append(game["version"]["name"].capitalize())
        print(f"Juegos: {', '.join(games)}")
    else:
        print(f"Error {response.status_code}: juegos no encontrados.")
else:
    print(f"Error {response.status_code}: Pokémon no encontrado.")





