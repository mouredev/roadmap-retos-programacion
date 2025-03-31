""" 
# 45 - Github Octoverse 
"""

# https://octoverse.github.com
# Utilizando el API de GitHub, crea un informe asociado a un usuario concreto.

# Se debe poder definir el nombre del usuario sobre el que se va a generar el informe.
# Crea un informe de usuario basándote en las 5 métricas que tú quieras, utilizando la información que te proporciona GitHub. Por ejemplo:
    # Lenguaje más utilizado
    # Cantidad de repositorios
    # Seguidores/Seguidos
    # Stars/forks
    # Contribuciones


import requests
from datetime import datetime

def generate_github_report(username: str):
    
    base_url = "https://api.github.com"
    
    # Get user data
    user_url = f"{base_url}/users/{username}"
    response = requests.get(user_url)
    
    if response.status_code != 200:
        print(f"Error: No se pudo obtener información para el usuario {username}. Código: {response.status_code}")
        return
        
    user_data = response.json()
    
    # Get repositories data
    repos_url = f"{base_url}/users/{username}/repos"
    repos_response = requests.get(repos_url)
    
    if repos_response.status_code != 200:
        print(f"Error: No se pudo obtener los repositorios para {username}")
        repos = []
    else:
        repos = repos_response.json()
    
    # Basic user info
    name = user_data.get("name") or username
    company = user_data.get("company") or "No especificado"
    location = user_data.get("location") or "No especificado"
    bio = user_data.get("bio") or "Sin biografía"
    followers = user_data.get("followers", 0)
    following = user_data.get("following", 0)
    created_at = user_data.get("created_at")
    updated_at = user_data.get("updated_at")  # Fixed typo here
    public_repos = user_data.get("public_repos", 0)
    
    # Format dates
    if created_at:
        created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
    if updated_at:
        updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
    
    # Calculate metrics
    languages = {}
    total_stars = 0
    total_forks = 0
    
    for repo in repos:
        # Count stars and forks
        total_stars += repo.get("stargazers_count", 0)
        total_forks += repo.get("forks_count", 0)
        
        # Count languages
        language = repo.get("language")
        if language:
            languages[language] = languages.get(language, 0) + 1
    
    # Find most used language
    most_used_language = max(languages, key=languages.get) if languages else "No disponible"
    
    # Print the report
    print("\n" + "=" * 50)
    print(f"REPORTE DE GITHUB PARA: {name}")
    print("=" * 50)
    print(f"Trabaja en: {company}")
    print(f"Vive en: {location}")
    print(f"Bio: {bio}")
    print("\n--- MÉTRICAS ---")
    print(f"1. Repositorios públicos: {public_repos}")
    print(f"2. Lenguaje más utilizado: {most_used_language}")
    print(f"3. Seguidores/Seguidos: {followers}/{following}")
    print(f"4. Stars/Forks totales: {total_stars}/{total_forks}")
    print(f"5. Perfil creado el: {created_at}")
    print(f"Última actualización: {updated_at}")
    print("=" * 50)

# Main program
username = input("Ingresa el username del usuario que deseas consultar en GitHub: ")
generate_github_report(username)