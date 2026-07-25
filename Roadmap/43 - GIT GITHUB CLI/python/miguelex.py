import os
import subprocess

class GitHubCLI:
    def __init__(self):
        self.working_directory = ""

    def set_working_directory(self, directory):
        if os.path.isdir(directory):
            self.working_directory = directory
            print(f"Directorio de trabajo establecido en: {self.working_directory}")
        else:
            print("Error: El directorio no existe.")

    def create_repository(self, name):
        if not self.working_directory:
            print("Error: Debe establecer un directorio de trabajo primero.")
            return
        os.chdir(self.working_directory)
        subprocess.run(['git', 'init', name])
        print(f"Repositorio '{name}' creado.")

    def create_branch(self, branch_name):
        os.chdir(self.working_directory)
        subprocess.run(['git', 'checkout', '-b', branch_name])
        print(f"Rama '{branch_name}' creada.")

    def change_branch(self, branch_name):
        os.chdir(self.working_directory)
        subprocess.run(['git', 'checkout', branch_name])
        print(f"Cambiado a la rama '{branch_name}'.")

    def show_pending_commits(self):
        os.chdir(self.working_directory)
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        print(result.stdout)

    def commit_changes(self, message):
        os.chdir(self.working_directory)
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', message])
        print(f"Cambios comprometidos con el mensaje: '{message}'.")

    def show_commit_history(self):
        os.chdir(self.working_directory)
        result = subprocess.run(['git', 'log'], capture_output=True, text=True)
        print(result.stdout)

    def delete_branch(self, branch_name):
        os.chdir(self.working_directory)
        subprocess.run(['git', 'branch', '-d', branch_name])
        print(f"Rama '{branch_name}' eliminada.")

    def set_remote_repository(self, url):
        os.chdir(self.working_directory)
        subprocess.run(['git', 'remote', 'add', 'origin', url])
        print(f"Repositorio remoto establecido en: {url}.")

    def pull(self):
        os.chdir(self.working_directory)
        subprocess.run(['git', 'pull'])
        print("Pull realizado correctamente.")

    def push(self):
        os.chdir(self.working_directory)
        subprocess.run(['git', 'push', 'origin', 'HEAD'])
        print("Push realizado correctamente.")

    def run(self):
        while True:
            print("\nSelecciona una opción:")
            print("1. Establecer el directorio de trabajo")
            print("2. Crear un nuevo repositorio")
            print("3. Crear una nueva rama")
            print("4. Cambiar de rama")
            print("5. Mostrar ficheros pendientes de hacer commit")
            print("6. Hacer commit")
            print("7. Mostrar el historial de commits")
            print("8. Eliminar rama")
            print("9. Establecer repositorio remoto")
            print("10. Hacer pull")
            print("11. Hacer push")
            print("12. Salir")

            option = input("Opción: ")
            if option == '1':
                dir_name = input("Introduce el directorio de trabajo: ")
                self.set_working_directory(dir_name)
            elif option == '2':
                repo_name = input("Introduce el nombre del repositorio: ")
                self.create_repository(repo_name)
            elif option == '3':
                branch_name = input("Introduce el nombre de la nueva rama: ")
                self.create_branch(branch_name)
            elif option == '4':
                branch_name = input("Introduce el nombre de la rama a la que deseas cambiar: ")
                self.change_branch(branch_name)
            elif option == '5':
                self.show_pending_commits()
            elif option == '6':
                message = input("Introduce el mensaje del commit: ")
                self.commit_changes(message)
            elif option == '7':
                self.show_commit_history()
            elif option == '8':
                branch_name = input("Introduce el nombre de la rama a eliminar: ")
                self.delete_branch(branch_name)
            elif option == '9':
                url = input("Introduce la URL del repositorio remoto: ")
                self.set_remote_repository(url)
            elif option == '10':
                self.pull()
            elif option == '11':
                self.push()
            elif option == '12':
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    cli = GitHubCLI()
    cli.run()
