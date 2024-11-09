r"""
 EJERCICIO:
 ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!

 Desarrolla un CLI (Command Line Interface) que permita 
 interactuar con Git y GitHub de manera real desde terminal.
 
 El programa debe permitir las siguientes opciones:
 1. Establecer el directorio de trabajo
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

 Puedes intentar controlar los diferentes errores.
"""
import git
import os


def check_path(repo_path: str) -> bool:
    return os.path.isdir(repo_path)


def is_repo(repo_path: str) -> bool:
    return os.path.isdir(repo_path + "/.git")


def menu() -> int:
    print("\nIngresar número de opción")
    print("\t1 - Ver ramas")
    print("\t2 - Cambiar rama")
    print("\t3 - Nueva rama")
    print("\t4 - Eliminar rama")
    print("\t5 - Ver status")
    print("\t6 - Commit")
    print("\t7 - Pull")
    print("\t8 - Push")
    print("\t9 - Log")
    print("\t0 - Salir\n")
    while True:
        opcion = input("\t\t==> ")
        if opcion.isnumeric() and int(opcion) in range(0, 10):
            return int(opcion)


def branch_index() -> int:
    for ind, r in enumerate(repo.heads):
        if r == repo.active_branch:
            print(f"\t{ind} - * {r}")
        else:
            print(f"\t{ind} - {r}")
    while True:
        repo_ind = input("\nIngrese el número de rama: ")
        if repo_ind.isnumeric() and int(repo_ind) in range(0, repo.heads.__len__()):
            return int(repo_ind)


def new_branch():
    while True:
        branch_name = input("\nIngrese el nombre de la nueva rama (Enter para cancelar): ")
        if branch_name.lower() in [str(x).lower() for x in repo.heads]:
            print(f"La rama {branch_name} YA existe")
        else:
            break
    if branch_name:
        repo.create_head(branch_name)
        print(f"Rama {branch_name} creada")


def delete_branch():
    deleting_branch = repo.heads[branch_index()]
    if yes_no(f"Eliminar {deleting_branch}"):
        repo.delete_head(deleting_branch)
        print(f"Rama {deleting_branch} eliminada.")


def change_branch() -> None:
    global repo

    branch_num = branch_index()
    if repo.heads[branch_num] != repo.active_branch:
        repo.heads[branch_num].checkout()
    print(f"Rama actual {repo.active_branch}")


def show_branches() -> None:
    for r in repo.branches:
        if r == repo.active_branch:
            print("* " + str(r))
        else:
            print(r)


def show_status() -> None:
    untracked = repo.untracked_files
    news_ = repo.index.diff(repo.head.commit)
    modified = repo.index.diff(None)
    sep_ = "\n"

    if untracked:
        print(f"\nFicheros 'untracked'")
        for r in untracked:
            print(f"\t{str(r).split(sep_)[0]}")

    if news_:
        print(f"\nFicheros nuevos")
        for r in news_:
            print(f"\t{str(r).split(sep_)[0]}")

    if modified:
        print(f"\nFicheros modificados")
        for r in modified:
            print(f"\t{str(r).split(sep_)[0]}")


def show_log() -> None:
    current_branch = repo.active_branch
    for x in list(repo.iter_commits(current_branch, max_count=20)):
        print(f"{x.committed_date} - {x.message} - {x}")


def yes_no(question: str) -> bool:
    yes_no = input(question + " (Y/N) => ")
    return True if yes_no.lower().startswith("y") else False


def new_directory(repo_path: str) -> bool:
    try:
        os.mkdir(repo_path)
        return new_repo(repo_path)
    except Exception as e:
        print(str(e))
        return False


def new_repo(repo_path: str) -> bool:
    try:
        _ = git.Repo.init(repo_path, bare=False)
        return True
    except Exception as e:
        print(str(e))
        return False


def set_repo() -> git.Repo:

    repo_path = input("Ingresar directorio: ")
    if check_path(repo_path):
        if not is_repo(repo_path):
            if yes_no("Crear nuevo repo?"):
                if new_repo(repo_path):
                    print(f"Repositorio creado en {repo_path}")
                else:
                    quit(3)
            else:
                quit(2)
    else:
        if yes_no("Crear Directorio y generar repo?"):
            new_directory(repo_path)
        else:
            quit(1)
    return git.Repo(repo_path)


def add_commit() -> None:
    message = input("Ingrese detalle del commit: ")
    message = "Commit manual" if not message else message
    if repo.is_dirty():
        untracked = repo.untracked_files
        news_ = repo.index.diff(repo.head.commit)
        modified = repo.index.diff(None)
        sep_ = "\n"

        files = [str(r).split(sep_)[0] for r in untracked]
        if files:
            repo.index.add(files)

        files = [str(r).split(sep_)[0] for r in news_]
        if files:
            repo.index.add(files)

        files = [str(r).split(sep_)[0] for r in modified]
        if files:
            repo.index.add(files)

        repo.index.commit(message)


def pull() -> None:
    origin = repo.remote(name="origin")
    origin.pull()


def push() -> None:
    origin = repo.remote(name="origin")
    origin.push()


repo = set_repo()
while True:
    option = menu()
    match option:
        case  0:
            # Salir
            break
        case 1:
            # Mostrar ramas
            show_branches()
        case 2:
            # Cambiar de rama
            change_branch()
        case 3:
            # Crear rama
            new_branch()
        case 4:
            delete_branch()
        case 5:
            # Ver status
            show_status()
        case 6:
            # Commit
            add_commit()
        case 7:
            # Pull
            pull()
        case 8:
            # Push
            push()
        case 9:
            # Ver commits history
            show_log()
