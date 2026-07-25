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

# Usar pip install gitpython

import os
import sys
import git
from git import Repo, GitCommandError

def set_working_directory():
    path = input("Introduce la ruta del directorio de trabajo: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"Directorio cambiado a: {os.getcwd()}")
    else:
        print("Ruta no válida. Inténtalo de nuevo.")

def create_repository():
    try:
        Repo.init(os.getcwd())
        print("Repositorio creado exitosamente.")
    except GitCommandError as e:
        print(f"Error al crear el repositorio: {e}")

def create_branch(repo):
    branch_name = input("Nombre de la nueva rama: ")
    try:
        repo.git.branch(branch_name)
        repo.git.checkout(branch_name)
        print(f"Rama '{branch_name}' creada y cambiada.")
    except GitCommandError as e:
        print(f"Error al crear la rama: {e}")

def switch_branch(repo):
    branch_name = input("Nombre de la rama a la que quieres cambiar: ")
    try:
        repo.git.checkout(branch_name)
        print(f"Cambiado a la rama '{branch_name}'.")
    except GitCommandError as e:
        print(f"Error al cambiar de rama: {e}")

def show_pending_files(repo):
    try:
        status = repo.git.status()
        print(status)
    except GitCommandError as e:
        print(f"Error al mostrar archivos pendientes: {e}")

def make_commit(repo):
    commit_message = input("Mensaje del commit: ")
    try:
        repo.git.add(all=True)
        repo.git.commit(m=commit_message)
        print("Commit realizado.")
    except GitCommandError as e:
        print(f"Error al hacer el commit: {e}")

def show_commit_history(repo):
    try:
        log = repo.git.log("--oneline")
        print(log)
    except GitCommandError as e:
        print(f"Error al mostrar el historial de commits: {e}")

def delete_branch(repo):
    branch_name = input("Nombre de la rama a eliminar: ")
    try:
        repo.git.branch("-d", branch_name)
        print(f"Rama '{branch_name}' eliminada.")
    except GitCommandError as e:
        print(f"Error al eliminar la rama: {e}")

def set_remote_repository(repo):
    remote_url = input("URL del repositorio remoto: ")
    try:
        repo.create_remote("origin", remote_url)
        print(f"Repositorio remoto '{remote_url}' añadido como 'origin'.")
    except GitCommandError as e:
        print(f"Error al añadir el repositorio remoto: {e}")

def pull_changes(repo):
    try:
        repo.git.pull("origin")
        print("Pull realizado.")
    except GitCommandError as e:
        print(f"Error al hacer pull: {e}")

def push_changes(repo):
    try:
        repo.git.push("origin")
        print("Push realizado.")
    except GitCommandError as e:
        print(f"Error al hacer push: {e}")

def show_menu():
    print("\n--- Git CLI ---")
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

def main():
    repo = None
    while True:
        show_menu()
        choice = input("Selecciona una opción: ")
        
        # Opciones
        if choice == '1':
            set_working_directory()
            repo = Repo(os.getcwd()) if os.path.isdir(os.getcwd()) and ".git" in os.listdir(os.getcwd()) else None
        elif choice == '2':
            create_repository()
            repo = Repo(os.getcwd())
        elif repo is None:
            print("Primero establece el directorio de trabajo y crea o abre un repositorio.")
        elif choice == '3':
            create_branch(repo)
        elif choice == '4':
            switch_branch(repo)
        elif choice == '5':
            show_pending_files(repo)
        elif choice == '6':
            make_commit(repo)
        elif choice == '7':
            show_commit_history(repo)
        elif choice == '8':
            delete_branch(repo)
        elif choice == '9':
            set_remote_repository(repo)
        elif choice == '10':
            pull_changes(repo)
        elif choice == '11':
            push_changes(repo)
        elif choice == '12':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
