#37 OASIS VS LINKIN PARK
#### Dificultad: Media | Publicación: 09/09/24 | Corrección: 16/09/24

## Ejercicio
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
import base64

import requests

# Credenciales de Spotify
client_id = ''
client_secret = ''

# Obtener el token de acceso
def get_access_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth_header}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(auth_url, headers=headers, data=data)
    response_data = response.json()
    return response_data['access_token']

# Obtener datos del artista
def get_artist_data(artist_name, access_token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': artist_name,
        'type': 'artist'
    }
    response = requests.get(search_url, headers=headers, params=params)
    artist_data = response.json()['artists']['items'][0]
    return artist_data

# Comparar estadísticas de las bandas
def compare_bands(artist1, artist2):
    access_token = get_access_token(client_id, client_secret)
    artist1_data = get_artist_data(artist1, access_token)
    artist2_data = get_artist_data(artist2, access_token)

    print(f"""{artist1}:
            Followers: {artist1_data['followers']['total']} de seguidores en total
            Popularity: {artist1_data['popularity']} puntos de popularidad
            Generos: {artist1_data['genres']}
            """)
    print(f"""{artist2}:
            Followers: {artist2_data['followers']['total']} de seguidores en total
            Popularity: {artist2_data['popularity']} puntos de popularidad
            Generos: {artist2_data['genres']}
            """)

    if artist1_data['followers']['total'] > artist2_data['followers']['total']:
        print(f"{artist1} es más popular que {artist2}.")
    else:
        print(f"{artist2} es más popular que {artist1}.")

# Uso del programa
compare_bands('soda stereo', 'Los enanitos verdes')