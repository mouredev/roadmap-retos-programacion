import requests
from colorama import Fore

query = requests.get('https://comandos-de-linux.reflex.run/')

statusCode = query.status_code

if statusCode == 200:
    print(Fore.GREEN + "[+] Petición exitosa" + Fore.RESET)
    print(query.content.decode('utf-8'))
else:
    print(Fore.RED + "[-] Algo salió mal!" + Fore.RESET)

'''
EXTRA
'''
baseURL = "https://pokeapi.co/api/v2/pokemon"
def getDataPokemon(name):
    url = baseURL + "/" + name
    try:
        query = requests.get(url)
        query.raise_for_status()
        data = query.json()

        print(f"Name: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Weight: {data['weight']}")
        print(f"Height: {data['height']}")
        print(f"Types: {''.join([i['type']['name'] for i in data['types']])}")
        print(f"Games: {[game['version']['name'] for game in data['game_indices']]}")


    except requests.exceptions.HTTPError as e:
        if query.status_code == 404:
            print(Fore.RED + f"[-] Error 404: Pokemon '{name}' Not found" + Fore.RESET)

name = input("Nombre de pokemon: ")
getDataPokemon(name)
