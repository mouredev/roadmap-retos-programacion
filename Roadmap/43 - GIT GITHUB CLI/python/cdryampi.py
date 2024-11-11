# /*
#  * EJERCICIO:
#  * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
#  *
#  * Desarrolla un CLI (Command Line Interface) que permita 
#  * interactuar con Git y GitHub de manera real desde terminal.
#  * 
#  * El programa debe permitir las siguientes opciones:
#  * 1. Establecer el directorio de trabajo
#  * 2. Crear un nuevo repositorio
#  * 3. Crear una nueva rama
#  * 4. Cambiar de rama
#  * 5. Mostrar ficheros pendientes de hacer commit
#  * 6. Hacer commit (junto con un add de todos los ficheros)
#  * 7. Mostrar el historial de commits
#  * 8. Eliminar rama
#  * 9. Establecer repositorio remoto
#  * 10. Hacer pull
#  * 11. Hacer push
#  * 12. Salir
#  *
#  * Puedes intentar controlar los diferentes errores.
#  */

import os
import subprocess
import http.client
from urllib.parse import urlparse


class Directory:
    __PATH_DIRECTORY = None

    def __init__(self) -> None:
        self.__PATH_DIRECTORY = os.getcwd()

    def select_folder(self) -> None:
        """Selecciona una ruta válida"""
        while self.__PATH_DIRECTORY is None:
            route = input("Introduce una ruta o presiona 0 para usar la carpeta actual:\n")
            self.check_folder(route)

    def check_folder(self, route) -> bool:
        """Establece una carpeta por defecto si no se ha seleccionado ninguna."""
        if route == '0':
            self.__PATH_DIRECTORY = os.getcwd()
            print("Hemos asignado la carpeta por defecto.")
            return True
        elif os.path.isdir(route):
            self.__PATH_DIRECTORY = route
            print(f"Nueva ruta establecida: {self.__PATH_DIRECTORY}")
            return True
        else:
            print("La ruta no es válida.")
            return False

    def clear_path(self) -> None:
        self.__PATH_DIRECTORY = None

    def get_path(self) -> str:
        return self.__PATH_DIRECTORY if self.__PATH_DIRECTORY else "No se ha establecido una ruta."


class CLIControl:
    def __init__(self):
        self.__DIRECTORY = Directory()
        self.__SUBPROCESS = subprocess
        self.__CURRENT_BRANCH = None

    def is_git_initialized(self) -> bool:
        """Verificar si .git existe en el directorio actual"""
        directory_path = self.__DIRECTORY.get_path()
        
        # Asegurarse de que la ruta esté configurada
        if not directory_path or directory_path == "Aún no se ha establecido una ruta.":
            print("No se ha establecido un directorio de trabajo válido.")
            return False
        
        git_path = os.path.join(directory_path, '.git')
        
        # Debug: Imprimir la ruta donde se está buscando la carpeta .git
        print(f"Verificando si existe .git en la ruta: {git_path}")
        
        if os.path.isdir(git_path):
            return True
        else:
            print("Git no está inicializado en este directorio. Utiliza un directorio con un repositorio Git.")
            return False


    def create_repository(self):
        """Crear un repositorio Git en el directorio actual"""
        if not self.is_git_initialized():
            resultado = self.__SUBPROCESS.run(
                ["git", "init"],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
            print(resultado.stdout)
        else:
            print("Ya hay un repositorio Git en el directorio.")

    def create_branch(self, branch_name):
        """Crear una nueva rama"""
        if self.is_git_initialized():
            resultado = self.__SUBPROCESS.run(
                ["git", "branch", branch_name],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
                    # Verificar si la creación de la rama fue exitosa
        if resultado.returncode == 0:
            print(f"La rama '{branch_name}' ha sido creada con éxito.")
        else:
            print("Error al crear la rama:")
            print(resultado.stderr)

    def select_folder_CLI(self):
        """Limpiar todo y volver a pedir carpeta"""
        self.__DIRECTORY.clear_path()
        self.__DIRECTORY.select_folder()
        self.__CURRENT_BRANCH = None

    def status(self):
        """Mostrar archivos pendientes de commit"""
        if self.is_git_initialized():
            resultado = self.__SUBPROCESS.run(
                ["git", "status"],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
            print(resultado.stdout)

    def commit_git(self, msg='Commit desde CLI'):
        """Agregar y hacer commit de todos los cambios"""
        if self.is_git_initialized():
            self.__SUBPROCESS.run(["git", "add", "."], cwd=self.__DIRECTORY.get_path())
            resultado = self.__SUBPROCESS.run(
                ["git", "commit", "-m", msg],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
            print(resultado.stdout)

    def log(self):
        """Mostrar historial de commits"""
        if self.is_git_initialized():
            resultado = self.__SUBPROCESS.run(
                ["git", "log", "--oneline"],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
            print(resultado.stdout)

    def delete_branch(self):
        """Eliminar la rama actual"""
        if self.is_git_initialized():
            # Por si acaso llamamos a la función para seleccionar rama para no eliminar la rama sin querer.
            self.select_remote_or_local_branch()
            if self.__CURRENT_BRANCH:
                resultado = self.__SUBPROCESS.run(
                    ["git", "branch", "-d", self.__CURRENT_BRANCH],
                    capture_output=True,
                    text=True,
                    cwd=self.__DIRECTORY.get_path()
                )
                print(resultado.stdout)
                self.__CURRENT_BRANCH = None
            else:
                print("Selecciona una rama primero.")

    def add_remote(self, url_remote):
        """Establecer un repositorio remoto"""
        if self.is_git_initialized():
            resultado = self.__SUBPROCESS.run(
                ["git", "remote", "add", "origin", url_remote],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
            print(resultado.stdout)

    def select_remote_or_local_branch(self):
        """Función para seleccionar una rama local o remota"""
        if self.is_git_initialized():
            resultado = self.__SUBPROCESS.run(
                ["git", "branch", "-a"],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
            
            # Obtiene la lista de ramas y elimina líneas en blanco
            branches = [branch.strip() for branch in resultado.stdout.splitlines() if branch.strip()]
            
            # Muestra las opciones al usuario de forma numerada
            print("Selecciona la rama que deseas utilizar:")
            for idx, branch in enumerate(branches, 1):
                print(f"{idx}. {branch}")
            
            # Verifica la elección del usuario
            while True:
                try:
                    choice = int(input("Introduce el número de la rama: "))
                    if 1 <= choice <= len(branches):
                        selected_branch = branches[choice - 1].replace("*", "").strip()
                        self.__CURRENT_BRANCH = selected_branch
                        print(f"Has seleccionado la rama: {self.__CURRENT_BRANCH}")
                        break
                    else:
                        print("Número fuera de rango. Por favor, selecciona un número válido.")
                except ValueError:
                    print("Entrada no válida. Por favor, introduce un número.")

    def check_url_github(self, url) -> bool:
        """Comprueba si la URL devuelve un estado 200 o un estado 301 usando http.client."""
        parsed_url = urlparse(url)
        connection = http.client.HTTPConnection(parsed_url.netloc)
        try:
            connection.request("GET", parsed_url.path or "/")
            response = connection.getresponse()
            
            # Verificar el estado
            if response.status == 200 or response.status == 301:
                print(f"Conexión exitosa a {url} (Estado 200).")
                return True
            else:
                print(f"Error: estado {response.status} en {url}.")
                return False
        except Exception as e:
            print(f"Hubo un problema con la solicitud: {e}")
            return False
        finally:
            connection.close()

    def git_pull(self):
        """Hacer pull de la rama actual"""
        if self.is_git_initialized():
            resultado = self.__SUBPROCESS.run(
                ["git", "pull"],
                capture_output=True,
                text=True,
                cwd=self.__DIRECTORY.get_path()
            )
            print(resultado.stdout)

    def git_push(self):
        """Hacer push de la rama actual"""
        if self.is_git_initialized():
            # Asegúrate de que haya una rama seleccionada
            if self.__CURRENT_BRANCH:
                print(f"Intentando hacer push a la rama '{self.__CURRENT_BRANCH}' en el remoto 'origin'...")
                
                # Comprueba si el remoto 'origin' está configurado
                remote_check = self.__SUBPROCESS.run(
                    ["git", "remote", "-v"],
                    capture_output=True,
                    text=True,
                    cwd=self.__DIRECTORY.get_path()
                )
                if 'origin' not in remote_check.stdout:
                    print("El remoto 'origin' no está configurado. Por favor, agrega un repositorio remoto.")
                    return
                
                # Realiza el push
                resultado = self.__SUBPROCESS.run(
                    ["git", "push", "-u", "origin", self.__CURRENT_BRANCH],
                    capture_output=True,
                    text=True,
                    cwd=self.__DIRECTORY.get_path()
                )
                
                # Verifica la salida y los errores
                if resultado.returncode == 0:
                    print("Push exitoso:")
                    print(resultado.stdout)
                else:
                    print("Error al hacer push:")
                    print(resultado.stderr)
            else:
                print("Selecciona una rama primero.")


    def menu(self):
        """Menú interactivo"""
        while True:
            print("\nSelecciona una opción:")
            print("1. Establecer directorio de trabajo")
            print("2. Crear repositorio")
            print("3. Crear rama")
            print("4. Cambiar de rama")
            print("5. Mostrar ficheros pendientes de commit")
            print("6. Hacer commit")
            print("7. Mostrar historial de commits")
            print("8. Eliminar rama")
            print("9. Establecer repositorio remoto")
            print("10. Hacer pull")
            print("11. Hacer push")
            print("12. Salir")

            opcion = input("Opción: ")
            match opcion:
                case '1':
                    self.select_folder_CLI()
                case '2':
                    self.create_repository()
                case '3':
                    branch_name = input("Nombre de la nueva rama: ")
                    self.create_branch(branch_name)
                case '4':
                    self.select_remote_or_local_branch()
                case '5':
                    self.status()
                case '6':
                    msg = input("Mensaje de commit: ")
                    self.commit_git(msg)
                case '7':
                    self.log()
                case '8':
                    self.delete_branch()
                case '9':
                    url = input("URL del repositorio remoto: ")
                    if self.check_url_github(url):
                        self.add_remote(url)
                    else:
                        print("URL no válida. No se ha establecido el remoto.")
                case '10':
                    self.git_pull()
                case '11':
                    self.git_push()
                case '12':
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida.")

def main():
    cli = CLIControl()
    cli.menu()

if __name__ == '__main__':
    main()