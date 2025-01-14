import requests

url = "https://httpbin.org/get"

r = requests.get(url)


if r.status_code == 200:
    print("Get executed")
    print(r.json())
elif r.status_code == 401:
    print("Unauthorized")
elif r.status_code == 403:
    print("Forbidden")    
else:
    print(f'Error executing get request with status code {r.status_code}')    

#Extra

uri = "https://pokeapi.co/api/v2/"

while(True):
    print("Enter 1 to search pokemon by name or ID")
    print("Enter 2 to exit")
    value = int(input())

    if value == 1:
        pokemon = input("Enter  name or id for pokemon ")
        pokemon = pokemon.lower()
        url_final = uri +"pokemon/"+pokemon
        
        request = requests.get(url_final)

        if request.status_code == 200 or request.status_code == 201:
            
            #Get JSON data
            data = request.json()
            #Extract data from the response
            name = data["name"]
            id = data["id"]
            weight = data["weight"]
            height = data["height"]
            #Get type
            pokemon_type = []
            for type in data["types"]:
                pokemon_type.append(type["type"]["name"])
            #Get game list
            game_list = []
            for game in data["game_indices"]:
                game_list.append(game["version"]["name"])

            #Get evolution list

            #First get speies URL
            species_url = data["species"]["url"]
            request_evo = requests.get(species_url)
            if request_evo.status_code == 200 or request_evo.status_code == 201:
                data_evo = request_evo.json()
                #if Success get URL for evolution chain
                evo_chain = data_evo["evolution_chain"]["url"]
                #Now we have URL to get evolutions
                request_evo = requests.get(evo_chain)
                if request_evo.status_code == 200 or request_evo.status_code == 201:
                    evo_details = request_evo.json()
                    evolution_chain = []
                    current_evo = evo_details["chain"]
                    #Iterate over evolutions
                    while current_evo:
                        evolution_chain.append(current_evo["species"]["name"])
                        if current_evo['evolves_to']:
                            #If there are more evolutions, check it
                            current_evo = current_evo['evolves_to'][0]
                        else:
                            current_evo = None   
                else:
                    print(f'Error executing {evo_chain} with status code {request_evo.status_code}')    
            else:
                print(f'Error executing {species_url} with status code {request_evo.status_code}')
            
            print(f'Name: {name}, id: {id}, Weight: {weight}, Height: {height}, Pokemon type: {pokemon_type}, Evoloves: {evolution_chain},Game list: {game_list}')
        else:
            print(f'Error executing API status code: {request.status_code}')    
    elif value == 2:
        break

    