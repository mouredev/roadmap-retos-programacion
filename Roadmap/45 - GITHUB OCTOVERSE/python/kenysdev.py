# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 45 GITHUB OCTOVERSE
# ------------------------------------

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
 *   que tú quieras, utilizando la informración que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
"""

import requests
from collections import Counter
import textwrap

class GitHubApi:
    def __init__(self, user_name: str) -> None:
        # El límite es de 60 solicitudes por hora
        url: str = f"https://api.github.com/users/{user_name}"
        self.__user_data: dict = self.__get_json(url)

    def __get_json(self, url: str) -> dict:
        try:
            user_data: dict = requests.get(url).json()
            return user_data
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
            return {}

    def __verify_status(self) -> bool:
        if self.__user_data.get("status") == "404":
            print(f"Usuario '{user_name}' no encontrado.")
            return False
        return True

    def __get_repo_info(self, dt: dict) -> str:
        return textwrap.dedent(f"""
            Lang:  {dt.get("full_name", "Desconocido")}")
            Repo:  {dt.get("language")}")
            Stars: {dt.get("stargazers_count", 0)}")
            Forks: {dt.get("forks_count", 0)}")"""
        )

    def print_basic_info(self) -> None:
        if not self.__verify_status:
            return

        dt: dict = self.__user_data
        print(textwrap.dedent(f"""
            -------------------------------------------
            Nombre:     {dt.get("name", "Desconocido")}
            Creación:   {dt.get("created_at", "Desconocido")}
            Repos:      {dt.get("public_repos", 0)}
            Gists:      {dt.get("public_gists", 0)}
            Seguidores: {dt.get("followers", 0)}
            Seguidos:   {dt.get("following", 0)}
            -------------------------------------------"""
        ))

    def print_repos_info(self):
        if not self.__verify_status:
            return
        
        url: str = self.__user_data.get("repos_url", "None")
        repos_data = self.__get_json(url)
        languages = Counter()

        print("Repositorios publicos:")
        for repo in repos_data:
            language = repo.get("language")
            print(self.__get_repo_info(repo))
            if language:
                languages[language] += 1
        
        most_c, count = languages.most_common(1)[0]
        print(f"________\nTotal de repositorios: '{len(repos_data)}'")
        print(f"El lenguaje más utilizado: '{most_c}'({count})")

if __name__ == "__main__":
    print("Informe sobre los datos del usuario en GitHub")
    user_name: str = input("Usuario: ")
    github = GitHubApi(user_name)
    github.print_repos_info()
    github.print_basic_info()
