import requests

# ------ Ejercicio

URL: str = r"http://worldtimeapi.org/api/timezone/America/Bogota"

status = requests.request("GET", URL)

if status.status_code == 200:
    data = status.json()
    time = data["datetime"].split('T')[1].split('.')[0]
    decorator: str = '-' * 72
    print(f"{decorator}\nResponse [{status.status_code}] OK\nHiciste una petición a 'World Time Api' a las {time}, hora Colombiana.\n{decorator}\n")

else:
    print(f"Error, Response [{status.status_code}]")
    

# ------ Extra

POKEMON_INFO_BASE_URL: str = r"https://pokeapi.co/api/v2/pokemon/"
POKEMON: str = input("* Ingrese el nombre o id del Pokemon: ").lower()
URL_POKEMON_INFO_API: str = POKEMON_INFO_BASE_URL + POKEMON + '/'

status = requests.request("GET", URL_POKEMON_INFO_API)

if status.status_code == 200:
    pokemon = status.json()

    # info
    print(f"\n{decorator}")
    print("Información del Pokemon →\n")

    print("- Nombre:", pokemon["name"].capitalize())
    print("- Id:", pokemon["id"])
    print("- Peso:", pokemon["weight"])
    print("- Altura:", pokemon["height"])
    print("- Tipo(s):")

    # pokemon types
    for type in pokemon["types"]:
        item = type["type"]["name"].capitalize()
        print(f"  {item}")

    # pokemon games
    print("- Juego(s):")

    for game in pokemon["game_indices"]:
        item = game["version"]["name"].capitalize()
        print(f"  {item}")
    
    print(decorator)

else:
    print(f"Error, Response [{status.status_code}]")
