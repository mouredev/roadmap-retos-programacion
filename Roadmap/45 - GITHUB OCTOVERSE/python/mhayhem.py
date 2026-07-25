# @Author Daniel Grande (Mhayhem)

# EJERCICIO:
# GitHub ha publicado el Octoverse 2024, el informe
# anual del estado de la plataforma:
# https://octoverse.github.com
#
# Utilizando el API de GitHub, crea un informe asociado
# a un usuario concreto.
# 
# - Se debe poder definir el nombre del usuario
#   sobre el que se va a generar el informe.
#   
# - Crea un informe de usuario basándote en las 5 métricas
#   que tú quieras, utilizando la información que te
#   proporciona GitHub. Por ejemplo:
#   - Lenguaje más utilizado
#   - Cantidad de repositorios
#   - Seguidores/Seguidos
#   - Stars/forks
#   - Contribuciones
#   (lo que se te ocurra)

import requests
import json
import dotenv
import os

dotenv.load_dotenv()

def get_user_info():
    username = input("Nombre de usuario: ")
    token = os.getenv('TOKEN')
    url = f"https://api.github.com/users/{username}"
    
    if not token:
        print("No se ha encontrado ningún token")
    
    headers = {"Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"}
    
    count_language = {}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        languages_dev = requests.get(url + "/repos", headers=headers)
        language_data = languages_dev.json()
        for item in language_data:
            if item["language"] != None:
                if item["language"] not in count_language:
                    count_language.setdefault(item["language"], 1)
                else:
                    count_language[item["language"]] += 1
        
        if count_language:
            favorite_language = max(count_language, key=count_language.get)
        else:
            favorite_language = "Ninguno"
        
        print(f"Nombre: {data['name']}\n"
            f"Repos publicos: {data['public_repos']}\n"
            f"Seguidores: {data['followers']}\n"
            f"Siguiendo: {data['following']}\n"
            f"Lenguaje mas utilizado: {favorite_language}"
            )
    
    elif response.status_code == 404:
        print(f"Usuario {username} no encontrado.")
    elif response.status_code == 401:
        print("Token invalido")
    else:
        print(f"ERROR: {response.status_code}")
    
    

get_user_info()

