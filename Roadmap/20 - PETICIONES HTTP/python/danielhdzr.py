# #20 PETICIONES HTTP
#### Dificultad: Difícil | Publicación: 13/05/24 | Corrección: 20/05/24

## Ejercicio

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
'''
import requests

'''
response = requests.get(("https://google.com"))
if response.status_code == 200:
    print(response.text)
    print("*****Se ha imprimido el codigo fuente de la pagina*****")
else:
    print(f"Error: {response.status_code}")
'''
    
# Extra

pokemon = input("Introduce el nombre o numero del pokemon: ").lower()
# Peticion al sitio web, a la seccion del pokemon elegido
pokedata = requests.get((f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"))
# Si la conexion es exitosa
if pokedata.status_code == 200:
    # Guardo los datos json de la web
    datos = pokedata.json()
    # Extraigo datos de los children correspondientes
    print("Nombre: ", datos["name"])
    print("Id: ", datos["id"])
    print("Peso: ", datos["weight"])
    print("Altura: ", datos["height"])
    # Para pokemon con mas de un tipo
    contador_de_tipos = 1
    for type in datos["types"]: # types guarda los tipos como un dict 
        # donde la key "type" guarda el value que es el "name" del tipo de pokemon
        print(f"Tipo({contador_de_tipos}): ", type["type"]["name"])
        contador_de_tipos += 1
    # Imprime los juegos
    print("Juegos:")
    # Itera dentro de la etiqueta y extrae lo encontrado
    for game in datos["game_indices"]:
        print(game["version"] ["name"])

        '''
        En busca de la cadena de evoluciones del pokemon
        '''
    # Peticion al sitio web del pokemon de nuevo, en el apartado de species
    cadena_evoluciones = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    # Si conexion exitosa
    if cadena_evoluciones.status_code == 200:
    # Guardo el json, accedo al child "evolucion_chain", y a su grandchild "url"
    # Asi obtengo la url de cada pokemon donde se guarda su cadena evolutiva
        url = cadena_evoluciones.json()["evolution_chain"]["url"]
        # Peticion al url que tiene la cadena evolutiva
        response = requests.get(url)

        if response.status_code == 200:
            # Guardo el json de la url de la cadena de evoluciones
            datos = response.json()
        # Funcion recursiva para obtener las evoluciones si las hubiera
            def get_evolves(datos): # datos guarda el json
                print(f"especie y nombre: {datos["species"]["name"]}") # acceder al child y su sub-child
                # etiqueta "evolves_to" contiene la evolcion en el json
                if "evolves_to" in datos:
                    '''
                    Si encuentra "evolves_to" llama a la funcion de nuevo
                    y trae las evoluciones encontradas dentro de cada evolucion
                    '''
                    for evolve in datos["evolves_to"]:
                        get_evolves(evolve)
            # Llamado a la funcion. Parametro es la etiqueta "chain"
            get_evolves(datos["chain"])

        else:
            print(f"Error {response.status_code}: Error con response")

    else:
        print(f"Error {cadena_evoluciones.status_code}: Error obteniendo cadena evolutiva")

else:
    print(f"Error {pokedata.status_code}: Pokemon no encontrado")