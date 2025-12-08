import requests

#Exercise

response = requests.get("https://w3schools.com")
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error with code {response.status_code} when making the request")


#Extra Exercise

pokemon = input("Insert the name or number of the Pokemon to search:  ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json()
    print("Name: ", data["name"])
    print("Id: ", data["id"] )
    print("Weight: ", data["weight"] )
    print("Height: ", data["height"] )
    print("Type: ")
    for type in data["types"]:
        print(type["type"]["name"])
    print("Games: ")
    for game in data["game_indices"]:
        print(game["version"]["name"])

    response2 = requests.get(f" https://pokeapi.co/api/v2/pokemon-species/{pokemon}")
    if response2.status_code == 200: 
        url = response2.json()["evolution_chain"]["url"]
        response2 = requests.get(url)
        if response2.status_code == 200:
            data = response2.json()

            print("Evolution chain: ")
            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])
        else:
            print(f"Error {response.status_code}: Obtaining evolutions")

    else:
        print(f"Error {response.status_code}: Obtaining evolutions")

else:
    print(f"Error {response.status_code}: Pokemon not found")


