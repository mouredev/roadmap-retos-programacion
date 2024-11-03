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

import os
import subprocess

# Función para ejecutar comandos en la terminal y capturar su salida o errores
def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

# Funciones para las diferentes opciones del CLI
def set_working_directory():
    path = input("Introduce el directorio de trabajo: ")
    try:
        os.chdir(path)
        print(f"Directorio de trabajo establecido en: {os.getcwd()}")
    except FileNotFoundError:
        print("Error: Directorio no encontrado.")

def create_repository():
    print(run_command(["git", "init"]))

def create_branch():
    branch_name = input("Nombre de la nueva rama: ")
    print(run_command(["git", "branch", branch_name]))

def switch_branch():
    branch_name = input("Nombre de la rama a la que deseas cambiar: ")
    print(run_command(["git", "checkout", branch_name]))

def show_pending_files():
    print(run_command(["git", "status"]))

def make_commit():
    message = input("Mensaje para el commit: ")
    run_command(["git", "add", "."])
    print(run_command(["git", "commit", "-m", message]))

def show_commit_history():
    print(run_command(["git", "log", "--oneline"]))

def delete_branch():
    branch_name = input("Nombre de la rama a eliminar: ")
    print(run_command(["git", "branch", "-d", branch_name]))

def set_remote_repository():
    remote_url = input("Introduce la URL del repositorio remoto: ")
    print(run_command(["git", "remote", "add", "origin", remote_url]))

def pull_changes():
    print(run_command(["git", "pull", "origin", "main"]))

def push_changes():
    print(run_command(["git", "push", "origin", "main"]))

# Función principal del CLI
def main():
    while True:
        print("\nOpciones:")
        print("1. Establecer el directorio de trabajo")
        print("2. Crear un nuevo repositorio")
        print("3. Crear una nueva rama")
        print("4. Cambiar de rama")
        print("5. Mostrar ficheros pendientes de hacer commit")
        print("6. Hacer commit (junto con un add de todos los ficheros)")
        print("7. Mostrar el historial de commits")
        print("8. Eliminar rama")
        print("9. Establecer repositorio remoto")
        print("10. Hacer pull")
        print("11. Hacer push")
        print("12. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            set_working_directory()
        elif option == "2":
            create_repository()
        elif option == "3":
            create_branch()
        elif option == "4":
            switch_branch()
        elif option == "5":
            show_pending_files()
        elif option == "6":
            make_commit()
        elif option == "7":
            show_commit_history()
        elif option == "8":
            delete_branch()
        elif option == "9":
            set_remote_repository()
        elif option == "10":
            pull_changes()
        elif option == "11":
            push_changes()
        elif option == "12":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
