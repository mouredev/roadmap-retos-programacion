# 43 - Git Github CLI
import os
import subprocess

def show_return_menu():
    input("Enter para volver al menu...")

def run_command(command: str):

    try:
        result = subprocess.run(
            ["pwsh","-Command",command],
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")

def show_menu():
    os.system("cls")
    print("\nDirectorio actual de trabajo:")
    run_command("(Get-Location).Path")
    print("\n=== [+] Bienvenido al CLI de GIT/GITHUB by Gordo-Master [+] ===")
    print("Seleccione un opción: ")
    text = """1. Establecer el directorio de trabajo
2. Crear un nuevo repositorio
3. Crear una nueva rama
4. Cambiar de rama
5. Mostrar ficheros pendientes de hacer commit
6. Hacer commit (junto con un add de todos los ficheros)
7. Mostrar el historial de commits
8. Eliminar rama
9. Establecer repositorio remoto
10. Hacer pull
11. Hacer push
12. Salir"""
    print(text)
    option = input("Selecciona una opcion (1 al 12): ")
    try:
        option = int(option)
    except ValueError:
        print("Valor incorrecto. \nSelecciona un número entero entre 1 - 12")
        show_return_menu()
        return None
    else:
        if option <= 0 or option > 12:
            print("Valor fuera de rango. \nSelecciona un número entero entre 1 - 12")
            show_return_menu()
            return None
        return option

def run_option(option):
    match option:
        case 1:
            set_working_directory()
            show_return_menu()
            return True
        case 2:
            new_repository()
            show_return_menu()
            return True
        case 3:
            new_branch()
            show_return_menu()
            return True
        case 4:
            switch_branch()
            show_return_menu()
            return True
        case 5:
            show_branch_status()
            show_return_menu()
            return True
        case 6:
            make_commit()
            show_return_menu()
            return True
        case 7:
            show_history()
            show_return_menu()
            return True
        case 8:
            del_branch()
            show_return_menu()
            return True
        case 9:
            set_remote_repository()
            show_return_menu()
            return True
        case 10:
            make_pull()
            show_return_menu()
            return True
        case 11:
            make_push()
            show_return_menu()
            return True
        case 12:
            print("[*] Saliendo de la aplicación...")
            return False
        case _:
            print("Valor incorrecto, ¿como llegaste a este lugar?")
            return True

def set_working_directory():

    path = input("Introduce el directorio de trabajo: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"Se a cambiado el directorio de trabajo: {path}")
    else:
        print(f"El directorio introducido no existe.")
        
def new_repository():
    if os.path.isdir(".git"):
        print("Ya existe un repositorio en la ubicación")
    else:
        run_command("git init")
        run_command("git branch -M main")
        print("Repositorio iniciado")

def new_branch():
    branch_name = input("Ingrese el nombre de la nueva rama: ")
    run_command(f"git branch -c {branch_name}")

def switch_branch():
    branch_name = input("Cambiar a la rama: ")
    run_command(f"git switch {branch_name}")

def show_branch_status():
    run_command("git status")

def make_commit(): # Hacer el add y el commit - hay que agregar el comentario
    comment = input("Ingrese el comentario para el commit: ")
    run_command("git add .")
    run_command(f"git commit -m '{comment}'")

def show_history():
    run_command("git log --oneline")

def del_branch():
    branch_name = input("Ingrese el nombre de la rama que desea eliminar: ")
    run_command(f"git branch -d {branch_name}")

def set_remote_repository():
    url = input("Indique la URL del reposotorio remoto a establecer: ")
    run_command(f"git remote add origion {url}")
    run_command(f"git push -u origin/{url}")

def make_pull():
    run_command(f"git pull")

def make_push():
    run_command(f"git push")


def main():
    while True:
        while True:
            option = show_menu()
            if not option is None:
                break
        status = run_option(option)
        if status is False:
            break

if __name__ == "__main__":
    main()