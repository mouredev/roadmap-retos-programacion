import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Spotify API credentials
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_token():
  """ Obtener el token de OAuth de Spotify API """
  url = 'https://accounts.spotify.com/api/token'
  data = {
    'grant_type': 'client_credentials'
  }
  response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
  token = response.json().get("access_token")
  return token

def get_artist_data(artist_id, token):
  """ Obtener los datos de un artista de Spotify """
  url = f'https://api.spotify.com/v1/artists/{artist_id}'
  headers = {
    'Authorization': f'Bearer {token}'
  }
  response = requests.get(url, headers=headers)
  return response.json()

def get_artist_top_tracks(artist_id, token):
  """ Obtener las canciones más populares de un artista """
  url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US'
  headers = {
    'Authorization': f'Bearer {token}'
  }
  response = requests.get(url, headers=headers)
  return response.json()

def compare_stat(oasis_stat, lp_stat, label, unit='', score=(0, 0), is_track=False):
  """Comparar estadísticas entre Oasis y Linkin Park y actualizar el marcador"""
  print(f"> {label}")

  if is_track:
    oasis_track, oasis_popularity = oasis_stat
    lp_track, lp_popularity = lp_stat
    print(f"    Oasis: \"{oasis_track}\" con {oasis_popularity}{unit}")
    print(f"    Linkin Park: \"{lp_track}\" con {lp_popularity}{unit}")
  else:
    print(f"    Oasis: {oasis_stat}{unit}")
    print(f"    Linkin Park: {lp_stat}{unit}")

  oasis_score, linkin_park_score = score

  # Comparar por popularidad si es una canción, o directamente los valores si no es canción
  if (is_track and oasis_stat[1] > lp_stat[1]) or (not is_track and oasis_stat > lp_stat):
    oasis_score += 1
  else:
    linkin_park_score += 1

  print(f"Oasis {oasis_score} - Linkin Park {linkin_park_score}\n")
  return oasis_score, linkin_park_score

def compare_bands():
  token = get_token()

  oasis_id = '2DaxqgrOhkeH0fpeiQq2f4'
  linkin_park_id = '6XyY86QOPPrYVGvF9ch6wz'

  # Obtener datos de ambas bandas
  oasis_data = get_artist_data(oasis_id, token)
  linkin_park_data = get_artist_data(linkin_park_id, token)

  # Obtener las canciones más populares de ambas bandas
  oasis_top_tracks = get_artist_top_tracks(oasis_id, token)
  linkin_park_top_tracks = get_artist_top_tracks(linkin_park_id, token)

  oasis_score = 0
  linkin_park_score = 0

  # Formatear datos
  oasis_followers = f"{oasis_data.get('followers', {}).get('total'):,}"
  oasis_popularity = oasis_data.get("popularity")
  oasis_top_track = (oasis_top_tracks['tracks'][0]['name'], oasis_top_tracks['tracks'][0]['popularity'])
    
  linkin_park_followers = f"{linkin_park_data.get('followers', {}).get('total'):,}"
  linkin_park_popularity = linkin_park_data.get("popularity")
  linkin_park_top_track = (linkin_park_top_tracks['tracks'][0]['name'], linkin_park_top_tracks['tracks'][0]['popularity'])

  # Comparar seguidores
  print("Oasis vs Linkin Park\n")
  oasis_score, linkin_park_score = compare_stat(oasis_followers, linkin_park_followers, "Seguidores", "", (oasis_score, linkin_park_score))

  # Comparar popularidad
  oasis_score, linkin_park_score = compare_stat(oasis_popularity, linkin_park_popularity, "Popularidad", "/100 pts.", (oasis_score, linkin_park_score))

  # Comparar canciones más populares (usando tuplas para nombre y popularidad)
  oasis_score, linkin_park_score = compare_stat(oasis_top_track, linkin_park_top_track, "Canción más popular", "/100 pts.", (oasis_score, linkin_park_score), is_track=True)

  # Determinar la banda más popular
  print(f"BANDA MÁS POPULAR: {'Oasis' if oasis_score > linkin_park_score else 'Linkin Park'}")

if __name__ == "__main__":
  compare_bands()