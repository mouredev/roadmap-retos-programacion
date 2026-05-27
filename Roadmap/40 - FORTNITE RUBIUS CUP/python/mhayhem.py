# @Author Daniel Grande (Mhayhem)


# ¡Rubius tiene su propia skin en Fortnite!
# Y va a organizar una competición para celebrarlo.
# Esta es la lista de participantes:
# https://x.com/Rubiu5/status/1840161450154692876
#
# Desarrolla un programa que obtenga el número de seguidores en
# Twitch de cada participante, la fecha de creación de la cuenta 
# y ordene los resultados en dos listados.
# - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
#   (NO subas las credenciales de autenticación)
# - Crea un ranking por número de seguidores y por antigüedad.
# - Si algún participante no tiene usuario en Twitch, debe reflejarlo.


import os
import json
import requests
import dotenv
from datetime import datetime

dotenv.load_dotenv()

streamers = [
    "abby","ache","adricontreras","agustin","alexby","ampeter",
    "ander","arigameplays","arigeli","auronplay","axocer","beniju","bycalitos","byviruzz","carrera","celopan",
    "cheeto","crystalmolly","darioemehache","dheylo","djmariio","doble","elvisa","elyas360","folagor","grefg",
    "guanyar","hika","hiper","ibai","ibelky","illojuan","imantado","irinaisasia","jesskiu","jopa",
    "jordiwild","kenaisouza","keroro","kiddkeo","kikorivera","knekro","koko","kronnozomber","leviathan","litkillah",
    "lolalolita","lolito","luh","luzu","mangel","mayichi","melo","missasinfonia","mixwell","mrjagger",
    "nategentile","nexxuz","nia","nilojeada","nissaxter","ollie","orslok","outconsumer","papigavi","paracetamor",
    "patica","paulagoonu","pausenpaii","perxitaa","plex","polispol","quackity","recuerdop","reven","rivers",
    "robertpg","roier","rojuu","rubius","shadoune","silithur","spokspohnha","spreen","spursito","staxx",
    "suzyroxx","vicens","vituber","werlyb","xavi","xcry","xokas","zarcort","zeling","zorman"
]


class Streamer:
    def __init__(self, name: str, id: str, followers: int, created_at: str, twitch_user: bool):
        self.name = name
        self.id = id
        self.followers = followers
        self.created_at = created_at
        self.twitch_user = twitch_user
    
    def __str__(self):
        if not self.twitch_user:
            return f"Nombre: {self.name}, No es usuario de Twitch."
        return f"Nombre: {self.name}, seguidores: {self.followers}, año de creación: {self.created_at}"

def credentials(token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": os.getenv("CLIENT_ID")
    }
    
    return headers

def get_token_api() -> str:
    
    url = "https://id.twitch.tv/oauth2/token"
    
    data = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception(f"ERROR: No se ha obtenido el token. {response.text}.")
    token_info = response.json()
    return token_info["access_token"]

def get_channel_info(array: list, headers: dict) -> list:
    
    for item in array:
        if item.twitch_user:
            url = f"https://api.twitch.tv/helix/channels/followers?broadcaster_id={item.id}"
    
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                return response.status_code
            
            info = response.json()
            item.followers = info['total']
    
    return array

def get_user_info(array: list, headers: dict) -> list:
    participants_object = []
    login_user = {}
    for i in range(0, len(array), 50):
        block = array[i:i + 50]
        params = [("login", name) for name in block]
        url = f"https://api.twitch.tv/helix/users"
        response = requests.get(url, headers=headers, params=params)
        info = response.json()
        login_user.update({
            user['login']: user
            for user in info['data']
        })
    
    
    
    for name in array:
        if name in login_user:
            data = login_user[name]
            date = datetime.strptime(data['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            format_date = date.strftime(("%Y/%m/%d"))
            streamer = Streamer(
                data['login'],
                data['id'],
                0,
                format_date,
                True
            )
        else:
            streamer = Streamer(name, None, None, None, False)
        participants_object.append(streamer)
    return participants_object

def separete_user_active(array: list) -> list:
    inactive_users = [item for item in array if not item.twitch_user]
    active_users = [item for item in array if item.twitch_user]
    
    return active_users, inactive_users

def followers_ranking(array: list) -> list:
    folowers_ranking = sorted(array, key=lambda x: x.followers)
    
    return folowers_ranking

def senority_ranking(array: list) -> list:
    senority_ranking = sorted(array, key=lambda x: datetime.strptime(x.created_at), reverse=False)
    return senority_ranking

def display_Rankings(arrayf: list, arrays: list, arrayi: list):
    positionf = 1
    print("Ranking por seguidores:\n")
    for item in arrayf:
        print(f"{positionf}- {item.name} {item.followers}.\n")
        positionf += 1
    print("Ranking por antigüedad:\n")
    positions = 1
    for item in arrays:
        print(f"{positions}- {item.name} {item.created_at}\n")
        positions += 1
    print("Aquí los usuarios sin twitch:\n")
    for item in arrayi:
        print(f"{item.name}\n")

try:
    headers = credentials(get_token_api())
    participants = get_user_info(streamers, headers)
    participants_update = get_channel_info(participants, headers)
    active, inactive = separete_user_active(participants_update)
    followers = followers_ranking(active)
    senority = senority_ranking(active)
    display_Rankings(followers, senority, inactive)
except TimeoutError:
    print("Tiempo excedido")