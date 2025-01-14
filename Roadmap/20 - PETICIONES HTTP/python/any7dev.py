""" /*
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
 */ """

#EJERCICIO
import requests

def peticion(web):
    respuesta = requests.get(web)

    if respuesta.status_code == 200:
        print("Petición Exitosa")
        print(f"Contenido de la web:\n{respuesta.text}\n")
    else:
        print(f"Fallo al hacer la petición, código {respuesta.status_code}\n")

peticion("https://www.google.es")
peticion("https://retosdeprogramacion.com/roadmap/")
peticion("https://thepiratebay3.com/")

#DIFICULTAD EXTRA
INFO_POKEMON = "https://pokeapi.co/api/v2/pokemon/"
INFO_SPECIES = "https://pokeapi.co/api/v2/pokemon-species/"

def inicio(pokemon):
    url = INFO_POKEMON + pokemon
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos            

def datos_simples(datos):
    id = datos['id']
    peso = datos['weight']
    altura = datos['height']
    return id, peso, altura

def tipos(datos):
    tipos = datos['types']
    lista_tipos = []
    for tipo in tipos:
        lista_tipos.append(tipo['type']['name'])
    return lista_tipos

def games(datos):
    juegos = datos['game_indices']
    lista_juegos = []
    for juego in juegos:
        lista_juegos.append(juego['version']['name'])    
    return lista_juegos

def datos_evo(id):
    species = INFO_SPECIES + str(id) 
    respuesta = requests.get(species)
    datos = respuesta.json()
    evo_url = datos['evolution_chain']['url']
    respuesta = requests.get(evo_url)
    evo_json = respuesta.json()
    return evo_json

def evoluciones(evo_json, lista = []):
    lista.append(evo_json['species']['name'])
    if "evolves_to" in evo_json: 
        for evo in evo_json['evolves_to']:
            evoluciones(evo)
    return lista

def extra():
    pokemon = input("Dime el pokemon: ")
    pokemon = pokemon.lower()
    try:
        data = inicio(pokemon)
        id, peso, altura = datos_simples(data)
        juegos = games(data)
        json = datos_evo(id)
        evo = evoluciones(json['chain'])
        print(f"Pokemon: {pokemon}, id: {id}, peso: {peso}, altura: {altura}")
        print(f"Evoluciones: {evo}")
        print(f"Juegos: {juegos}")
    except requests.exceptions.JSONDecodeError:
        print("Pokemon no encontrado")       

extra()