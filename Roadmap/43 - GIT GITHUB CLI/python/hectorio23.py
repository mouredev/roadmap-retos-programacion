# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import os
import subprocess

def set_working_directory():
    path = input("Enter the working directory path: ")
    try:
        os.chdir(path)
        print(f"Working directory set to {os.getcwd()}")
    except FileNotFoundError:
        print("Invalid directory path.")

def create_repository():
    subprocess.run(["git", "init"])
    print("Repository initialized.")

def create_branch():
    branch = input("Enter branch name: ")
    subprocess.run(["git", "branch", branch])
    print(f"Branch '{branch}' created.")

def switch_branch():
    branch = input("Enter branch name: ")
    subprocess.run(["git", "checkout", branch])

def show_pending_files():
    subprocess.run(["git", "status"])

def commit_changes():
    message = input("Enter commit message: ")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])

def show_commit_history():
    subprocess.run(["git", "log", "--oneline"])

def delete_branch():
    branch = input("Enter branch name to delete: ")
    subprocess.run(["git", "branch", "-d", branch])

def set_remote():
    remote_url = input("Enter remote repository URL: ")
    subprocess.run(["git", "remote", "add", "origin", remote_url])

def pull_changes():
    subprocess.run(["git", "pull", "origin"])

def push_changes():
    subprocess.run(["git", "push", "origin"])

def exit_program():
    print("Goodbye!")
    exit()

actions = {
    "1": set_working_directory,
    "2": create_repository,
    "3": create_branch,
    "4": switch_branch,
    "5": show_pending_files,
    "6": commit_changes,
    "7": show_commit_history,
    "8": delete_branch,
    "9": set_remote,
    "10": pull_changes,
    "11": push_changes,
    "12": exit_program
}

while True:
    print("\nOptions:")
    for key, func in actions.items():
        print(f"{key}. {func.__name__.replace('_', ' ').capitalize()}")
    choice = input("\nSelect an option: ")
    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid option.")
