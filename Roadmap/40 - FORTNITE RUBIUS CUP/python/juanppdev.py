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

import requests

# Configura tus credenciales de Twitch
CLIENT_ID = 'CLIENT_ID'
CLIENT_SECRET = 'CLIENT_SECRET'

# Obtén el token de acceso
def get_access_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    return response.json()['access_token']

# Obtén la información del usuario de Twitch
def get_user_info(username, access_token):
    url = f'https://api.twitch.tv/helix/users?login={username}'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'data' in data and data['data']:
        return data['data'][0]
    else:
        return None

# Lista de participantes
participants = [
    "abby", "djmariio", "kiko rivera", "nissaxter", "shadoune", "ache", "doble", "knekro",
    "ollie", "silithur", "adri contreras", "elvisa", "koko", "orslok", "spokspongha", "agustin",
    "elyas360", "kronnozomber", "outconsumer", "spreen", "alexby", "folagor", "leviathan",
    "papi gavi", "spursito", "ampeter", "grefg", "lit killah", "paracetamor", "staxx", "ander",
    "guanyar", "lola lolita", "patica", "suzyroxx", "ari gameplays", "hika", "lolito", "paula gonu",
    "vicens", "arigeli", "hiper", "luh", "pausenpaii", "vituber", "auronplay", "ibai", "luzu",
    "perxitaa", "werlyb", "axozer", "ibelky", "mangel", "plex", "xavi", "beniju", "illojuan",
    "mayichi", "polispol", "xcry", "by calitos", "imantado", "melo", "quackity", "xokas", "byviruzz",
    "irina isasia", "missasinfonia", "recuerdop", "zarcort", "carrera", "jesskiu", "mixwell",
    "reven", "zeling", "celopan", "jopa", "mr.jagger", "rivers", "zorman", "cheeto", "jordiwild",
    "nate gentile", "robertpg", "crystalmolly", "kenai souza", "nexxuz", "roier", "dario emehache",
    "keroro", "nia", "rojuu", "dheylo", "kidd keo", "nil ojeda", "rubius"
]

access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)

followers_ranking = []
creation_date_ranking = []

for participant in participants:
    user_info = get_user_info(participant, access_token)
    if user_info:
        print(user_info)  # Imprime la información del usuario para verificar las claves disponibles
        followers_ranking.append((participant, user_info.get('view_count', 'N/A')))
        creation_date_ranking.append((participant, user_info['created_at']))
    else:
        print(f"{participant} no tiene usuario en Twitch.")

# Ordenar por número de seguidores (view_count en este caso)
followers_ranking.sort(key=lambda x: x[1], reverse=True)

# Ordenar por fecha de creación
creation_date_ranking.sort(key=lambda x: x[1])

print("Ranking por número de seguidores:")
for user in followers_ranking:
    print(user)

print("\nRanking por antigüedad:")
for user in creation_date_ranking:
    print(user)
