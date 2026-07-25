import requests

class GitHubUserReport:
    def __init__(self, username: str):
        self.username = username
        self.base_api_url = "https://api.github.com"
        self.headers = {
            "User-Agent": "GitHub-Report-App",
            "Accept": "application/vnd.github.v3+json"
        }

    def api_request(self, endpoint: str):
        url = f"{self.base_api_url}{endpoint}"
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise Exception(f"Error al conectar con la API de GitHub (HTTP {response.status_code}). Verifica el nombre de usuario.")

        return response.json()

    def get_user_info(self):
        return self.api_request(f"/users/{self.username}")

    def get_user_repos(self):
        return self.api_request(f"/users/{self.username}/repos")

    def generate_report(self):
        try:
            user_info = self.get_user_info()
            repos = self.get_user_repos()

            total_repos = len(repos)
            followers = user_info.get("followers", 0)
            following = user_info.get("following", 0)

            languages = [repo["language"] for repo in repos if repo["language"]]
            language_counts = {}
            for lang in languages:
                language_counts[lang] = language_counts.get(lang, 0) + 1

            top_language = max(language_counts, key=language_counts.get, default="N/A")

            total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
            total_forks = sum(repo.get("forks_count", 0) for repo in repos)

            print(f"=== Informe de GitHub para el usuario: {self.username} ===")
            print(f"Nombre: {user_info.get('name', 'N/A')}")
            print(f"Bio: {user_info.get('bio', 'N/A')}")
            print(f"Ubicación: {user_info.get('location', 'N/A')}")
            print(f"Total de repositorios: {total_repos}")
            print(f"Seguidores: {followers}")
            print(f"Seguidos: {following}")
            print(f"Lenguaje más utilizado: {top_language}")
            print(f"Total de estrellas: {total_stars}")
            print(f"Total de forks: {total_forks}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    username = input("Ingrese el nombre de usuario de GitHub: ").strip()

    if not username:
        print("Debe ingresar un nombre de usuario.")
    else:
        report = GitHubUserReport(username)
        report.generate_report()
