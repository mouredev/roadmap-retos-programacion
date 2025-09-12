import os
from pdb import run
import subprocess


def run_command(command: str):

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")


def set_working_directory():

    path = input("Introduce el directorio completo de trabajo: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"El directorio de trabajo ha cambiado a: {path}")
    else:
        print("El directorio introducido no existe.")


def create_repository():
    if os.path.isdir(".git"):
        print("Ya existe un repositorio en este directorio.")
    else:
        run_command("git init")
        run_command("git branch -M main")
        print("Repositorio inicializado.")


def create_branch():
    branch_name = input("Nombre de la nueva rama: ")
    run_command(f"git branch {branch_name}")


def switch_branch():
    branch_name = input("Nombre de la rama a la que quieres cambiar: ")
    run_command(f"git checkout {branch_name}")


def show_pending_files():
    run_command("git status -s")


def make_commit():
    message = input("Mensaje para el commit: ")
    run_command("git add .")
    run_command(f"git commit -m \"{message}\"")


def show_commit_history():
    run_command("git log --oneline")


def delete_branch():
    branch_name = input("Nombre de la rama a eliminar: ")
    run_command(f"git branch -d {branch_name}")


def set_remote_repository():
    remote_url = input("URL del repositorio remoto: ")
    run_command(f"git remote add origin {remote_url}")
    run_command("git push -u origin main")


def make_pull():
    run_command("git pull")


def make_push():
    run_command("git push")


while True:

    print("\nDirectorio actual de trabajo:")
    run_command("pwd")

    print("\nGit y GitHub CLI - Opciones:")
    print("1. Establecer el directorio de trabajo")
    print("2. Crear un nuevo repositorio")
    print("3. Crear una nueva rama")
    print("4. Cambiar de rama")
    print("5. Mostrar ficheros pendientes de hacer commit")
    print("6. Hacer commit (+add)")
    print("7. Mostrar el historial de commits")
    print("8. Eliminar rama")
    print("9. Establecer repositorio remoto")
    print("10. Hacer pull")
    print("11. Hacer push")
    print("12. Salir")

    choice = input("Selecciona una opción (1 al 12): ")

    match choice:
        case "1":
            set_working_directory()
        case "2":
            create_repository()
        case "3":
            create_branch()
        case "4":
            switch_branch()
        case "5":
            show_pending_files()
        case "6":
            make_commit()
        case "7":
            show_commit_history()
        case "8":
            delete_branch()
        case "9":
            set_remote_repository()
        case "10":
            make_pull()
        case "11":
            make_push()
        case "12":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")
