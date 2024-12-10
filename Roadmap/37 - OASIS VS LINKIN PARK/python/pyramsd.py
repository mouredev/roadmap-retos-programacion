import requests
import base64

client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"

auth_url = 'https://accounts.spotify.com/api/token'
base_url = 'https://api.spotify.com/v1/'

artists = {
    "Oasis": "2DaxqgrOhkeH0fpeiQq2f4",
    "Linkin Park": "6XyY86QOPPrYVGvF9ch6wz"
}

# Función para obtener el token de autenticación
def get_token(client_id, client_secret):
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        'Authorization': f'Basic {b64_auth_str}',
    }
    data = {
        'grant_type': 'client_credentials'
    }
    
    response = requests.post(auth_url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Error en la autenticación. Verifica tus credenciales.")
    
    response_data = response.json()
    return response_data['access_token']

# Función para obtener datos del artista (Oasis y Linkin Park)
def get_artist_data(artist_id, token):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    try:
        artist_url = f'{base_url}artists/{artist_id}'
        artist_data = requests.get(artist_url, headers=headers).json()

        top_tracks_url = f'{base_url}artists/{artist_id}/top-tracks?market=US'
        top_tracks_data = requests.get(top_tracks_url, headers=headers).json()
        
        return artist_data, top_tracks_data
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos del artista: {e}")
        return None, None

def compare_artists(artists_data):
    for artist, data in artists_data.items():
        artist_info, top_tracks = data
        if artist_info and top_tracks:
            print(f"Artista: {artist}")
            print(f"Seguidores: {artist_info['followers']['total']}")
            print(f"Popularidad: {artist_info['popularity']}")
            print(f"Canción más popular: {top_tracks['tracks'][0]['name']} - {top_tracks['tracks'][0]['popularity']} popularidad\n")
        else:
            print(f"No se pudo obtener datos para {artist}")

def main():
    # Obtener el token de acceso
    token = get_token(client_id, client_secret)
    
    # Obtener datos
    artists_data = {}
    for artist_name, artist_id in artists.items():
        artist_info, top_tracks = get_artist_data(artist_id, token)
        artists_data[artist_name] = (artist_info, top_tracks)
    
    compare_artists(artists_data)

if __name__ == "__main__":
    main()
    
