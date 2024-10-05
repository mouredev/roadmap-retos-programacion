import requests
import json
from datetime import datetime
import urllib.parse 

client_id = "Your ID"
client_secret = "Your secret"

def getToken():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_secret': client_secret,
        'client_id': client_id
    }
    try:
        result = requests.post("https://id.twitch.tv/oauth2/token",headers=headers,data=data)
        if result.status_code == 200:
            return result.json()['access_token']
        else:
            return None
    except Exception as err:
        print("Error getting token: ")

def getInfo(users:list):
    
    #Get token
    token = getToken()

    users_info = []
    for user in users:
        user_name = str(user).replace(" ","")
        user_name = urllib.parse.quote_plus(user_name)
        #Get Twicth profile for user
        query = f'?login={user_name}'
        header = {
            'Authorization': f'Bearer {token}',
            'Client-Id': client_id
        }
        try:
            #Get channel general info
            result = requests.get('https://api.twitch.tv/helix/users'+query,headers=header)
            if result.status_code == 200:
                user_info = result.json()
                broadcaster_id = user_info['data'][0]['id']
                created_at = user_info['data'][0]['created_at']
                #Get followers 
                query = f'?broadcaster_id={broadcaster_id}'
                result = requests.get("https://api.twitch.tv/helix/channels/followers"+query,headers=header)
                followers = 0
                if result.status_code == 200:
                    followers = result.json()['total']    
                else:
                    print(f'Error getting followers for {user_name}')    
                user_info =  {
                    'user_name': user,
                    'followers': followers,
                    'creation_date': created_at
                }
                users_info.append(user_info)
    
            else:
                 print(f'Error obteniendo cuenta de twitch para {user} con status: {result.status_code}')     
        except:
            print(f'Error obteniendo cuenta twicth para: {user}')

    return users_info     

def order_by_followers(users:list):
    #Order list by followers descending
    new_list = sorted(users,key=lambda x: x['followers'],reverse=True)
    return new_list

def order_by_creation_date(users:list):
    new_list = sorted(users,key=lambda user: user['creation_date'],reverse=True)
    return new_list

users = [
        'Abby', 'Ache', 'Adri Contreras', 'Agustin', 'Alexby', 'Ampeter', 'Ander', 'Ari Gameplays',
        'Arigely', 'Auronplay', 'Axozer', 'Beniju', 'By Calitos', 'Byviruzz', 'Carrera', 'Celopan',
        'Cheto', 'CrystalMolly', 'Dario Eme Hache', 'Dheyo', 'DjMariio', 'Doble', 'Elvisa', 'Elyas360',
        'Folagor', 'Grefg', 'Guanyar', 'Hika', 'Hiper', 'Ibai', 'Ibelky', 'Illojuan', 'Imantado',
        'Irina Isasia', 'JessKiu', 'Jopa', 'JordiWild', 'Kenai Souza', 'Keroro', 'Kidd Keo', 'Kiko Rivera',
        'Knekro', 'Koko', 'KronnoZomber', 'Leviathan', 'Lit Killah', 'Lola Lolita', 'Lolito', 'Luh',
        'Luzu', 'Mangel', 'Mayichi', 'Melo', 'MissaSinfonia', 'Mixwell', 'Mr. Jagger', 'Nate Gentile',
        'Nexxuz', 'Nia', 'Nil Ojeda', 'NissaXter', 'Ollie', 'Orslok', 'Outconsumer', 'Papi Gavi',
        'Paracetamor', 'Patica', 'Paula Gonu', 'Pausenpaii', 'Perxitaa', 'Plex', 'Polispol', 'Quackity',
        'RecueroDP', 'Reven', 'Rivers', 'RobertPG', 'Roier', 'Rojuu', 'Rubius', 'Shadoune', 'Silithur',
        'SpokSponha', 'Spreen', 'Spursito', 'Staxx', 'SuzyRoxx', 'Vicens', 'Vituber', 'Werlyb', 'Xavi',
        'Xcry', 'Xokas', 'Zarcort', 'Zeling', 'Zorman'
    ]
users_info = getInfo(users)

order_followers = order_by_followers(users_info)
print("Participantes ordenados por numero de followers")
for element in order_followers:
    print(f'User: {element['user_name']} followers: {element['followers']}')

list_order_creation = order_by_creation_date(users_info)
print("Participantes ordenados por fecha de creacion del canal")
for element in list_order_creation:
    print(f'User {element['user_name']} creation date: {element['creation_date']}')    