#40 { Retos para Programadores } FORTNITE RUBIUS CUP 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
 * EJERCICIO:
 * ¡Rubius tiene su propia skin en Fortnite!
 * Y va a organizar una competición para celebrarlo.
 * Esta es la lista de participantes:
 * https://x.com/Rubiu5/status/1840161450154692876
 *
 * Desarrolla un programa que obtenga el número de seguidores en
 * Twitch de cada participante, la fecha de creación de la cuenta 
 * y ordene los resultados en dos listados.
 * - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
 *   (NO subas las credenciales de autenticación)
 * - Crea un ranking por número de seguidores y por antigüedad.
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo.

"""
log = print

import requests
from datetime import datetime

# Replace here with your Twitch client ID and client secret
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

"""  
We will use https://jpgtoexcel.com/es to extract the list of the participants from the post image related with the first url of the challenge to a Excell file an then incorpore it to a participant list.
"""

participants = [
    'ABBY', 'DJMARIIO', 'KIKO RIVERA', 'NISSAXTER', 'SHADOUNE', 'SILTHURA',
    'ACHE', 'DOBLE', 'KNEKRO', 'OLLI', 'SPOKSPHORA', 'SPREEN', 'ADRI CONTRERAS',
    'ELVISA', 'KOKO', 'OUTCONSUMER', 'PAPI GAVI', 'PARACETAMOR', 'AGUSTIN',
    'ELYAS360', 'KRONONOMZOR', 'LEVIATHAN', 'LT KILAH', 'PATTAC', 'ALEXBY',
    'FOLAGOR', 'LOLA LOLITA', 'PAULA GONI', 'PAUSENPAI', 'PERKITA', 'AMPETER',
    'GREGR', 'LUH', 'MANGEL', 'PLEX', 'QUACKITY', 'ARI GAMEPLAYS', 'HIKA',
    'HIPER', 'ILAI', 'MELO', 'RECEDROP', 'AUXOZER', 'IBELKY', 'ILOI JUAN',
    'MAYICH', 'RIVERS', 'ROBERTP', 'BYCLITOS', 'IMANOTAD', 'IRINA ISAIA',
    'MIKEL', 'ROJER', 'ROHI', 'BYVIRUZZ', 'JESKSU', 'JOPA', 'MR. JAGGER',
    'ROJER', 'RUBIUS', 'CARRERA', 'JORIDWILD', 'KEANI SOUZA', 'NEXUZ',
    'RIVERA', 'ZELIN', 'CHEETO', 'KERSO', 'KIDD KEO', 'NIL OJEDA', 'SUZYROXX',
    'VICENS', 'CRYSTALMOLLY', 'DARIO MELACHE', 'DHEYO', 'MOUREDEV', 'FATZ',
    'BUBBCODE', 'CODETRAIN', 'NINJACODE',
]

import requests
from datetime import datetime
import time

# Replace here with your Twitch client ID and client secret
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

participants = [
    # ... (your list of participants)
]

def get_oauth_token():
    response = requests.post('https://id.twitch.tv/oauth2/token', params={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    })
    return response.json().get('access_token')

def get_user_data(username, token):
    try:
        response = requests.get(f'https://api.twitch.tv/helix/users?login={username}', headers={
            'Client-ID': CLIENT_ID,
            'Authorization': f'Bearer {token}'
        })
        return response.json().get('data', [None])[0]  # Return the first user data
    except Exception as e:
        print(f'Error fetching data for {username}: {e}')
        return None

def get_follower_count(username, token):
    try:
        user_data = get_user_data(username, token)
        if user_data:
            user_id = user_data['id']
            response = requests.get(f'https://api.twitch.tv/helix/users/follows?to_id={user_id}', headers={
                'Client-ID': CLIENT_ID,
                'Authorization': f'Bearer {token}'
            })
            return response.json().get('total', 0)  # Return the total number of followers
    except Exception as e:
        print(f'Error fetching follower count for {username}: {e}')
        return 'N/A'  # Return 'N/A' if there's an error

def fetch_participants_data():
    token = get_oauth_token()
    results = []

    for username in participants:
        user_data = get_user_data(username, token)
        if user_data:
            follower_count = get_follower_count(username, token)
            results.append({
                'username': user_data['login'],
                'followers': follower_count,
                'createdAt': datetime.fromisoformat(user_data['created_at'].replace('Z', '+00:00')),
            })
        else:
            results.append({
                'username': username,
                'followers': 'N/A',
                'createdAt': 'N/A',
            })
        
        # Introduce a delay to avoid hitting rate limits
        time.sleep(1)  # Adjust the sleep time as necessary

    # Sort by followers
    sorted_by_followers = sorted(results, key=lambda x: (x['followers'] == 'N/A', -x['followers'] if isinstance(x['followers'], int) else 0))
    
    # Sort by account creation date
    sorted_by_creation_date = sorted(results, key=lambda x: (x['createdAt'] == 'N/A', x['createdAt'] if isinstance(x['createdAt'], datetime) else datetime.min), reverse=True)

    print('Ranking by Followers:')
    for result in sorted_by_followers:
        print(result)

    print('\nRanking by Account Creation Date:')
    for result in sorted_by_creation_date:
        print(result)

if __name__ == '__main__':
    fetch_participants_data()

