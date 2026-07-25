"""* EJERCICIO:
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
 * - Controla posibles errores"""
import requests

url = 'https://pokeapi.co'

respuesta = requests.get(url)
if respuesta.status_code==200:
    print(respuesta.text)
elif respuesta.status_code == 404:
    print("La petición no es válida")
elif respuesta.status_code == 500:
    print("Error interno del servidor")

# EXTRA
while True:    
    nombre_pokemon = input("Introduce el nombre o el número del Pokémon, S/s para salir: ")
    if nombre_pokemon == 'S' or nombre_pokemon == 's':
        break
    else:
        # Datos generales del Pokémon
        url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
        respuesta = requests.get(url_pokemon)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            print(f'Id->{datos['id']}, Nombre-> {datos['name']}, peso-> {datos['weight']}, altura-> {datos['height']}')
            print('Tipo(s):')
            for type in datos['types']:
                print(f'Tipo-> {type["type"]["name"]}')  
                
            # Cadena de evoluciones
            url_evoluciones = f'https://pokeapi.co/api/v2/pokemon-species/{nombre_pokemon}'
            respuesta = requests.get(url_evoluciones)
            if respuesta.status_code == 200:
                url = respuesta.json()['evolution_chain']['url']
                respuesta = requests.get(url)
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    print('EVOLUCIÓN DEL POKEMON')                                        
                    
                    def evolucion(datos):                       
                        print(datos['species']['name'])
                        if 'evolves_to' in datos:
                            for  evo in datos['evolves_to']:
                                evolucion(evo)
                                                            
                    evolucion(datos['chain'])
                
                elif respuesta.status_code == 400:
                    print("El nombre o el número del Pokémon no es válido")
                elif respuesta.status_code == 500:
                    print("Error interno del servidor")
                    
                # Juegos
                respuesta = requests.get(url_pokemon)
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    print('JUEGOS: ')
                    for juego in datos['game_indices']:
                        print(f'Número-> {juego['game_index']} - versión-> {juego["version"]["name"]} - URL-> {juego["version"]["url"]}')
                elif respuesta.status_code == 400:
                    print("El nombre o el número del Pokémon no es válido")
                elif respuesta.status_code == 500:
                    print("Error interno del servidor")
                    
            elif respuesta.status_code == 400:
                print("El nombre o el número del Pokémon no es válido")
            elif respuesta.status_code == 500:
                print("Error interno del servidor")
                
        elif respuesta.status_code == 400:
            print("El nombre o el número del Pokémon no es válido")
        elif respuesta.status_code == 500:
            print("Error interno del servidor")