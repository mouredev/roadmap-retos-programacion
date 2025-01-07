import requests


def generate_github_report(username: str):

    base_url = "https://api.github.com"

    user_url = f"{base_url}/users/{username}"
    user_data = requests.get(user_url).json()

    if "status" in user_data and user_data["status"] == "404":
        print(f"Usuario {username} no encontrado.")
        return

    report = {
        "Nombre": user_data.get("name", "Desconocido"),
        "Compañía": user_data.get("company", "Desconocida"),
        "Repositorios públicos": user_data.get("public_repos", 0),
        "Gists": user_data.get("public_gists", 0),
        "Seguidores": user_data.get("followers", 0),
        "Seguidos": user_data.get("following", 0)
    }

    print(f"Informe para el usuario: {username}.")
    for key, value in report.items():
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
    for language_name, language_count in languages.items():
        if language_count > max_count:
            most_used_language = language_name
            max_count = language_count

    print(
        f"\nLenguaje más usado: {
            most_used_language if most_used_language else "Desconocido"}"
    )


username = input("Introduce el nombre de usuario de GitHub: ")
generate_github_report(username)
