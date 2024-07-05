import os


def user_file(data: list):
    file_name = f"{data[0]}.txt"

    with open(file_name, "w") as file:
        file.write(f"{data[1]}\n")
        file.write(f"{data[2]}\n")
        file.write(f"{data[3]}\n")

    with open(file_name, "r") as file:
        print(file.read())

    os.remove(file_name)


def sales_manager(file_manager: str):
    file_name = f"{file_manager}.txt"
    while True:
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir")

        option = input("Selecciona la opción deseada: ")

        if option == "1":
            product_name, quantity, price = input("Producto,cantidad,precio: ").split(
                ","
            )
            with open(file_name, "a") as file:
                file.write(f"{product_name}, {quantity}, {price}\n")
        elif option == "2":
            product_name, quantity, price = input("Producto,cantidad,precio: ").split(
                ","
            )
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == product_name:
                        file.write(f"{product_name}, {quantity}, {price}\n")
                    else:
                        file.write(line)
        elif option == "3":
            product_name = input("Producto: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != product_name:
                        file.write(line)
        elif option == "4":
            with open(file_name, "r") as file:
                print(file.read())
        elif option == "5":
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    items = line.split(", ")
                    quantity = int(items[1])
                    price = float(items[2])
                    total += quantity * price
            print(total)
        elif option == "6":
            product_name = input("Producto: ")
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    items = line.split(", ")
                    if items[0] == product_name:
                        quantity = int(items[1])
                        price = float(items[2])
                        total += quantity * price
                        break
            print(total)
        elif option == "7":
            os.remove(file_name)
            break
        else:
            print("Selecciona una de las opciones disponibles.")


if __name__ == "__main__":
    user_file(["mikelm2020", "Miguel Angel Lopez", "52", "Python"])
    sales_manager("ventas")
