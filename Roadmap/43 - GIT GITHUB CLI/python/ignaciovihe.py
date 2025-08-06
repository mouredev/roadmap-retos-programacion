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

from git import Repo, GitCommandError
import os

def clear_console():
    """
    Limpia la consola, tneiendo en cuenta el sistema operativo.
    """
    os.system('cls' if os.name =='nt' else 'clear')


def exist_repo(path):
    """
    Comprueba si existe un repositorio de git, comprobando si existe el ficrero .git en el path pasado.
    """
    git_folder = os.path.join(path, '.git')
    return os.path.isdir(git_folder)


def set_working_directory():
    """
    Establece el nuevo directorio de trabajo y comprueba si ya existe un repositorio en él.
    Devuelve el nuevo directorio y el objeto Repo si ya existe o None si no.
    """
    new_directory = input("Introduce el nuevo directorio:")
    if os.path.exists(new_directory) and os.path.isdir(new_directory):
        print(f"Se ha modificado el directorio de trabajo.")
        if exist_repo(new_directory): # Si ya hay un repositorio en el directorio.
            new_repo = Repo(new_directory)
            print(f"Se ha encontrado un repositorio en el directorio. Se establece como repositorio actual.")
        else:
            new_repo = None
        input("ENTER para continuar")
        return new_directory, new_repo
    else:
        raise Exception("El nuevo directorio de trabajo no existe. No se modifica.")
    

def init_new_repository(path):
    """
    Comprueba si existe un repositorio en el directorio pasado.
    Si ya existe lanza una excepción y si no, crea el repsitorio y lo devuelve.
    """
    if exist_repo(path):
        raise Exception("Ya existe un repositorio creado en el directorio de trabajo. No se hace nada.")
    print(f"Nuevo repositorio iniciado en '{path}'")
    input("ENTER para continuar")
    return Repo.init(path)


def create_new_branch(repo: Repo):
    """
    Crea una nueva rama y cambia el Head a esa nueva rama.
    """
    branch_name = input("Nombre de la nueva rama: ")
    repo.git.checkout("-b", branch_name)
    print(f"Nueva rama {branch_name} creada correctamente.")
    input("ENTER para continuar")


def change_branch(repo: Repo):
    """
    Cambia la rama activa a la que le pasemos comprobando si existe la rama.
    """
    branch_name = input("Nombre de la nueva rama: ")
    if branch_name in repo.heads and branch_name != repo.active_branch:
        repo.git.checkout(branch_name)
    else:
        print(f"La rama '{branch_name}' no existe o ya es la rama activa.")
        input("ENTER para continuar")
        return
    print(f"Nueva rama activa '{branch_name}'")
    input("ENTER para continuar")


def check_repo_status(repo :Repo):
    """
    Comprueba el estado del repositorio e imprime el resultado.
    Equivalente a 'git status'
    """
    print(repo.git.status())
    input("ENTER para continuar")


def commit_files(repo: Repo, all= True):
    """
    Realiza el add y commit de:
    -Todos los archivos nuevos.
    -Un directorio en particular(buscando los ficheros nuevos en su interior).
    -Un archivo en particular.
    Dependiendo de la opcion pasada del menu.
    """
    if not repo.is_dirty(untracked_files=True):# Esto comprueba si hay cambios en el repo
        print("No hay cambios para commitear.")
        input("ENTER para continuar")
        return
    
    result=""

    if all:
        repo.git.add(all=True)
        result = "todos los archivos."
    else:
        file = input("Nombre del archivo a commitear: ").strip()
        modified_files = [diff.a_path for diff in repo.index.diff(None)]
        files_to_add = []

        # Ruta absoluta al archivo/carpeta
        if repo.working_tree_dir:
            abs_path = os.path.join(repo.working_tree_dir, file)
        else:
            raise Exception("No se pudo determinar el directorio raíz del repositorio.")

        # Si es carpeta, buscar archivos dentro
        if os.path.isdir(abs_path):
            for root, _, filenames in os.walk(abs_path):
                for name in filenames:
                    full_path = os.path.join(root, name)
                    # Normalizar la ruta relativa a la raíz del repo
                    rel_path = os.path.relpath(full_path, repo.working_tree_dir)
                    rel_path = rel_path.replace(os.sep, "/")
                    print(f"rel_path: {rel_path}")
                    print(f"Untracked: {repo.untracked_files}")
                    print(f"Modified: {modified_files}")
                    if rel_path in repo.untracked_files or rel_path in modified_files:
                        files_to_add.append(rel_path)

        # Si es archivo directamente                
        elif file in repo.untracked_files or file in modified_files: #archivos no trackeados - archivos modificados
            files_to_add.append(file)

        if not files_to_add:
            print("No existe el fichero/carpeta a comitear o no contiene archivos nuevos.")
            input("ENTER para continuar")
            return
        # Añadir todos los archivos detectados
        repo.index.add(files_to_add)
        result = ", ".join(files_to_add)

    message = input("Mensaje de commit: ")
    repo.index.commit(message)
    print(f"Commit de {result} correcto.")
    input("ENTER para continuar")


def show_commits_history(repo: Repo):
    """
    Imprime el historial de commits del repositorio pasado.
    """
    for commit in repo.iter_commits():
        print(f"Hash: {commit.hexsha}")
        print(f"Autor: {commit.author.name} <{commit.author.email}>")
        print(f"Fecha: {commit.committed_datetime}")
        print(f"Mensaje: {commit.message.strip()}")
        print("-" * 40)
    input("ENTER para continuar")


def merge_branch(repo: Repo):
    """
    Realiza el merge de una rama source a la rama activa. Comprueba si hay archivos que mergear,
    y si es asi los mergea. Si hay conflictos lanza una excepción y te proporciona instrucciones para 
    recolver los conflictos manualmente, haciendo una pausa en la ejecución para poder solucionarlos.
    Finalmente hace un commit automatico de mergeo.
    """
    print(f"Rama activa: {repo.active_branch}")
    if repo.is_dirty(untracked_files=True):# Por seguridad comprobamos que no haya cambios sin commitear.
        raise Exception("Hay cambios sin commitear. Haz commit antes de hacer merge")
    
    target_branch = repo.active_branch
    source_branch = input("Introduce el nombre de la rama fuente: ")

    if source_branch not in repo.branches:# Comprobamos que la rama exista.
        print(f"No se encuentra la rama '{source_branch}'. Comprueba el nombre.")
        input("ENTER para continuar")
        return
    
    # Comprobamos si hay algo que mergear antes de lanzarlo
    # repo.git.rev_list compara los commits entre dos ramas. left only = solo cuenta los de la izq
    # count que cuente los commits del lado indicado
    # source ... target(o alreves como se desee) que compare ambas ramas
    # devuelve cuantos commits hay en source que no esten en target
    commits_to_merge = int(repo.git.rev_list('--left-only', '--count', f'{source_branch}...{target_branch}'))
    if commits_to_merge == 0:
        print(f"No hay cambios nuevos en '{source_branch}' que mergear en '{target_branch}'.")
        input("ENTER para continuar")
        return

    try:
        repo.git.merge(source_branch)# Hacemos el merge. Si hay conflicto lanza una excepcion GitCommandError
        print(f"Se hizo merge de '{source_branch}' a '{target_branch}' correctamente.")
        input("ENTER para continuar")

    except GitCommandError as e:
        # Mostrar archivos en conflicto
        unmerged_paths = list(repo.index.unmerged_blobs().keys())
        print("\nArchivos en conflicto:")
        for path in unmerged_paths:
            print(f"  - {path}")

        if "Merge conflict" in str(e):# si hay conflicto en el mensaje de la excepción. Lanzamos instrucciones.
            print("Conflicto detectado durante el merge.")
            print("Edita manualmente los archivos en conflicto y guarda los cambios.")
            input("Pulsa ENTER cuando hayas resuelto todos los conflictos...")

            # Intentar hacer add a esos archivos
            for path in unmerged_paths:
                try:
                    repo.git.add(path) # Esta linea no puede ser repo.index.add(path). porque eso no elimina el archivo como conflictivo.
                except Exception as ex:# debe usar git.add que si tiene el contexto del merge.
                    print(f"Error al hacer add a {path}: {ex}")
                    input("ENTER para continuar")

            # Verifica si quedan conflictos sin resolver
            if repo.index.unmerged_blobs():
                print("Aún hay archivos en conflicto. No se puede hacer commit.")
                input("ENTER para continuar")
                return
            
            # Hacer commit automatico para concluir el merge. Debe ser con git.commit que tiene en cuenta el contexto del merge.
            repo.git.commit('-m', f"Conflictos resueltos y merge completado. ({target_branch}) <- ({source_branch})")
            print("Conflictos resueltos. Merge finalizado correctamente.")
            input("ENTER para continuar")
        else:
            print("Error inesperado durante el merge:", e)
            input("ENTER para continuar")


def delete_branch(repo: Repo):
    """
    Borra la rama que le indiquemos, teniendo en cuenta antes, si esta ha sido ya mergeada.
    En el caso de que no haya problemas la borra.
    Enel caso de que todavia haya archivos sin mergear, nos dara la opción de borrarla a la fuerza.
    teniendo que confirmar dos veces el borrado.
    """

    if len(repo.branches) == 1:
        print(f"Solo existe main. No hay rama que borrar.")
        input("ENTER para continuar")
        return
    
    branch = input(f"Nombre de la rama a borrar: ")

    if branch not in repo.branches:
        print(f"La rama {branch} no existe.")
        input("ENTER para continuar")
        return
    
    if branch == repo.active_branch.name:
        print("No puedes borrar la rama en la que estás actualmente.")
        input("ENTER para continuar")
        return

    try:
        repo.delete_head(branch, force=False)
        print(f"Rama {branch} borrada con exito.(Ya estaba mergeada)")
    except GitCommandError as e:
        if 'is not fully merged' in str(e):
            op1, op2 = 0, 0
            print(f"La rama '{branch}' No está mergeada. No se ha borrado.")
            print(f"Quieres forzar el borrado?")
            print(f"1. SI")
            print(f"2. NO")
            while op1 not in [1, 2]:
                try:
                    op1 = int(input("Introduce una opción valida(1 o 2): "))
                except ValueError:
                    print("Debes introducir un número.")

            if op1 == 1:
                print(f"Estas seguro. No se podra recuperar?")
                print(f"1. SI")
                print(f"2. NO")
                while op2 not in [1, 2]:
                    try:
                        op2 = int(input("Introduce una opción valida (1 o 2): "))
                    except ValueError:
                        print("Debes introducir un número.")
                if  op2 == 1:
                    repo.delete_head(branch, force=True)
                    print(f"Rama {branch} borrada con exito.(Borrado a la fuerza.)")
                else:
                    print("No se ha borrado la rama. Haz merge y vuelve a initentarlo.")
        else:
            print(f"Error al intentar borrar la rama: {e}")
    input("ENTER para continuar")


def show_branches(repo: Repo):
    """
    Imprime la ramas del repositorio.
    """
    branches = [head.name for head in repo.heads]
    for branch in branches:
        print(f"-{branch}")
    input("ENTER para continuar")


def show_remote(repo: Repo):
    """
    Imprime los remotos asociados al repositorio actual con sus url
    """
    for remote in repo.remotes:
        print(f"Remoto asociado al repositorio actual: {remote.name}")
        for url in remote.urls:
            print(f"\t-URL: {url}")


def set_remote_repository(repo: Repo, remote_url: str, remote_name: str = "origin"):
    """
    Establece el remoto al repositorio local del directorio de trabajo.
    Comprueba si ya existe el remoto en cuyo caso te permite cambiarlo.
    En el caso de que sea la primera vez, también configura el upstream,
    para evitar errores al hacer push por primera vez.
    """
    try:
        #Verificamos que existe el repositorio
        if remote_name in repo.remotes:
            print(f"El remoto '{remote_name} ya existe.")
            update = ""
            while update not in ("s", "n"):
                update = input("¿Quieres alctualizar su URL? (s/n) ").lower()
                if update not in ("s", "n"):
                    print("Introduce una opción correcta: (s/n)")
            if update == "s":
                remote = repo.remotes[remote_name]
                repo.delete_remote(remote)
                repo.create_remote(remote_name, remote_url)
                print(f"URl del remoto '{remote_name}' actualizada.")
            else:
                print(f"No se realiza ninguna acción.")
        else:
            repo.create_remote(remote_name, remote_url)
            print(f"Remoto '{remote_name}' añadido con URL: {remote_url}")

        branch = repo.active_branch
        tracking = branch.tracking_branch()
        if tracking is None:
            origin = repo.remote(name="origin")
            origin.push(refspec="main:main", set_upstream=True)
            print(f"Upstream configurado: rama local 'main' sigue a 'origin/main'")
        else:
            print(f"La rama '{branch.name}' ya sigue a '{tracking}'")

        input("ENTER para continuar")
    except Exception as e:
        raise Exception(e)
    

def get_branch_sync_status(repo: Repo) -> tuple[int, int]:
    """
    Comprueba la sincronizacion entre local y remoto indicando cuantos commits va uno u otro
    por delante. Esta considerado el caso de que ambos tengan commits adelantados.
    """
    branch = repo.active_branch
    tracking_branch = branch.tracking_branch()

    if not tracking_branch:
        print("Esta rama no está vinculada a ninguna rama remota.")
        input("ENTER para continuar")
        return (-1, -1)
    
    # Actualizamos el remoto para comparar correctamente
    repo.remotes.origin.fetch()

    # Contar commits que están solo en local y solo en remoto
    # rev-list --count A..B → cuenta los commits que están en B pero no en A
    # ahead significa que el local va por delante. Habría que hacer push.
    # behind significa que el remoto va por delante. Habría que hacer pull.
    ahead = int(repo.git.rev_list('--count', f'{tracking_branch}..{branch}'))
    behind = int(repo.git.rev_list('--count', f'{branch}..{tracking_branch}'))

    print(f"Commits por delante (local): {ahead}")
    print(f"Commits por detrás (remoto): {behind}")

    return (ahead, behind)


def pull(repo: Repo):
    """
    Hace 'pull' de la rama actual desde el remoto 'origin' si hay commits nuevos.
    - Verifica si el remoto y la rama remota (upstream) están configurados.
    - No permite hacer pull si hay cambios sin guardar en el repositorio local.
    - Compara con el estado remoto y solo hace pull si hay commits nuevos (behind > 0).
    """

    if 'origin' not in repo.remotes:
        print(f"No hay un remoto 'origin' configurado.")
        input("ENTER para continuar")
        return
    
    if not repo.active_branch.tracking_branch():
        print("Esta rama no está vinculada a ninguna rama remota (upstream).")
        input("ENTER para continuar")
        return
    
    if repo.is_dirty(untracked_files=True):
        print("Hay cambios sin commitear. Haz commit o stash antes de hacer pull.")
        input("ENTER para continuar")
        return

    try:
        ahead, behind = get_branch_sync_status(repo)

        if behind == -1:
            return
        if behind == 0:
            print("Ya estás actualizado con el remoto. Nada que hacer.")
        else:
            repo.remotes.origin.pull()
            print(f"Pull completado correctamente. (Había {behind} commit/s nuevos)")
    except GitCommandError as e:
        print("Error al hacer pull.", e)

    input("ENTER para continuar")


def push(repo: Repo):
    """
    Hace push de la rama actual si está por delante del remoto.
    - Si hay commits pendientes en remoto: muestra advertencia y no hace push.(antes necesario pull)
    - Si todo está sincronizado: indica que no hay nada que subir.
    """

    branch = repo.active_branch.name

    if 'origin' not in repo.remotes:
        print(f"El remoto no esta configurado.")
        input("ENTER para continuar")
        return
    
    ahead, behind = get_branch_sync_status(repo)

    if ahead == -1:
        return
    if ahead > 0:
        if behind > 0:
            print("Hay cambios en el remoto. Haz pull antes de hacer push.")
        else:
            origin = repo.remotes.origin
            try:
                origin.push()
                print(f"Push completado con exito.")

            except GitCommandError as e:
                print(f"Error al hacer push: {e}")
    else:
        print("Ya esta todo actualizado.")

    input("ENTER para continuar")






def main():
    current_working_directory = os.getcwd()
    current_repository = None

    while True:
        print(f"=== GIT CLI ===")
        print(f"1. Establecer nuevo directorio de trabajo")
        print(f"2. Crear un nuevo repositorio")
        print(f"3. Crear una nueva rama")
        print(f"4. Cambiar de rama")
        print(f"5. Mostrar estado del repositorio")
        print(f"6. Hacer commit (junto con un add de todos los ficheros)")
        print(f"7. Hacer commit (junto con un add de un fichero)")
        print(f"8. Mostrar el historial de commits")
        print(f"9. Mergear rama")
        print(f"10. Eliminar rama")
        print(f"11. Listar ramas")
        print(f"12. Establecer repositorio remoto")
        print(f"13. Hacer pull")
        print(f"14. Hacer push")
        print(f"15. Salir")
        print("")
        print(f"Directorio de trabajo actual: '{current_working_directory}'")
        print("Repositorio activo: SI" if current_repository else "Repositorio activo: NO" )
        print(f"Rama activa: {current_repository.active_branch.name}" if current_repository else "")
        if current_repository and current_repository.remotes:
            show_remote(current_repository)


        try:
            option = int(input("Opción: "))
            match option:
                case 1:
                    current_working_directory, current_repository = set_working_directory()
                    clear_console()
                case 2:
                    current_repository = init_new_repository(current_working_directory)
                    clear_console()
                case 3:
                    if current_repository:
                        create_new_branch(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 4:
                    if current_repository:
                        change_branch(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 5:
                    if current_repository:
                        check_repo_status(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 6:
                    if current_repository:
                        commit_files(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 7:
                    if current_repository:
                        commit_files(current_repository, all=False)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 8:
                    if current_repository:
                        show_commits_history(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 9:
                    if current_repository:
                        merge_branch(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 10:
                    if current_repository:
                        delete_branch(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 11:
                    if current_repository:
                        show_branches(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 12:
                    if current_repository:
                        remote_url = input(" Introduce la URL del repositorio remoto: ")
                        set_remote_repository(current_repository, remote_url)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 13:
                    if current_repository:
                        pull(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                
                case 14:
                    if current_repository:
                        push(current_repository)
                        clear_console()
                    else:
                        raise Exception("Todavia no hay un repositorio en el diretorio de trabajo actual. Incicializa uno primero.")
                case 15:
                    print("Saliendo...")
                    break
        except Exception as e:
            print(e)
            input("ENTER para continuar")
            clear_console()

main()


