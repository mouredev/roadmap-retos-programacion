import base64
import requests

CLIENT_ID = "Mi CLIENT_ID"
CLIENT_SECRET = "Mi CLIENT_SECRET"


def get_token() -> str:
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo el token de Spotify: {response.json()}."
        )

    return response.json()["access_token"]


def search_artist(token: str, name: str):
    url = f"https://api.spotify.com/v1/search?q={name}&type=artist&limit=1"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo el artista: {response.json()}."
        )

    results = response.json()
    if results["artists"]["items"]:
        return results["artists"]["items"][0]["id"]
    else:
        raise Exception(
            f"El artista {name} no se ha encontrado."
        )


def get_artist_data(token: str, id: str):

    url = f"https://api.spotify.com/v1/artists/{id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo los datos del artista: {response.json()}."
        )

    results = response.json()
    return {
        "name": results["name"],
        "followers": results["followers"]["total"],
        "popularity": results["popularity"]
    }


def get_artist_top_track(token: str, id: str):

    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo las canciones del artista: {response.json()}."
        )

    results = response.json()

    top_track = max(results["tracks"], key=lambda track: track["popularity"])

    return {
        "name": top_track["name"],
        "popularity": top_track["popularity"]
    }


# 1. Token
token = get_token()

# 2. IDs
artist_1_id = search_artist(token, "Taylor Swift")
artist_2_id = search_artist(token, "Linkin Park")

# 3. Data

# 3.1. Seguidores y popularidad
artist_1 = get_artist_data(token, artist_1_id)
artist_2 = get_artist_data(token, artist_2_id)

# 3.2. Canción más popular
top_track_artist_1 = get_artist_top_track(token, artist_1_id)
top_track_artist_2 = get_artist_top_track(token, artist_2_id)

# 4. Comparativa
artist_1_counter = 0
artist_2_counter = 0

print(f"\nComparación de artistas:\n")
print(f"{artist_1["name"]}")
print(f"{artist_2["name"]}")

# 4.1. Seguidores
print(f"\nComparación seguidores:\n")
print(f"Seguidores {artist_1["name"]}: {artist_1["followers"]}")
print(f"Seguidores {artist_2["name"]}: {artist_2["followers"]}")

if artist_1["followers"] > artist_2["followers"]:
    print(f"{artist_1["name"]} es más popular en número de seguidores.")
    artist_1_counter += 1
else:
    print(f"{artist_2["name"]} es más popular en número de seguidores.")
    artist_2_counter += 1

# 4.2. Popularidad
print(f"\nComparación popularidad:\n")
print(f"Popularidad {artist_1["name"]}: {artist_1["popularity"]}")
print(f"Popularidad {artist_2["name"]}: {artist_2["popularity"]}")

if artist_1["popularity"] > artist_2["popularity"]:
    print(f"{artist_1["name"]} es más popular a nivel general.")
    artist_1_counter += 1
else:
    print(f"{artist_2["name"]} es más popular a nivel general.")
    artist_2_counter += 1

# 4.3. Canción
print(f"\nComparación canción:\n")
print(
    f"Canción {top_track_artist_1["name"]} ({artist_1["name"]}): {top_track_artist_1["popularity"]} popularidad.")
print(
    f"Canción {top_track_artist_2["name"]} ({artist_2["name"]}): {top_track_artist_2["popularity"]} popularidad.")

if top_track_artist_1["popularity"] > top_track_artist_2["popularity"]:
    print(
        f"La canción {top_track_artist_1["name"]} de {artist_1["name"]} es más popular.")
    artist_1_counter += 1
else:
    print(
        f"La canción {top_track_artist_2["name"]} de {artist_2["name"]} es más popular.")
    artist_2_counter += 1

# 5. Resultado
print(f"\nResultado final:\n")
print(
    f"{artist_1["name"] if artist_1_counter > artist_2_counter else artist_2["name"]} es más popular.")
