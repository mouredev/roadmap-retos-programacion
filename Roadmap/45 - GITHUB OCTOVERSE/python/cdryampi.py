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

import aiohttp
import asyncio
from collections import defaultdict

class APIGitHub():
    """
    https://docs.github.com/en/rest?apiVersion=2022-11-28
    """
    __ACCESS_TOKEN = ':)'
    __BASE_URL_API = "https://api.github.com/"
    __HEADERS = None
    __ENDPOINTS = {
        "repos": "users/{owner}/repos",
        "languages": "repos/{owner}/{repo_name}/languages",
        "user": "users/{owner}",
        "commits": 'repos/{owner}/{repo_name}/commits?author={owner}'
    }

    __USER_REPO_DATA = None
    __OWNER = None


    async def clear_data(self) -> None:
        """Función que sirve para limpiar las variables del fetch"""
        self.__USER_REPO_DATA = None
        self.__OWNER = None

    async def set_user(self) -> str:
        if self.__OWNER == None:
            self.__OWNER = input("Intoduce un usuario de github:\n")

    async def get_headers(self) -> dict:
        """Función para obtener la cabecera con el token sacado del settings de una cuenta del github"""
        if self.__HEADERS is None:
            self.__HEADERS = {
                'Authorization': f'token {self.__ACCESS_TOKEN}',
                'Accept': 'application/vnd.github.v3+json'
            }
        return self.__HEADERS

    async def get_total_respos(self, session) -> None:
        """Función para obtener el total de repositorios"""
        headers = await self.get_headers()
        await self.set_user()
        url = f"{self.__BASE_URL_API}{self.__ENDPOINTS['repos']}".format(owner = self.__OWNER)

        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                self.__USER_REPO_DATA = data
            else:
                print(f'Error fetching: {response.status}')

    async def get_user_data(self, session) -> None:
        languages_count = defaultdict(int)
        headers = await self.get_headers()
        await self.get_total_respos(session)

        total_repos = 0
        total_stars = 0
        total_forks = 0
        total_commits = 0

        if self.__USER_REPO_DATA is not None:
            total_repos = len(self.__USER_REPO_DATA)
            for repo in self.__USER_REPO_DATA:
                repo_name = repo['name']
                owner = repo['owner']['login']
                total_stars += repo.get("stargazers_count", 0)
                total_forks += repo.get("forks_count", 0)
                languages_url = f'{self.__BASE_URL_API}{self.__ENDPOINTS['languages']}'.format(owner = owner, repo_name = repo_name)
                commits_url = f"{self.__BASE_URL_API}{self.__ENDPOINTS['commits']}".format(owner = owner, repo_name = repo_name)

                async with session.get(commits_url, headers = headers) as response_commits:
                    if response_commits.status == 200:
                        commits = await response_commits.json()
                        total_commits += len(commits)
                    else:
                        print(f"Error al obtener commits para {repo_name}: {response_commits.status}\nPuede ser que no tengas commits realizados")

                async with session.get(languages_url, headers = headers) as response_languages:
                    if response_languages.status == 200:
                        languages = await response_languages.json()
                        for language, bytes_count in languages.items():
                            languages_count[language] += bytes_count
                    else:
                        print(f"Error fetching: {response_languages.status}")

        await self.print_user_data(session=session, languages_count=languages_count, total_repos=total_repos, total_stars= total_stars, total_forks = total_forks, total_commits= total_commits)
    

    async def print_user_data(self, session, languages_count, total_repos, total_stars, total_forks, total_commits):
        """Función que sirve para pintar los datos del usuario"""
        await self.print_user_info(session)
        if languages_count:
            most_used_language = max(languages_count, key=languages_count.get)
            print(f"El lenguaje más utilizado es: {most_used_language}")
        else:
            print("No se encontraron lenguajes en tus repositorios.")
        print(f'Total de repositorios:{total_repos}')
        print(f"Total de estrellas (stars) en todos los repositorios: {total_stars}")
        print(f"Total de bifurcaciones (forks) en todos los repositorios: {total_forks}")
        print(f"Total de commits realizados: {total_commits}")

    async def print_user_info(self, session):
        headers = await self.get_headers()
        url = f"{self.__BASE_URL_API}{self.__ENDPOINTS['user']}".format(owner = self.__OWNER)
        async with session.get(url, headers =headers) as response:
            if response.status == 200:
                user_info = await response.json()
                print(f"Nombre: {user_info['name']}")
                print(f"Empresa: {user_info['company']}")
                print(f"Ubicación: {user_info['location']}")
                print(f"Bio: {user_info['bio']}")
                print(f"Blog: {user_info['blog']}")
                print(f"Seguidores: {user_info['followers']}")
                print(f"Siguiendo: {user_info['following']}")
            else:
                print(f"Error fetching: {response.status}")


async def main():
    api = APIGitHub()

    async with aiohttp.ClientSession() as session:
        await api.get_user_data(session)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())