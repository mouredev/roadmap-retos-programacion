import base64
import requests

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

def get_access_token():
    auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    return response.json()['access_token']

def get_artist_data(token, artist_name):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f"https://api.spotify.com/v1/search?q={artist_name}&type=artist", headers=headers)
    return response.json()['artists']['items'][0]  
def get_artist_stats(artist_id, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers)
    data = response.json()
    return {
        'name': data['name'],
        'followers': data['followers']['total'],
        'popularity': data['popularity'],
        'genres': data['genres']
    }

def get_artist_top_tracks(artist_id, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US", headers=headers)
    data = response.json()
    most_popular_track = data['tracks'][0]  
    return {
        'name': most_popular_track['name'],
        'playCount': most_popular_track['popularity'],  
        'album': most_popular_track['album']['name']
    }

def compare_bands(band1, band2):
    token = get_access_token()
    
    band1_data = get_artist_data(token, band1)
    band2_data = get_artist_data(token, band2)
    
    band1_stats = get_artist_stats(band1_data['id'], token)
    band2_stats = get_artist_stats(band2_data['id'], token)
    
    band1_top_track = get_artist_top_tracks(band1_data['id'], token)
    band2_top_track = get_artist_top_tracks(band2_data['id'], token)
    
    print(f"\n{band1} Stats:", band1_stats)
    print(f"Canción más popular de {band1}:", band1_top_track)
    
    print(f"\n{band2} Stats:", band2_stats)
    print(f"Canción más popular de {band2}:", band2_top_track)
    
    more_followers = band1 if band1_stats['followers'] > band2_stats['followers'] else band2
    more_popular_track = band1 if band1_top_track['playCount'] > band2_top_track['playCount'] else band2
    
    print(f"\nLa banda con más seguidores es: {more_followers}")
    print(f"La banda con la canción más popular es: {more_popular_track}")

band1 = input("Introduce el nombre del primer grupo: ")
band2 = input("Introduce el nombre del segundo grupo: ")

compare_bands(band1, band2)
