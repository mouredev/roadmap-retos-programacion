"""
Peticiones HTTP
"""

# Es la forma como un programa puede comunicarse con servidores web
# Se usa para:
    # Interactuar con APIs
    # Descargar contenido
    # Construir aplicaciones WEB

import requests

response = requests.get('https://www.google.com/adsr4eta4rtserq32qDFA')
if response.status_code == 200:
    print(response.text)
else:
    print(f'Error con codigo: {response.status_code} al realizar la peticion.')

print('--------------')

"""
Extra
"""

pokemon = input('Introdusca el nombre o numero de Pokemon a consultar: ').lower()

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
if response.status_code == 200:
    data = response.json()
    print('Nombre: ', data['name'])
    print('ID: ', data['id'])
    print('Peso: ', data['weight'])
    print('Altura: ', data['height'])
    print('Tipos:')
    for type in data['types']:
        print(type['type']['name'])

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/')
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("Cadena de evolución:")

            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])

        else:
            print(f"Error {response.status_code} obteniendo las evoluciones.") 
    else:
        print(f"Error {response.status_code} obteniendo las evoluciones.")
else:
    print(f'Error {response.status_code}: Pokemon no encontrado.')

