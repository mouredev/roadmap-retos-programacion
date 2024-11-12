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

class InformeGitHub:
    def __init__(self, username):
        self.username = username
        self.url = f"https://api.github.com/users/{username}"
        self.response = requests.get(self.url)
        self.data = self.response.json()

    def obtener_informe(self):
        return {
            "Nombre": self.data["name"],
            "Avatar": self.data["avatar_url"],
            "Pais": self.data["location"],
            "Bio": self.data["bio"],
            "Empresa": self.data["company"],
            "Seguidores": self.data["followers"],
            "Seguidos": self.data["following"],
            "Repositorios": self.data["public_repos"],
            "Stars": self.data["public_gists"],
        }
    def actualizar_informe(self):
        self.response = requests.get(self.url)
        self.data = self.response.json()
    def imprimir_informe(self):
        informe = self.obtener_informe()
        print(f"Nombre: {informe['Nombre']}")
        print(f"Seguidores: {informe['Seguidores']}")
        print(f"Avatar: {informe['Avatar']}")
        print(f"Bio: {informe['Bio']}")
        print(f"Empresa: {informe['Empresa']}")
        print(f"Seguidos: {informe['Seguidos']}")
        print(f"Repositorios: {informe['Repositorios']}")
        print(f"Stars: {informe['Stars']}")
        print(f"Pais: {informe['Pais']}")

# Prueba

informe_Emmanuel = InformeGitHub("EmmanuelMMontesinos")
informe_Emmanuel.imprimir_informe()
print()
informe_Mouredev = InformeGitHub("MoureDev")
informe_Mouredev.imprimir_informe()