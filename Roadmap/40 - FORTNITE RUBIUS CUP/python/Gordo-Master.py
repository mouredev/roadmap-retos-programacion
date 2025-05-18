# 40 - Fornite Rubius Cup
import env
import requests

CLIENT_ID = env.CLIENT_ID
CLIENT_SECRET = env.CLIENT_SECRET

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

def get_token(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "client_id" : client_id,
        "client_secret" : client_secret,
        "grant_type" : "client_credentials"
    }
    response = requests.post(url=url, headers= headers, data=data)
    respuesta =response.json()
    return respuesta["access_token"]

def get_user(token,client_id, name):
    url = f"https://api.twitch.tv/helix/users?login={name}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Client-Id' : client_id
        }
    response = requests.get(url,headers=headers)
    return response.json()

def get_followers(token, client_id, id):
    url = f"https://api.twitch.tv/helix/channels/followers?broadcaster_id={id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Client-Id' : client_id
        }
    response = requests.get(url, headers=headers)
    return response.json()["total"]

token = get_token(CLIENT_ID,CLIENT_SECRET)

no_twitch_users = []
twitch_users = []
count = 0
number_users = len(users)
for user in users:
    count += 1
    print(f"[*] Progreso: {count}/{number_users} ({count/number_users*100:.0f}%)",end="\r")
    data = get_user(token,CLIENT_ID,user)
    if not data["data"]:
        no_twitch_users.append(user)
    else:
        followers = get_followers(token,CLIENT_ID,data["data"][0]["id"])
        twitch_users.append(
            {
                "name": user,
                "date_creation" : data["data"][0]["created_at"],
                "followers" : followers
            }
        )

ranking_followers = sorted(twitch_users,key= lambda x: x["followers"],reverse=True)
ranking_date_creation = sorted(twitch_users,key= lambda x: x["date_creation"])

print("\nRanking segun followers:")
for index, streamer in enumerate(ranking_followers):
    print(f"{index+1}. {streamer["name"]} : {streamer["followers"]:,}")
print("\n Ranking segun fecha de creación")
for index, streamer in enumerate(ranking_date_creation):
    print(f"{index+1}. {streamer["name"]} : {streamer["date_creation"]}")

print("\nNo Twitch Users:")
for index, streamer in enumerate(no_twitch_users):
    print(f"{index+1}. {streamer}")