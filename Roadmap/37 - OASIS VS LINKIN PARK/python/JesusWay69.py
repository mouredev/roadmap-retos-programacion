import os, platform, spotipy, credentials
from spotipy.oauth2 import SpotifyClientCredentials


if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

"""* EJERCICIO:
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
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
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular."""

client_ID = credentials.client_ID #clave de cliente propia de 32 caracteres
secret_ID = credentials.secret_ID #clave secreta propia de 32 caracteres

ccm = SpotifyClientCredentials(client_id=client_ID, client_secret=secret_ID)
sp = spotipy.Spotify(client_credentials_manager=ccm)


def get_artist(artist_name:str)->object:
    artist = sp.search(q=artist_name, limit=1, type="artist", offset=0)
    if artist == None:
        return f"El artista {artist_name} no existe"
    return artist

def get_artist_stats(artist:object)->tuple:
    total_popularity_songs = 0
    artist_id = artist["artists"]["items"][0]["id"]
    top_songs = sp.artist_top_tracks(artist_id)
    artist_name = artist["artists"]["items"][0]["name"]
    artist_followers = artist["artists"]["items"][0]["followers"]["total"]
    popularity_level = artist["artists"]["items"][0]["popularity"]
    for song in top_songs["tracks"]:
        total_popularity_songs = total_popularity_songs + song["popularity"]

    return artist_name, artist_followers, popularity_level, total_popularity_songs

def print_top_songs(artist:object): 
    artist = artist["artists"]["items"][0]
    print(f"\nCanciones más populares de {artist["name"]}")
    print("************************************************")
    print('{:<30}'.format("   TITULO"), "PUNTUACIÓN")
    top_songs = sp.artist_top_tracks(artist["id"])
    for song in top_songs["tracks"]:
        song_name = song["name"].split(" - ")
        print("- ",'{:<30}'.format(song_name[0]), song["popularity"])
        

def print_artist_stats(artist:object):
    artist = artist["artists"]["items"][0]
    print (f"""\nNombre del artista: {artist["name"]}
Género musical: {artist["genres"][0]}/{artist["genres"][1]}
Número de followers: {artist["followers"]["total"]}
Nivel de popularidad: {artist["popularity"]}""")

def print_albums(artist:object):
    artist = artist["artists"]["items"][0]
    print(f"\nDiscografía de {artist["name"]}:")
    print("**********************************************************************************")
    print('{:<63}'.format("  TITULO"), "AÑO DE LANZAMIENTO")
    albums = sp.artist_albums(artist["id"], album_type="album",offset=0, limit=30)
    for album in albums["items"]:
        print(f"- " '{:<63}'.format(album["name"]), album["release_date"][:4])

def compare(artist1:object, artist2:object):
    name1, followers1, popularity1, popularity_songs1 = get_artist_stats(artist1)
    name2, followers2, popularity2, popularity_songs2 = get_artist_stats(artist2)

    print(f"\n{name1} tiene {followers1} seguidores y su índice de popularidad es de {popularity1} puntos.")
    print(f"\n{name2} tiene {followers2} seguidores y su índice de popularidad es de {popularity2} puntos.")
    print(f"\nLa suma de la puntuación por escuchas de las 10 mejores canciones de {name1} es de: {popularity_songs1} puntos.")
    print(f"\nLa suma de la puntuación por escuchas de las 10 mejores canciones de {name2} es de: {popularity_songs2} puntos.")

    if followers1 > followers2 and popularity1 > popularity2:
        print(f"\n{name1} tiene más seguidores e índice de popularidad que {name2}")
        if popularity_songs1 > popularity_songs2:
            print(f"Además {name1} acumula más puntos que {name2} en las escuchas de sus 10 mejores canciones...")
            print(f"\n..por lo tanto el ganador claro es: {name1.upper()}")
        elif popularity_songs1 == popularity_songs2:
            print(f"En puntuación acumulada de las escuchas de sus 10 mejores canciones están empatados..")
            print(f"\n..aun así el ganador es: {name1.upper()}")
        else:
            print(f"{name2} tiene mejor puntuación en sus 10 mejores canciones pero {name1} ha ganado en todo lo demás..")
            print(f"\n...por lo tanto el ganador es: {name1.upper()}")
            
    elif followers1 < followers2 and popularity1 < popularity2:
        print(f"\n{name2} tiene más seguidores e índice de popularidad que {name1}")
        if popularity_songs1 < popularity_songs2:
            print(f"Además {name2} acumula más puntos que {name1} en las escuchas de sus 10 mejores canciones...")
            print(f"\n..por lo tanto el ganador claro es: {name2.upper()}")
        elif popularity_songs1 == popularity_songs2:
            print(f"En puntuación acumulada de las escuchas de sus 10 mejores canciones están empatados..")
            print(f"\n..aun así el ganador es: {name2.upper()}")
        else:
            print(f"{name1} tiene mejor puntuación en las escuchas de sus 10 mejores canciones pero {name2} ha ganado en todo lo demás..")
            print(f"\n...por lo tanto el ganador es: {name2.upper()}")

    elif followers1 > followers2 and popularity1 < popularity2:
        print(f"\n{name1} tiene más seguidores que {name2} pero este tiene mejor índice de popularidad")
        if popularity_songs1 > popularity_songs2:
            print(f"{name1} acumula más puntos que {name2} en las escuchas de sus 10 mejores canciones y acumula también más seguidores...")
            print(f"\n..aunque {name2} tenga más índice de popularidad el ganador es: {name1.upper()}")
        elif popularity_songs1 == popularity_songs2:
            print(f"En puntuación acumulada de las escuchas de sus 10 mejores canciones están empatados..")
            print(f"\n..no hay un ganador claro, ambos artistas tienen estadísticas muy similares.")
        else:
            print(f"{name2} tiene mejor puntuación en las escuchas de sus 10 mejores canciones que {name1} y ha ganado también en popularidad..")
            print(f"\n...aunque {name1} tenga más seguidores el ganador es: {name2.upper()}")

    elif followers1 < followers2 and popularity1 > popularity2:
        print(f"\n{name2}tiene más seguidores que {name1} pero este tiene mejor índice de popularidad")
        if popularity_songs1 < popularity_songs2:
            print(f"{name2} acumula más puntos que {name1} en las escuchas de sus 10 mejores canciones y acumula también más seguidores...")
            print(f"..aunque {name1} tenga más índice de popularidad el ganador es: {name2.upper()}")
        elif popularity_songs1 == popularity_songs2:
            print(f"En puntuación acumulada de las escuchas de sus 10 mejores canciones están empatados..")
            print(f"\n..no hay un ganador claro, ambos artistas tienen estadísticas muy similares.")
        else:
            print(f"{name1} tiene mejor puntuación en las escuchas de sus 10 mejores canciones que {name2} y ha ganado también en popularidad..")
            print(f"\n...aunque {name2} tenga más seguidores el ganador es: {name1.upper()}")

    elif followers1 < followers2 and popularity1 == popularity2:
        print(f"\n{name2}tiene más seguidores que {name1} pero en índice de popularidad están empatados")
        if popularity_songs1 < popularity_songs2:
            print(f"{name2} acumula más puntos que {name1} en las escuchas de sus 10 mejores canciones y acumula también más seguidores...")
            print(f"..aunque ambos tengan el índice de popularidad empatado el ganador es: {name2.upper()}")
        elif popularity_songs1 == popularity_songs2:
            print(f"En puntuación acumulada de las escuchas de sus 10 mejores canciones están empatados..")
            print(f"\n..no hay un ganador claro, ambos artistas tienen estadísticas muy similares.")
        else:
            print(f"{name1} tiene mejor puntuación en las escuchas de sus 10 mejores canciones que {name2} y han empatado en popularidad..")
            print(f"\n...pero {name2} tiene más seguidores así que no hay un ganador claro.")

    elif followers1 > followers2 and popularity1 == popularity2:
        print(f"\n{name1}tiene más seguidores que {name2} pero en índice de popularidad están empatado")
        if popularity_songs1 < popularity_songs2:
            print(f"{name2} acumula más puntos que {name1} en las escuchas de sus 10 mejores canciones y en popularidad están empatados...")
            print(f"\n...como {name1} tiene más seguidores no hay un ganador claro")
        elif popularity_songs1 == popularity_songs2:
            print(f"En puntuación acumulada de las escuchas de sus 10 mejores canciones están empatados..")
            print(f"\n..no hay un ganador claro, ambos artistas tienen estadísticas muy similares.")
        else:
            print(f"{name1} tiene mejor puntuación en las escuchas de sus 10 mejores canciones que {name2} y han empatado en popularidad..")
            print(f"..y aunque ambos tengan el índice de popularidad empatado el ganador es: {name1.upper()}")  
    print()

    
oasis = get_artist("Oasis")
linkin_park = get_artist("Linkin park")

print_artist_stats(linkin_park)
print_albums(linkin_park)
print_top_songs(linkin_park)

print_artist_stats(oasis)
print_albums(oasis)
print_top_songs(oasis) 

compare(linkin_park, oasis)





