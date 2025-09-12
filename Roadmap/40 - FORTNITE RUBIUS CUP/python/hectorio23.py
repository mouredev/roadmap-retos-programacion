# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import requests

# Función para obtener datos de un usuario de Twitch.
def get_twitch_user_data(username, auth_token):
    url = f"https://api.twitch.tv/helix/users?login={username}"
    headers = {
        'Client-ID': 'YOUR_CLIENT_ID',
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()['data']
        if data:
            return {
                'username': username,
                'followers': get_twitch_followers(data[0]['id'], auth_token),
                'created_at': data[0]['created_at']
            }
        else:
            return {'username': username, 'followers': None, 'created_at': None}
    else:
        raise Exception(f"Error in API request: {response.status_code}")

# Función para obtener el número de seguidores de un usuario de Twitch.
def get_twitch_followers(user_id, auth_token):
    url = f"https://api.twitch.tv/helix/users/follows?to_id={user_id}"
    headers = {
        'Client-ID': 'YOUR_CLIENT_ID',
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['total']
    return None

# Genera el ranking por seguidores y por antigüedad.
def generate_rankings(participants, auth_token):
    user_data = [get_twitch_user_data(user, auth_token) for user in participants]
    
    # Ranking por seguidores.
    by_followers = sorted([u for u in user_data if u['followers'] is not None], key=lambda x: x['followers'], reverse=True)
    
    # Ranking por antigüedad.
    by_creation_date = sorted([u for u in user_data if u['created_at'] is not None], key=lambda x: x['created_at'])
    
    return by_followers, by_creation_date

# Ejemplo de uso:
if __name__ == "__main__":
    participants = ["user1", "user2", "user3"]
    auth_token = "YOUR_AUTH_TOKEN"
    
    followers_ranking, creation_ranking = generate_rankings(participants, auth_token)
    
    print("Ranking por seguidores:")
    for user in followers_ranking:
        print(f"{user['username']} - {user['followers']} seguidores")

    print("\nRanking por antigüedad:")
    for user in creation_ranking:
        print(f"{user['username']} - Creado el {user['created_at']}")
