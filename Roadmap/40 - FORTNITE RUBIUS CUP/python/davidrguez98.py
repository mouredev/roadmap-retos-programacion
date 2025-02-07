""" /*
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
``` """

#EJERCICIO

import env
import requests

CLIENT_ID = env.CLIENT_ID
CLIENT_SECRET = env.CLIENT_SECRET

def get_access_token(client_id: str, client_secret: str) -> str:

    url = "https://id.twitch.tv/oauth2/token"

    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, params=params)
    return response.json().get("access_token")

def get_user_info(token: str, client_id: str, login: str):

    url = "https://api.twitch.tv/helix/users"

    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id
    }

    params = {"login": login}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json().get("data", None)
    

    if not data:
        return None
    return data[0]

def get_total_followers(token: str, client_id: str, id: str) -> int:

    url = "https://api.twitch.tv/helix/channels/followers"

    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id
    }

    params = {"broadcaster_id": id}

    response = requests.get(url, headers=headers, params=params)
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

token = get_access_token(CLIENT_ID, CLIENT_SECRET)

for user_name in users:

    user = get_user_info(token, CLIENT_ID, user_name)

    if user is None:
        not_found_users.append(user_name)
    else:
        followers = get_total_followers(token, CLIENT_ID, user["id"])
        users_data.append({
            "user_name": user_name,
            "created_at": user["created_at"],
            "followers": followers
        })

sort_by_followers = sorted(users_data, key=lambda x: x["followers"], reverse=True)
sort_by_date = sorted(users_data, key=lambda x: x["created_at"])

print("Ranking por número de seguidores:")
for id, user, in enumerate(sort_by_followers):
    print(f"{id + 1} - {user["user_name"]}: {user["followers"]} seguidores.")

print()

print("Ranking por antiguedad:")
for id, user, in enumerate(sort_by_date):
    print(f"{id + 1} - {user["user_name"]}: Creado el {user["created_at"]}.")

print()

if not_found_users:
    print("Usuarios no encontrados:")
    for user in not_found_users:
        print(user)
