"""
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
"""

import base64
import requests
import aiohttp
import asyncio

CLIENT_ID = "Mi CLIENT_ID"
CLIENT_SECRET = "Mi CLIENT_SECRET"

id_oasis = "2DaxqgrOhkeH0fpeiQq2f4"
id_linkin_park = "6XyY86QOPPrYVGvF9ch6wz"

def get_token():

    # Codificamos las credenciales para conseguir el token de acceso, el cual usaremos para hacer peticiones get.
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"# Este es el formato de user:pass que se necesita codificar en base 64.
    b64_auth_string = base64.b64encode(auth_string.encode()).decode()#encode para un string a bytes, luego se codifica en base 64 y al final se vuelve a pasar a string.

    # Armamos la petición post: Url
    url = "https://accounts.spotify.com/api/token"
    #Headers
    headers = {
        "Authorization": f"Basic {b64_auth_string}",#aqui le pasamos el user:pass codificado
        "Content-Type": "application/x-www-form-urlencoded" # indicando que lo pasamos como un formulario
    }
    #Body
    data = {
        "grant_type": "client_credentials"# indica que el tipo de credenciales son para acceso a datos de la api sin usuario
    }

    # Enviamos la petición POST
    response = requests.post(url, headers=headers, data=data)
    token_data = response.json()

    return token_data["access_token"]



async def call_api(session, url, headers):
    async with session.get(url, headers=headers) as answer:
        if answer.status != 200:
            return None
        else:
            return await answer.json()
        
        
def print_info_artist(info_artist):
    print(f"Name: {info_artist["name"]}")
    print("Genres:")
    for genre in info_artist["genres"]:
        print(f"\t{genre}")
    print(f"Followers: {info_artist["followers"]["total"]}")
    print(f"Popularity: {info_artist["popularity"]}")

def print_info_tracks(info_tracks, artist: str):
    print(f"Ten Most popular tracks of {artist} :")
    sorted_tracks = sorted(info_tracks["tracks"], key=lambda t: t["popularity"], reverse=True)
    for i, track in enumerate(sorted_tracks):
        print(f"{i + 1}.Name: {track["name"]} | Popularity: {track["popularity"]} | Album: {track["album"]["name"]}")


async def compare_artists(token: str, artist_id1: str, artist_id2):
    url_artist_id1 = f"https://api.spotify.com/v1/artists/{artist_id1}"
    url_artist_id2 = f"https://api.spotify.com/v1/artists/{artist_id2}"
    url_tracks_id1 = f"https://api.spotify.com/v1/artists/{artist_id1}/top-tracks"
    url_tracks_id2 = f"https://api.spotify.com/v1/artists/{artist_id2}/top-tracks"


    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with aiohttp.ClientSession() as session:

        info_artist_1, info_artist_2, info_tracks_1, info_tracks_2  = await asyncio.gather(
                                                            call_api(session, url_artist_id1, headers), 
                                                            call_api(session, url_artist_id2, headers),
                                                            call_api(session, url_tracks_id1, headers), 
                                                            call_api(session, url_tracks_id2, headers)
                                                            )

        if info_artist_1:
            print_info_artist(info_artist_1)

        if info_tracks_1:
            print_info_tracks(info_tracks_1, info_artist_1["name"])

        print("---------------------------------------------------------------")

        if info_artist_2:
            print_info_artist(info_artist_2)

        if info_tracks_2:
            print_info_tracks(info_tracks_2, info_artist_2["name"])




async def main():
    token = get_token()
    await compare_artists(token, id_oasis,id_linkin_park)

asyncio.run(main())

