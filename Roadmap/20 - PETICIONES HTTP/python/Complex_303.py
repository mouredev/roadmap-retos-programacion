"""
Peticiones HTTP
"""

"""una petición HTTP es una solicitud que un cliente (como un navegador o una app) 
envía a un servidor para pedir o enviar información a través de la web. 
Se compone de un método (como GET, POST, PUT o DELETE), una URL, y opcionalmente cabeceras y datos."""

# Importamos la librería requests, que permite hacer peticiones HTTP en Python.
import requests

# Realizamos una petición GET a la URL indicada (en este caso, el sitio de eBay)
# response = requests.get("https://www.ebay.com/")

# # Verificamos si el código de estado de la respuesta es 200 (lo que significa que la petición fue exitosa)
# if response.status_code == 200:
#     # Si la respuesta fue exitosa, imprimimos el contenido de la página (en texto HTML)
#     print(response.text)
# else:
#     # Si la respuesta no fue exitosa, mostramos un mensaje de error con el código de estado recibido
#     print(f"Error con codigo {response.status_code} al realizar la peticion")




""" * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores"""

#un endpoint es una URL específica dentro de una API o servicio web a la que se puede enviar una petición para obtener o enviar datos.

# Pedimos al usuario que escriba el nombre o número del Pokémon, lo convertimos a minúsculas para evitar errores por mayúsculas
pokemon = input("Introduce el nombre o el numero del pokemon a buscar: ").lower()



# Hacemos una petición HTTP GET a la API de Pokémon usando el nombre o número que el usuario escribió
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

# Verificamos si la respuesta fue exitosa (código 200 significa OK)
if response.status_code == 200: 
    data = response.json()     # Convertimos la respuesta de JSON a un diccionario de Python
    # Mostramos el nombre del Pokémon
    print("Nombre: ", data["name"])
    # Mostramos el ID del Pokémon
    print("ID: ", data["id"])
    # Mostramos el peso del Pokémon
    print("Peso: ", data["weight"])
    # Mostramos la altura del Pokémon
    print("Altura: ", data["height"])
      # Mostramos los tipos del Pokémon sin salto de línea al final
    print("Tipo(s): ", end="")
    # Usamos join para unir todos los nombres de tipos separados por comas
    print(", ".join(tipo["type"]["name"] for tipo in data["types"]))
        # Mostramos los juegos donde aparece el Pokémon sin salto de línea al final
    print("Juegos: ", end="")
    # Usamos join para unir todos los nombres de versiones de juegos separados por comas
    print(", ".join(tipo["version"]["name"] for tipo in data["game_indices"]))


    # Hacemos otra petición para obtener información adicional de la especie del Pokémon
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        # Obtenemos la URL de la cadena de evolución de esa especie desde el JSON
        url = response.json()["evolution_chain"]["url"]

        # Hacemos una petición a esa URL para obtener los datos de evolución
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() # Convertimos el JSON de la cadena de evolución en un diccionario
            print("Cadena de evolucion: ") # Mostramos un título para la cadena de evolución

             # Definimos una función llamada get_evolves que recibe datos y muestra las evoluciones
            def get_evolves(data):
                # Muestra el nombre de la especie actual
                print(data["species"]["name"])
                # Si existe la clave "evolves_to" (es una lista de evoluciones)
                if "evolves_to" in data:
                    # Por cada evolución en esa lista
                    for evolve in data["evolves_to"]:
                        # Llama recursivamente a sí misma para mostrar las evoluciones de esa evolución
                        get_evolves(evolve)



            # Llama a la función get_evolves con el inicio de la cadena de evolución
            get_evolves(data["chain"])

        # Si la petición de la cadena de evolución falla, muestra un error
        else:
            print(f"Error {response.status_code} obteniendo evoluciones")

    
    # Si la petición de especie falla, muestra un error
    else:
        print(f"Error {response.status_code} obteniendo evoluciones")

# Si la primera petición del Pokémon falla, muestra que no se encontró
else:
    print(f"Error: {response.status_code} pokemon no encontrado")