import requests

"""
    HTTP REQUESTS
"""

response = requests.get("https://github.com/elhdrond")
if response.status_code == 200:
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}.")

response2 = requests.get("https://github.com/elhdrondB")
if response2.status_code == 200:
    print(response2.text)
else:
    print(f"Request failed with status code {response2.status_code}.")


"""
    EXTRA EXERCISE
"""

pokemon = input("Enter a Pokémon name or number: ").lower()

poke_api_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if poke_api_response.status_code == 200:
    poke_data = poke_api_response.json()
    print("Name: ", poke_data["name"])
    print("Id: ", poke_data["id"])
    print("Weight: ", poke_data["weight"])
    print("Height: ", poke_data["height"])
    poke_types = ", ".join(t["type"]["name"] for t in poke_data["types"]) + "."
    print(f"Type(s): {poke_types}")
    print("Pokemon Games:")
    poke_games = (
        ", ".join(game["version"]["name"] for game in poke_data["game_indices"]) + "."
    )
    print(f"\t{poke_games}")

    poke_evol_api_response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/"
    )

    if poke_evol_api_response.status_code == 200:
        url = poke_evol_api_response.json()["evolution_chain"]["url"]
        poke_evol_api_response = requests.get(url)

        if poke_evol_api_response.status_code == 200:
            poke_evol_data = poke_evol_api_response.json()

            evol_names = []

            def get_evolves(data):
                evol_names.append(data["species"]["name"])
                for evolve in data.get("evolves_to", []):
                    get_evolves(evolve)
                return evol_names

            print(
                f"Evolution chain: {', '.join(get_evolves(poke_evol_data['chain']))}."
            )

        else:
            print(
                f"Error {poke_evol_api_response.status_code}: could not retrieve evolution chain."
            )
    else:
        print(
            f"Error {poke_evol_api_response.status_code}: could not retrieve evolution chain."
        )

else:
    print(f"Error {poke_api_response.status_code}: Pokémon not found.")
