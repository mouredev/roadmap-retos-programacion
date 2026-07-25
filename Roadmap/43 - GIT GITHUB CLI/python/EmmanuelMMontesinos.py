"""
/*
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
 */
"""
import os

class GitCLI:
    def __init__(self):
        self.directorio = None
        self.remoto = None

    def mostrar_info(self):
        print(f"Directorio de trabajo: {self.directorio}")
        print(f"Repositorio remoto: {self.remoto}")
    def asignar_directorio(self):
        self.directorio = input("Introduce el directorio de trabajo: ")
        os.chdir(self.directorio)

    def nuevo_repositorio(self):
        os.system("git init")
        os.system("git branch -m main")

    def crear_rama(self):
        nombre_rama = input("Introduce el nombre de la rama para crear: ")
        os.system(f"git branch {nombre_rama}")

    def cambiar_rama(self):
        nombre_rama = input("Introduce el nombre de la rama a cambiar: ")
        os.system(f"git checkout {nombre_rama}")

    def mostrar_ficheros_pendientes(self):
        os.system("git status -s")

    def hacer_commit(self):
        os.system("git add .")
        mensaje = input("Introduce el mensaje del commit: ")
        os.system(f"git commit -m {mensaje}")

    def historial_commits(self):
        os.system("git log")

    def eliminar_rama(self):
        nombre_rama = input("Introduce el nombre de la rama a eliminar: ")
        os.system(f"git branch -d {nombre_rama}")

    def establecer_remoto(self):
        url = input("Introduce la URL del repositorio remoto: ")
        os.system(f"git remote add origin {url}")
        self.remoto = url
        os.system("git push -u origin main")

    def hacer_pull(self):
        os.system("git pull origin main")

    def hacer_push(self):
        os.system("git push")

    def bucle(self):
        while True:
            self.mostrar_info()
            print("\nSelecciona una opción: ")
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

            option = input("Opción: ")
            
            match option:
                case "1":
                    self.asignar_directorio()
                case "2":
                    self.nuevo_repositorio()
                case "3":
                    self.crear_rama()
                case "4":
                    self.cambiar_rama()
                case "5":
                    self.mostrar_ficheros_pendientes()
                case "6":
                    self.hacer_commit()
                case "7":
                    self.historial_commits()
                case "8":
                    self.eliminar_rama()
                case "9":
                    self.establecer_remoto()
                case "10":
                    self.hacer_pull()    
                case "11":
                    self.hacer_push()
                case "12":
                    break
                case _:
                    print("Opcion incorrecta")

# Prueba

if __name__ == "__main__":
    cli = GitCLI()
    cli.bucle()