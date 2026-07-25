"""
 EJERCICIO:
 ¡Dos de las bandas más grandes de la historia están de vuelta!
 Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 Desarrolla un programa que se conecte al API de Spotify y los compare.
 Requisitos:
 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 2. Conéctate al API utilizando tu lenguaje de programación.
 3. Recupera datos de los endpoint que tú quieras.
 Acciones:
 1. Accede a las estadísticas de las dos bandas.
    Por ejemplo: número total de seguidores, escuchas mensuales,
    canción con más reproducciones...
 2. Compara los resultados de, por lo menos, 3 endpoint.
 3. Muestra todos los resultados por consola para notificar al usuario.
 4. Desarrolla un criterio para seleccionar qué banda es más popular.
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class Artist:

    def __init__(self, name: str):
        artists = spotify.search(q='artist:' + name, type='artist')['artists']
        for art in artists['items']:
            if art['name'] == name:
                self.artist_name = name
                self.artist_id = art['id']
                self.artist_image = art['images'][0]['url']
                self.artist_followers = art['followers']['total']
                self.artist_genres = art['genres']
                self.artist_popularity = art['popularity']
                self.artist_songs_url = art['external_urls']['spotify']
            break
        if not self.artist_name:
            raise "Exception: Artista NO encontrado."

    def get_name(self):
        return self.artist_name

    def get_popularity(self):
        return self.artist_popularity

    def get_id(self):
        return self.artist_id

    def get_followers(self):
        return self.artist_followers

    def get_genres(self):
        return self.artist_genres

    def get_image(self):
        return self.artist_image

    def get_albums(self):
        albums = spotify.artist_albums(self.artist_id, country='AR')
        return [x['name'] for x in albums['items'] if x['album_type'] == 'album']

    def get_most_popular_song(self):
        top_tracks = spotify.artist_top_tracks(self.artist_id)
        track = top_tracks["tracks"][0]
        return [track["name"], track["popularity"]]

    def where_listen(self):
        return self.artist_songs_url


class Comparision:

    def __init__(self, artist_1: Artist, artist_2: Artist):
        self.artist_1 = artist_1
        self.artist_2 = artist_2
        self.rank = [0, 0]

    def add_point(self, artist: int):
        self.rank[artist] += 1

    def get_common_genres(self):
        g1 = self.artist_1.get_genres()
        g2 = self.artist_2.get_genres()
        genres = set.intersection(set(g1), set(g2))
        return genres

    def get_most_popular_band(self):
        f1 = self.artist_1.get_popularity()
        f2 = self.artist_2.get_popularity()
        if f1 > f2:
            self.add_point(0)
            return self.artist_1.get_name()
        elif f2 > f1:
            self.add_point(1)
            return self.artist_2.get_name()
        else:
            self.add_point(0)
            self.add_point(1)
            return ""

    def get_most_popular_song(self):
        s1 = self.artist_1.get_most_popular_song()
        s2 = self.artist_2.get_most_popular_song()
        if s1[1] > s2[1]:
            self.add_point(0)
            return [s1[0], self.artist_1.get_name()]
        elif s2[1] > s1[1]:
            self.add_point(1)
            return [s2[0], self.artist_2.get_name()]
        else:
            self.add_point(0)
            self.add_point(1)
            return [s1[0], self.artist_1.get_name(), s2[0], self.artist_2.get_name()]

    def get_most_follwed(self):
        f1 = self.artist_1.get_followers()
        f2 = self.artist_2.get_followers()
        if f1 > f2:
            self.add_point(0)
            return self.artist_1.get_name()
        elif f2 > f1:
            self.add_point(1)
            return self.artist_2.get_name()
        else:
            self.add_point(0)
            self.add_point(1)
            return ""

    def get_greater_number_of_albums(self):
        a1 = self.artist_1.get_albums()
        a2 = self.artist_2.get_albums()
        if a1.__len__() > a2.__len__():
            self.add_point(0)
            return [self.artist_1.get_name(), a1.__len__()]
        elif a2.__len__() > a1.__len__():
            self.add_point(1)
            return [self.artist_2.get_name(), a2.__len__()]
        else:
            self.add_point(0)
            self.add_point(1)
            return [a1.__len__()]

    def get_better_band(self):
        if self.rank[0] > self.rank[1]:
            return self.artist_1.get_name()
        elif self.rank[1] > self.rank[0]:
            return self.artist_2.get_name()
        else:
            return ""

    def get_report(self):
        report = []
        message = f"Las bandas {self.artist_1.get_name()} y {self.artist_2.get_name()} "
        common_genres = ""
        for genre in self.get_common_genres():
            common_genres += genre + ", "
        report.append(message + "tocan en común " + common_genres[:-2] if common_genres else message + "no tienen géneros en común.")

        band = self.get_most_follwed()
        report.append(band + " es la más seguida." if band else "Ambas bandas son igual de seguidas.")

        band = self.get_most_popular_band()
        report.append(band + " es la más popular." if band else "Ambas bandas son igual de populares.")

        song = self.get_most_popular_song()
        if song.__len__() == 2:
            report.append(f"La canción más popular es {song[0]} de {song[1]}")
        else:
            report.append(f"Las canciones más populares son {song[0]} de {song[1]} y {song[2]} de {song[3]}")

        albums = self.get_greater_number_of_albums()
        if albums.__len__() == 2:
            report.append(f"La banda {albums[0]} editó más álbumes ({albums[1]}).")
        else:
            report.append(f"Ambas bandas editaron ({albums[1]}) álbumes.")

        band = self.get_better_band()
        report.append(band + " es la mejor banda." if band else "Ambas bandas son igual de buenas.")

        report.append(f"Escuchá a {self.artist_1.get_name()} en {self.artist_1.where_listen()}")
        report.append(f"Escuchá a {self.artist_2.get_name()} en {self.artist_2.where_listen()}")

        return report


my_client_id = input("Ingresá tu Spotify client_id: ")
my_client_secret = input("Ingresa tu Spotify client_secret: ")

my_creds = SpotifyClientCredentials(client_id=my_client_id, client_secret=my_client_secret)
spotify = spotipy.Spotify(client_credentials_manager=my_creds)

oasis = Artist('Oasis')
lpark = Artist('Linkin Park')

comparision = Comparision(oasis, lpark)
for result in comparision.get_report():
    print(result)
