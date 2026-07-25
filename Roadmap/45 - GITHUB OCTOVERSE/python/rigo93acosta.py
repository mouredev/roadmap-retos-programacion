"""
/*
 * EJERCICIO:
 * GitHub ha publicado el Octoverse 2024, el informe
 * anual del estado de la plataforma:
 * https://octoverse.github.com
 *
 * Utilizando el API de GitHub, crea un informe asociado
 * a un usuario concreto.
 * 
 * - Se debe poder definir el nombre del usuario
 *   sobre el que se va a generar el informe.
 *   
 * - Crea un informe de usuario basándote en las 5 métricas
 *   que tú quieras, utilizando la informración que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
 */
"""

import requests
from collections import defaultdict

base_url = "https://api.github.com/users/"

def get_user_info(username):
    
    user_data = requests.get(base_url + username).json()
    
    if "status" in user_data and user_data["status"] == "404":
        return None
    else:
        return user_data

def get_info_basic(data):

    print(f"Name: {data.get('name', 'No name')}")
    print(f"Company: {data.get('company', 'No company')}")
    print(f"Total de repos: {data.get('public_repos', 0)}")
    print(f"Followers: {data.get('followers', 0)}")
    print(f"Following: {data.get('following', 0)}")

def get_info_repos(repos_url):
    ## Esta peticion se puede paginar si el usuario 
    ## tiene muchos repositorios
    repos_data = requests.get(repos_url).json()
    my_langauges = defaultdict(int)

    for repo in repos_data:
        lang = repo.get("language", "No language")
        my_langauges[lang] += 1
        print(f'\nRepo: {repo.get("full_name", "No name")}')
        print(f'Stars: {repo.get("stargazers_count", 0)}')
        print(f'Forks: {repo.get("forks_count", 0)}')

    most_lang = sorted(my_langauges.items(), 
                       key=lambda x: x[1], 
                       reverse=True)[0][0]
    
    print(f"\nLenguajes utilizados: {most_lang}")
if __name__ == "__main__":

    username = input("Introduce el nombre de usuario de GitHub: ")
    user_info = get_user_info(username)

    if user_info != None:
        print(f"Informe para el usuario: {username}")
        get_info_basic(user_info)
        repos_url = user_info["repos_url"]
        get_info_repos(repos_url)

    else:
        print(f"El usuario {username} no existe")