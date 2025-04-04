"""
# 43 - Git Github CLI
"""

# Desarrolla un CLI (Command Line Interface) que permita interactuar con Git y GitHub de manera real desde terminal.
# El programa debe permitir las siguientes opciones:
    # 1. Establecer el directorio de trabajo
    # 2. Crear un nuevo repositorio
    # 3. Crear una nueva rama
    # 4. Cambiar de rama
    # 5. Mostrar ficheros pendientes de hacer commit
    # 6. Hacer commit (junto con un add de todos los ficheros)
    # 7. Mostrar el historial de commits
    # 8. Eliminar rama
    # 9. Establecer repositorio remoto
    # 10. Hacer pull
    # 11. Hacer push
    # 12. Salir
# Puedes intentar controlar los diferentes errores.

import argparse
import requests
import subprocess
import os
import sys

current_dir = os.getcwd()

def set_working_directory(path):
    """Set the working directory for git operations"""
    global current_dir
    if os.path.exists(path):
        current_dir = path
        print(f"Working directory set to: {current_dir}")
        return True
    else:
        print(f"Error: Directory {path} does not exist")
        return False

def create_repository():
    """Create a new git repository in the current directory"""
    try:
        subprocess.run(["git", "init"], cwd=current_dir, check=True)
        print(f"Repository initialized in {current_dir}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating repository: {e}")
        return False

def create_branch(branch_name):
    """Create a new git branch"""
    try:
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=current_dir, check=True)
        print(f"Branch '{branch_name}' created")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e}")
        return False

# Add more functions for the remaining operations

def main():
    parser = argparse.ArgumentParser(description="Git and GitHub CLI")
    parser.add_argument("--dir", help="Set working directory")
    parser.add_argument("--init-repo", action="store_true", help="Create a new repository")
    parser.add_argument("--create-branch", metavar="BRANCH", help="Create a new branch")
    parser.add_argument("--checkout", metavar="BRANCH", help="Switch to branch")
    parser.add_argument("--status", action="store_true", help="Show pending files")
    parser.add_argument("--commit", metavar="MESSAGE", help="Add and commit all files")
    parser.add_argument("--log", action="store_true", help="Show commit history")
    parser.add_argument("--delete-branch", metavar="BRANCH", help="Delete a branch")
    parser.add_argument("--set-remote", metavar="URL", help="Set remote repository")
    parser.add_argument("--pull", action="store_true", help="Pull changes")
    parser.add_argument("--push", action="store_true", help="Push changes")
    
    args = parser.parse_args()
    
    # Process arguments and call appropriate functions
    if args.dir:
        set_working_directory(args.dir)
    elif args.init_repo:
        create_repository()
    # Add more conditions for other arguments
    
if __name__ == "__main__":
    main()