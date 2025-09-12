"""
/*
 * EJERCICIO:
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
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
 */

"""
import base64
import requests

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"


def get_token() -> str:
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo el token de spotify: {response.json()} ")
    return response.json()["access_token"]


def search_artist(artist, token):

    url = f"https://api.spotify.com/v1/search?q=artist:{artist}&type=artist&limit=1"
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(url=url,headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error obteniendo el artista: {response.json()} ")
    
    results = response.json()
    if results["artists"]["items"]:
        return results["artists"]["items"][0]["id"]
    else: 
        raise Exception(f"El {artist} no se ha encontrado")


def get_followers_popularity(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Se ha producido un error al obtener el número de seguidores")

    results = response.json()
    return {
        "followers": results["followers"]["total"],
        "popularity": results["popularity"]
    }



def get_top_tracks(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = {"Authorization": "Bearer " + token }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        print("Se ha producido un error al obtener las canciones")
    results = response.json()
    return {
        "top_track": results["tracks"][0]["name"],
        "popularity_track": results["tracks"][0]["popularity"]
    }


token = get_token()

artista_1 = input("Introduce el nombre del primer artista: ")
artista_1_id = search_artist(artista_1, token)
artista_2 = input("Introduce el nombre del segundo artista: ")
artista_2_id = search_artist(artista_2, token)

# ids


#artist data
artista_1_data = get_followers_popularity(artista_1_id, token)
artista_2_data = get_followers_popularity(artista_2_id, token)

# song data
artista_1_song = get_top_tracks(artista_1_id, token)
artista_2_song = get_top_tracks(artista_2_id, token)

popularidad_artista_1 = 0
popularidad_artista_2 = 0

print(f"Vamos a comparar la popularidad entre {artista_1} y {artista_2} ")
print(f"Popularidad de {artista_1}: {artista_1_data['popularity']}")
print(f"Popularidad de {artista_2}: {artista_2_data['popularity']}")

if artista_1_data['popularity'] > artista_2_data['popularity']:
    print(f"{artista_1} es más popular que {artista_2}")
    popularidad_artista_1 += 1
else:
    print(f"{artista_2} es más popular que {artista_1}") 
    popularidad_artista_2 += 1

print(f"Número de seguidores de {artista_1}: {artista_1_data['followers']} ")
print(f"Número de seguidores de {artista_2}: {artista_2_data['followers']} ")

if artista_1_data['followers'] > artista_2_data['followers']:
    print(f"{artista_1} tiene más seguidores que {artista_2}")
    popularidad_artista_1 += 1
else: 
    print(f"{artista_2} tiene más seguidores que {artista_1}")
    popularidad_artista_2 += 1

print(f"Canción más popular de {artista_1}: {artista_1_song['top_track']}")
print(f"Canción más popular de {artista_2}: {artista_2_song['top_track']}")
print(f"Popularidad de la canción Top de {artista_1}: {artista_1_song['popularity_track']}")
print(f"Popularidad de la canción Top de {artista_2}: {artista_2_song['popularity_track']}")

if artista_1_song['popularity_track'] > artista_2_song['popularity_track']:
    print(f"La canción {artista_1_song['top_track']} es más popular que {artista_2_song['top_track']} ")
    popularidad_artista_1 += 1
else:
    print(f"La canción {artista_2_song['top_track']} es más popular que {artista_1_song['top_track']} ")
    popularidad_artista_2 += 1

print("Resultados: ")
print(f"Popularidad de {artista_1}: {popularidad_artista_1}")
print(f"Popularidad de {artista_2}: {popularidad_artista_2}")

if popularidad_artista_1 > popularidad_artista_2:
    print(f"{artista_1} es más popular que {artista_2}")
else:
    print(f"{artista_2} es más popular que {artista_1}")