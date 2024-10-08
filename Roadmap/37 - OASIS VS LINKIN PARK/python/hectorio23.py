# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import requests
import json

# Credenciales (Obtenidas desde la cuenta de Spotify)
CLIENT_ID = "client_id"
CLIENT_SECRET = "client_secret"

# Autenticación con Spotify API
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

# Función para obtener datos de una banda/artista
def get_artist_data(artist_name, token):
    search_url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(search_url, headers=headers)
    artist_data = response.json()["artists"]["items"][0]
    return {
        "name": artist_data["name"],
        "followers": artist_data["followers"]["total"],
        "popularity": artist_data["popularity"],
        "monthly_listeners": artist_data["popularity"] * 1000  # Simplificación
    }

# Comparación de bandas
def compare_bands():
    token = get_access_token()
    oasis_data = get_artist_data("Oasis", token)
    linkin_park_data = get_artist_data("Linkin Park", token)

    print(f"Oasis: {oasis_data}")
    print(f"Linkin Park: {linkin_park_data}")

    # Criterio de comparación
    if oasis_data["followers"] > linkin_park_data["followers"]:
        print("Oasis es más popular en seguidores.")
    else:
        print("Linkin Park es más popular en seguidores.")

if __name__ == "__main__":
    compare_bands()
