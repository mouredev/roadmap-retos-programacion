### PETICIONES HTTP EN PYTHON

# Para realizar peticiones http en python requiere la importación del módulo requests
# Instalar previamente si no la tenemos
# pip install requests

import requests

# Realizamos una petición get:
#url = "https://www.marca.com"
#
##Almacenamos la respuesta
#response = requests.get(url=url)
#
## Si obtenemos un código de estado 200 la comunicación es correcta
#if response.status_code == 200:
#    print(f"Encabezados de la respuesta")
#    print(response.headers) # Imprimimos los encabezados de la respuesta
#    
#    print(f"La respuesta a la petición ha sido exitosa")
#    print(response.text) # Imprimimos el contenido en formato texto
#else:
#    print(f"La respuesta a la petición ha sido fallida")
#    print(response.status_code) # Imprimimos el código de estado de la respuesta


### EJERCICIO EXTRA

# Acceso a api pokemon
def get_pokemon_data(name: str = "", id: int = 0):
    
    if name:
        url= f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    
    response = requests.get(url=url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Estatus code: {response.status_code}')
        print({f'error: No se pudo obtener la información del pokemon'})
        return None

def get_pokemon_games(name: str = "", id: int = 0):
    
    if name:
        url= f"https://pokeapi.co/api/v2/version/{name.lower()}"
    else:
        url = f"https://pokeapi.co/api/v2/version/{id}"
    
    response = requests.get(url=url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Estatus code: {response.status_code}')
        print({f'error: No se pudo obtener la información del pokemon'})
        return None


def get_pokemon_evolution_chain(name: str = "", id: int = 0):
    
    if name:
        url= f"https://pokeapi.co/api/v2/evolution-chain/{name.lower()}"
    else:
        url = f"https://pokeapi.co/api/v2/evolution-chain/{id}"
    
    response = requests.get(url=url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Estatus code: {response.status_code}')
        print({f'error: No se pudo obtener la información del pokemon'})
        return None

name = ""
id = 0

print("Obtener datos de Pokemon: ")
option = input("Indica el dato para buscar (n: nombre, i: id): ")
while option[0].lower() not in ['n', 'i']:
    print("Error: Debes indicar una de las dos opciones.")
    option = input("Indica el dato para buscar (n: nombre, i: id)")

if option[0].lower() == 'n':
    name = input("Indica el nombre del Pokemon: ")
else:
    id = int(input("Indica el id del Pokemon: "))

data = get_pokemon_data(name=name, id=id)
games = get_pokemon_games(name=name, id=id)
evolution = get_pokemon_evolution_chain(name=name, id=id)

if data:
    print(f"Nombre: {data['name']}")
    print(f"Id: {data['id']}")
    print(f"Altura: {data['height']}" )
    print(f"Peso: {data['weight']}" )
    print("Tipos:")
    for type in data['types']:
        print(f"{type['type']['name']}" )
else:
    print("No hay información para mostrar...")

if evolution:
    print("Evolución:")
    print(evolution['chain']['species']['name'])

if games:
    print("Versiones:")
    for game in games['names']:
        if game['language']['name'] == 'es':
            print(f"{game['name']}")
else:
    print("No hay información para mostrar acerca de las versiones de juegos de este pokemon...")
    
    

### FIN EJERCICIO EXTRA

### FIN PETICIONES HTTP EN PYTHON


