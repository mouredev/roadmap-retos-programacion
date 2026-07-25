import os
import subprocess
import sys


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr.strip()}")
        else:
            print("ejecuto bien")
            print(result.stdout.strip())
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    current_directory = os.getcwd()
    print(f"Starting in directory: {current_directory}")
    
    while True:
        print("\nGit CLI Menu:")
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

        choice = input("\nSelecciona una opción: ")

        if choice == "1":
            new_directory = input("Introduce el nuevo directorio de trabajo: ")
            if os.path.isdir(new_directory):
                os.chdir(new_directory)
                current_directory = os.getcwd()
                print(f"Directorio cambiado a: {current_directory}")
            else:
                print("Directorio no válido.")
        
        elif choice == "2":
            run_command("git init")
        
        elif choice == "3":
            branch_name = input("Introduce el nombre de la nueva rama: ")
            run_command(f"git branch {branch_name}")
        
        elif choice == "4":
            branch_name = input("Introduce el nombre de la rama a la que deseas cambiar: ")
            run_command(f"git checkout {branch_name}")
        
        elif choice == "5":
            run_command("git status")
        
        elif choice == "6":
            commit_message = input("Introduce el mensaje del commit: ")
            run_command("git add .")
            run_command(f'git commit -m "{commit_message}"')
        
        elif choice == "7":
            run_command("git log --oneline")
        
        elif choice == "8":
            branch_name = input("Introduce el nombre de la rama a eliminar: ")
            run_command(f"git branch -d {branch_name}")
        
        elif choice == "9":
            remote_url = input("Introduce la URL del repositorio remoto: ")
            run_command(f"git remote add origin {remote_url}")
        
        elif choice == "10":
            run_command("git pull origin $(git branch --show-current)")
        
        elif choice == "11":
            run_command("git push origin $(git branch --show-current)")
        
        elif choice == "12":
            print("¡Hasta luego!")
            sys.exit(0)
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
