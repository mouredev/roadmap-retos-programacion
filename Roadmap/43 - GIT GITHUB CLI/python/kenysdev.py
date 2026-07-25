# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 43 GIT GITHUB CLI
# ------------------------------------

"""
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
"""

import subprocess
import os

def run_command(command: str, msg="") -> None:
    print(msg)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅: {result.stdout.strip()}")
    else:
        print(f"❌: {result.stderr.strip()}")

def set_directory() -> None:
    print("Establecer directorio de trabajo:")
    path = input("Ruta: ")
    if os.path.isdir(path):
        os.chdir(path)
    else:
        print("Esta ruta no existe.")

def set_remote_repository() -> None:
    remote_url = input("URL del repositorio: ")
    run_command(f"git remote add origin {remote_url}")
    run_command("git push -u origin main")

MENU = """
Interactuar con Git y GitHub:
------------------------------------------------------------
| 1. Establecer directorio       | 7. Historial de commits |  
| 2. Crear repositorio           | 8. Eliminar rama        |
| 3. Crear rama                  | 9. Configurar remoto    |
| 4. Cambiar rama                | 10. pull                | 
| 5. Mostrar cambios pendientes  | 11. push                | 
| 6. 'add' + 'commit'            | 12. Salir               | 
------------------------------------------------------------
Directorio actual:"""

while True:
    print(MENU)
    run_command("cd" if os.name == "nt" else "pwd")
    option = input("\nOpción: ")

    match option:
        case "1": 
            set_directory()
        case "2":
            run_command("git init && git branch -M main", "Crear repositorio")

        case "3":
            print("Crear nueva rama:")
            run_command(f"git branch -c {input('Nombre: ')}")

        case "4":
            print("Cambiar de rama:")
            run_command(f"git switch {input('Nombre: ')}")

        case "5":
            run_command("git status -s", "Mostrar cambios")

        case "6":
            print("Nuevo commit:")
            run_command(f"git add . && git commit -m '{input('Mensaje: ')}'")

        case "7":
            run_command("git log --oneline", "Historial de commits")

        case "8":
            print("Eliminar rama") 
            run_command(f"git branch -d {input('Nombre: ')}")

        case "9":
            set_remote_repository()

        case "10": 
            run_command(f"git pull origin {input('rama: ')}")

        case "11":
            run_command(f"git push origin {input('rama: ')}")

        case "12": 
            print("Bye.")
            break
        case _: 
            print("Opción no válida.")

