import os


"""Ejercicio"""

# file_name = "Tomas-LunaH"

# with open(file_name, "w") as file:
#     file.write("Tomas Luna\n")
#     file.write("20\n")
#     file.write("Python")
# with open(file_name, "r") as file:
#     print(file.read())

# os.remove(file_name)

# """Extra"""
file_sale = "Ventas de la tienda.txt"
action = 0


def add_product():
    product = input("Ingrese nombre del producto: ")
    quantity = int(input("Ingresa cantidad vendida: "))
    price = float(input("Ingrese el precio del producto: "))
    with open(file_sale, "a") as file:
        file.write(f"{product.lower()}, {quantity}, {price} \n")

def search_product():
    if os.path.isfile(file_sale):
        with open(file_sale, "r") as file:
                search = input("Ingresa el producto a buscar: ").lower()
                print(search)
                status = False
                for line in file:
                    data = line.split(",")
                    if search in data[0].strip(""):
                        print("Se a encontrado una coincidencia")
                        print(f"Producto: {data[0]}, Unidades vendidas :{data[1]}, Precio : {data[2]} ")
                        status = True
                        break
                if status == False:
                    print("No se encontro nada")
    else:
        print("No existe ningun fichero")
def update_product():
    if os.path.isfile(file_sale):
        with open(file_sale,"r") as file:
            lines = file.readlines()
            found = False
            new_file = []
            old_product = input("Ingrese el producto a realizar ").lower()
            for line in lines:
                data = line.split(",")
                if data[0].strip() == old_product:
                    print(f"El pruducto {data[0]} se actualizara")
                    quantity = int(input("Ingresa la nueva cantidad vendida: "))
                    price = float(input("Ingrese el nuevo precio del producto: "))
                    new_file.append(f"{data[0].strip().lower()} ,{quantity}, {price}\n")
                    found = True
                else:
                    new_file.append(line)
            if found == False:
                print(f"No se encontro {old_product} en el archivo")
            else:
                with open(file_sale, "w") as file:
                    file.writelines(new_file)
                    print("Producto actualizado con exito")
    else:
        print("No existe ningun fichero")
def delete_product():
    if os.path.isfile(file_sale):
        with open(file_sale,"r") as file:
            lines = file.readlines()
            found = False
            new_file = []
            old_product = input("Ingrese el producto a eliminar: ").lower()
            for line in lines:
                data = line.split(",")
                if data[0].strip() == old_product:
                    print(f"El pruducto {data[0]} se eliminara")
                    found = True
                else:
                    new_file.append(line)
            if found == False:
                    print(f"No se encontro {old_product} en el archivo")
            else:
                with open(file_sale, "w") as file:
                    file.writelines(new_file)
                    print("Producto eliminado con exito")
    else:
        print("No existe ningun fichero")
def total_sale():
    if os.path.isfile(file_sale):
        tot_sale = 0
        with open(file_sale, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(",")
                tot_quantity = int(data[1].strip())
                tot_price = float(data[2].strip())
                tot_sale += tot_quantity*tot_price
            print(f"El total de ventas es de : {tot_sale}")
    else:
        print("NO existe ningun fichero")
def total_product():
    if os.path.isfile(file_sale):
        with open(file_sale,"r") as file:
            lines = file.readlines()
            found = False
            tot_product = 0
            cal_product = input("Ingrese el producto a calcular: ").lower()
            for line in lines:
                data = line.split(",")
                if data[0].strip() == cal_product:
                    tot_quantity = int(data[1].strip())
                    tot_price = float(data[2].strip())
                    tot_product += tot_quantity*tot_price
                    found = True
            if found == False:
                print(f"No se encontro {cal_product} en el archivo")
            else:
                print(f"El total de ventas del producto '{cal_product}' es de: {tot_product}")
    else:
        print("No existe ningun fichero")
while True:
    action = int(input("1. Anadir producto \n" 
    "2. Consultar producto \n" 
    "3. Actualizar producto \n" 
    "4. Eliminar producto \n" 
    "5. Calcular venta total \n"
    "6. Calcular venta de producto \n"
    "7. Salir \n"
    "Ingrese la actividad a realizar: "
    ))
    match action:
        case  1:
            add_product()

        case 2:
            search_product()

        case 3:
            update_product()

        case 4:
            delete_product()

        case 5:
            total_sale()

        case 6:
            total_product()

        case 7:
            if os.path.isfile(file_sale):
                print(f"Saliendo del archivo: {file_sale}")
                os.remove(file_sale)
                break
            else:
                print("No tienes ningun archivo para eliminar. Saliendo....")
                break
        case _:
            print("Accion no establecida")
    