import requests

baseURL = 'https://pokeapi.co/api/v2/pokemon'

def getData(number):
  url = baseURL + '/' + number
  res = requests.get(url)
  data = res.json()
  print('Name: ', data['name'])
  print('ID: ', data['id'])
  print('Weight: ', data['weight'])
  print('Height: ', data['height'])

  types = [type_info['type']['name'] for type_info in data['types']]
  print('Types:', types)

  games = [game['version']['name'] for game in data['game_indices']]
  print('Games:', games)


getData('9')