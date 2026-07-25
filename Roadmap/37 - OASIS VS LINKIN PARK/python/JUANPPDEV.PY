"""
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
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configura tus credenciales
client_id = 'TU_CLIENT_ID'
client_secret = 'TU_CLIENT_SECRET'

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Función para obtener estadísticas de una banda
def obtener_estadisticas(artista):
    resultados = sp.search(q='artist:' + artista, type='artist')
    artista_info = resultados['artists']['items'][0]
    seguidores = artista_info['followers']['total']
    popularidad = artista_info['popularity']
    top_tracks = sp.artist_top_tracks(artista_info['id'])
    cancion_mas_popular = top_tracks['tracks'][0]['name']
    reproducciones_cancion_mas_popular = top_tracks['tracks'][0]['popularity']
    
    return {
        'seguidores': seguidores,
        'popularidad': popularidad,
        'cancion_mas_popular': cancion_mas_popular,
        'reproducciones_cancion_mas_popular': reproducciones_cancion_mas_popular
    }

# Obtener estadísticas de Oasis y Linkin Park
estadisticas_oasis = obtener_estadisticas('Oasis')
estadisticas_linkin_park = obtener_estadisticas('Linkin Park')

# Comparar resultados
print("Estadísticas de Oasis:", estadisticas_oasis)
print("Estadísticas de Linkin Park:", estadisticas_linkin_park)

# Criterio para determinar la banda más popular
if estadisticas_oasis['seguidores'] > estadisticas_linkin_park['seguidores']:
    print("Oasis es más popular en términos de seguidores.")
else:
    print("Linkin Park es más popular en términos de seguidores.")

if estadisticas_oasis['popularidad'] > estadisticas_linkin_park['popularidad']:
    print("Oasis es más popular en términos de popularidad.")
else:
    print("Linkin Park es más popular en términos de popularidad.")

if estadisticas_oasis['reproducciones_cancion_mas_popular'] > estadisticas_linkin_park['reproducciones_cancion_mas_popular']:
    print("Oasis tiene la canción más popular.")
else:
    print("Linkin Park tiene la canción más popular.")


"""
Explicación
1. Autenticación: Utilizamos SpotifyClientCredentials para autenticar nuestra aplicación.
2. Obtener estadísticas: La función obtener_estadisticas busca al artista, obtiene su número de seguidores, popularidad y la canción más popular.
3. Comparar resultados: Comparamos las estadísticas de Oasis y Linkin Park y mostramos los resultados en la consola.
"""