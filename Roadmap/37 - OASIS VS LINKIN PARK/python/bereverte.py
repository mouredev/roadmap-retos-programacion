import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_access_token():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    try:
        response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
        token_info = response.json()
        return token_info['access_token']
    
    except Exception as e:
        print(f"Error obteniendo el access token: {e}")
        return None

def get_artist_data(artist_id, access_token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    try:
        response = requests.get(url, headers=headers)
        artist_data = response.json()
        
        followers = artist_data['followers']['total']
        popularity = artist_data['popularity']
        
        return followers, popularity
    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return None, None

def get_album_data(artist_id, access_token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = {"Authorization": f"Bearer {access_token}"}

    params = {"include_groups": "album"} 
    total_albums = []

    try:    
        while url:
            response = requests.get(url, headers=headers, params=params)
            album_data = response.json()
            total_albums.extend(album_data['items'])
            url = album_data['next']
        
        return len(total_albums)
    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return None

def get_artist_top_tracks(artist_id, access_token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(url, headers=headers)
        top_tracks_data = response.json()
        
        top_track_name = top_tracks_data['tracks'][0]['name']
        top_track_popularity = top_tracks_data['tracks'][0]['popularity']

        return top_track_name, top_track_popularity

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return None, None
    
def compare(follO, follLP, popO, popLP, albumsO, albumsLP, topSongO, topSongLP):

    try:
        if (follO > follLP):
            print("Oasis tiene más seguidores.")
        elif (follO < follLP):
            print("Linkin Park tiene más seguidores.")
        else:
            print("Ambas bandas tienen el mismo número de seguidores.")

        if (popO > popLP):
            print("Oasis tiene una puntuación de popularidad superior.")
        elif (popO < popLP):
            print("Linkin Park tiene una puntuación de popularidad superior.")
        else:
            print("Ambas bandas tienen la misma puntuación de popularidad.")

        if (albumsO > albumsLP):
            print("Oasis sacó más álbumes.")
        elif (albumsO < albumsLP):
            print("Linkin Park sacó más álbumes.")
        else:
            print("Ambas bandas sacaron el mimso número de álbumes.")

        if (topSongO > topSongLP):
            print("La canción más popular es de Oasis.")
        elif (topSongO < topSongLP):
            print("La canción más popular es de Linkin Park.")
        else:
            print("Ambas bandas tienen la mimsa popularidad en su canción más top.")
    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


def main():

    access_token = "BQCTQL7k82YgsiEJWPCUzcQh3KRTr5Vv37bocLQemNTzpV-9iJluHBnEQSPmT9GFOfIXyPG2WfRZN4zZrW7KL6kCwmE4gPJ-4cYA06Cf5FurSiIjI_M"
    oasis_id = "2DaxqgrOhkeH0fpeiQq2f4"
    linkin_park_id = "6XyY86QOPPrYVGvF9ch6wz"

    print("\nOasis:\n")
    followers_Oasis, popularity_Oasis = get_artist_data(oasis_id, access_token)
    print(f"Seguidores: {followers_Oasis}, Popularidad de la banda: {popularity_Oasis}/100")
    albums_Oasis = get_album_data(oasis_id, access_token)
    print(f"Álbumes de estudio totales: {albums_Oasis}")
    top_song_Oasis, top_song_popularity_Oasis = get_artist_top_tracks(oasis_id, access_token)
    print(f"Canción más popular: {top_song_Oasis}, Popularidad de la canción: {top_song_popularity_Oasis}/100")

    print("\nLinkin Park:\n")
    followers_LinkinPark, popularity_LinkinPark = get_artist_data(linkin_park_id, access_token)
    print(f"Seguidores: {followers_LinkinPark}, Popularidad de la banda: {popularity_LinkinPark}/100")
    albums_LinkinPark = get_album_data(linkin_park_id, access_token)
    print(f"Álbumes de estudio totales: {albums_LinkinPark}")
    top_song_LinkinPark, top_song_popularity_LinkinPark = get_artist_top_tracks(linkin_park_id, access_token)
    print(f"Canción más popular: {top_song_LinkinPark}, Popularidad de la canción: {top_song_popularity_LinkinPark}/100")

    print("\n¿Qué banda es más popular?\n")
    compare(followers_Oasis, followers_LinkinPark, popularity_Oasis, popularity_LinkinPark, albums_Oasis, albums_LinkinPark, top_song_popularity_Oasis, top_song_popularity_LinkinPark)


if __name__ == '__main__':
    main()