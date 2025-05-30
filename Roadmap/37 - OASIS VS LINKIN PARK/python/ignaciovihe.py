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
import aiohttp #para hacer llamadas a la api de forma asincrona
import asyncio

CLIENT_ID = "Mi CLIENT_ID"
CLIENT_SECRET = "Mi CLIENT_SECRET"


def get_token():
    # Configuracion de una autenticacion OAuth
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
    if response.status_code != 200:
        raise Exception("Error obteniendo el token de Spotify.")
    token_data = response.json()

    return token_data["access_token"]



async def call_api(session, url, headers):
    #Funcion asincronaque se encarga de hacer el get  con la session y url pasadas
    async with session.get(url, headers=headers) as answer:
        if answer.status != 200:
            return None
        else:
            return await answer.json()# Tiene que esperar a que reciba los datos y los genere, por eso el await.
        
async def search_artists(token: str, artist_1: str, artist_2: str):
    url_artist1_query = f"https://api.spotify.com/v1/search?q={artist_1}&type=artist&limit=1"
    url_artist2_query = f"https://api.spotify.com/v1/search?q={artist_2}&type=artist&limit=1"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with aiohttp.ClientSession() as session:# Se crea la sesion para llamadas asincronas. Session = request
        info_artist_1, info_artist_2 = await asyncio.gather(# Lanzamos la llamadas que no dependen entre ellas
                                                            call_api(session, url_artist1_query, headers), 
                                                            call_api(session, url_artist2_query, headers),
                                                            )
        if info_artist_1 and info_artist_2:
            return info_artist_1["artists"]["items"][0]["id"], info_artist_2["artists"]["items"][0]["id"]
        else:
            raise Exception("Hubo un problema al buscar los ids de los artistas")


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
        else:
            raise Exception("Error obteniendo los datos de los artistas.")

        if info_tracks_1 and info_tracks_2:
            sorted_tracks1 = sorted(info_tracks_1["tracks"], key=lambda t: t["popularity"], reverse=True)
            sorted_tracks2 = sorted(info_tracks_2["tracks"], key=lambda t: t["popularity"], reverse=True)
            name_track_1 = sorted_tracks1[0]["name"]
            name_track_2 = sorted_tracks2[0]["name"]
            popularity_track1 = sorted_tracks1[0]["popularity"]
            popularity_track2 = sorted_tracks2[0]["popularity"]
        else:
            raise Exception("Error obteniendo los datos de los tracks.")

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

        print("Canciones más populares:")
        print(f"\tCanción de {name1}: {name_track_1} - {popularity_track1}")
        print(f"\tCanción de {name2}: {name_track_2} - {popularity_track2}")
        more_popular = max((popularity_track1, name_track_1, name1), (popularity_track2, name_track_2, name2))
        print(f"La canción {more_popular[1]} de {more_popular[2]} es más popular.\n")
        points[more_popular[2]] += 1.5

        print("RESULTADO FINAL:")
        print(f"{name1}: {points[name1]}")
        print(f"{name2}: {points[name2]}")
        if points[name1] > points[name2]:
            print(f"{name1} es más popular")
        else:
            print(f"{name2} es más popular")


async def main():
    token = get_token()
    query1 = input("Introduce el nombre del primer artista: ")
    query2 = input("Introduce el nombre del segundo artista: ")
    id_artist_1, id_artist_2 = await search_artists(token, query1, query2)
    await compare_artists(token, id_artist_1, id_artist_2)

asyncio.run(main())

