""" /*
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
 */ """

import requests

def generate_github_report(username: str):

    base_url = "https://api.github.com"

    user_url = f"{base_url}/users/{user_name}"
    user_data = requests.get(user_url).json()

    if "status" in user_data and user_data["status"] == "404":
        print(f"Usuario {user_name} no encontrado.")
        return

    report = {
        "name": user_data.get("name", "Desconocido"),
        "company": user_data.get("company", "Desconocida"),
        "public_repos": user_data.get("public_repos", 0),
        "public_gists": user_data.get("public_gists", 0),
        "followers": user_data.get("followers", 0),
        "following": user_data.get("following", 0)
    }

    print(f"Informe del usuario {user_name}:")
    for key,value in report.items():
        print(f"{key}: {value}")

    repos_url = user_data["repos_url"]
    repos_data = requests.get(repos_url).json()

    languages = {}
    
    for repo in repos_data:

        language = repo.get("language")
        if language:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

        print(f"\nRepo: {repo.get("full_name")}")
        print(f"Stars: {repo.get("stargazers_count", 0)}")
        print(f"Forks: {repo.get("forks_count", 0)}")

    most_used_language = None
    max_count = 0
    for name, count in languages.items():
        if count > max_count:
            most_used_language = name
            max_count = count

    print(f"\nLenguaje más usado {most_used_language if most_used_language else "Desconocido"}")



user_name = input("Ingresa el nombre de usuario de GitHub: ")
generate_github_report(user_name)