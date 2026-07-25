""" 
# 37 - Oasis vs Linkin Park 
"""

#  Desarrolla un programa que se conecte al API de Spotify y los compare."

"""
Requisitos:
"""
# 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
# 2. Conéctate al API utilizando tu lenguaje de programación.
# 3. Recupera datos de los endpoint que tú quieras.

"""
Acciones:
"""
# 1. Accede a las estadísticas de las dos bandas.
    # Por ejemplo: número total de seguidores, escuchas mensuales,
    # canción con más reproducciones...
# 2. Compara los resultados de, por lo menos, 3 endpoint.
# 3. Muestra todos los resultados por consola para notificar al usuario.
# 4. Desarrolla un criterio para seleccionar qué banda es más popular.


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (opcional)
load_dotenv()

# Configuración de credenciales
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')


# Inicializar el cliente de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

# IDs de Oasis y Linkin Park
oasis_id = '2DaxqgrOhkeH0fpeiQq2f4'
linkin_park_id = '6XyY86QOPPrYVGvF9ch6wz'

def get_artist_info(artist_id):
    """Obtiene información básica del artista"""
    return sp.artist(artist_id)

def get_artist_top_tracks(artist_id, country='US'):
    """Obtiene las canciones más populares del artista"""
    return sp.artist_top_tracks(artist_id, country=country)

def get_artist_albums(artist_id):
    """Obtiene los álbumes del artista"""
    return sp.artist_albums(artist_id, album_type='album')

def get_related_artists(artist_id):
    """Obtiene artistas relacionados"""
    return sp.artist_related_artists(artist_id)

def compare_artists(artist1_id, artist2_id):
    # 1. Comparar información general (seguidores, popularidad, géneros)
    artist1 = get_artist_info(artist1_id)
    artist2 = get_artist_info(artist2_id)
    
    print(f"\n--- COMPARANDO {artist1['name']} VS {artist2['name']} ---\n")
    
    # Mostrar información general
    print(f"--- INFORMACIÓN GENERAL ---")
    print(f"{artist1['name']}:")
    print(f"- Seguidores: {artist1['followers']['total']:,}")
    print(f"- Popularidad: {artist1['popularity']}/100")
    print(f"- Géneros: {', '.join(artist1['genres'])}")
    
    print(f"\n{artist2['name']}:")
    print(f"- Seguidores: {artist2['followers']['total']:,}")
    print(f"- Popularidad: {artist2['popularity']}/100")
    print(f"- Géneros: {', '.join(artist2['genres'])}")
    
    # 2. Comparar canciones más populares
    top_tracks1 = get_artist_top_tracks(artist1_id)
    top_tracks2 = get_artist_top_tracks(artist2_id)
    
    print(f"\n--- TOP 5 CANCIONES ---")
    print(f"{artist1['name']}:")
    for i, track in enumerate(top_tracks1['tracks'][:5], 1):
        print(f"{i}. {track['name']} - Popularidad: {track['popularity']}/100")
    
    print(f"\n{artist2['name']}:")
    for i, track in enumerate(top_tracks2['tracks'][:5], 1):
        print(f"{i}. {track['name']} - Popularidad: {track['popularity']}/100")
    
    # 3. Comparar álbumes
    albums1 = get_artist_albums(artist1_id)
    albums2 = get_artist_albums(artist2_id)
    
    print(f"\n--- ÁLBUMES ---")
    print(f"{artist1['name']}: {len(albums1['items'])} álbumes")
    print(f"{artist2['name']}: {len(albums2['items'])} álbumes")
    
    # 4. Desarrollar criterio de popularidad
    # Podemos usar una combinación de seguidores y popularidad
    popularity_score1 = artist1['followers']['total'] * artist1['popularity'] / 100
    popularity_score2 = artist2['followers']['total'] * artist2['popularity'] / 100
    
    print(f"\n--- RESULTADO DE POPULARIDAD ---")
    print(f"{artist1['name']}: {popularity_score1:,.0f} puntos")
    print(f"{artist2['name']}: {popularity_score2:,.0f} puntos")
    
    if popularity_score1 > popularity_score2:
        print(f"\n¡{artist1['name']} es más popular según nuestros criterios!")
    elif popularity_score2 > popularity_score1:
        print(f"\n¡{artist2['name']} es más popular según nuestros criterios!")
    else:
        print("\n¡Ambas bandas tienen la misma popularidad!")

# Ejecutar la comparación
compare_artists(oasis_id, linkin_park_id)