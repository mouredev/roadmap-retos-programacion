import requests

#Hacemos la petición a la web con el la función get del modulo requests
response = requests.get('https://cargad.com/')

#Comprobamos que la petición ha resultado exitosa
if response.status_code == 200:
    print("Conexión exitosa")
    
    #Mostar por consola el contenido de la web
    print(response.text)
else:
    print(f"La conexión ha fallado, código de error {response.status_code}")

print("---"*10,"\n")

#Extra
def info_pokemon(arg):
    url = "https://pokeapi.co/api/v2/"

    #Realizar la llamada, asegurando que el nombre se recibe en minusculas
    response = requests.get(f"{url}pokemon/{arg.lower()}")
    
    if response.status_code == 200:
        #Almacenar los datos del pokemon en una variable
        pokemon_data = response.json()
        
        #Mostrar la información
        print(f"Nombre: {pokemon_data["name"].capitalize()}")
        print(f"Id: {pokemon_data["id"]}")
        print(f"Peso: {pokemon_data["weight"]}")
        print(f"Altura: {pokemon_data["height"]}")

        #Mostrar el tipo o tipos de pokemon que es
        types = []
        for element in pokemon_data["types"]:
            types.append(element["type"]["name"].capitalize())
        print(f"Tipo: {", ".join(types)}")

        #Guardar el id del pokemon para mostrar el nombre de su cadena de evoluciones
        id = pokemon_data["id"]

        #Buscar el pokemon por especie
        response_species = requests.get(f"{url}/pokemon-species/{id}")
        pokemon_species = response_species.json()
        url_evolution_chain = pokemon_species["evolution_chain"]["url"]

        #Buscar la cadena de evolución
        response_evo = requests.get(url_evolution_chain)
        evolution_chain = response_evo.json()
        evolution_list = []

        #Recorrer el objeto json, para obtener el nombre de la cadena de evoluciones
        for key, value in evolution_chain["chain"].items():
            if key == "species":
                evolution_list.insert(0, value["name"])
            elif key == "evolves_to":
                for key1 in evolution_chain["chain"]["evolves_to"]:
                    if key1["species"]:
                        evolution_list.append(key1["species"]["name"])
                    
                    if key1["evolves_to"]:
                        evolution_list.append(key1["evolves_to"][0]["species"]["name"])

        print(f"Evoluciones: {" -> ".join(evolution_list).title()}")

        #Buscar los juegos en los que aparece
        games_titles = []
        for items in pokemon_data["game_indices"]:
            games_titles.append(items["version"]["name"])

        print(f"Juegos en los que aparece: {", ".join(games_titles).title()}\n")
    else:
        print(f"La conexión ha fallado, código de error {response.status_code}\n")

query = True
while query:
    pokemon = input("Introduce el nombre o el id del pokemon a consultar. Para cerrar el programa escribe la letra q: ")
    if pokemon == "q":
        query = False
    else:
        info_pokemon(pokemon)