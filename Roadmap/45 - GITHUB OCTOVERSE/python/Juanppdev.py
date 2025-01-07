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

def obtener_informe_usuario(usuario, token=None):
    """Genera un informe para un usuario de GitHub."""
    base_url = "https://api.github.com"
    headers = {"Authorization": f"token {token}"} if token else {}

    try:
        # Obtener información básica del usuario
        respuesta_usuario = requests.get(f"{base_url}/users/{usuario}", headers=headers)
        respuesta_usuario.raise_for_status()
        datos_usuario = respuesta_usuario.json()
        
        # Métricas básicas
        nombre = datos_usuario.get("name", "N/A")
        seguidores = datos_usuario.get("followers", 0)
        seguidos = datos_usuario.get("following", 0)
        repos_publicos = datos_usuario.get("public_repos", 0)

        # Obtener los repositorios del usuario
        respuesta_repos = requests.get(f"{base_url}/users/{usuario}/repos", headers=headers, params={"per_page": 100})
        respuesta_repos.raise_for_status()
        repositorios = respuesta_repos.json()

        # Métricas de repositorios
        lenguajes = {}
        estrellas_totales = 0

        for repo in repositorios:
            leng = repo.get("language")
            if leng:
                lenguajes[leng] = lenguajes.get(leng, 0) + 1
            estrellas_totales += repo.get("stargazers_count", 0)

        # Determinar el lenguaje más utilizado
        lenguaje_mas_utilizado = max(lenguajes, key=lenguajes.get, default="N/A")

        # Crear el informe
        informe = f"""
        Informe de Usuario de GitHub: {usuario}
        ---------------------------------
        Nombre: {nombre}
        Seguidores: {seguidores}
        Seguidos: {seguidos}
        Repositorios Públicos: {repos_publicos}
        Lenguaje más utilizado: {lenguaje_mas_utilizado}
        Total de Stars recibidas: {estrellas_totales}
        """
        print(informe)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")

# Ejemplo de uso
usuario = "juanppdev"  # Cambia por el nombre de usuario deseado
token = "TU_TOKEN_PERSONAL"  # Opcional, para evitar límites de la API
obtener_informe_usuario(usuario, token)
