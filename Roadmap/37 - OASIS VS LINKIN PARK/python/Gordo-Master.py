import requests
import env

CLIENT_ID = env.CLIENT_ID
CLIENT_SECRET = env.CLIENT_SECRET

def get_token():
    url = "https://accounts.spotify.com/api/token"
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret" : CLIENT_SECRET
            }

    response = requests.post(url,headers=header, data= data)
    if response.status_code == 200:
        data = response.json()
        return data["access_token"]
    else:
        raise Exception("Error opteniendo el token de spotify ", response.status_code, response.text)


class Artist():
    def __init__(self, name, artist_id):
        self.name = name
        self.artist_id = artist_id
        self.number_followers = 0
        self.popularity = 0
        self.albums = []
        self.album_url = f"https://api.spotify.com/v1/artists/{self.artist_id}/albums?include_groups=album"
        self.most_populars_albums = []
        self.top_track = {}
    

    def get_artist_data(self, access_token):
        url = f"https://api.spotify.com/v1/artists/{self.artist_id}"
        header = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url,headers= header)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.text)

    def get_albums(self,access_token,  url):
        if url == None:
            return
        else:
            header = {
                "Authorization": f"Bearer {access_token}"
            }

            response = requests.get(url,headers= header)

            if response.status_code == 200:
                data = response.json()
                for albums in data["items"]:
                    self.albums.append(
                        {
                            "id" : len(self.albums)+1,
                            "album" : albums["name"],
                            "album_id": albums["id"]
                        }
                    )
                next_item = data["next"]
                self.get_albums(access_token, next_item)
            else:
                print("Error: ", response.status_code, response.text)

    def get_album_popularity(self,access_token, id):
        url = f"https://api.spotify.com/v1/albums/{id}"
        header = {
                "Authorization": f"Bearer {access_token}"
            }
        response = requests.get(url,headers= header)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.text)
    
    def get_top_track(self, access_token):

        url = f"https://api.spotify.com/v1/artists/{self.artist_id}/top-tracks"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Error obteniendo las canciones del artista: {response.json()}."
            )

        results = response.json()

        top_track = max(results["tracks"], key=lambda track: track["popularity"])

        return {
            "name": top_track["name"],
            "popularity": top_track["popularity"]
        }

    def print_profile(self):
        print(f"Perfil de : {self.name}")
        print(f"Numero de seguidores: {self.number_followers}")
        print(f"Popularidad: {self.popularity}")
        print(f"Los albumes mas populares: ")
        # print(json.dumps(self.most_populars_albums,indent=4))
        # print(f"El top tracks: ")
        print(self.top_track)


def three_most_popular(albums: list):
    albums.sort(key = lambda x: x["Popularity"], reverse= True)
    return albums[0],albums[1],albums[2]

def make_artist_profile(artist: Artist, access_token):
    url = artist.album_url
    artist.get_albums(access_token, url)

    for album in artist.albums:
        data = artist.get_album_popularity(access_token, album["album_id"])
        album["Popularity"] = data["popularity"]

    for album in three_most_popular(artist.albums):
        artist.most_populars_albums.append(
            {
                "name": album["album"],
                "Popularity" : album["Popularity"]
            }
        )

    data_2 = artist.get_artist_data(access_token)
    artist.number_followers = data_2["followers"]["total"]
    artist.popularity = data_2["popularity"]
    artist.top_track = artist.get_top_track(access_token)

def search_artist(access_token: str, name: str):
    url = f"https://api.spotify.com/v1/search?q={name}&type=artist&limit=1"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo el artista: {response.json()}."
        )

    results = response.json()
    if results["artists"]["items"]:
        return results["artists"]["items"][0]["id"]
    else:
        raise Exception(
            f"El artista {name} no se ha encontrado."
        )

def main():
    access_token = get_token()
    artist_1 = Artist("Linkin Park", search_artist(access_token, "Linkin Park"))
    artist_2 = Artist("Oasis", search_artist(access_token, "Oasis"))
    make_artist_profile(artist_1, access_token)
    make_artist_profile(artist_2, access_token)
    # linkin_park.print_profile()
    # oasis.print_profile()
    artist_1_counter = 0
    artist_2_counter = 0
    print(f"\nComparación de artistas:\n")
    print(f"{artist_1.name}")
    print(f"{artist_2.name}")

    # Seguidores
    print(f"\nComparación seguidores:\n")
    print(f"Seguidores {artist_1.name}: {artist_1.number_followers}")
    print(f"Seguidores {artist_2.name}: {artist_2.number_followers}")
    if artist_1.number_followers > artist_2.number_followers:
        print(f"{artist_1.name} es más popular en número de seguidores.")
        artist_1_counter += 1
    else:
        print(f"{artist_2.name} es más popular en número de seguidores.")
        artist_2_counter += 1
    
    # Popularidad
    print(f"\nComparación popularidad:\n")
    print(f"Popularidad {artist_1.name}: {artist_1.popularity}")
    print(f"Popularidad {artist_2.name}: {artist_2.popularity}")

    if artist_1.popularity > artist_2.popularity:
        print(f"{artist_1.name} es más popular a nivel general.")
        artist_1_counter += 1
    else:
        print(f"{artist_2.name} es más popular a nivel general.")
        artist_2_counter += 1
    
    # Cancion
    print(f"\nComparación canción:\n")
    print(
        f"Canción {artist_1.top_track["name"]} ({artist_1.name}): {artist_1.top_track["popularity"]} popularidad.")
    print(
        f"Canción {artist_2.top_track["name"]} ({artist_2.name}): {artist_2.top_track["popularity"]} popularidad.")

    if artist_1.top_track["popularity"] > artist_2.top_track["popularity"]:
        print(
            f"La canción {artist_1.top_track["name"]} de {artist_1.name} es más popular.")
        artist_1_counter += 1
    else:
        print(
            f"La canción {artist_2.top_track["name"]} de {artist_2.name} es más popular.")
        artist_2_counter += 1

    # Resultado
    print(f"\nResultado final:\n")
    print(
        f"{artist_1.name if artist_1_counter > artist_2_counter else artist_2.name} es más popular.")

if __name__ == "__main__":
    main()