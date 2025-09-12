import requests
from bs4 import BeautifulSoup

def get_website_content(url):
  response = requests.get(url)
  status = response.status_code
  if status == 200:
    print("La petición fue correcta")
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
  else:
    print(f"Petición fallida, código: {status}")

def get_pokemon_data(name_or_id):
  try:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name_or_id}')
    response.raise_for_status()
    data = response.json() 
    name = data["name"].capitalize()
    id = data["id"]
    weight = data["weight"] / 10
    height = data["height"] / 10
    types = [type["type"]["name"].capitalize() for type in data["types"]]
    evolution_chain_url = data["species"]["url"]
    evolution_chain_response = requests.get(evolution_chain_url)
    evolution_chain_response.raise_for_status()
    evolution_chain_data = evolution_chain_response.json()

    if "chain" in evolution_chain_data and evolution_chain_data["chain"]:
      evolution_chain = [pokemon["species"]["name"].capitalize() for pokemon in evolution_chain_data["chain"]["evolves_to"]]
    else:
      evolution_chain = [name]
      game_appearances = [game["version"]["name"] for game in data["game_indices"]]

    pokemon_info = f'''
    POKEMON DATA:
    -Name: {name}
    -Id: {id}
    -Weight: {weight} kg
    -Height: {height} m
    -Type(s): {', '.join(types)}
    -Evolution chain: {' to '.join(evolution_chain)}
    -Games: {', '.join(game_appearances)}
    '''
    return pokemon_info
  except requests.HTTPError as err:
    return f'Error al obtener datos: {err}'

if __name__ == "__main__":
    url = 'https://retosdeprogramacion.com/'
    get_website_content(url)
    pokemon_name_or_id = input("Enter the name or number of the Pokémon: ")
    pokemon_info = get_pokemon_data(pokemon_name_or_id)
    print(pokemon_info)
