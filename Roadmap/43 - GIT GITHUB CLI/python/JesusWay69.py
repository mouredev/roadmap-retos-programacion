import os, platform
from datetime import datetime as DT
from git import Repo
from git import exc

if platform.platform().startswith("macOS"):
    path = "/Users/jesus/python3_project/GitProjectPython"
    os.system('clear')
elif platform.platform().startswith("Linux"):
    path = "/Users/jesus/Documents/python3_project/GitProjectPython"
    os.system('clear')
elif platform.platform().startswith("Windows"):
    path = r"C:\Users\jesus\Documents\Python3project\GitProjectPython\\"
    os.system('cls')

"""* EJERCICIO:
 * Desarrolla un CLI (Command Line Interface) que permita
 * interactuar con Git y GitHub de manera real desde terminal.
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
 * 12. Salir"""

repo_url = 'https://github.com/Jesusway69/GitProjectPython'

def git_init(local_path:str)->object:
    if os.path.exists(local_path):
        repo = Repo.init(local_path)
    else:
        print("la ruta especificada no existe en este ordenador")
        return
    return repo

def git_clone(github_url:str, local_path:str)->object:
    if not os.path.exists(local_path):
        repo = Repo.clone_from(github_url, local_path)
    else:
        repo = Repo(path)
    return repo

def git_branch(repo:object):
    print("Ramas actuales en este repositorio:")
    print(repo.git.branch())
    branch_name = input("Escriba el nombre de la nueva rama a crear: ")
    try:
        repo.git.branch(branch_name)
        print("Nueva rama creada: ", branch_name)
    except exc.GitCommandError as ex:
        print(f"\n{ex} la rama {branch_name} ya existe")
    
def git_checkout(repo:object):
    print("Ramas actuales en este repositorio:")
    print(repo.git.branch())
    try:  
        branch_name = input("Escriba el nombre de la rama a la que quiere cambiar (con asterisco la actual): ")
        repo.git.checkout(branch_name)
    except exc.GitCommandError as ex:
        print(f"\n{ex} la rama {branch_name} no existe")

def git_add(repo:object):
    try:
        repo.git.add('.')
        print("\nCambios añadidos a stage correctamente")
    except exc.GitError as ex:
        print(ex)

def git_commit(repo:object):
    message = input("Introduzca el mensaje del commit: ")
    current_date = '{}{}{}'.format(DT.now().year, DT.now().month, DT.now().day)
    try:
        repo.index.commit(current_date + " " + message)
        print(f"\nCommit realizado correctamente con el mensaje '{message}' ")
    except exc.GitError as ex:
        print(ex)

def modify_repository(local_path:str):
    current_datetime = '{}/{}/{} a las {}:{}'.format(DT.now().day, DT.now().month, DT.now().year, DT.now().hour, DT.now().minute)
    with open(f'{local_path}/file1.txt', 'a') as f:
        f.writelines(f'\nañadimos otra línea el {current_datetime}')

def git_status(repo:object):
    print("\nEstado actual del repositorio:")
    print (repo.git.status())

def git_log(repo:object):
    print("\nCommits realizados:")
    print(repo.git.log())

def git_remote_add(repo:object):
    try:
        remote_branch = input("Introduzca el nombre de la rama principal remota (origin por defecto pulsando enter): ")
        if len(remote_branch) == 0: remote_branch = 'origin'
        repo_url = input("Introduzca una url válida para crear repositorio remoto en github: ")
        repo.create_remote(remote_branch, repo_url)
    except exc.InvalidGitRepositoryError as ex:
        print(f"\n{ex} la url {repo_url} no existe o la rama remota ya existe")

def git_pull(repo:object):
    try:
        repo.git.pull('origin', 'main')
        print("\nRepositorio remoto origin fusionado correctamente en main")
    except exc.GitError as ex:
        print(ex)

def git_push(repo:object):
    try:
        repo.git.push("--set-upstream", 'origin', 'main')
        print("\nRepositorio remoto origin actualizado correctamente")
    except exc.GitError as ex:
        print(ex)

def delete_branch(repo:object):
    print("Ramas actuales en este repositorio:")
    print(repo.git.branch())
    branch_name = input("Escriba el nombre de la rama a eliminar: ")
    try:
        repo.git.branch("-d", branch_name)
        print(f"Rama {branch_name} eliminada con éxito " )
    except exc.InvalidGitRepositoryError as ex:
        print(f"\n{ex} la rama {branch_name} no existe")
    except exc.GitError as ex:
        print(f"La rama {branch_name} no está fusionada con HEAD")

my_repo = git_init(path)


while True:
    print("""
    
    1- Crear repositorio local (init)
    2- Clonar repositorio desde Github (clone)
    3- Crear nueva rama (branch)
    4- Cambiar de rama (checkout)
    5- Mostrar estado de repositorio (status)
    6- Añadir todos los cambios a stage (add .)
    7- Hacer commit del repositorio (commit)
    8- Mostrar historial de commits (log)
    9- Establecer repositorio remoto (remote)
    10- Actualizar fichero txt (branch -d)
    11- Actualizar repositorio local desde remoto (pull)
    12- Subir cambios locales a remoto (push)
    13- Eliminar rama
    14- Salir""")

    option = input("Selecciona una opción del 1 al 12: ")

    match option:
        case "1":
            git_init(path)
        case "2":
            git_clone(repo_url, path)
        case "3":
            git_branch(my_repo)
        case "4":
            git_checkout(my_repo)
        case "5":
            git_status(my_repo)
        case "6":
            git_add(my_repo)
        case "7":
            git_commit(my_repo)
        case "8":
            git_log(my_repo)
        case "9":
            git_remote_add(my_repo)
        case "10":
            modify_repository(path)
        case "11":
            git_pull(my_repo)
        case "12":
            git_push(my_repo)
        case "13":
            delete_branch(my_repo)
        case "14":
            print("Fin del programa")
            break
        case _:
            print("Opción no válida.")