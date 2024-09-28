# -- exercise
url: str = "https://www.dota2.com/hero/legioncommander"

import requests


def get_web_content(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        return f"err: {err}"
    except requests.exceptions.RequestException as err:
        return f"err: {err}"
    except Exception as err:
        return f"err: {err}"


if __name__ == "__main__":
    print(get_web_content(url))


# -- extra challenge
poke_api: str = "https://pokeapi.co/api/v2/pokemon/"


class Pokemon:
    def __init__(self, name: str):
        self.name = name
        self.url = f"{poke_api}{name}"
        self.data = self.get_data()

    def get_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            return f"err: {err}"
        except requests.exceptions.RequestException as err:
            return f"err: {err}"
        except Exception as err:
            return f"err: {err}"

    def get_info(self):
        if isinstance(self.data, dict):
            name = self.data.get("name")
            id = self.data.get("id")
            weight = self.data.get("weight")
            height = self.data.get("height")
            types = [t["type"]["name"] for t in self.data.get("types")]
            return f"Name: {name}\nID: {id}\nWeight: {weight}\nHeight: {height}\nTypes: {types}"
        return self.data

    def get_evolution_chain(self):
        if isinstance(self.data, dict):
            species_url = self.data.get("species").get("url")
            species_data = requests.get(species_url).json()
            evolution_chain_url = species_data.get("evolution_chain").get("url")
            evolution_chain_data = requests.get(evolution_chain_url).json()
            chain = evolution_chain_data.get("chain")
            evolutions = []
            while chain:
                evolutions.append(chain["species"]["name"])
                chain = chain.get("evolves_to")[0] if chain.get("evolves_to") else None
            return " -> ".join(evolutions)
        return self.data

    def get_games(self):
        if isinstance(self.data, dict):
            games = [v["version"]["name"] for v in self.data.get("game_indices")]
            return games
        return self.data


if __name__ == "__main__":
    name = input("enter a Pokémon name or number: ")
    pokemon = Pokemon(name)
    print(pokemon.get_info())
    print(pokemon.get_evolution_chain())
    print(pokemon.get_games())
