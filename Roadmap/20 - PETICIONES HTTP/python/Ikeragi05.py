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

base_url ="https://pokeapi.co/api/v2"
pokemon= input("¿Que Pokemon quieres consultar?\n").lower()


request= requests.get(f"{base_url}/pokemon/{pokemon}")


def obtener_cadena_evoluciones(pokemon):
    global base_url
    request= requests.get(f"{base_url}/pokemon-species/{pokemon}")

    if request.status_code==200:
        data= request.json()
        cadena_url= data['evolution_chain']['url']
        request_evolution= requests.get(cadena_url)

    if request_evolution.status_code==200:
        data_chain= request_evolution.json()
        cadena_evoluciones = []
        chain = data_chain['chain']
        while chain:
            cadena_evoluciones.append(chain['species']['name'])
            if chain['evolves_to']:
                chain = chain['evolves_to'][0]
            else:
                break

        return cadena_evoluciones
if request.status_code==200:
    tipos=[]
    evoluciones=obtener_cadena_evoluciones(pokemon)
    juegos=[]
    data=request.json()
    print(f"Nombre: {data['forms'][0]['name']}")
    print(f"ID: {data['id']}")
    print(f"Peso: {data['weight']}")
    print(f"Altura: {data['height']}")
    for tipo in data['types']:
        tipos.append(tipo['type']['name'])
    print(f"Tipos: {tipos}")
    print(f"Cadena de evoluciones: {evoluciones}")
    for juego in data['game_indices']:
        juegos.append(juego['version']['name'])
    print(f"Juegos en los que aparece: {juegos}")
elif request.status_code==404:
   print("Pokemon no encontrado")
else:
    print("Algo salió mal")


