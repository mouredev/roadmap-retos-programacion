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
from dotenv import load_dotenv, find_dotenv
import os
import requests
import json
import aiohttp #para hacer llamadas a la api de forma asincrona
import asyncio


# Cargar automáticamente el archivo .env - find_dotenv buscar automaticamente el directorio donde esta el archivo.
load_dotenv(find_dotenv())

# Obtener las variables de entorno
CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")


def get_token():
    #Url para obtener el token de twitch
    url = "https://id.twitch.tv/oauth2/token"

    #Parametros para la llamada 
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    #Llmada post para obtener el token
    response = requests.post(url, params=params)
    if response.status_code != 200:
        raise Exception("Error obteniendo el token de Twitch.")
    token_data = response.json()

    return token_data['access_token']


async def call_api(session: aiohttp.ClientSession, url, headers):
    async with session.get(url, headers=headers)as answer:
        if answer.status != 200:
            return None
        else:
            return await answer.json()# Tiene que esperar a que reciba los datos y los genere, por eso el await.

async def get_info_users(token: str, users: list):

    usernames_query = "&".join([f"login={user}" for user in usernames[:100]])
    users_info_url = f"https://api.twitch.tv/helix/users?{usernames_query}"

    headers = {
    "Client-ID": CLIENT_ID,
    "Authorization": f"Bearer {token}"
    }

    async with aiohttp.ClientSession() as session:# Se crea la sesion para llamadas asincronas. Session = request
        data_users = await call_api(session, users_info_url, headers)

        if data_users:
            info_users = {
                streamer["display_name"]:{
                    "id": streamer["id"],
                    "fecha": streamer["created_at"],
                    "followers": 0.0
                } for streamer in data_users.get("data", [])
            }
    return info_users

async def get_followers(token:str, info_users):

    async with aiohttp.ClientSession() as session:

        headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {token}"
        }

        tasks = [
            call_api(session, f"https://api.twitch.tv/helix/channels/followers?broadcaster_id={info['id']}", headers)
            for name, info in info_users.items()
        ]

        channel_data = await asyncio.gather(*tasks)

        if channel_data:
            for i, (name, info) in enumerate(info_users.items()):
                channel = channel_data[i]
                if channel:
                    followers = channel["total"]
                    info["followers"] = followers

        return info_users
    

async def get_ranking(participants: list, twitch_users: dict):
    followers = dict(sorted(twitch_users.items(), key=lambda item: item[1]["followers"], reverse=True))
    old = dict(sorted(twitch_users.items(), key=lambda item: item[1]["fecha"]))
    print("Ranking de followers:")
    for i, (name, info) in enumerate(followers.items()):
        print(f"{i+1}. {name} - {info["followers"]} followers")
        participants.remove(name.lower())
    for name in participants:
        print(f"{name} no tiene cuenta de Twitch")
    print("-----------------------------------")
    print("Ranking de antiguedad:")
    for i, (name, info) in enumerate(old.items()):
        print(f"{i+1}. {name} - {info["fecha"]}")
    for name in participants:
        print(f"{name} no tiene cuenta de Twitch")




############################################

usernames = [
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
    "thezarcort", "zeling", "zormanworld"
]


async def main():
    token = get_token()
    info_users = await get_info_users(token, usernames)
    info_users = await get_followers(token, info_users)
    #print(json.dumps(info_users, indent= 4, ensure_ascii=False))
    await get_ranking(usernames, info_users)


asyncio.run(main())