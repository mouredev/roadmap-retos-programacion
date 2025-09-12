"""
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
 *   que tú quieras, utilizando la información que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
"""

import requests
import json



name = input("Introduce el nombre del usuario de GitHub que quieres consultar: ")
url = "https://api.github.com/users/" + name

answer = requests.get(url)
if answer.status_code == 200:
    user_data = answer.json()
    #print(json.dumps(user_data, indent=4))

    print(f"Nombre de usuario: {user_data["login"]}")
    print(f"Compañia: {user_data["company"]}")
    print(f"Repositorios públicos: {user_data["public_repos"]}")
    print(f"Gits públicos: {user_data["public_gists"]}")
    print(f"Seguidores: {user_data["followers"]}")
    print(f"Seguidos: {user_data["following"]}")

    most_used_languages = dict()
    repos_url = user_data["repos_url"]

    answer = requests.get(repos_url)
    if answer.status_code == 200:
        repos_data = answer.json()
        #print(json.dumps(repos_data, indent=4))

        for repo in repos_data:
            print(f"Nombre del repositorio: {repo["full_name"]}")
            print(f"\tEstrellas: {repo["stargazers_count"]}")
            print(f"\tForks: {repo["forks_count"]}")
            
            if not repo["fork"]:
                languages_url = repo["languages_url"]
                answer = requests.get(languages_url)
                if answer.status_code == 200:
                    languages_data = answer.json()
                    #print(json.dumps(languages_data, indent=4))
                    print(f"\tLenguages utilizados:")
                    for language, bytes in languages_data.items():
                        print(f"\t\t-{language} - {bytes} bytes.")
                        if language in most_used_languages:
                            most_used_languages[language] += bytes
                        else:
                            most_used_languages[language] = bytes
                else:
                    print("Hubo un problema al obtener los lenguajes del repositorio.")
    else:
        print("Problemas al obtener los repositorios del usuario.")
    most_used_languages_sorted = dict(sorted(most_used_languages.items(), key=lambda item: item[1], reverse=True))
    print(f"Lenguages mas utilizados:")
    for index , (lg, bytes) in enumerate(most_used_languages_sorted.items()):
        print(f"{index + 1}.- {lg}: {bytes} bytes")

else:
    print(f"Hubo un problema al obtener la info del usuario")



