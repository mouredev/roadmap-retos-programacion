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

#Extra

def sales_management():
    open("sales management.txt", "a")

    while True:
        print(
        "1. Añadir producto\n" \
        "2. Consultar producto\n" \
        "3. Actualizar producto\n" \
        "4. Eliminar producto\n" \
        "5. Mostrar productos\n" \
        "6. Calcular venta total\n" \
        "7. Calcular venta producto\n" \
        "8. Salir")

        option = int(input("Introduce el número de la opción que desea realizar: "))

        match option:
            case 1:
                #Solicitamos que el usuario nos introduca nombre del producto, cantidad vendida y el precio
                name = input("Introduce el nombre del producto: ")
                amount = input("Introduce la cantidad vendida: ")
                price = input("Introduce el precio: ")

                with open("sales management.txt", "a") as file:
                    file.write(f"{name}, {amount}, {price}\n")
                
            case 2:
                name = input("Introduce el nombre del producto a consultar: ")

                with open("sales management.txt", "r") as file:
                    content_file = file.readlines()
                    for line in content_file:
                        element = line.split(",")
                        if name == element[0]:
                            print(line)

            case 3:
                name = input("Introduce el nombre del producto a actualizar: ")
                update = False

                with open("sales management.txt", "r") as file:
                    content_file = file.readlines()
                    #Buscamos la posición donde se encuentra el producto a actualizar
                    for element in content_file:
                        if name in element:
                            position = content_file.index(element)
                            name = input("Introduce el nombre del producto: ")
                            amount = input("Introduce la cantidad vendida: ")
                            price = input("Introduce el precio: ")
                            #Actualizamos el producto
                            content_file[position] = f"{name}, {amount}, {price}\n"
                            update = True
                
                if update:
                    #Escribimos de nuevo el fichero con los cambios            
                    with open("sales management.txt", "w")as file:
                            for line in content_file:
                                file.writelines(line)
                    print("Producto actualizado")
                else:
                    print("Producto no encontrado")

            case 4:
                name = input("Introduce el nombre del producto a eliminar: ")
                update = False

                with open("sales management.txt", "r") as file:
                    content_file = file.readlines()
                    #Buscamos la posición donde se encuentra el producto a actualizar
                    for element in content_file:
                        if name in element:
                            position = content_file.index(element)
                            #Borramos producto
                            content_file.remove(content_file[position])
                            print("Producto eliminado")
                            update = True
                
                if update:
                    #Escribimos de nuevo el fichero con los cambios            
                    with open("sales management.txt", "w")as file:
                        for line in content_file:
                            file.writelines(line)
                else:
                    print("Producto no encontrado")
                
            case 5:
                with open("sales management.txt", "r") as file:
                    lines = file.readlines()

                    for line in lines:
                        print(line.replace("\n","")) 

            case 6:
                total = 0
                with open("sales management.txt", "r") as file:
                    content_file = file.readlines()
                    for line in content_file:
                        element = line.split(",")
                        amount = int(element[1])
                        price = float(element[2])
                        total += amount * price
                print(f"El valor total de los productos es {total}")
                
            case 7:
                total = 0
                name = input("Introduce el nombre del producto del que desea ver su venta: ")

                with open("sales management.txt", "r") as file:
                    content_file = file.readlines()
                    for line in content_file:
                        element = line.split(",")
                        if name in element:
                            amount = int(element[1])
                            price = float(element[2])
                            total = amount * price
                    print(f"El valor total de la venta del producto {name} es: {total}")

            case 8:
                #Borrado del fichero indicado
                os.remove("sales management.txt")

                return False    
            case _:
                print("Debes indicar un número entre 1 y 8")
            

sales_management()