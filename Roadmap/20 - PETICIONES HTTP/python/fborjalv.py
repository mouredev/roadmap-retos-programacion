
"""
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""


import requests

response = requests.get("https://www.elmundo.es")

if response.status_code == 200: 
    print("Respuesta correcta")
else:
    print(f"Se ha producido un error: {response.status_code}")

#print(response.text)


"""
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

pokemon = input("¿Qué pokemon deseas consultar? ").lower()


response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200: 
    data = response.json()
    print(f'Nombre: {data["name"]}')
    print(f'ID: {data["id"]}')
    print(f'Altura: {data["height"]}')
    print(f'Peso: {data["weight"]}')
    print(f'Tipo/s: {", ".join([type["type"]["name"] for type in data["types"]])}')
    print(f"Juegos en los que aparece: {', '.join([game['version']['name'] for game in data['game_indices']])}")
    print(f'Evoluciones: ')
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        data = response.json()
        response = requests.get(data["evolution_chain"]["url"])
        if response.status_code == 200: 
            data = response.json()
            
            def get_evolutions(data):
                if "evolves_to" in data:
                    for item in data["evolves_to"]:
                        print((item["species"]["name"]))
                        get_evolutions(item)
                        
            get_evolutions(data["chain"])
        else: 
            print(f"Error: {response.status_code}. ")
    else: 
        print(f"Error: {response.status_code}. ")

else:
    print(f"Error 404: el pokemon {pokemon} no existe")