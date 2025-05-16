#45 { Retos para Programadores } GITHUB OCTOVERSE 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

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

import asyncio
import aiohttp
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.info

async def fetch_github_data(username):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.github.com/users/{username}') as response:
            user_data = await response.json()
        
        async with session.get(f'https://api.github.com/users/{username}/repos') as response:
            repos_data = await response.json()
        
        return user_data, repos_data

async def generate_user_report(username):
    user_data, repos_data = await fetch_github_data(username)

    # Calculate metrics
    most_used_language = None
    total_stars = 0
    total_repos = len(repos_data)
    followers = user_data.get('followers', 0)
    following = user_data.get('following', 1)  # Avoid division by zero
    contributions = user_data.get('contributions', 'N/A')  # This may still be N/A

    # Analyze repositories
    language_count = {}
    for repo in repos_data:
        if 'language' in repo and repo['language']:
            language_count[repo['language']] = language_count.get(repo['language'], 0) + 1
            total_stars += repo.get('stargazers_count', 0)

    if language_count:
        most_used_language = max(language_count, key=language_count.get)

    followers_following_ratio = (followers / following) if following > 0 else 'N/A'
    stars_forks_ratio = (total_stars / total_repos) if total_repos > 0 else 'N/A'

    metrics = [
        {'name': 'Most Used Language', 'key': 'language', 'value': most_used_language or 'N/A'},
        {'name': 'Number of Repositories', 'key': 'public_repos', 'value': total_repos},
        {'name': 'Followers/Following', 'key': 'followers_following_ratio', 'value': f"{followers_following_ratio:.2f}" if isinstance(followers_following_ratio, float) else 'N/A'},
        {'name': 'Stars/Forks', 'key': 'stars_forks_ratio', 'value': stars_forks_ratio},
        {'name': 'Contributions', 'key': 'contributions', 'value': contributions},
    ]

    report = f'GitHub User Report for {username}:\n\n'
    for metric in metrics:
        report += f"{metric['name']}: {metric['value']}\n"

    return report


async def main():
    username = 'mouredev'
    report = await generate_user_report(username)
    log(report)

if __name__ == '__main__':
    asyncio.run(main())

# Output:
"""   
Most Used Language: Swift
Number of Repositories: 30
Followers/Following: 13220.50
Stars/Forks: 1392.8666666666666
Contributions: N/A

"""