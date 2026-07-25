# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 40 FORTNITE RUBIUS CUP
# ------------------------------------

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

import asyncio
from os import getenv

# https://pytwitchapi.dev/en/stable/
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv

async def get_user_info(user_name, twitch) -> dict:
    user = await first(twitch.get_users(logins=user_name))
    if user is not None:
        followers = await twitch.get_channel_followers(user.id)
        return {"username": user_name, "created_at": user.created_at, "followers": followers.total}

    return {}

def print_rankings(users_data) -> None:
    sort_by_followers = sorted(users_data, key=lambda x: x["followers"], reverse=True)
    sort_by_date = sorted(users_data, key=lambda x: x["created_at"])

    print("\nRanking por número de seguidores:")
    for i, user, in enumerate(sort_by_followers):
        print(f"{i + 1} - {user['username']}: {user['followers']} seguidores")

    print("\nRanking por antigüedad:")
    for i, user, in enumerate(sort_by_date):
        print(f"{i + 1} - {user['username']}: Creado el {user['created_at']}")

async def main(users) -> None:
    load_dotenv()
    twitch = await Twitch(str(getenv("TWITCH_CLIENT_ID")), getenv("TWITCH_CLIENT_SECRET"))
    users_data = []
    not_found_users = []

    print("Obteniendo datos...")
    for name in users:
        user = await get_user_info(name, twitch)
        if user:
            users_data.append(user)
        else:
            not_found_users.append(name)

    print_rankings(users_data)

    if not_found_users:
        print("\nUsuarios no encontrados:")
        for user in not_found_users:
            print(user)

users = [
    "abby", "ache", "adricontreras", "agustin", "alexby", "ampeter", "ander", "arigameplays", 
    "arigeli", "auronplay", "axozer", "beniju", "bycalitos", "byviruzz", "carrera", "celopan", 
    "cheeto", "crystalmolly", "darioemehache", "dheyo",
    "djmario", "doble", "elvisa", "elyas360", "folagor", "grefg", "guanyar", "hika", 
    "hiper", "ibai", "ibelky", "illojuan", "imantado", "irinaisasia", "jesskiu", "jopa", 
    "jordiwild", "kenaisouza", "keroro", "kiddkeo",
    "kikorivera", "knekro", "koko", "kronnozomber", "leviathan", "litkillah", "lolalolita", "lolito", 
    "luh", "luzu", "mangel", "mayichi", "melo", "missasinonia", "mixwell", "mrjagger", 
    "nategentile", "nexxuz", "nia", "nilojeda",
    "nissaxter", "ollie", "orslok", "outconsumer", "papigavi", "paracetamor", "patica", "paulagonu", 
    "pausenpaii", "perxitaa", "plex", "polispol", "quackity", "recuerdop", "reven", "rivers", 
    "robertpg", "roier", "rojuu", "rubius",
    "shadoune", "silithur", "spoksponha", "spreen", "spursito", "staxx", "suzyroxx", "vicens", 
    "vituber", "werlyb", "xavi", "xcry", "xokas", "zarcort", "zeling", "zorman"
]

asyncio.run(main(users))

