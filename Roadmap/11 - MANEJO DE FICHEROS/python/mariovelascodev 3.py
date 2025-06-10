#Importamos el modulo os para trabajar con el sistema
import os

#Función que crea un fichero con la extensión .txt
def create_file():
    #Abrimos el fichero, y le indicamos el nombre con el que se guardara
    file = open("mariovelascodev.txt", "w")
    
    #Solicitamos que el usuario nos introduca su nombre, edad, y lenguaje de programación favorito
    add_data = []
    name = input("Introduce tu nombre: ")
    age = input("Introduce tu edad: ")

    #Añadimos lo datos introducidos por el usuario a una lista
    add_data.append(name)
    add_data.append(age)
    
    #Solicitamos tantos lenguajes de programción como quiera añadir el usuario
    while True:
        favorite_language = input("Introduce tu lenguaje de programación favorito(escribe \"q\" para salir): ")
        if favorite_language == "q":
            break
        else:
            add_data.append(favorite_language)
    
    #Recorremos la lista y escribimos los valores en lineas distintas del fichero
    for line in add_data:
        file.write(f"{line.title()}\n")

    #Cerramos el fichero
    file.close()

#Función que lee un fihero
def read_file():
    #Abrimos el fichero y lo leemos
    file = open("mariovelascodev.txt", "r")

    print("\nEl contenido del fichero es:")
    print(file.read())

    #Cerramos el fichero
    file.close() 

#Función que elimina un fichero
def remove_file():
    #Nombre del fichero a eliminar
    file = "mariovelascodev.txt"

    #Borrado del fichero indicado
    os.remove(file)


create_file()
read_file()
remove_file()