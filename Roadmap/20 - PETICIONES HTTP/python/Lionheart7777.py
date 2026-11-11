import requests
# EJERCICIO
response = requests.get("https://google.com")
if response.status_code == 200:
    print(response.text)    
else:
    print(f"falla de tipo: {response.status_code} al realizar petición")
   
# EXTRA
pokemon = input("Introduce un nombre o núnero del Pokémon a buscar: ").lower().strip()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    pok_data = response.json()
    print("Nombre: ", pok_data["name"])
    print("ID: ", pok_data["id"])
    print("Peso: ", pok_data["weight"])
    print("Altura: ", pok_data["height"])
    print("Tipos: ") 
    for type_info in pok_data["types"]:
        print(type_info["type"]["name"])
    print("Juegos:")
    for game in pok_data["game_indices"]:
        print(game["version"]["name"])
        
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        
        response = requests.get(url)
        
        if response.status_code == 200:
            spec_data = response.json()
            
            print("Cadena de evolución: ")
            
            def get_evolves(data):
                print(data["species"]["name"])
                for evolve in data["evolves_to"]:
                    get_evolves(evolve)
                    
            get_evolves(spec_data["chain"])
        else:
            print(f"Error: {response.status_code} obteniendo evoluciones")
    
    else:
        print(f"Error: {response.status_code} obteniendo evoluciones")
   
else:
    print(f"Error: {response.status_code} : Pokémon no encontrado")


  