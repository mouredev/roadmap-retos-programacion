"""
# 40 - Fornite Rubius
"""
import requests
import json
from dotenv import load_dotenv
import os
import time

# Lista de participantes
participants = [
    "ABBY","DJMARIIO", "KIKO RIVERA", "NISSAXTER", "SHADOUNE", "ACHE", "DOBLE", "KNEKRO", 
    "OLLIE", "SILITHUR", "ADRI CONTRERAS", "ELVISA", "KOKO", "ORSLOK", "SPOKSPONHA", 
    "AGUSTIN", "ELYAS360", "KRONNOZOMBER", "OUTCONSUMER", "SPREEN","ALEXBY","FOLAGOR",
    "LEVIATHAN","PAPI GAVI","SPURSITO","AMPETER","GREFG","LIT KILLAH","PARACETAMOR",
    "STAXX","ANDER","GUANYAR","LOLA LOLITA","PATICA","SUZYROXX","ARI GAMEPLAYS","HIKA",
    "LOLITO","PAULA GONU","VICENS","ARIGELI","HIPER","LUH","PAUSENPAII","VITUBER",
    "AURONPLAY","IBAI","LUZU","PERXITAA","WERLYB","AXOZER","IBELKY","MANGEL","PLEX",
    "XAVI","BENIJU","ILLOJUAN","MAYICHI","POLISPOL","XCRY","BY CALITOS","IMANTADO",
    "MELO","QUACKITY","XOKAS","BYVIRUZZ","IRINA ISASIA","MISSASINFONIA","RECUERDOP",
    "ZARCORT","CARRERA","JESSKIU","MIXWELL","REVEN","ZELING","CELOPAN","JOPA","MR.JAGGER",
    "RIVERS","ZORMAN","CHEETO","JORDIWILD","NATE GENTILE","ROBERTPG","CRYSTALMOLLY",
    "KENAI SOUZA","NEXXUZ","ROIER","DARIO EMEHACHE","KERORO","NIA","ROJUU","DHEYLO",
    "KIDD KEO","NIL OJEDA","RUBIUS"
]

# Cargar credenciales del archivo .env
load_dotenv()
CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

# Validar credenciales
if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Las credenciales de Twitch no están configuradas en el archivo .env")

def get_app_access_token():
    """Obtener el token de acceso para la API de Twitch"""
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        token_data = response.json()
        access_token = token_data["access_token"]
        print("Token de acceso obtenido correctamente")
        return access_token
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el token: {e}")
        return None

def get_user_info(username, access_token):
    """
    Obtiene información de un usuario de Twitch incluyendo ID, nombre y fecha de creación
    """
    url = 'https://api.twitch.tv/helix/users'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }
    params = {'login': username.lower()}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['data'] and len(data['data']) > 0:
            user = data['data'][0]
            # Obtener el recuento de seguidores
            follower_count = get_follower_count(user['id'], access_token)
            
            return {
                'id': user['id'],
                'display_name': user['display_name'],
                'followers': follower_count,
                'created_at': user['created_at']
            }
        print(f"Usuario no encontrado: {username}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar {username}: {e}")
        return None

def get_follower_count(user_id, access_token):
    """
    Obtiene el número de seguidores de un usuario usando su ID
    """
    url = 'https://api.twitch.tv/helix/users/follows'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }
    params = {'to_id': user_id}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('total', 0)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener seguidores: {e}")
        return 0

def create_rankings(participants, access_token):
    """
    Crea y muestra rankings de streamers por número de seguidores y antigüedad
    """
    user_data = []
    total = len(participants)
    
    print(f"Obteniendo datos de {total} participantes...")
    
    for i, participant in enumerate(participants, 1):
        print(f"Procesando ({i}/{total}): {participant}")
        info = get_user_info(participant, access_token)
        
        if info:
            user_data.append({
                'username': participant,
                'display_name': info['display_name'],
                'followers': info['followers'],
                'created_at': info['created_at']
            })
        else:
            user_data.append({
                'username': participant,
                'display_name': participant,
                'followers': 0,
                'created_at': None
            })
        
        # Añadir pequeña pausa para evitar límites de rate
        time.sleep(0.5)
    
    # Ranking por seguidores (descendente)
    followers_ranking = sorted(user_data, key=lambda x: x['followers'], reverse=True)
    print("\nRanking por número de seguidores:")
    for i, user in enumerate(followers_ranking, 1):
        print(f"{i}. {user['display_name']} - Seguidores: {user['followers']}")
    
    # Ranking por antigüedad (fecha de creación más antigua primero)
    antiquity_ranking = sorted(
        user_data, 
        key=lambda x: x['created_at'] or '9999-12-31', 
        reverse=False
    )
    print("\nRanking por antigüedad:")
    for i, user in enumerate(antiquity_ranking, 1):
        created_at = user['created_at'] or 'No disponible'
        print(f"{i}. {user['display_name']} - Fecha de creación: {created_at}")

def main():
    """Función principal"""
    # Obtener token de acceso
    access_token = get_app_access_token()
    if not access_token:
        print("No se pudo continuar sin token de acceso.")
        return
    
    # Crear rankings
    create_rankings(participants, access_token)

if __name__ == '__main__':
    main()