'''
Ejercicio:
Desarrollo un programa que obtenga el numero de seguidores en Twitch de cada participante, la fecha de creacion de la cuenta y ordene los resultados en dos listados.
    * Usa el API de Twitch.
    * Crea un ranking por numero de seguidores y por antiguedad.
    * Si algun participante no tiene usuario en Twitch, debe reflejarlo.
'''

participantes = ["littleragergirl", "ache", "adricontreras4", "agustin51", "alexby11", "ampeterby7", "tvander",
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
    "thezarcort", "zeling", "zormanworld", "mouredev"]

import requests as rq
from datetime import datetime

secret_key = "5ozi6n4wssn6drmdoi7nsmnk215mgx"
client_id = "terbu2vl1e76j9iln3z0bk4k3877z9"


payload = {
    "client_id": client_id,
    "client_secret": secret_key,
    "grant_type": "client_credentials"
}

# Obtenemos el token
response = rq.post("https://id.twitch.tv/oauth2/token", data = payload)
data = response.json()

token = data['access_token']

headers = {
    "Client-ID": client_id,
    "Authorization": f"Bearer {token}"
}

def get_streamer_id(name: str) -> int:
    try:
        response = rq.get(f"https://api.twitch.tv/helix/users?login={name}", headers = headers)
        data = response.json()

        # Verificamos que se haya obtenido informacion
        if not data['data']:
            print(f"El usuario {name} no existe o no posee twitch.")
            return None

        streamer_id = data['data'][0]['id']
        return streamer_id
    except Exception as e:
       print(f"El streamer no existe o ha surgido el siguiente error: {str(e)}")


def get_streamer_followers(streamer_id: int) -> int:

    # Verificamos que el id tiene un valor
    if streamer_id is None:
        return None

    # Hacemos la llamada para obtener la informacion del streamer
    response = rq.get(f"https://api.twitch.tv/helix/channels/followers?broadcaster_id={streamer_id}", headers = headers)
    data = response.json()
    
    # Retornamos el valor total de followers del streamer
    followers = data['total']
    return followers

def get_create_date_streamer(name: str):
    response = rq.get(f"https://api.twitch.tv/helix/users?login={name}", headers = headers)
    data = response.json()

    if not data['data']:
        print("El usuario no existe o no tiene twitch.")
        return None
    
    # Retornamos la fecha de creacion de la cuenta
    creation_date = data['data'][0]['created_at']
    dt_obj = datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%SZ")
    return dt_obj

# Creamos una funcion que pueda obtener los datos de las demas funciones
def get_info_streamers(name: str):
    # Obtenemos los resultados de las demas funciones
    streamer_id = get_streamer_id(name)
    followers = get_streamer_followers(streamer_id)
    creation_date = get_create_date_streamer(name)

    # Verificamos si el usuario existe 
    if followers is None:
        followers = 0
    
    if creation_date is None:
        creation_date = None

   # Retornamos los datos en forma de diccionario
    return {
        "name": name,
        "id": streamer_id,
        "followers": followers,
        "created_date": creation_date 
    }
    
datos_streamers = []
for nombre in participantes:
   info = get_info_streamers(nombre)
   datos_streamers.append(info)

# Imprimimos los datos de los streamers por seguidores y antiguedad
ranking_followers = sorted(datos_streamers, key = lambda x: x['followers'], reverse = True)

ranking_age = sorted(datos_streamers, key = lambda y: y['created_date'] or datetime.max)

# Imprimimos el listado por seguidores
print("---- Listado por seguidores ----")
for i, streamer in enumerate(ranking_followers, 1):
    print(f"{i}. {streamer['name']}")
    if streamer['followers'] == 0:
        print(f"\n{streamer['name']} No existe en Twitch.")
    else:
        print(f"\n{streamer['followers']} seguidores")

    if streamer['created_date'] is None:
        print(f"\n{streamer['name']} No registrado en Twitch.")
    else:
        print(f"\n{streamer['created_date'].strftime('%Y-%m-%d')}")

# Imprimimos el listado por antiguedad
print("---- Listado por antiguedad del canal ----")
for i, streamer in enumerate(ranking_age, 1):
    print(f"{i}. {streamer['name']}")
    if streamer['followers'] == 0:
        print(f"\n{streamer['name']} No existe en Twitch.")
    else:
        print(f"\n{streamer['followers']} seguidores")

    if streamer['created_date'] is None:
        print(f"\n{streamer['name']} No registrado en Twitch.")
    else:
        print(f"\n{streamer['created_date'].strftime('%Y-%m-%d')}")
