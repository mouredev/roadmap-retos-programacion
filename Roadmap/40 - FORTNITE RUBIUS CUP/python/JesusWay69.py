import os, platform, credentials, asyncio, requests
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
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
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo."""

streamers_list = ["Abby", "Ache", "AdriContreras4", "agustin51", "alexby11", "ampeterby7" , "AriGameplays", "Arigeli_",
                 "auronplay","axozer", "beniju03", "bycalitos", "byViruZz" ,"Carreraaa" , "celopan", "crystalmolly",
                 "darioemehache","dheylo", "djmariio", "doble", "elvisayomastercard", "elxokas", "elyas360" , "FolagorLives", 
                 "guanyar", "hika","hiperop", "ibai", "ibelky_", "IlloJuan" ,"imantado" , "irinaisasia", "jesskiu",
                 "jopa","jordiwild", "kenaisouza", "keroro", "TheKiddKeo95" ,"kikorivera" , "knekro", "kokorok", "kronnozomber",
                 "leviathan", "littleragergirl", "lola_lolita", "lolito" ,"lolkilla" , "luzu", "mangel", "mayichi",
                 "meelo", "MissaSinfonia", "mixwell", "mrjagger" ,"NateGentile7" , "nexxuz", "nissaxter", "NoSoyPlex", "OllieGamerz",
                 "orslok", "outconsumer", "papigavi", "paracetamor" ,"patica" , "paulagonu", "pausenpaii", "perxitaa",
                 "polispol1", "quackity", "recuerdop" ,"reven" , "rivers_gg", "robertpg", "roier",
                 "rojuu", "Rubius", "shadoune", "silithur" ,"ElSpreen" , "Spursito", "srcheeto", "staxx",
                 "suzyrox", "TheGrefg", "tvandeR", "Vicens" ,"vitu" , "werlyb", "Xavi", "xcrystal",
                  "zarcort", "Zeling", "ZormanWorld"]

dev_streamers_list = ["afor_digital", "altaskur", "AppleCoding", "CarlosAzaustre", "CarlosGameDeveloper",
                     "CursosDeDesarrollo", "dimaspython", "ElPinguinoDeMario","Guinxu", 
                     "ManzDev", "MelenitasDev", "midudev", "MoureDev", "programacion_es",
                     "r2d2_Coder", "RafaLagoon", "RothioTome", "todocode", "vamoacodear"]

client_id = credentials.client_id_v3
secret_id = credentials.secret_id_v3

def get_token(client_id, client_secret) -> str:
    url = 'https://id.twitch.tv/oauth2/token'

    response = requests.post(url, data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    })

    if response.status_code != 200:
        return f"Error token: {response.status_code}"
        
    result = response.json()
    if result['token_type'] != "bearer":
        raise Exception("Unexpected token type")
    return result.get("access_token")

async def get_user_data(channel:str) -> tuple:
    client = await Twitch(client_id,secret_id)
    user = await first(client.get_users(logins=channel))
    if user == None:
        return None, None, None
    return user.id, user.display_name, user.created_at


def get_followers(id, token, client_id) -> int:
    url = f'https://api.twitch.tv/helix/channels/followers'

    response = requests.get(url, headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {token}'
    }, params={"broadcaster_id":id})

    if response.status_code == 200:
        return response.json().get('total')
        
    else:
        return f"Error data: {response.json()}"

def sort_by_date(streamers:list):
    print("\nSTREAMERS ORDENADOS POR ANTIGÜEDAD")
    print("------------------------------------")
    [print (f"{name}-> Fecha de creación del canal: {date}") for name, date in zip(list((map(lambda streamer: '{:<20}'.format(streamer[0]),
    sorted(streamers, key=lambda streamer: streamer[1])))), list(map(lambda streamer: streamer[1].strftime('%d/%m/%Y'),
    sorted(streamers, key=lambda streamer: streamer[1]))))]

def sort_by_followers(streamers:list):
    print("\nSTREAMERS ORDENADOS POR SEGUIDORES")                                          
    print("--------------------------------------")
    [print (f"{name}-> Seguidores totales: {followers}") for name, followers in zip(list((map(lambda streamer: '{:<20}'.format(streamer[0]),
    sorted(streamers, key=lambda streamer: streamer[2], reverse=True)))), list(map(lambda streamer: streamer[2],
    sorted(streamers, key=lambda streamer: streamer[2], reverse=True))))]

token = get_token(client_id, secret_id)
sorted_list:list = []
print("STREAMERS DE PROGRAMACIÓN EN ESPAÑOL")
print("------------------------------------")
for index, streamer in enumerate(dev_streamers_list):
    sorted_list.append([])
    id, name, since = asyncio.run(get_user_data(streamer))
    followers = get_followers(id, token, client_id)
    if id == None:
        print(f"{index}- Usuario '{streamer}' no encontrado")
        dev_streamers_list.pop(index)
        index+=1
        continue
    print(f"{index+1}- {name}, Antiguedad: {since.day}/{since.month}/{since.year}, Seguidores: {followers}")
    sorted_list[index].append(name)
    sorted_list[index].append(since.strptime(f"{since.day}/{since.month}/{since.year}", "%d/%m/%Y"))
    sorted_list[index].append(followers)

sort_by_date(sorted_list)
sort_by_followers(sorted_list)










