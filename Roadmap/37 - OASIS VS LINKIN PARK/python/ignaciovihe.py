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
id_mago_de_oz = "5ZNxiPcbKgaNcBrERMpqeu"
id_dartagnan= "7Lj8CmxeAuJ2c2I6YxA6AJ"

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
        
        if info_artist_1 and info_artist_2:
            name1, name2 = info_artist_1["name"], info_artist_2["name"]
            followers1, followers2 = info_artist_1["followers"]["total"], info_artist_2["followers"]["total"]
            popularity1, popularity2 = info_artist_1["popularity"], info_artist_2["popularity"]

        if info_tracks_1 and info_tracks_2:
            sorted_tracks1 = sorted(info_tracks_1["tracks"], key=lambda t: t["popularity"], reverse=True)
            sorted_tracks2 = sorted(info_tracks_2["tracks"], key=lambda t: t["popularity"], reverse=True)
            name_track_1 = sorted_tracks1[1]["name"]
            name_track_2 = sorted_tracks2[1]["name"]
            popularity_track1 = sorted_tracks1[1]["popularity"]
            popularity_track2 = sorted_tracks2[1]["popularity"]

        points={
            name1: 0,
            name2: 0
        }
        
        print("Comparacion de artistas:")        

        print(f"\t {name1} VS {name2}\n")

        print("Número de seguidores:")
        print(f"\tSeguidores de {name1}: {followers1}")
        print(f"\tSeguidores de {name2}: {followers2}")
        more_popular = max((followers1, name1), (followers2, name2))
        print(f"{more_popular[1]} es más popular en número de seguidores.\n")
        points[more_popular[1]] += 2

        print("Popularidad:")
        print(f"\t{name1}: {popularity1}")
        print(f"\t{name2}: {popularity2}")
        more_popular = max((popularity1, name1), (popularity2, name2))
        print(f"{more_popular[1]} es más popular según el ranking de Spotify.\n")
        points[more_popular[1]] += 3

        print("Canción más populares:")
        print(f"\tCanción de {name1}: {name_track_1} - {popularity_track1}")
        print(f"\tCanción de {name2}: {name_track_2} - {popularity_track2}")
        more_popular = max((popularity1, name_track_1, name1), (popularity2, name_track_2, name2))
        print(f"La cancion {more_popular[1]} de {more_popular[2]} es más popular.\n")
        points[more_popular[2]] += 1.5

        print("RESULTADO FINAL:")
        if points[name1] > points[name2]:
            print(f"{name1} es más popular")
        else:
            print(f"{name2} es más popular")





async def main():
    token = get_token()
    await compare_artists(token, id_oasis, id_linkin_park)

asyncio.run(main())

