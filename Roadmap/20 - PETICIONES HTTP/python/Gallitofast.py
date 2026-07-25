#Peticiones http
import requests

response = requests.get("https://www.facebook.com")
if response.status_code==200:
    print(response.text)
else:
    print(f"Error con codigo: {response.status_code} al realizar esta peticion.")


"""Dificultad extra"""
pokemon= input("Introduce the pokemon name or national pokedex number to search: ").lower()

response= requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code==200:
    data=response.json()
    print("Pokemon name: ",data["name"])
    print("ID: ", data["id"])
    print("Weight: ",data["weight"])
    print("Height: ",data["height"])
    print("Types: ")
    for type in data["types"]:
        print(type["type"]["name"])
    print("Games: ")
    for game in data["game_indices"]:
        print(game["version"]["name"])
    
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code==200:
        url=response.json()["evolution_chain"]["url"]

        response=requests.get(url)

        if response.status_code==200:
            data= response.json()

            print("Evolution Chain")

            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)
            get_evolves(data["chain"])
        else:
            print(f"Error: {response.status_code} obtaining evolutions.")
    else:
            print(f"Error: {response.status_code} obtaining evolutions.")
else:
    print(f"Error: {response.status_code} Pokemon not found")

 