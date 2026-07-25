import requests
from collections import Counter

def get_user_info(username):
    # URL base de GitHub API
    base_url = "https://api.github.com/users"
    # Obtener información del usuario
    user_url = f"{base_url}/{username}"
    user_data = requests.get(user_url).json()

    # Obtener la lista de repositorios del usuario
    repos_url = f"{base_url}/{username}/repos"
    repos_data = requests.get(repos_url).json()

    # Métricas a recolectar
    total_repos = user_data.get("public_repos", 0)
    followers = user_data.get("followers", 0)
    following = user_data.get("following", 0)

    # 1. Lenguaje más utilizado
    languages = [repo.get("language") for repo in repos_data if repo.get("language")]
    most_common_language = Counter(languages).most_common(1)[0][0] if languages else "No disponible"

    # 2. Repositorio con más estrellas
    top_starred_repo = max(repos_data, key=lambda x: x.get("stargazers_count", 0), default=None)
    top_repo_name = top_starred_repo.get("name") if top_starred_repo else "No disponible"
    top_repo_stars = top_starred_repo.get("stargazers_count", 0) if top_starred_repo else 0

    # 3. Última fecha de contribución
    recent_commit_url = f"https://api.github.com/users/{username}/events"
    recent_events = requests.get(recent_commit_url).json()
    push_events = [event for event in recent_events if event["type"] == "PushEvent"]
    last_contribution_date = push_events[0]["created_at"] if push_events else "No disponible"

    # Generar informe
    report = {
        "Usuario": username,
        "Repositorios públicos": total_repos,
        "Seguidores": followers,
        "Seguidos": following,
        "Lenguaje más utilizado": most_common_language,
        "Repositorio más popular": {
            "Nombre": top_repo_name,
            "Estrellas": top_repo_stars,
        },
        "Última fecha de contribución": last_contribution_date,
    }

    return report

# Solicitar el nombre de usuario y generar el informe
username = input("Introduce el nombre de usuario de GitHub: ")
user_report = get_user_info(username)

# Imprimir el informe de usuario
for key, value in user_report.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")
