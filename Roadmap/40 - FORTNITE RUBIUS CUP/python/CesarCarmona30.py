import requests

def get_access_token(client_id, client_secret):
  url = "https://id.twitch.tv/oauth2/token"
  params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
  }
  response = requests.post(url, params=params)
  response.raise_for_status()
  return response.json().get("access_token")

def get_user_info(token, client_id, login):
  url = "https://api.twitch.tv/helix/users"
  headers ={
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

def get_total_followers(token, client_id, id):
  url = "https://api.twitch.tv/helix/channels/followers"
  headers = {
    "Authorization": f"Bearer {token}",
    "Client-Id": client_id
  }
  params = {"broadcaster_id": id}
  response = requests.get(url, headers=headers, params=params)
  response.raise_for_status()
  return response.json().get("total", 0)

CLIENT_ID = "client_id"
CLIENT_SECRET = "client_secret"

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

for username in users:

  user = get_user_info(token, CLIENT_ID, username)

  if user is None:
    not_found_users.append(username)
  else:
    followers = get_total_followers(token, CLIENT_ID, user["id"])
    users_data.append({
      "username": username,
      "created_at": user["created_at"],
      "followers": followers
        })

sort_by_followers = sorted(
  users_data, key=lambda x: x["followers"], reverse=True)

sort_by_date = sorted(
  users_data, key=lambda x: x["created_at"])

print("\nRanking por número de seguidores:")
for id, user, in enumerate(sort_by_followers):
  print(f"{id + 1} - {user["username"]}: {user["followers"]} seguidores")

print("\nRanking por antigüedad:")
for id, user, in enumerate(sort_by_date):
  print(f"{id + 1} - {user["username"]}: Creado el {user["created_at"]}")

if not_found_users:
  print("\nUsuarios no encontrados:")
  for user in not_found_users:
    print(user)