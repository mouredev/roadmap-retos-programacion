import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Reemplaza con tus credenciales
client_id = '****'
client_secret = '****'

# Autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Funciones definidas
def obtener_id_artista(sp, nombre_artista):
    resultado = sp.search(q=f'artist:"{nombre_artista}"', type='artist')
    if resultado['artists']['items']:
        return resultado['artists']['items'][0]['id']
    else:
        print(f"No se encontró el artista: {nombre_artista}")
        return None

def obtener_info_artista(sp, artista_id):
    return sp.artist(artista_id)

def obtener_cancion_mas_popular(sp, artista_id, pais='US'):
    top_tracks = sp.artist_top_tracks(artista_id, country=pais)
    if top_tracks['tracks']:
        return top_tracks['tracks'][0]
    else:
        print("No se encontraron canciones top para este artista.")
        return None

def obtener_numero_albumes(sp, artista_id):
    albums = sp.artist_albums(artista_id, album_type='album')
    return len(albums['items'])

def comparar_metricas(artistas, metrica):
    artista1, artista2 = list(artistas.keys())
    puntos = {artista1: 0, artista2: 0}
    
    valor1 = artistas[artista1][metrica]
    valor2 = artistas[artista2][metrica]
    
    if valor1 > valor2:
        puntos[artista1] = 1
        print(f"{artista1} gana en {metrica.replace('_', ' ')}.")
    elif valor2 > valor1:
        puntos[artista2] = 1
        print(f"{artista2} gana en {metrica.replace('_', ' ')}.")
    else:
        print(f"Empate en {metrica.replace('_', ' ')}.")
    
    return puntos

def comparar_popularidad_cancion(artistas):
    artista1, artista2 = list(artistas.keys())
    puntos = {artista1: 0, artista2: 0}
    
    valor1 = artistas[artista1]['cancion_popular']['popularidad']
    valor2 = artistas[artista2]['cancion_popular']['popularidad']
    
    if valor1 > valor2:
        puntos[artista1] = 1
        print(f"{artista1} tiene la canción más popular.")
    elif valor2 > valor1:
        puntos[artista2] = 1
        print(f"{artista2} tiene la canción más popular.")
    else:
        print("Empate en popularidad de la canción más popular.")
    
    return puntos

# Lista de artistas a comparar
artistas = {
    'Oasis': {},
    'Linkin Park': {}
}

# Obtener datos de cada artista
for nombre_artista in artistas.keys():
    artista_id = obtener_id_artista(sp, nombre_artista)
    if artista_id:
        info = obtener_info_artista(sp, artista_id)
        cancion_popular = obtener_cancion_mas_popular(sp, artista_id)
        numero_albumes = obtener_numero_albumes(sp, artista_id)
        
        artistas[nombre_artista]['id'] = artista_id
        artistas[nombre_artista]['seguidores'] = info['followers']['total']
        artistas[nombre_artista]['popularidad'] = info['popularity']
        artistas[nombre_artista]['cancion_popular'] = {
            'nombre': cancion_popular['name'],
            'popularidad': cancion_popular['popularity']
        }
        artistas[nombre_artista]['numero_albumes'] = numero_albumes
    else:
        print(f"No se pudieron obtener datos para {nombre_artista}.")

# Mostrar la información recopilada
for nombre_artista, datos in artistas.items():
    print(f"\n{nombre_artista} tiene {datos['seguidores']} seguidores y una popularidad de {datos['popularidad']}.")
    print(f"La canción más popular de {nombre_artista} es '{datos['cancion_popular']['nombre']}' con una popularidad de {datos['cancion_popular']['popularidad']}.")
    print(f"{nombre_artista} tiene {datos['numero_albumes']} álbumes.")

# Comparación y asignación de puntos
metricas = ['seguidores', 'popularidad', 'numero_albumes']
puntos_totales = {artista: 0 for artista in artistas.keys()}

# Comparación de seguidores
puntos = comparar_metricas(artistas, 'seguidores')
for artista in puntos_totales:
    puntos_totales[artista] += puntos[artista]

# Comparación de popularidad general
puntos = comparar_metricas(artistas, 'popularidad')
for artista in puntos_totales:
    puntos_totales[artista] += puntos[artista]

# Comparación de popularidad de la canción más popular
puntos = comparar_popularidad_cancion(artistas)
for artista in puntos_totales:
    puntos_totales[artista] += puntos[artista]

# Comparación de número de álbumes
puntos = comparar_metricas(artistas, 'numero_albumes')
for artista in puntos_totales:
    puntos_totales[artista] += puntos[artista]

# Mostrar la puntuación final y el ganador
print(f"\nPuntuación final:")
for artista, puntos in puntos_totales.items():
    print(f"{artista}: {puntos} puntos")

# Determinar el ganador
artista1, artista2 = list(artistas.keys())
if puntos_totales[artista1] > puntos_totales[artista2]:
    print(f"\n¡{artista1} es la banda más popular!")
elif puntos_totales[artista2] > puntos_totales[artista1]:
    print(f"\n¡{artista2} es la banda más popular!")
else:
    print("\nAmbas bandas son igual de populares")
