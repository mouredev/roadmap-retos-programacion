'''
Ejercicio:
Desarrolla un programa que se conecte al API de Spotify y los compare.

Requisitos:
    1. Crea una cuenta de desarrollo en spotify
    2. Conectate al API utilizando tu lenguaje de programacion.
    3. Recupera los datos de los endpoint que tu quieras.

Acciones: 
    1. Accede a las estadisticas de las dos bandas.
    Por ejemplo: numero total de seguidores, escuchas mensuales, cancion con mas reproducciones..
    2. Compara los resultados de, por lo menos, 3 endpoint.
    3. Muestra todos los resultados por consola para notificar al usuario.
    4. Desarrolla un criterio para seleccionar que banda es mas popular.
'''

import requests as rq
import base64

client_id = "50ca8278c9e448ffbeb7ff24d30883e7"
cliente_secret = "768aaab1245f490f9bac43c50215b476"

auth_str = f"{client_id}:{cliente_secret}"
b64_auth = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Authorization": f"Basic {b64_auth}"
}

data = {
    "grant_type": "client_credentials"
}

response = rq.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
token = response.json()['access_token']

headers = {
    "Authorization": f"Bearer {token}"
}

# Obtenemos los datos de linkin y Oasis
res = rq.get("https://api.spotify.com/v1/search?q=Linkin_park&type=artist", headers=headers)

res_oasis = rq.get("https://api.spotify.com/v1/search?q=Oasisk&type=artist", headers=headers)

oasis = res_oasis.json()['artists']

linkin = res.json()['artists']

# Obtenemos el id de la banda
artist_id = linkin['items'][0]['id']
artist_id_oasis = oasis['items'][0]['id']

# Obtenemos la cantidad de followers
linkin_followers = linkin['items'][0]['followers']['total']
oasis_followers = oasis['items'][0]['followers']['total']

# Obtenemos la popularidad
linkin_popularity = linkin['items'][0]['popularity']
oasis_popularity = oasis['items'][0]['popularity']

# Obtenemos los top-tracks de la banda
re = rq.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US", headers=headers)
tracks = re.json()
re_oasis = rq.get(f"https://api.spotify.com/v1/artists/{artist_id_oasis}/top-tracks?market=US", headers=headers)
tracks_oasis = re_oasis.json()

# Obtenemos la popularidad del track
linkin_track_popularity = tracks['tracks'][0]['popularity']

oasis_track_popularity = tracks_oasis['tracks'][0]['popularity']

# Obtenemos el nombre de la cancion
linkin_track_name = tracks['tracks'][0]['name']
oasis_track_name = tracks_oasis['tracks'][0]['name']

# Comparamos los resultados obtenimos
linkin_park = linkin['items'][0]['name']
oasis_band = oasis['items'][0]['name']

most_popular = linkin_park if linkin_popularity > oasis_popularity else oasis_band
most_followers = linkin_park if linkin_followers > oasis_followers else oasis_band
most_track_popular = linkin_park if linkin_track_popularity > oasis_track_popularity else oasis_band

print(f"Comparacion de Bandas: ")
print(f"Seguidores: {linkin_park}({linkin_followers}) vs {oasis_band}({oasis_followers}) -> Mas seguidores: {most_followers}")
print(f"Popularidad: {linkin_park}({linkin_popularity}) vs {oasis_band}({oasis_popularity}) -> Mas popular: {most_popular}")
print(f"Cancion mas popular: {linkin_track_name}({linkin_track_popularity}) vs {oasis_track_name}({oasis_track_popularity}) -> Hit mas popular: {most_track_popular}")