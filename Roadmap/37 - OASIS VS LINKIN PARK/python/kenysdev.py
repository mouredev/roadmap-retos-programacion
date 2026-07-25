# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 37 OASIS VS LINKIN PARK
# ------------------------------------
"""
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

# https://spotipy.readthedocs.io/en/2.24.0/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv

class Spotify:
    def __init__(self):
        load_dotenv() # SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    
    def get_artists(self, name: str) -> dict:
        results = self.sp.search(q='artist:' + name, type='artist', limit=3)
        if not results:
            return {}

        artists = results['artists']['items']
        return artists
    
    def get_most_popular_artist(self, name: str) -> dict:
        artists: dict = self.get_artists(name)
        if not artists:
            return {}

        artists_sorted = sorted(artists, key=lambda x: x['popularity'], reverse=True)
        most_popular_artist = artists_sorted[0]
        return most_popular_artist

    def artist_top_tracks(self, id_artist) -> dict:
        top_track = self.sp.artist_top_tracks(id_artist)
        if not top_track:
            return {}
        return top_track

    def artist_albums(self, id_artist) -> dict:
        albums = self.sp.artist_albums(id_artist, album_type='album')
        if not albums:
            return {}
        return albums
    
class Versus:
    def __init__(self, artist1: dict, artist2: dict, spotify_instance):
        self.a1 = artist1
        self.a2 = artist2
        self.sp = spotify_instance
        self.a1_score = 0
        self.a2_score = 0

    def __popularity(self):
        a1_pop: int = self.a1['popularity']
        a2_pop: int = self.a2['popularity']

        print(f"Popularidad: {a1_pop} vs {a2_pop}")
        if a1_pop > a2_pop:
            self.a1_score += 1
        elif a2_pop > a1_pop:
            self.a2_score += 1
    
    def __followers(self):
        a1_foll: int = self.a1['followers']['total']
        a2_foll: int = self.a2['followers']['total']

        print(f"Seguidores: {a1_foll} vs {a2_foll}")
        if a1_foll > a2_foll:
            self.a1_score += 1
        elif a2_foll > a1_foll:
            self.a2_score += 1

    def __top3_tracks(self):
        a1_top: dict = self.sp.artist_top_tracks(self.a1['id'])
        a2_top: dict = self.sp.artist_top_tracks(self.a2['id'])
        a1_pop: int = sum(track['popularity'] for track in a1_top['tracks'][:3])
        a2_pop: int = sum(track['popularity'] for track in a2_top['tracks'][:3])
        print(f"Popularidad Top 3 canciones: {a1_pop} vs {a2_pop}")

        if a1_pop > a2_pop:
            self.a1_score += 1
        elif a2_pop > a1_pop:
            self.a2_score += 1

    def __albums_and_active_years(self):
        a1_albums: list = self.sp.artist_albums(self.a1['id'])['items']
        a2_albums: list = self.sp.artist_albums(self.a2['id'])['items']
        print(f"Número de álbumes: {len(a1_albums)} vs {len(a2_albums)}")
        if len(a1_albums) > len(a2_albums):
            self.a1_score += 1
        elif len(a2_albums) > len(a1_albums):
            self.a2_score += 1

        a1_years = set(album['release_date'][:4] for album in a1_albums)
        a2_years = set(album['release_date'][:4] for album in a2_albums)
        print(f"Años activos: {len(a1_years)} vs {len(a2_years)}")
        if len(a1_years) > len(a2_years):
            self.a1_score += 1
        elif len(a2_years) > len(a1_years):
            self.a2_score += 1

    def __final_result(self):
        print("\nRESULTADO FINAL:")
        print(f"{self.a1['name']}: {self.a1_score} puntos")
        print(f"{self.a2['name']}: {self.a2_score} puntos")

        if self.a1_score > self.a2_score:
            print(f"\n¡'{self.a1['name']}' gana el versus!")
        elif self.a2_score > self.a1_score:
            print(f"\n¡'{self.a2['name']}' gana el versus!")
        else:
            print("\n¡Es un empate!")

    def start(self):
        print(f"{self.a1['name']} vs {self.a2['name']}")
        self.__popularity()
        self.__followers()
        self.__top3_tracks()
        self.__albums_and_active_years()
        self.__final_result()


def main():
    print("VERSUS")
    sp = Spotify()
    artist1: dict = sp.get_most_popular_artist(name="Oasis")
    artist2: dict = sp.get_most_popular_artist(name="Linkin Park")

    if not artist1 and not artist2:
        print("Artistas no encontrados")
        return

    vs = Versus(artist1, artist2, sp)
    vs.start()
    

if __name__ == "__main__":
    main()

