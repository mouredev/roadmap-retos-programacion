"""
/*
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
 */
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

"""
curl -X POST 'https://id.twitch.tv/oauth2/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'client_id=<your client id goes here>&client_secret=<your client secret goes here>&grant_type=client_credentials'
"""
def get_access_token(client_id: str, client_secret: str) -> str:
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url=url, data=data)

    #Verificar si la respuesta es correcta, se puede hacer con response.raise_for_status() también
    if response.status_code == 200:
        token_data = response.json()
        return token_data.get("access_token")
    else:
        print(f"Error: Unable to get access token. Status Code {response.status_code}.")
        return None
"""
curl -X GET 'https://api.twitch.tv/helix/users?id=141981764' \
-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'
"""
def get_user_info(token: str, client_id: str, login: str):
    url = "https://api.twitch.tv/helix/users"
    headers = {
        "Authorization": f"Bearer {token}", 
        "Client-Id": client_id
    }
    params = {"login": login}

    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json().get("data", []) #Si no hay data, devolver lista vacía, lo hace el ", [])"
    if not data:
        return None
    
    return data[0]

"""
curl -X GET 'https://api.twitch.tv/helix/channels/followers?broadcaster_id=123456' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'
"""
def get_user_followers(token: str, client_id: str, user_id: str) -> int:
    url = "https://api.twitch.tv/helix/channels/followers"
    headers = {
        "Authorization": f"Bearer {token}", 
        "Client-Id": client_id
    }
    params = {"broadcaster_id": user_id}
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("total", 0)

users = [
    "littleragergirl", "ache", "adricontreras4", "agustin51", "alexby11", "ampeterby7", "tvander",
    "arigameplays", "arigeli_", "auronplay", "axozer", "beniju03", "bycalitos",
    "byviruzz", "carreraaa", "celopan", "srcheeto", "crystalmolly", "darioemehache",
    "dheylo", "djmariio", "doble", "elvisayomastercard", "elyas360", "folagorlives", "thegrefg",
    "guanyar", "hika", "hiperop", "ibai", "ibelky_", "illojuan", "imantado",
    "irinaissaia", "jesskiu", "jopa", "jordiwild", "kenaivsouza", "mrkeroro10",
    "thekiddkeo95", "kikorivera", "knekro", "kokoop", "kronnozomberoficial", "leviathan",
    "litkillah", "lolalolita", "lolitofdez", "luh", "luzu", "mangel", "mayichi",
    "melo", "missasinfonia", "mixwell", "jaggerprincesa", "nategentile7", "nexxuz",
    "lakshartnia", "nilojeda", "nissaxter", "olliegamerz", "orslok", "outconsumer", "papigavitv",
    "paracetamor", "patica1999", "paulagonu", "pausenpaii", "perxitaa", "nosoyplex",
    "polispol1", "quackity", "recuerd0p", "reventxz", "rivers_gg", "robertpg", "roier",
    "ceuvebrokenheart", "rubius", "shadoune666", "silithur", "spok_sponha", "elspreen", "spursito",
    "bystaxx", "suzyroxx", "vicens", "vitu", "werlyb", "xavi", "xcry", "elxokas",
    "thezarcort", "zeling", "zormanworld", "mouredev"
]
users_data = []
not_found_users = []

TOKEN = get_access_token(CLIENT_ID, CLIENT_SECRET)

for user_name in users:
    user = get_user_info(TOKEN, CLIENT_ID, user_name)
    if user is None:
        not_found_users.append(user_name)
    else:

        followers = get_user_followers(TOKEN, CLIENT_ID, user.get("id"))
        users_data.append({  
                "username": user_name,
                "created_at": user.get("created_at"),
                "followers": followers
            })
        
#Usuarios no encontrados
print (not_found_users)

#Ordenar por seguidores
users_data.sort(key=lambda x: x["followers"], reverse=True)

print("Ranking por seguidores:")
for id, user, in enumerate(users_data):
    print(f"{id + 1} - {user['username']}: {user['followers']} seguidores")

#Ordenar por antigüedad
users_data.sort(key=lambda x: x["created_at"])

print("Ranking por antigüedad:")
for id, user, in enumerate(users_data):
    print(f"{id + 1} - {user['username']}: {user['created_at']}")




