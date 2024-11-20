'''
 * EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita 
 * interactuar con Git y GitHub de manera real desde terminal.
 * 
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir
 *
 * Puedes intentar controlar los diferentes errores.
'''

import os
import subprocess

def run_command(command: str):
    
    try:
        result = subprocess.run(
            command, 
            shell=True,
            check=True,
            text=True,
            capture_output=True)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")


def set_working_directory():

    path = input("Introduce la ruta del directorio de trabajo: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"Directorio de trabajo establecido en: {path}")
    else:
        print(f"El directorio no existe, por favor verifique.")

def create_repository():

    if os.path.isdir(".git"):
        print("El directorio ya es un repositorio git.")
    else:
        run_command("git init")
        run_command("git branch -M main")
        print("Repositorio inicializado.")

def create_branch(name: str):

    run_command(f"git branch {name}")

def switch_branch(name: str):

    run_command(f"git switch {name}")

def show_pending_files():
    run_command("git status")

def make_commit(msg: str):
    run_command("git add .")
    run_command(f"git commit -m \"{msg}\"")

def show_commit_history():
    run_command("git log --oneline")

def delete_branch(name: str):
    run_command(f"git branch -d {name}")

def set_remote_repository(remote_url: str):
    run_command(f"git remote add origin {remote_url}")
    run_command("git push -u origin main")

def make_pull():
    run_command("git pull")

def make_push():
    run_command("git push")


if __name__ == '__main__':

    "/home/riacosta/Desktop/Test"
    while True:
        print("\n Git y GitHub CLI\n")
        run_command("pwd")

        print(f"1-Establecer el directorio de trabajo")
        print(f"2-Crear un nuevo repositorio")
        print(f"3-Crear una nueva rama")
        print(f"4-Cambiar de rama")
        print(f"5-Mostrar ficheros pendientes de hacer commit")
        print(f"6-Hacer commit (junto con un add de todos los ficheros)")
        print(f"7-Mostrar el historial de commits")
        print(f"8-Eliminar rama")
        print(f"9-Establecer repositorio remoto")
        print(f"10-Hacer pull")
        print(f"11-Hacer push")
        print(f"12-Salir")

        choice = int(input("Opción (1-12): "))
        

        match choice:
            case 1:
                set_working_directory()
            case 2:
                create_repository()
            case 3:
                branch = input("Nombre de la rama: ")
                create_branch(branch)
            case 4:
                branch = input("Nombre de la rama a ir: ")
                switch_branch(branch)
            case 5:
                show_pending_files()
            case 6:
                msg = input("Mensaje del commit: ")
                make_commit(msg)
            case 7:
                show_commit_history()
            case 8:
                branch = input("Nombre de la rama a eliminar: ")
                delete_branch(branch)
            case 9:
                remote_url = input("URL del repositorio remoto: ")
                set_remote_repository(remote_url)
            case 10:
                make_pull()
            case 11:
                make_push()
            case 12:
                print("Saliendo ...")
                break
            case _:
                print("Opción no válida")