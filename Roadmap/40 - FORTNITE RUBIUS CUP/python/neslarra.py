import twitch
from datetime import timedelta
import requests


my_id = input("Ingresar nro cliente: ")
my_secret = input("Ingresar secret: ")

my_twitch = twitch.Helix(my_id, my_secret, use_cache=True, cache_duration=timedelta(minutes=10))
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

url_token = "https://id.twitch.tv/oauth2/token"
response = requests.post(url_token, params={"client_id": my_id, "client_secret": my_secret, "grant_type": "client_credentials"})
response.raise_for_status()
token = response.json().get("access_token")

url_followers = "https://api.twitch.tv/helix/channels/followers"

users_data = []
for user in my_twitch.users(users):
    dict_ = {"name": user.display_name, "id": user.id, "created": user.created_at, "followers": 0}
    params = {"broadcaster_id": id}
    response = requests.get(url_followers, headers={"Authorization": f"Bearer {token}", "Client-Id": my_id}, params={"broadcaster_id": user.id})
    response.raise_for_status()
    dict_["followers"] = response.json().get("total", 0)
    users_data.append(dict_)

print("\nOrdenado por cantidad ed seguidores")
for x in sorted(users_data, key=lambda x: x["followers"], reverse=True):
    print(x)
print("\n\nOrednado por antigüedad")
for x in sorted(users_data, key=lambda x: x["created"]):
    print(x)
print("\n\nUsuarios que no se encontraron")
print([x for x in users if x not in [y["name"].lower() for y in users_data]])
