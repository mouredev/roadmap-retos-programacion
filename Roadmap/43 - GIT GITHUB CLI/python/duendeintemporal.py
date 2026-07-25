#43 { Retos para Programadores } GIT GITHUB CLI 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

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

# Set up logging
log = print

current_directory = os.getcwd()
current_branch = 'main'
remote_repository = ''

def is_git_repository():
    return os.path.isdir(os.path.join(current_directory, '.git'))

def run_git_command(command):
    global current_directory
    try:
        result = subprocess.run(
            ['git'] + command.split(),
            cwd=current_directory,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise Exception(e.stderr.strip())

def main():
    log('Welcome to the GitHub Universe 2024 CLI!')

    while True:
        options = [
            '1. Set working directory',
            '2. Create new repository',
            '3. Create new branch',
            '4. Switch branch',
            '5. Show pending files',
            '6. Commit changes',
            '7. Show commit history',
            '8. Delete branch',
            '9. Set remote repository',
            '10. Pull from remote',
            '11. Push to remote',
            '12. Exit'
        ]

        log('\nPlease select an option:')
        log('\n'.join(options))

        choice = input('Enter your choice: ')

        if choice == '1':
            current_directory = input('Enter the new working directory: ')
            log(f'Working directory set to: {current_directory}')
        elif choice == '2':
            new_repo_name = input('Enter the name of the new repository: ')
            run_git_command(f'init {new_repo_name}')
            log(f'New repository created: {new_repo_name}')
        elif choice == '3':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            new_branch_name = input('Enter the name of the new branch: ')
            run_git_command(f'checkout -b {new_branch_name}')
            global current_branch
            current_branch = new_branch_name
            log(f'New branch created: {new_branch_name}')
        elif choice == '4':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            branch_to_switch = input('Enter the name of the branch to switch to: ')
            run_git_command(f'checkout {branch_to_switch}')
            current_branch = branch_to_switch
            log(f'Switched to branch: {branch_to_switch}')
        elif choice == '5':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            pending_files = run_git_command('status --porcelain')
            log('Pending files:')
            log(pending_files)
        elif choice == '6':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            run_git_command('add .')
            commit_message = input('Enter the commit message: ')
            run_git_command(f'commit -m "{commit_message}"')
            log('Changes committed successfully')
        elif choice == '7':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            commit_history = run_git_command('log --oneline')
            log('Commit history:')
            log(commit_history)
        elif choice == '8':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            branch_to_delete = input('Enter the name of the branch to delete: ')
            run_git_command(f'branch -d {branch_to_delete}')
            log(f'Branch {branch_to_delete} deleted')
        elif choice == '9':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            global remote_repository
            remote_repository = input('Enter the URL of the remote repository: ')
            run_git_command(f'remote add origin {remote_repository}')
            log(f'Remote repository set to: {remote_repository}')
        elif choice == '10':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            run_git_command(f'pull origin {current_branch}')
            log('Pulled changes from remote repository')
        elif choice == '11':
            if not is_git_repository():
                log('Error: Not in a Git repository. Please initialize a repository first.')
                continue
            run_git_command(f'push -u origin {current_branch}')
            log('Pushed changes to remote repository')
        elif choice == '12':
            log('Exiting the GitHub Universe 2024 CLI...')
            break
        else:
            log('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()

