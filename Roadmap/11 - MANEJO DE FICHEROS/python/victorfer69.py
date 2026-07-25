import os

#EJERCICIO

file_name = "victorfer69.txt"

#Escribir en el fichero
with open(file_name, "w") as file:
    file.write("Victor\n")
    file.write("21\n")
    file.write("Python")

#Leer el fichero
with open(file_name, "r") as file:
    print(file.read())

#Borrar el fichero
os.remove(file_name)


#EJERCICIO EXTRA

def gestionDeVentas(file_name:str):

    salir = False

    while not salir:
        
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Borrar producto")
        print("5. Mostrar productos")
        print("6. Calcular venta total")
        print("7. Calcular venta por producto")
        print("8. Salir")
        action = input("Seleccione el modo:")

        match action:

            case "1":

                name = input("Dame el nombre del producto: ")
                quantity = int(input("Dame la cantidad: "))
                price = float(input("Dame el precio: "))

                with open(file_name, "a") as file:
                    if name != None and quantity != None and quantity > 0 and price != None and price > 0:
                        file.write(f"{name}, {quantity}, {price}\n")
                    else:
                        print("Algún argumento invalido")
                
            case "2":

                product = input("¿Que producto quieres consultar?: ")
                existe = False

                with open(file_name, "r") as file:
                    for line in file.readline():
                        if line.split(",")[0] == product:
                            print(line)
                            existe = True

                if not existe:
                    print(f"No hay {product}")   

            case "3":

                name = input("Dame el nombre del producto: ")
                quantity = int(input("Dame la cantidad: "))
                price = float(input("Dame el precio: "))

                with open(file_name, "r") as file:
                    lines = file.readlines()

                with open(file_name, "w") as file:
                    for line in lines:
                        if line.split(", ")[0] == name:
                            file.write(f"{name}, {quantity}, {price}\n")
                        else:
                            file.write(line)

            case "4":
                
                name = input("Dame el nombre del producto: ")

                with open(file_name, "r") as file:
                    lines = file.readlines()

                with open(file_name, "w") as file:
                    for line in lines:
                        if line.split(", ")[0] != name:
                            file.write(line)

            case "5":
                
                with open(file_name, "r") as file:
                    print(file.read())

            case "6":

                total = 0

                with open(file_name, "r") as file:
                    for line in file.readlines():
                        components = line.split(", ")
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                
                print(total)

            case "7":
                
                name = input("Nombre: ")
                total = 0
                existe = False

                with open(file_name, "r") as file:
                    for line in file.readlines():
                        components = line.split(", ")
                        if components[0] == name:
                            quantity = int(components[1])
                            price = float(components[2])
                            total += quantity * price
                            existe = True
                            break

                if existe:
                    print(total)
                else:
                    print(f"El producto {name} no existe")

            case "8":

                print("Saliendo del programa (borrando fichero)")
                os.remove(file_name)
                salir = True

            case _:
                
                print("Seleccione una opcion correcta.")


#Fichero inicial
with open("ventas.txt", "a") as file:
    file.write("Patata, 4, 0.25\n")
    file.write("Pan, 5, 0.2\n")
    file.write("Sopa, 2, 0.5\n")
    file.write("Carne, 1, 1\n")

gestionDeVentas("ventas.txt")