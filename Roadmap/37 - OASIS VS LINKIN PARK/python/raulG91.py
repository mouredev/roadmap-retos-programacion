import requests
import json
def getToken()->str:
    token_url = "https://accounts.spotify.com/api/token"
    data = {
        'grant_type':'client_credentials',
        'client_id': "YOUR CLIENT ID",
        'client_secret': "YOUR SECRET"

    }
    result =  requests.post(token_url,data=data)
    return json.loads(result.text)['access_token']
   
def getGroupDetails(groupId:str,name:str):

    artist_info = {
        'name':name,
        'popularity': 0,
        'followers': 0,
        'songs_popularity':0,
        'total_albums':0
    }
    api_url = "https://api.spotify.com/v1/"
    bearer_token = getToken()
    headers = {
        "Authorization": f'Bearer {bearer_token}'
    }

    #Get popularity and followers from artists API
    url = f'{api_url}artists/{groupId}'
    result = requests.get(url=url,headers=headers)

    if result.status_code >= 200 and result.status_code < 300:
        artist_dict = json.loads(result.text)
        artist_info['popularity'] = artist_dict['popularity']
        artist_info['followers'] = artist_dict['followers']['total']
    else:
        print("Connection error")

    #Get averrage  top-tracks popularity
    url = f'{api_url}artists/{groupId}/top-tracks?market=ES'
    result = requests.get(url=url,headers=headers)
    averrage_popularity = 0

    if result.status_code >= 200 and result.status_code < 300:
        tracks = json.loads(result.text)['tracks']
        sum = 0
        for track in tracks:
            sum += track['popularity']
        averrage_popularity = sum / len(tracks)
        artist_info['songs_popularity']=averrage_popularity
    else:
        print("Connection error")

    #Get albums
    url = f'{api_url}artists/{groupId}/albums'

    result = requests.get(url=url,headers=headers)
    if result.status_code >= 200 and result.status_code < 300:
        items = json.loads(result.text)['items']
        artist_info['total_albums'] = len(items)

    else:
        print("Connection error")

    return artist_info

def choose_band(band1:dict,band2:dict)->str:
    band1_count = 0
    band2_count = 0
    if band1['popularity'] > band2['popularity']:
        band1_count += 1
    elif band1['popularity'] < band2['popularity']:
        band2_count += 1

    if band1['followers'] > band2['followers']:
        band1_count += 1
    elif band1['followers'] < band2['followers']:
        band2_count +=1

    if band1['songs_popularity'] > band2['songs_popularity']:
        band1_count += 1
    elif band1['songs_popularity'] < band2['songs_popularity']:
        band2_count += 1

    if band1['total_albums'] > band2['total_albums']   :
        band1_count += 1
    elif band1['total_albums'] < band2['total_albums']:
        band2_count += 1     

    if band1_count > band2_count:
        return band1['name']
    else:
        return band2['name']

    

oasis_id = "2DaxqgrOhkeH0fpeiQq2f4"
linkin_park_id = "6XyY86QOPPrYVGvF9ch6wz"

oasis_details = getGroupDetails(oasis_id,"Oasis")
print('Details for Oasis',oasis_details)
linkin_park = getGroupDetails(linkin_park_id,"Linkin Park")
print("Linkin Park details", linkin_park)

print("Bast band is: ", choose_band(oasis_details,linkin_park))