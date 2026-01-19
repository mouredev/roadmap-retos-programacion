# @Author Daniel Grande (Mhayhem)

import requests
import os
import base64
import json

# EJERCICIO:
# ¡Dos de las bandas más grandes de la historia están de vuelta!
# Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
# Desarrolla un programa que se conecte al API de Spotify y los compare.
# Requisitos:
# 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
# 2. Conéctate al API utilizando tu lenguaje de programación.
# 3. Recupera datos de los endpoint que tú quieras.
# Acciones:
# 1. Accede a las estadísticas de las dos bandas.
#    Por ejemplo: número total de seguidores, escuchas mensuales,
#    canción con más reproducciones...
# 2. Compara los resultados de, por lo menos, 3 endpoint.
# 3. Muestra todos los resultados por consola para notificar al usuario.
# 4. Desarrolla un criterio para seleccionar qué banda es más popular.

# get api token
def get_access_token():
    client_id = "client_id" # colocar información necesaria
    client_secret = "client_secret" # colocar información necesaria
    
    auth_string = f"{client_id}:{client_secret}"
    auth_base64 = base64.b64encode(auth_string.encode()).decode()
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization":f"Basic {auth_base64}",
        "Content-type":"application/x-www-form-urlencoded"
    }
    data = {
        "grant_type":"client_credentials"
    }
    
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    
    return response.json()["access_token"]

def get_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization":f"Bearer {token}"
    }
    params = {
        "q":artist_name,
        "type":"artist",
        "limit":1
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    return response.json()["artists"]["items"][0]

def get_top_track(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = {
        "Authorization":f"Bearer {token}"
    }
    params = {
        "market":"US"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    return response.json()["tracks"][0]

def get_album_count(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = {
        "Authorization":f"Bearer {token}"
    }
    params = {
        "limit": 50
    }
    
    response = requests.get(url , headers=headers, params=params)
    response.raise_for_status()
    
    return response.json()["total"]

def print_artist_status(artist, top_track, album_count):
    print(f"\n{artist['name']}")
    print(f"Seguidores: {artist['followers']["total"]}")
    print(f"Popularidad: {artist['popularity']}")
    print(f"Generos: {', '.join(artist['genres'])}")
    print(f"Canción mas popular: {top_track['name']} (popularity: {top_track['popularity']})")
    print(f"Número de albunes: {album_count}")

def calculate_score(artist, top_track):
    return (
        artist["followers"]["total"] * 0.5 +
        artist["popularity"] * 1.0 +
        top_track["popularity"]
    )

def main():
    token = get_access_token()
    
    oasis = get_artist(token, "Oasis")
    linkin_park = get_artist(token, "Linkin Park")
    
    oasis_top = get_top_track(token, oasis["id"])
    lp_top = get_top_track(token, linkin_park["id"])
    
    oasis_albums = get_album_count(token, oasis["id"])
    lp_albums = get_album_count(token, linkin_park["id"])
    
    print_artist_status(oasis, oasis_top, oasis_albums)
    print_artist_status(linkin_park, lp_top, lp_albums)
    
    oasis_scores = calculate_score(oasis, oasis_top)
    lp_scores = calculate_score(linkin_park, lp_top)
    
    print("\n RESULTADO FINAL")
    if oasis_scores > lp_scores:
        print(f"Oasis gana en populareidad, {oasis_scores}.")
    else:
        print(f"Linkin Park gana en populardiada, {lp_scores}")

main()