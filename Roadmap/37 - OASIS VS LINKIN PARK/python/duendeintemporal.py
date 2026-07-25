#37 { Retos para Programadores } OASIS VS LINKIN PARK 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
  * EJERCICIO:
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
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.

"""

log = print

import requests
from flask import Flask, request, redirect, session, jsonify
import os
import base64
import hashlib
import random
import string

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key for session management

CLIENT_ID = "YOUR_CLIENT_ID"
REDIRECT_URI = "YOUR_APP_REDIRECT_URI"
SCOPE = "user-read-private user-read-email user-top-read"

def generate_code_verifier(length=128):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_code_challenge(code_verifier):
    digest = hashlib.sha256(code_verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).decode().rstrip("=")

@app.route('/')
def index():
    code_verifier = generate_code_verifier()
    session['verifier'] = code_verifier
    code_challenge = generate_code_challenge(code_verifier)

    auth_url = (
        f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&"
        f"response_type=code&redirect_uri={REDIRECT_URI}&"
        f"scope={SCOPE}&code_challenge_method=S256&code_challenge={code_challenge}"
    )
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "No authorization code found.", 400

    access_token = get_access_token(code)
    if access_token:
        profile = fetch_profile(access_token)
        oasis_id = get_artist_id(access_token, "Oasis")
        linkin_park_id = get_artist_id(access_token, "Linkin Park")

        oasis_data = get_artist_data(access_token, oasis_id)
        linkin_park_data = get_artist_data(access_token, linkin_park_id)

        oasis_top_tracks = get_top_tracks(access_token, oasis_id)
        linkin_park_top_tracks = get_top_tracks(access_token, linkin_park_id)

        oasis_data['tracks'] = oasis_top_tracks['tracks']
        linkin_park_data['tracks'] = linkin_park_top_tracks['tracks']

        comparison_result = compare_artists(oasis_data, linkin_park_data)
        return jsonify(comparison_result)
    else:
        return "Failed to get access token.", 400

CLIENT_SECRET = "YOUR_CLIENT_SECRET"  # Add your client secret here

def get_access_token(code):
    verifier = session.get('verifier')
    print("Code Verifier:", verifier)
    token_url = 'https://accounts.spotify.com/api/token'
    
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "code_verifier": verifier
    }
    
    response = requests.post(token_url, data=data)

    # Log the response for debugging
    print("Request URL:", token_url)
    print("Request Data:", data)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)

    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        print("Failed to get access token:", response.status_code, response.text)
        return None




def fetch_profile(token):
    response = requests.get("https://api.spotify.com/v1/me", headers={"Authorization": f"Bearer {token}"})
    response.raise_for_status()
    return response.json()

def get_artist_id(token, artist_name):
    response = requests.get(f"https://api.spotify.com/v1/search?q={artist_name}&type=artist", headers={"Authorization": f"Bearer {token}"})
    data = response.json()
    if data['artists']['items']:
        return data['artists']['items'][0]['id']
    return None

def get_artist_data(token, artist_id):
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers={"Authorization": f"Bearer {token}"})
    response.raise_for_status()
    return response.json()

def get_top_tracks(token, artist_id, market='US'):
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={market}", headers={"Authorization": f"Bearer {token}"})
    response.raise_for_status()
    return response.json()

def compare_artists(oasis_data, linkin_park_data):
    comparison = {
        "oasis": {
            "followers": oasis_data['followers']['total'],
            "popularity": oasis_data['popularity'],
            "top_track": oasis_data['tracks'][0] if oasis_data['tracks'] else None
        },
        "linkin_park": {
            "followers": linkin_park_data['followers']['total'],
            "popularity": linkin_park_data['popularity'],
            "top_track": linkin_park_data['tracks'][0] if linkin_park_data['tracks'] else None
        }
    }
    
    # Compare followers
    if comparison['oasis']['followers'] > comparison['linkin_park']['followers']:
        comparison['winner'] = "Oasis is more popular based on followers."
    elif comparison['oasis']['followers'] < comparison['linkin_park']['followers']:
        comparison['winner'] = "Linkin Park is more popular based on followers."
    else:
        comparison['winner'] = "Both artists have the same number of followers."

    # Compare popularity
    if comparison['oasis']['popularity'] > comparison['linkin_park']['popularity']:
        comparison['popularity_winner'] = "Oasis is more popular based on popularity score."
    elif comparison['oasis']['popularity'] < comparison['linkin_park']['popularity']:
        comparison['popularity_winner'] = "Linkin Park is more popular based on popularity score."
    else:
        comparison['popularity_winner'] = "Both artists have the same popularity score."

    # Compare top track popularity
    if comparison['oasis']['top_track'] and comparison['linkin_park']['top_track']:
        if comparison['oasis']['top_track']['popularity'] > comparison['linkin_park']['top_track']['popularity']:
            comparison['top_track_winner'] = "Oasis is more popular based on top track popularity score."
        elif comparison['oasis']['top_track']['popularity'] < comparison['linkin_park']['top_track']['popularity']:
            comparison['top_track_winner'] = "Linkin Park is more popular based on top track popularity score."
        else:
            comparison['top_track_winner'] = "Both artists have the same top track popularity score."
    else:
        comparison['top_track_winner'] = "One or both artists do not have top tracks available."

    return comparison

if __name__ == '__main__':
    app.run(port=5173, debug=True)


