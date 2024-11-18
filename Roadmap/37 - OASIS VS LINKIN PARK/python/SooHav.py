# 37 - OASIS VS LINKIN PARK

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Datos de la aplicación
load_dotenv()

# Obtener los valores del entorno
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
scope = os.getenv("scope")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# Clase para buscar información sobre artistas


class SpotifyAPI:
    def __init__(self, sp):
        """Inicializa la clase con una instancia autenticada de Spotify."""
        self.sp = sp

    def buscar_artista(self, nombre_artista):
        """Busca un artista por endpoint: search."""
        resultados = self.sp.search(q=nombre_artista, type='artist')
        if resultados['artists']['items']:
            return resultados['artists']['items'][0]
        return None

    def obtener_info_artista(self, artist_id):
        """Obtiene información detallada de un artista por endpoint: artist."""
        return self.sp.artist(artist_id)

    def obtener_top_tracks(self, artist_uri):
        """Obtiene las canciones más populares por endpoint: artist_top_tracks."""
        top_tracks = self.sp.artist_top_tracks(artist_uri)
        return top_tracks['tracks']

    def comparar_artistas(self, artist_id1, artist_id2):
        """Compara dos artistas y devuelve un DataFrame."""
        # Buscar artistas
        artista_1_data = self.obtener_info_artista(artist_id1)
        artista_2_data = self.obtener_info_artista(artist_id2)
        popularidad_artista1 = artista_1_data['popularity']
        popularidad_artista2 = artista_2_data['popularity']
        seguidores_artista1 = artista_1_data['followers']['total']
        seguidores_artista2 = artista_2_data['followers']['total']

        if not artista_1_data or not artista_2_data:
            return None

        data = {
            "Nombre": [artista_1_data['name'], artista_2_data['name']],
            "Géneros": [", ".join(artista_1_data['genres']), ", ".join(artista_2_data['genres'])],
            "Popularidad": [artista_1_data['popularity'], artista_2_data['popularity']],
            "Seguidores": [artista_1_data['followers']['total'], artista_2_data['followers']['total']]
        }

        df = pd.DataFrame(data)

        # Determinar cuál es más exitoso
        if popularidad_artista1 > popularidad_artista2:
            mensaje = f"{artista_1_data['name']} es más popular."
        elif popularidad_artista2 > popularidad_artista1:
            mensaje = f"{artista_2_data['name']} es más popular."
        else:
            mensaje = f"Ambos artistas tienen la misma popularidad."
        print(mensaje)

        if seguidores_artista1 > seguidores_artista2:
            mensaje = f"{artista_1_data['name']} tiene mas seguidores."
        elif seguidores_artista2 > seguidores_artista1:
            mensaje = f"{artista_2_data['name']} tiene mas seguidores."
        else:
            mensaje = f"Ambos artistas tienen la misma cantidad de seguidores."
        print(mensaje)
        print()
        return df

    def comparar_top_tracks(self, artista_id1, artista_id2, num_tracks=1):
        """Compara los tracks más populares de dos artistas."""

        # Buscar artistas
        artista_1 = self.obtener_info_artista(artista_id1)
        artista_2 = self.obtener_info_artista(artista_id2)
        nombre_real_artista1 = artista_1['name']
        nombre_real_artista2 = artista_2['name']

        if not artista_1 or not artista_2:
            return None

        # Obtener los top tracks de cada artista
        top_tracks_artista1 = self.obtener_top_tracks(artista_1['uri'])[
            :num_tracks]
        top_tracks_artista2 = self.obtener_top_tracks(artista_2['uri'])[
            :num_tracks]

        cancion_mas_popular_artista1 = max(
            top_tracks_artista1, key=lambda x: x['popularity'])
        cancion_mas_popular_artista2 = max(
            top_tracks_artista2, key=lambda x: x['popularity'])

        # DataFrame
        data = {
            "Artista": [nombre_real_artista1, nombre_real_artista2],
            "Tema": [cancion_mas_popular_artista1['name'], cancion_mas_popular_artista2['name']],
            "Popularidad": [cancion_mas_popular_artista1['popularity'], cancion_mas_popular_artista2['popularity']]
        }

        df = pd.DataFrame(data)

        # Artista más popular
        if cancion_mas_popular_artista1['popularity'] > cancion_mas_popular_artista2['popularity']:
            artista_mas_popular = nombre_real_artista1
            mensaje = f"{artista_mas_popular} tiene una canción más popular."
        else:
            artista_mas_popular = nombre_real_artista2
            mensaje = f"{artista_mas_popular} tiene una canción más popular."
        print(mensaje)
        print()

        return df


# Uso del codigo

sp_api = SpotifyAPI(sp)
print("Bandas de ayer, hoy y siempre:")
print("Hoy comparamos ...")
artista_nombre = "Oasis"
artista = sp_api.buscar_artista(artista_nombre)
artista_id_1 = artista['id']
print(artista['name'])

artista_nombre = "Linkin Park"
artista = sp_api.buscar_artista(artista_nombre)
artista_id_2 = artista['id']
print(artista['name'])
print("De los dos concluimos que ...")

# Comparar dos artistas
df_comparacion = sp_api.comparar_artistas(artista_id_1, artista_id_2)
if df_comparacion is not None:
    print(df_comparacion)
else:
    print("Uno o ambos artistas no fueron encontrados.")
print()

# Comparar los track de dos artistas
df_comparacion = sp_api.comparar_top_tracks(artista_id_1, artista_id_2)
if df_comparacion is not None:
    print(df_comparacion)
else:
    print("Uno o ambos artistas no fueron encontrados.")
