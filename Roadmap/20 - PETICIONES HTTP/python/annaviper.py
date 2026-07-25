import requests
import pandas as pd

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
r = requests.get(BASE_URL + "jigglypuff")

if str(r.status_code).startswith("2"):
    data = r.json()
    print(r.text)
else:
    raise 

print(f"Nombre: {data['name']}")
print(f"ID: {data['id']}")
print(f"Peso: {data['weight']}")
print(f"Altura: {data['height']}")
print(f"Tipo(s): {', '.join([i['type']['name'] for i in data['types']])}")
print(f"Juegos(s): {', '.join([i['version']['name'] for i in data['game_indices']])}")