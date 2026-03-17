
# EJERCICIO:
# ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
#
# Desarrolla un CLI (Command Line Interface) que permita 
# interactuar con Git y GitHub de manera real desde terminal.
# 
# El programa debe permitir las siguientes opciones:
# 1. Establecer el directorio de trabajo
# 2. Crear un nuevo repositorio
# 3. Crear una nueva rama
# 4. Cambiar de rama
# 5. Mostrar ficheros pendientes de hacer commit
# 6. Hacer commit (junto con un add de todos los ficheros)
# 7. Mostrar el historial de commits
# 8. Eliminar rama
# 9. Establecer repositorio remoto
# 10. Hacer pull
# 11. Hacer push
# 12. Salir
#
# Puedes intentar controlar los diferentes errores.

import os
import subprocess as sb


class Cli:
    def __init__(self, directory):
        self.directory = directory
        self.not_git = "Git no esta iniciado, inicialice Git primero."

    def command(self, *args):
        result = sb.run(args , cwd=self.directory, capture_output=True, text=True)
        
        if result.returncode != 0:
            return result.stderr.strip()
        return result.stdout.strip()

    def its_repository(self):
        repository = self.command("git", "remote", "-v")
        return bool(repository)

    def has_commits(self):
        return self.command("git", "rev-parse" "--verify HEAD")

    def check_git_init(self):
        return os.path.isdir(os.path.join(self.directory, ".git"))

    def init_repository(self):
        if self.check_git_init():
            return "Ya es un repositorio git."
        else:
            try:
                return  self.command("git", "init")
            except FileNotFoundError as e:
                return f"ERROR: Git no esta instalado o no esta en el PATH."
        

    def create_branch(self, branch: str):
        if self.check_git_init():
            if not self.has_commits():
                return "El repositorio aún no tiene commits"
            return self.command("git", "branch", branch)
        
        return self.not_git

    def switch_branch(self, branch):
        if self.check_git_init():
            branches = self.command("git", "branch","--format=%(refname:short)")
            branches_list = branches.splitlines()
            if branch not in branches_list:
                return "La rama no existe."
            return self.command("git", "switch", branch)

    def status(self):
        if self.check_git_init():
                return self.command("git", "status")
        return self.not_git

    def add_all(self):
        if self.check_git_init():
            if self.command("git", "status", "--porcelain"):
                return self.command("git", "add", ".")
            return "No hay cambios que añadir."
        return self.not_git

    def commit(self, message: str):
        if not self.check_git_init():
            return self.not_git
        if self.command("git", "status", "--porcelain"):
            return self.command("git", "commit", "-m", message)
        return "No hay cambios en el work tree"

    def logs(self):
        if self.check_git_init():
            return self.command("git", "log", "--oneline")

    def delete_branch(self, branch: str):
        if self.check_git_init():
            branches = self.command("git", "branch","--format=%(refname:shrot)")
            branches_list = branches.splitlines()
            branches_no_merged = self.command("git", "branch", "--no-merged", "--format=%(refname:short)")
            branches_no_merged_list = branches_no_merged.splitlines()
            if branch == "main" or branch == "master":
                return "La rama principal no se puede borrar."
            if branch not in branches_list:
                return "La rama no existe."
            
            if branch in branches_no_merged_list:
                return "La rama no esta mergeada aún."
            return self.command("git", "branch","-d", branch)

    def add_remote(self, url: str):
        if not self.its_repository():
            return self.command("git", "remote", "add", "origin", url)
        return "Ya existe un repositorio remoto."

    def pull(self):
        if self.its_repository():
            return self.command("git", "pull")
        return "No hay repositorio remoto."

    def push(self):
        if self.its_repository():
            return self.command("git", "push")
        return "No hay repositorio remoto."

def main():
    directory_path = input("indicar dirección del directorio deonde quiere trabajar (si no existiese se creaara).\n")
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)
    cli = Cli(directory_path)
    while True:
        print("Opciones del CLI.")
        print("1. Iniciar git en el directorio actual.\n"
            "2. Crear rama.\n"
            "3. Cambiar de rama.\n"
            "4. Mostrar archivos en workstage.\n"
            "5. Hacer commit.\n"
            "6. Mostrar historial de commits.\n"
            "7. Eliminar rama.\n"
            "8. Establecer repositorio remeto.\n"
            "9. Hacer pull.\n"
            "10. Hacer Push.\n"
            "11. Cerrar CLI.")

        choose = int(input())
        match choose:
            case 1:
                print(cli.init_repository())
            case 2:
                branch_name = input("Nombre de la nueva rama: ").lower()
                print(cli.create_branch(branch_name))
            case 3:
                switch = input("Rama a la que cambiar: ").lower()
                print(cli.switch_branch(switch))
            case 4:
                print(cli.status())
            case 5:
                message = input("Mensaje del commit: ").lower()
                print(cli.commit(message))
            case 6:
                print(cli.logs())
            case 7:
                del_branch = input("Rama que quiere eliminar: ").lower()
                print(cli.delete_branch(del_branch))
            case 8:
                url = input("Url del proyecto a clonar: ")
                print(cli.add_remote(url))
            case 9:
                print(cli.pull())
            case 10:
                print(cli.push())
            case _:
                print("Opción invalida, solo números entre 1 y 11.")