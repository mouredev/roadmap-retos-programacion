""" /*
 * EJERCICIO:
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
 */ """

#EJERCICIO

import requests
import base64
import env

CLIENT_ID = "4f9f3bdc792649ad984cfcbd05be06d2"
CLIENT_SECRET = env.CLIENT_SECRET

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
        raise Exception(f"Error obteniendo el artista: {response.json()}")
    
    results = response.json()
    if results["artists"]["items"]:
        return results["artists"]["items"][0]["id"]
    else:
        raise Exception(f"El artista {name} no se ha encontrado.")
    
def get_artist_data(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo los datos del artista: {response.json()}")
    
    results = response.json()
    return {
        "name": results["name"],
        "followers": results["followers"]["total"],
        "popularity": results["popularity"],
    }

def get_artist_top_track(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo las canciones del artista: {response.json()}")
    
    results = response.json()
    top_track = max(results["tracks"], key=lambda track: track["popularity"])

    return {
        "name": top_track["name"],
        "popularity": top_track["popularity"]
    }


token = get_token()

artist_1_id = search_artist(token, "Oasis")
artist_2_id = search_artist(token, "Linkin Park")

artist_1 = get_artist_data(token, artist_1_id)
artist_2 = get_artist_data(token, artist_2_id)

top_track_artist_1 = get_artist_top_track(token, artist_1_id)
top_track_artist_2 = get_artist_top_track(token, artist_2_id)

artist_1_counter = 0
artist_2_counter = 0

print(f"\nComparación de artistas:\n")
print(f"{artist_1["name"]}")
print(f"{artist_2["name"]}")

print(f"\nComparación de seguidores:\n")
print(f"Seguidores {artist_1["name"]}: {artist_1["followers"]}")
print(f"Seguidores {artist_2["name"]}: {artist_2["followers"]}")

if artist_1["followers"] > artist_2["followers"]:
    print(f"\nEl artista {artist_1["name"]} tiene más seguidores que {artist_2["name"]}")
    artist_1_counter += 1
else:
    print(f"\nEl artista {artist_2["name"]} tiene más seguidores que {artist_1["name"]}")
    artist_2_counter += 1

print(f"\nComparación popularidad:\n")
print(f"Popularidad {artist_1["name"]}: {artist_1["popularity"]}")
print(f"Popularidad {artist_2["name"]}: {artist_2["popularity"]}")

if artist_1["popularity"] > artist_2["popularity"]:
    print(f"{artist_1["name"]} es más popular a nivel general.")
    artist_1_counter += 1
else:
    print(f"{artist_2["name"]} es más popular a nivel general.")
    artist_2_counter += 1

print(f"\nComparación de popularidad de la canción más escuchada:\n")
print(f"Canción {top_track_artist_1["name"]} ({artist_1["name"]}): {top_track_artist_1["popularity"]} popularidad.")
print(f"Canción {top_track_artist_2["name"]} ({artist_2["name"]}): {top_track_artist_2["popularity"]} popularidad.")

if top_track_artist_1["popularity"] > top_track_artist_2["popularity"]:
    print(f"La canción más escuchada del artista {artist_1["name"]} es más popular que {artist_2["name"]}")
    artist_1_counter += 1
else:
    print(f"\nLa canción más escuchada del artista {artist_2["name"]} es más popular que {artist_1["name"]}")
    artist_2_counter += 1

if artist_1_counter > artist_2_counter:
    print(f"\nEl artista {artist_1["name"]} es más popular que el artista {artist_2["name"]}")
else:
    print(f"\nEl artista {artist_2["name"]} es más popular que el artista {artist_1["name"]}")