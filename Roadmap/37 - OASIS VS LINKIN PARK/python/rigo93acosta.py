'''
/*
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
 */
'''
import requests
import base64

CLIENT_ID = ""
CLIENT_SECRET = ""

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

def search_artist(token: str, artist: str):

    url = f"https://api.spotify.com/v1/search?q={artist}&type=artist&limit=1"
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
            f"No se encontró el artista {artist}."
            )
    
def get_artist_data(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo datos del artista: {response.json()}."
    )

    results = response.json()
    return {
        "name": results["name"],
        "followers": results["followers"]["total"],
        "popularity": results["popularity"]
    }

def get_top_tracks(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo los top tracks del artista: {response.json()}."
        )
    
    results = response.json()
    top_track = max(results["tracks"], key=lambda track: track["popularity"])

    return {
        "name": top_track["name"],
        "popularity": top_track["popularity"]
    }

token = get_token()
artist_1_id = search_artist(token, "Taylor Swift")
artist_2_id = search_artist(token, "Linkin Park")

art_1 = get_artist_data(token, artist_1_id)
art_2 = get_artist_data(token, artist_2_id)

art_1_top = get_top_tracks(token, artist_1_id)
art_2_top = get_top_tracks(token, artist_2_id)

art_1_counter = 0
art_2_counter = 0

print(f"Comparación de seguidores entre \n {art_1["name"]} y {art_2["name"]}:")

print(f"{art_1["name"]} tiene {art_1["followers"]} de seguidores")
print(f"{art_2["name"]} tiene {art_2["followers"]} de seguidores")

if art_1["followers"] > art_2["followers"]:
    print(f"{art_1["name"]} tiene más seguidores que {art_2["name"]}")
    art_1_counter += 1
else:
    print(f"{art_2["name"]} tiene más seguidores que {art_1["name"]}")
    art_2_counter += 1

print(f"\nComparación de popularidad entre \n {art_1["name"]} y {art_2["name"]}:")
print(f"{art_1["name"]} tiene {art_1["popularity"]} de popularidad")
print(f"{art_2["name"]} tiene {art_2["popularity"]} de popularidad")

if art_1["popularity"] > art_2["popularity"]:
    print(f"{art_1["name"]} es más popular que {art_2["name"]}")
    art_1_counter += 1
else:
    print(f"{art_2["name"]} es más popular que {art_1["name"]}")
    art_2_counter += 1

print(f"\nComparación de canción entre \n {art_1["name"]} y {art_2["name"]}:")
print(f"{art_1["name"]}, canción popular {art_1_top["name"]} con {art_1_top["popularity"]} de popularidad")
print(f"{art_2["name"]}, canción popular {art_2_top["name"]} con {art_2_top["popularity"]} de popularidad")

if art_1_top["popularity"] > art_2_top["popularity"]:
    print(f"La canción {art_1_top["name"]} de {art_1["name"]} es más popular.")
    art_1_counter += 1
else:
    print(f"La canción {art_2_top["name"]} de {art_2["name"]} es más popular.")
    art_2_counter += 1

print(f"\nResultado final:")
print("="*64)
if art_1_counter > art_2_counter:
    print(f"{art_1["name"]} es más popular que {art_2["name"]}")
else:
    print(f"{art_2["name"]} es más popular que {art_1["name"]}")
print("="*64)
