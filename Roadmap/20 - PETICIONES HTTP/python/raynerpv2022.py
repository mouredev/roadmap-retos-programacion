# /*
#  * EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores
#  */

import requests


def execrcice(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
         
        print("Error Conexion Lost Code :", e)
        
    else :
        print("Conexion Succesfully, Code :", response.status_code)
        print("Data")
        print()    
        print(response.text)
    
def extra():
    value = input("Numero o Nombredel  pOkEmOn:")
    url = f"https://pokeapi.co/api/v2/pokemon/{value}"
   
    poke = get_Poke_url(url)
    if not poke :
         return

    print(f' Nombre {poke["name"]}' )
    print(f' ID {poke["id"]}' )
    print(f' Weight {poke["weight"]}' )
    print(f' Height {poke["height"]}' )
    print("Tipos ")
    for  t in poke["types"] :
        print(f"\tNOmbre: {t['type']['name']} URL: {t['type']['url']}")
        print()
        
    print("GAmes  ")
    for g in poke["game_indices"]:
        print(f" \t {g['version']['name']} *** url: {g['version']['url']}")


    specie_url = f"https://pokeapi.co/api/v2/pokemon-species/{value}"
    specie_json = get_Poke_url(specie_url)
    if not specie_json:
         return
    
    evolution_chain_json = get_Poke_url(specie_json["evolution_chain"]["url"])
    if not evolution_chain_json:
         return
     
    print("EVOLUTION CHAIN")
    get_evolution(evolution_chain_json["chain"])

def get_evolution(evolution):
         
        if "evolves_to" in evolution:
                        for i in evolution["evolves_to"]:            
                            
                            get_evolution(i)
                        print(f'\t  {evolution["species"]["name"]}')

def get_Poke_url(url):
     response = requests.get(url)
     status_code = response.status_code
     if  status_code >= 300 or status_code < 200:
        print(f"Pokemon No encontrado, Error : {status_code}")
        return False
     return response.json()
     


# execrcice("https://mouredev.pro/")
extra()
