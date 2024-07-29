"""
20 - PETICIONES HTTP

Autor de la solución: Oriaj3

Teoría:
Las peticiones HTTP son solicitudes que se envían a un servidor web para obtener
o enviar información. En Python, el módulo requests proporciona una forma sencilla
de realizar peticiones HTTP a través de una API fácil de usar.

Existen distintos tipos de peticiones HTTP:
- GET: se utiliza para obtener información del servidor.
- POST: se utiliza para enviar información al servidor.
- PUT: se utiliza para actualizar información en el servidor.   
- DELETE: se utiliza para eliminar información del servidor.
- PATCH: se utiliza para modificar información en el servidor.
- HEAD: se utiliza para obtener la cabecera de una respuesta.
- OPTIONS: se utiliza para obtener información sobre los métodos HTTP permitidos.
- TRACE: se utiliza para realizar un seguimiento de la ruta de una petición.
- CONNECT: se utiliza para convertir la conexión en un túnel TCP/IP.

"""

"""
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""
import requests 

#path url rickyandmorty
url = "https://rickandmortyapi.com/api/character"

response = requests.get(url)
if response.status_code == 200:
    #Muestra solo los nonmbres de los personajes
    data = response.json()
    for character in data["results"]:
        print(character["name"])
elif response.status_code == 404:
    print("Error 404: Página no encontrada")


"""
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
print("\n\n*****EXTRA POKEMON*****")
def pokedex(data):
    #Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["height"])
    print("Tipo(s): ")
    for type in data["types"]:
        print(type["type"]["name"])
    print("Juegos:")
    for game in data["game_indices"]:
        print(game["version"]["name"])
    
    
def evoluciones(data):
    #Muestra el nombre de su cadena de evoluciones
    #Para esto se hace otra petición a la API de pokemon-species
    #para obtener la url de la cadena de evolución
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
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
    
pokemon = input("Introduce el nombre o el número del pokemon a mostrar: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

if response.status_code == 200:
    data = response.json()
    pokedex(data)
    evoluciones(data)
else:
    print(f"Error {response.status_code}: Pokémon no encontrado")
    
    





