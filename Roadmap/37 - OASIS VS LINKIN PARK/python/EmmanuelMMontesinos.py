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
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Datos de tu cuenta Spotify Developer
API_ID = 'TU_PUBLIC_ID'
API_KEY = 'TU_SECRET_KEY'

credenciales = SpotifyClientCredentials(client_id=API_ID, client_secret=API_KEY)
api = spotipy.Spotify(client_credentials_manager=credenciales)

# Accede a las estadísticas de las dos bandas.
class Grupo:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        try:
            self.resultado = api.search(self.nombre, type='artist')
            self.id = self.resultado["artists"]["items"][0]["id"]
            self.top_canciones = api.artist_top_tracks(self.id,country='es')
            
            seguidores = api.artist(self.id)
            self.seguidores = seguidores['followers']['total']
            self.registro = {}
            check = 0
            self.popular = 0
            self.cancion_top = (self.top_canciones['tracks'][0]['name'],self.top_canciones['tracks'][0]['popularity'])
            for track in self.top_canciones['tracks']:
                if check == 5:
                    break
                else:
                    check += 1
                    track_id = track['id']
                    track_name = track['name']
                    track_info = api.track(track_id)
                    self.popular += int(track_info['popularity'])
                    self.registro[track_name] = track_info['popularity']

            self.popular /= 5
                
        except Exception as e:
            print(f"El grupo {self.nombre} no existe\nError: {e}")

    # Muestra todos los resultados por consola para notificar al usuario
    def mostrar_resultado(self):
        print("-"*10)
        print(f"{self.nombre.upper()}")
        print(f"{self.seguidores} seguidores : {self.popular} popularidad")
        print("-----TOP 5 CANCIONES-----")
        for cancion,rankin in self.registro.items():
            print(f"{cancion} : {rankin} popularidad")
        print("-"*20)
        print()
            

# Compara los resultados de, por lo menos, 3 endpoint
def comparar_grupos(grupo1, grupo2):
    puntuacion_1 = 0
    puntuacion_2 = 0

    # Desarrolla un criterio para seleccionar qué banda es más popular
    print("Criterios de puntuación:")
    print("1. Seguidores")
    print("2. Popularidad")
    print("3. Popularidad de canción más escuchada")
    print()
    print("-"*10)
    # Seguidores
    if grupo1.seguidores > grupo2.seguidores:
        puntuacion_1 += 1
        print(f"{grupo1.nombre} es más seguido que {grupo2.nombre}")
    elif grupo1.seguidores < grupo2.seguidores:
        puntuacion_2 += 1
        print(f"{grupo2.nombre} es más seguido que {grupo1.nombre}")
    # Popularidad
    if grupo1.popular > grupo2.popular:
        puntuacion_1 += 1
        print(f"{grupo1.nombre} es más popular que {grupo2.nombre}")
    elif grupo1.popular < grupo2.popular:
        puntuacion_2 += 1
        print(f"{grupo2.nombre} es más popular que {grupo1.nombre}")
    # Canción mas escuchada
    if grupo1.cancion_top[1] > grupo2.cancion_top[1]:
        puntuacion_1 += 1
        print(f"{grupo1.cancion_top[0]} es más popular que {grupo2.cancion_top[0]}")
    elif grupo1.cancion_top[1] < grupo2.cancion_top[1]:
        puntuacion_2 += 1
        print(f"{grupo2.cancion_top[0]} es más popular que {grupo1.cancion_top[0]}")

    print()
    print("-"*10)

    if puntuacion_1 > puntuacion_2:
        print(f"{grupo1.nombre} es más popular")
    elif puntuacion_1 < puntuacion_2:
        print(f"{grupo2.nombre} es más popular")
    else:
        print("Los grupos tienen la misma puntuación")
        

    
# Prueba
oasis = Grupo('Oasis')
linkin = Grupo('Linkin Park')

oasis.mostrar_resultado()
linkin.mostrar_resultado()

comparar_grupos(oasis,linkin)