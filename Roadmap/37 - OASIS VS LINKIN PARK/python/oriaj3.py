"""
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
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv() #Carga las variables del archivo .env

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
X_RAPIDAPI_KEY = os.getenv("X_RAPIDAPI_KEY")

#TODO: IMPLEMENTAR EXCEPCIONES PARA MANEJAR ERRORES DE CONEXIÓN

#Función para obtener el token de acceso
def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    data={"grant_type":"client_credentials" }
    auth=(client_id, client_secret)
    response = requests.post(url=url, data=data, auth=auth)
    #Verificar si la respuesta es correcta
    if response.status_code == 200:
        token_data = response.json()
        return token_data.get("access_token")
    else:
        #Mostrar error
        print(f"Error: Unable to get access token. Status Code {response.status_code}.")
        return None


#Función para obtener el ID de un artista
def get_artist_ID(artist_name, token):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        items = response_data.get("artists", {}).get("items", [])

        if items:
            # Buscar el artista cuyo nombre coincide con el proporcionado
            for artist in items:
                if artist.get("name").lower() == artist_name.lower():
                    artist_id = artist.get("id")
                    return artist_id
            
            # Si no se encontró coincidencia exacta, devolver el primer resultado
            return items[0].get("id")
        else:
            print("No se encontraron artistas.")
            return None
    else:
        print(f"Error: Unable to get artist data. Status Code {response.status_code}.")
        return None

#Función para obtener el nombre de un artista, sus generos, seguidores y su popularidad dado un ID
def get_artist_data(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        artist_name = response_data.get("name")
        artist_genres = response_data.get("genres")
        artist_followers = response_data.get("followers").get("total")
        artist_popularity = response_data.get("popularity")

        return artist_name, artist_genres, artist_followers, artist_popularity
    else:
        print(f"Error: Unable to get artist data. Status Code {response.status_code}.")
        return None, None, None
    
# Función para obtener el número de escuchas mensuales de un artista con el API de RapidAPI
def get_monthly_listeners(artist_id, x_rapidapi_key):
    url = "https://spotify-artist-monthly-listeners.p.rapidapi.com/artists/spotify_artist_monthly_listeners"
    querystring = {"spotify_artist_id": artist_id}
    headers = {
        "x-rapidapi-key": x_rapidapi_key,
        "x-rapidapi-host": "spotify-artist-monthly-listeners.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            response_data = response.json()
            monthly_listeners = response_data.get("monthly_listeners")
            return monthly_listeners
        else:
            print(f"Error: Unable to get monthly listeners. Status Code {response.status_code}.")
            print(response.json())  # Imprimir el contenido de la respuesta para más detalles
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
#Función para obtener las mejores canciones de un artista
def get_artist_top_tracks(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=ES"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        print(f"Error: Unable to get top tracks. Status Code {response.status_code}.")
        return None

#Función para obtener los índices de popularidad de mejores canciones de un artista
def get_top_tracks_popularity(top_tracks):
    top_tracks_popularity = []
    for track in top_tracks.get("tracks", []):
        track_name = track.get("name")
        track_popularity = track.get("popularity")
        top_tracks_popularity.append((track_name, track_popularity))
    mean = sum([track[1] for track in top_tracks_popularity]) / len(top_tracks_popularity)
    #Obtiene la canción más popular
    top_tracks_popularity.sort(key=lambda x: x[1], reverse=True)
    return mean, top_tracks_popularity, top_tracks_popularity[0]

#Función para comparar la popularidad de dos artistas:
def compare_two_artist(artist1_name, artist2_name, token):
    id1 = get_artist_ID(artist1_name, token)
    id2 = get_artist_ID(artist2_name, token)

    top_tracks1 = get_artist_top_tracks(id1, token)
    top_tracks2 = get_artist_top_tracks(id2, token)

    mean1, top_tracks1, top_track1 = get_top_tracks_popularity(top_tracks1)
    mean2, top_tracks2, top_track2 = get_top_tracks_popularity(top_tracks2)

    name1, gen1, popularity1, followers1 = get_artist_data(id1, token)
    name2, gen2, popularity2, followers2 = get_artist_data(id2, token)

    points1 = 0
    points2 = 0 
    #Mostrar los datos de los artistas
    print(f"\n*** Comparación de popularidad entre {name1} y {name2}: ***\n")
    print(f"[Artista 1]: {name1}")
    print(f"Géneros: {gen1}")
    print(f"Popularidad: {popularity1}")
    print(f"Seguidores: {followers1}")
    print(f"Media de popularidad mejores canciones: {mean1}")
    print(f"Mejores canciones: {top_tracks1}\n")

    print(f"\n[Artista 2]: {name2}")
    print(f"Géneros: {gen2}")
    print(f"Popularidad: {popularity2}")
    print(f"Seguidores: {followers2}")
    print(f"Media de popularidad mejores canciones: {mean2}")
    print(f"Mejores canciones: {top_tracks2}\n")

    input("Presiona Enter para continuar...")
    #Comparar seguidores
    print("\n - Batalla 1: Comparación de seguidores")
    if followers1 > followers2:
        print(f"{artist1_name} tiene más seguidores.")
        points1 += 1 
    elif followers1 < followers2:
        print(f"{artist2_name} tiene más seguidores.")
        points2 += 1
    else:
        print(f"{artist1_name} y {artist2_name} tienen el mismo número de seguidores.")

    # Comparar índices de popularidad total
    print("\n - Batalla 2: Comparación de popularidad")
    if popularity1 > popularity2:
        print(f"{artist1_name} tiene un índice de popularidad mayor.")
        points1 += 1
    elif popularity1 < popularity2:
        print(f"{artist2_name} tiene un índice de popularidad mayor.")
        points2 += 1
    else:
        print(f"{artist1_name} y {artist2_name} tienen el mismo índice de popularidad.")

    # Comparar popularidad de la mejor canción
    print("\n - Batalla 3: Mejor canción")
    if top_track1[1] > top_track2[1]:
        print(f"La canción más popular de {artist1_name} es más popular")
        points1 += 1
    elif top_track1[1] < top_track2[1]:
        print(f"La canción más popular de {artist2_name} es más popular")
        points2 += 1
    else:
        print(f"La canción más popular de {artist1_name} y {artist2_name} tienen la misma popularidad.")

    #Comparar la media de popularidad de las canciones más populares
    print("\n - Batalla Final: Mejores canciones")
    if mean1 > mean2:
        print(f"La media de popularidad de las canciones de {artist1_name} es mayor")
        points1 += 1
    elif mean1 < mean2:
        print(f"La media de popularidad de las canciones de {artist2_name} es mayor")
        points2 += 1
    else:
        print(f"La media de popularidad de las canciones de {artist1_name} y {artist2_name} es la misma.")

    #Recuento de puntos
    print("\n***El ganador es ... ***")
    if points1 > points2:
        print(f"{artist1_name}!\n\n")
    elif points1 < points2:
        print(f"{artist2_name}!\n\n")
    else:
        print("¡Es un empate!")
    input("Presiona Enter para continuar...")


#Ejemplos de funcionamiento del programa
#Obtener el token de acceso
TOKEN_LOGIN = get_access_token(CLIENT_ID, CLIENT_SECRET)

#Comparar dos artistas
compare_two_artist("Natos y Waor", "Ajax y Prok", TOKEN_LOGIN)
compare_two_artist("Oasis", "Linkin Park", TOKEN_LOGIN)
