# 45 - Github Octoverse
import requests
import env


def generate_report(name):
    base_url = "https://api.github.com"
    url = f"{base_url}/users/{name}"
    headers = {
        "Accept": "application/vnd.github+json", 
        "Authorization": f"Bearer {env.token}", 
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    basic_info = requests.get(url,headers=headers).json()
    
    if "status" in basic_info and basic_info["status"]=="404":
        print(f"Usuario {username} no encontrado")
        return
    
    report = {
        "Nombre" : basic_info.get("name", "Desconocido"),
        "Compañia" : basic_info.get("company", "Desconocida"),
        "Repositorio públicos" : basic_info.get("public_repos",0),
        "Gists" : basic_info.get("public_gists",0),
        "Seguidores" : basic_info.get("followers",0),
        "Seguidos" : basic_info.get("following",0),
    }

    print(f"Informe del usuario: {username}:")
    for key, value in report.items():
        print(f"{key}: {value}")
    

    repos_url = basic_info["repos_url"]
    repos_data = requests.get(repos_url).json()

    languages = {}

    for repo in repos_data:

        language = repo.get("language", "No especificado")
        if language:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

        print(f"\nRepo: {repo.get("full_name")}")
        print(f"Stars: {repo.get("stargazers_count",0)}")
        print(f"Forks: {repo.get("forks_count",0)}")

    if languages:
        most_used_languages = max(languages,key=languages.get)
    else:
        most_used_languages = "No definido"
    
    print(f"\nEl lenguaje favorito de {username} es: {most_used_languages}")

    print(languages)


username = input("Ingresa el nombre del usuario: ")
generate_report(username)

