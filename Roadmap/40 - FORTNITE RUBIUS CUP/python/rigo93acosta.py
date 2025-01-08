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

"""
Tasks:
1. Get the list of participants from the URL
2. Get the number of followers in Twitch for each participant
3. Get the account creation date for each participant
4. Sort the results by number of followers and by account creation date.
"""

## TODO: Borrar luego
CLIENT_ID = ''
CLIENT_SECRET = ''

import requests

"""
curl -X POST 'https://id.twitch.tv/oauth2/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'client_id=<your client id goes here>&client_secret=<your client secret goes here>&grant_type=client_credentials'
"""
def get_access_token(client_id: str, client_secret: str) -> str:
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    
    response = requests.post(url, params=params)
    response.raise_for_status()
    response = response.json().get("access_token")
    return response


"""
curl -X GET 'https://api.twitch.tv/helix/users?id=141981764' \
-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'
"""
def get_user_info(access_token: str, client_id: str, login: str):
    
    url = f'https://api.twitch.tv/helix/users'
    params ={"login": login}
    headers = {
        'Authorization': f"Bearer {access_token}",
        "Client-Id": client_id
        }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json().get("data", None)

    if not data:
        return None
    
    return data[0]

"""
curl -X GET 'https://api.twitch.tv/helix/channels/followers?broadcaster_id=123456' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'
"""
def get_followers(access_token: str, client_id: str, user_id: str) -> int:
        
        url = f'https://api.twitch.tv/helix/channels/followers'
        params ={"broadcaster_id": user_id}
        headers = {
            'Authorization': f"Bearer {access_token}",
            "Client-Id": client_id
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("total", 0)


if __name__ == '__main__':

    # users = ['rubius', 'ibai', 'mouredev']
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
    not_found = []

    token = get_access_token(CLIENT_ID, CLIENT_SECRET)

    for user_name in users:

        user = get_user_info(token, CLIENT_ID, user_name)

        if user is None:
            print(f"User {user_name} not found")
            not_found.append(user_name)
        else:
            followers = get_followers(token, CLIENT_ID, user["id"])
            users_data.append(
                {
                    "user_name": user_name,
                    "created_at": user.get("created_at", ""),
                    "followers": followers
                }
            )

    sorted_followers = sorted(users_data, 
                              key=lambda x: x["followers"], 
                              reverse=True)
    
    sorted_created_at = sorted(users_data, 
                               key=lambda x: x["created_at"], 
                               reverse=False)
    
    print("===Sorted by followers===")
    for num, user in enumerate(sorted_followers):
        print(f"{num + 1} - {user['user_name']}: {user['followers']} followers")

    print("===Sorted by created_at===")
    for num, user in enumerate(sorted_created_at):
        print(f"{num+1} - {user['user_name']}: {user['created_at']}")
