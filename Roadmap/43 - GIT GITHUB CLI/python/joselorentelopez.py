"""
Owner: José Lorente López | joselorente1105@gmail.com | Linkedin: www.linkedin.com/in/josé-lorente-lópez-0121b7148

Description: CLI capable of interacting with Git and Github from the terminal.

Coding: UTF-8
"""

import os
import subprocess

class CLI():
    def __init__(self) -> None:
        pass

class Git_CLI(CLI):
    def __init__(self):
        super().__init__()

    @staticmethod
    def set_working_directory():
        path_ = input("Enter the working directory: ").strip()
        try:
            os.chdir(path_)
            print(f"\nWorking directory changed to: {os.getcwd()}\n")
        except FileNotFoundError:
            print(f"\nError: The directory '{path_}' does not exist.\n")
        except Exception as e:
            print(f"\nError {e}: An unexpected error occurred while setting the working directory.\n")

    @staticmethod
    def create_new_repo():
        try:
            subprocess.run(["git", "init"], check=True)
            print(f"\nNew repository generated in {os.getcwd()}\n")
        except subprocess.CalledProcessError as e:  # CalledProcessError means that a subprocess started by Python exited with an error
            print(f"\nError {e}: Failed to create the new repository.\n")

    @staticmethod
    def create_new_branch():
        branch_name = input("Enter the new branch name: ").strip()
        if not branch_name:
            print("Branch name cannot be empty.")
            return

        # Check if the repository has an initial branch
        result = subprocess.run(["git", "branch"], capture_output=True, text=True)
        branches = result.stdout.splitlines()

        if not branches:
            # If there are no branches, create 'main' as the initial branch
            try:
                subprocess.run(["git", "checkout", "-b", "main"], check=True)
                print("No initial branch found. 'main' created as the default branch.")
                
                # Make an initial commit to avoid further issues
                with open("README.md", "w") as f:
                    f.write("# Initial Commit\n")
                
                subprocess.run(["git", "add", "README.md"], check=True)
                subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
                print("Initial commit created in 'main'.")
            except subprocess.CalledProcessError as e:
                print(f"\nError {e}: Failed to create the 'main' branch and initial commit.\n")
                return

        # Proceed with creating the new branch
        try:
            subprocess.run(["git", "checkout", "main"], check=True)
            subprocess.run(["git", "branch", branch_name], check=True)
            print(f"\nNew branch '{branch_name}' created.\n")
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to create the new branch '{branch_name}'.\n")

    @staticmethod
    def show_branch_list():
        try:
            subprocess.run(["git", "branch", "-a"], check=True)
            print("\nList of available branches:")
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to display the branch list.\n")

    @staticmethod
    def change_branch():
        branch_name = input("Enter the name of the branch you wish to move to: ").strip()
        if not branch_name:
            print("Branch name cannot be empty.")
            return

        # Comprobar si es una rama remota
        if branch_name.startswith("origin/"):
            local_branch_name = branch_name.split("/")[1]  # Extraer el nombre de la rama local

            try:
                subprocess.run(["git", "checkout", "-b", local_branch_name, branch_name], check=True)
                print(f"\nCreated and switched to local branch '{local_branch_name}' from remote '{branch_name}'.\n")
            except subprocess.CalledProcessError as e:
                print(f"\nError {e}: Failed to create and switch to local branch '{local_branch_name}'.\n")
            return

        try:
            subprocess.run(["git", "checkout", branch_name], check=True)
            print(f"\nMoved to branch '{branch_name}'.\n")
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to move to branch '{branch_name}'.\n")


    @staticmethod
    def show_pending_files():
        try:
            subprocess.run(["git", "status"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to show pending files.\n")

    @staticmethod
    def commit_changes():
        commit_message = input("Enter the commit message: ").strip()
        if not commit_message:
            print("Commit message cannot be empty.")
            return
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            print(f"\nCommit made successfully.\n")
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to commit changes.\n")
    
    @staticmethod
    def show_commit_history():
        try:
            subprocess.run(["git", "log", "--oneline"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to show commit history.\n")

    @staticmethod
    def delete_branch():
        branch_name = input("Enter the name of the branch you wish to delete: ").strip()
        if not branch_name:
            print("Branch name cannot be empty.")
            return
        try:
            subprocess.run(["git", "branch", "-d", branch_name], check=True)
            print(f"\nBranch '{branch_name}' deleted.\n")
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to delete branch '{branch_name}'.\n")    

    @staticmethod
    def set_remote_repository():
        remote_url = input("Enter the remote repository URL: ").strip()
        if not remote_url:
            print("Remote repository URL cannot be empty.")
            return
        try:
            subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
            print(f"Remote repository '{remote_url}' set correctly.\n")
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to connect to remote repository '{remote_url}'.\n")

    @staticmethod
    def pull_changes(): # recommended pre push
        try:
            subprocess.run(["git", "pull"], check=True) # download and integrate changes from the server to your local repository
            print("Changes pulled successfully.\n")
        except subprocess.CalledProcessError as e:
            print(f"\nError {e}: Failed to pull changes.\n")

    @staticmethod
    def push_changes():

        result = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
        
        if result.returncode != 0:
            print("Not a valid Git repository. Please ensure you are in a valid Git directory.")
            return

        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
        current_branch = result.stdout.strip()

        if not current_branch:
            print("No branch detected. Please ensure you have a branch checked out before pushing.")
            return

        commit_result = subprocess.run(["git", "rev-parse", current_branch], capture_output=True, text=True)

        if commit_result.returncode != 0:
            print(f"The branch '{current_branch}' has no commits. Please make an initial commit before pushing.")
            return

        try:
            subprocess.run(["git", "push", "-u", "origin", current_branch], check=True)
            print(f"Changes pushed successfully to branch '{current_branch}'.\n")
        except subprocess.CalledProcessError as e:
            print(f"Error {e}: Failed trying to push changes to branch '{current_branch}'.\n")

def main():
    """
    Runs the main function of the project.
    """

    git_cli = Git_CLI()

    while True:
        print("\nOptions:")
        print("1. Set the working directory")
        print("2. Create a new repository")
        print("3. Create a new branch")
        print("4. Switch branches")
        print("5. Show branch list")
        print("6. Show files pending commit")
        print("7. Commit (along with adding all files)")
        print("8. Show commit history")
        print("9. Delete branch")
        print("10. Set remote repository")
        print("11. Pull")
        print("12. Push")
        print("13. Exit")
        
        choice = input("Choose an option: ").strip()
        print(" ")

        if choice == '1':
            git_cli.set_working_directory()
        elif choice == '2':
            git_cli.create_new_repo()
        elif choice == '3':
            git_cli.create_new_branch()
        elif choice == '4':
            git_cli.change_branch()
        elif choice == '5':
            git_cli.show_branch_list()
        elif choice == '6':
            git_cli.show_pending_files()
        elif choice == '7':
            git_cli.commit_changes()
        elif choice == '8':
            git_cli.show_commit_history()
        elif choice == '9':
            git_cli.delete_branch()
        elif choice == '10':
            git_cli.set_remote_repository()
        elif choice == '11':
            git_cli.pull_changes()
        elif choice == '12':
            git_cli.push_changes()
        elif choice == '13':
            print("See you later!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
