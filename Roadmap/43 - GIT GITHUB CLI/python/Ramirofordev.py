'''
Ejercicio:

Desarrolla un CLI (Command Line Interface) que permita interactuar con Git y Github de manera real desde la terminal.

El programa debe permitir las siguientes opciones:
    1. Establecer un nuevo directorio de trabajo
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
    12. Salir
'''
# Importamos el modulo subprocess y os 
import subprocess
import os
from functools import wraps

# Creamos un decorador que verifique que existe un repositorio git en el dir
def requiere_repo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not os.path.exists(".git"):
            print("E rror: No hay un repositorio Git en este directorio.")
            return None
        return func(*args, **kwargs)
    return wrapper

# Creamos una funcion que nos sirva como el menu y llame a las funciones
def menu():
        try:
            print("--- Bienvenido a Git ---")
            print("Escoja una de las siguientes opciones: \n" \
                "1. Establecer un nuevo direcotorio de trabajo.\n" \
                "2. Crear un nuevo repositorio.\n" \
                "3. Crear una nueva rama.\n" \
                "4. Cambiar de rama.\n" \
                "5. Mostrar ficheros pendientes de hacer commit.\n" \
                "6. Hacer commit (junto con un add de todos los ficheros).\n" \
                "7. Mostrar el historial de commits.\n" \
                "8. Eliminar rama.\n" \
                "9. Establecer repositorio remoto.\n" \
                "10. Hacer pull.\n" \
                "11. Hacer push.\n" \
                "12. Salir.")
            op = int(input("> ")) # Pedimos la opcion al usuario y la convertimos en entero
            return op
        except ValueError as e:
            print(f"Se ha producido un error: {str(e)}")
            return None

def establecer_dir():
    # Pedimos la ruta del directorio que desea establecer
    ruta_dir = input("Inserte la ruta que desea establecer como nuevo directorio de trabajo: ")

    # Verificamos que la ruta exista
    if os.path.isdir(ruta_dir):
        os.chdir(ruta_dir)
        print(f"Ahora esta trabajando en la ruta {ruta_dir}.")
        return ruta_dir
    else:
        print("La ruta de este directorio no existe.")
        return None
    
def crear_repo():
    ruta_actual = os.getcwd()

    if os.path.isdir(ruta_actual):
        if os.path.exists(".git"):
            print("Ya existe un repositorio en este directorio.")
            return None
        else:
            # Ejecutamos el comando de git
            try:
                resultado = subprocess.run(["git" ,"init"], check = True, capture_output = True, text = True)
                
                print("Repositorio creado correctamente.")
                print(resultado.stdout)

            except subprocess.CalledProcessError as e:
                print(f"Error al crear el repositorio {(e.stderr)}")

@requiere_repo         
def crear_rama():
    # Creamos la nueva rama con subprocess

    rama = input("Inserta el nombre de la rama: ")

    try:
        resultado = subprocess.run(["git", "switch", '-c', rama], check = True, capture_output = True, text = True)
        
        print("Rama creada correctamente.")
        print(resultado.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error al crear el repositorio {e.stderr}")

@requiere_repo
def cambiar_rama():
    # Preguntamos el nombre de la rama a la que se desea cambiar
    rama = input("Inserte el nombre de la rama a la que desea cambiarse: ")

    try:
        subprocess.run(["git", "switch", rama], check = True, capture_output = True, text = True)

        # Obtenemos la rama actual en la que estamos para informaserla al usuario
        resultado = subprocess.run(["git", "branch", "--show-current"], capture_output = True, text = True)

        print(f"Ahora estas en la rama: {resultado.stdout.strip()}")

    except subprocess.CalledProcessError as e:
        print(f"Se ha producido un error: {e.stderr}")

@requiere_repo
def mostrar_status():
    # Creamos tres listas
    staged = [] # archivos preparados para commit.
    unstaged = [] # archivos modificados pero no staged
    untracked = [] # archivos no rastreados

    try:
        resultado = subprocess.run(["git", "status", "--porcelain"], check = True, capture_output = True, text = True)

        for line in resultado.stdout.splitlines():
            if line.startswith("??"):
                untracked.append(line[3:])
            else:
                if line[0] != " ":
                    staged.append(line[3:])
                if line[1] != " ":
                    unstaged.append(line[3:])

        print("Archivos staged: ", staged)
        print("Archivos modificados: ", unstaged)
        print("Archivos no rastreados: ", untracked)

    except subprocess.CalledProcessError as e:
        print(f"Se ha producido un error: {e.stderr}")

@requiere_repo
def hacer_commit():
    try:
        # Añadimos todos los archivos a staged
        subprocess.run(["git", "add", "."], check = True)

        # Hacemos el commit
        mensaje = input("Inserte el mensaje del commit: ")
        resultado = subprocess.run(["git", "commit", "-m", mensaje], check = True, capture_output = True, text = True)

        print("El commit ha sido creado correctamente.")
        print(resultado.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Se ha producido un error: {e.stderr}")

@requiere_repo
def mostrar_historial():
    try:
        resultado = subprocess.run(["git", "log", "--oneline", "--graph", "--decorate"], check = True, capture_output = True, text = True)
        print("--- Historial de git ---")
        print(resultado.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Ha surgido un error: {e.stderr}")

@requiere_repo
def eliminar_rama():
    # Pedimos el nombre de la rama 
    rama = input("Inserte el nombre de la rama que desea eliminar: ")

    try:
        subprocess.run(["git", "branch", "-d", rama], check = True)

        print(f"La rama {rama} fue eliminada correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Ha surgido un error: {e.stderr}.")

@requiere_repo
def repo_remoto():
    # Le preguntamos al usuario la url remota del repo
    url_remota = input("Inserte la url remota del repositorio: ")

    try:
        subprocess.run(["git", "remote", "add", "origin", url_remota], check = True)
        print("Se ha conectado a su repositorio remoto.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Ha surgido un error: {e.stderr}")
        return False

# Creamos una funcion auxiliar que nos permita verificar que ya existe un repo remoto
def tiene_remoto():
    try:
        resultado = subprocess.run(['git', 'remote'], capture_output = True, text = True)

        remotos = resultado.stdout.splitlines()
        return "origin" in remotos
    except Exception:
        return False

@requiere_repo
def hacer_pull():
    # Comprobamos que el repositorio este conectado.
    if tiene_remoto():
        try:
            subprocess.run(['git', 'pull'], check = True)
            print("Se han actualizado los cambios en su repo local.")
        except subprocess.CalledProcessError as e:
            print(f"Se ha producido un error: {e.stderr}.")
    else:
        print("Este repositorio todavia no esta conectado a uno remoto.")
        return

@requiere_repo
def hacer_push():
    # Pedimos el nombre del remoto y el nombre de la rama
    remoto = input("Inserte el nombre de su repo remoto: ")
    rama = input("Inserte el nombre de la rama desde donde desea pushear: ")

    if tiene_remoto():
        try:
            subprocess.run(['git', 'push', remoto, rama], check = True)
            print("Push realizado con exito.")
        except subprocess.CalledProcessError as e:
            print(f"Se ha producido un error: {e.stderr}")

# Inicializamos un loop que sea eterno hasta que el usuario decida salirse
while True:
    opcion = menu()

    if opcion is None:
        print("Error")
        continue

    match opcion:
        case 1:
            establecer_dir()
        case 2:
            crear_repo()
        case 3:
            crear_rama()
        case 4:
            cambiar_rama()
        case 5:
            mostrar_status()
        case 6:
            hacer_commit()
        case 7:
            mostrar_historial()
        case 8:
            eliminar_rama()
        case 9:
            repo_remoto()
        case 10:
            hacer_pull()
        case 11:
            hacer_push()
        case 12:
            print("Saliendo de git..")
            break