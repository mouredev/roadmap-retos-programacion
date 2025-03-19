import requests, os
os.system('cls')

""" * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
"""

try:
    response = requests.get('https://retosdeprogramacion.com', timeout=1.00) 
    #Con la función get de response obtenemos la respuesta de la web que le pasemos por parámetro, también le podemos pasar
        # otros parámetros como en este caso un límite de tiempo de espera en este caso de 1 segundo.
    print(response.text) #Despues con el método text convertimos esa respuesta en el código html de la web.
    print(response.status_code) #Con el método status_code obtenemos el código de estado de la respuesta.
except requests.exceptions.RequestException: #Excepción genérica para cualquier fallo en la obtención de la respuesta
    print("No se ha podido obtener la información")
except ConnectionError: #Excepción de comunicación con el servidor remoto.
    print("Error de conexión")
except TimeoutError: #Excepción concreta de agotamiento del tiempo de espera especificado.
    print("Se ha agotado el tiempo de espera")

""" 
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores"""

def find():
    pokemon_name = input("Escriba el nombre o número del pokemon a buscar: ")
    try:
        pokedata = get_data('https://pokeapi.co/api/v2/pokemon/'+ pokemon_name)
    except requests.RequestException as ex:
        print ("URL no encontrada:  ",ex)
    except Exception as name:
        print("No se ha introducido ningún parámetro",name)
    else:
        pokemon_types = [types['type']['name'] for types in pokedata['types']]
        pokemon_games = [game_indices['version']['name'] for game_indices in pokedata['game_indices']]
        
        print('Nombre: ',pokedata['name'].capitalize())
        print('ID:     ',pokedata['id'])
        print('Peso:   ',pokedata['weight']/10, 'Kgs')
        print('Altura: ',pokedata['height']/10, 'm')
        print('Tipo/s:  ',', '.join(pokemon_types).title())
        print('Juegos: ',', '.join(pokemon_games).title())
        get_evolve('https://pokeapi.co/api/v2/evolution-chain/'+ str(pokedata['id']))

def get_data(url:str) ->dict:
    pokemon_data = {
    'name': '',
    'id':'',
    'weight':'',
    'height':'',
    'types':'',
    'game_indices':'' 
    }
  
    response = requests.get(url)
    data = response.json()
    
    pokemon_data['name'] = data['name']
    pokemon_data['id'] = data['id']
    pokemon_data['weight'] = data['weight']
    pokemon_data['height'] = data['height']
    pokemon_data['types'] = data['types']
    pokemon_data['game_indices'] = data['game_indices']
    return pokemon_data

def get_evolve(url:str):

    response = requests.get(url)
    data = response.json()['chain'] #diccionario principal
    evolve = data['evolves_to'] #lista de diccionarios que almacenan las evoluciones

    if (len(evolve) < 1):
        return
    else: 
        print("Evoluciones: ",end=' ')
        for i in range (len(evolve)):
            evo1:str = evolve[i]['species']['name']
            print('\b',evo1.capitalize(), end=', ')

    if (len(evolve[0]['evolves_to']) < 1) :
        return
    else:
        for j in range (len(evolve[0]['evolves_to'])):
            evo2:str = evolve[0]['evolves_to'][j]['species']['name']
            print('\b',evo2.capitalize(), end=' ')
print()
find()




