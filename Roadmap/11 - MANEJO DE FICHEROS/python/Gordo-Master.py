"""
Manejo de ficheros
"""

import os

with open("./Gordo-Master.txt", 'w') as f:
    f.write("Mi nombre es Gordo-Master\n")
    f.write("Tengo 29 años\n")

with open("./Gordo-Master.txt", 'a') as f:
    f.write("¡Mi lenguaje de programación favorito es Python!")

with open("./Gordo-Master.txt", 'r') as f:
    text_1 = f.read()
    print(text_1)

os.remove("./Gordo-Master.txt")

"""
Ejercicio extra
"""

def consult(item = "all_list", present = False):
    
    consult_list = {}  

    with open("./ventas.txt","r") as f:

        sell_list = f.readlines()

        if item == "all_list":

            for n,i in enumerate(sell_list):
                consult_list[n] = i.split(", ")
                consult_list[n][2] = consult_list[n][2].rstrip("\n")
                present = True
            
            if not present:
                    print("No se registraron ventas...")
                    return None
            
            return consult_list
        
        else:

            for n,i in enumerate(sell_list):
                sell_list[n] = i.split(", ")
                if sell_list[n][0] == item:
                    consult_list[n] = sell_list[n]
                    consult_list[n][2] = consult_list[n][2].rstrip("\n")
                    present = True
            
            if not present:
                    print("No se encontro el producto...")
                    return None
            
            return consult_list
    
def add_to_file(name, count, price):
    
    with open("./ventas.txt", "a") as f:
        add = ", ".join([name,count,price]) + "\n"
        f.write(add)

def del_item( item):
    consult_list = consult(item)
    all_list = consult()

    if consult_list:

        print("Elige la opción a eliminar: ")
        
        for i in consult_list:
            print(f"{i}. {consult_list[i][0]} , cant: {consult_list[i][1]}, pre: {consult_list[i][2]}")

        item_to_del = int(input("Numero: "))
        
        if item_to_del in consult_list:
            del all_list[item_to_del]
        
        else:
            print("Valor invalido")

    f = open("./ventas.txt", "w")
    f.close()
    
    for i in all_list:
        add_to_file(all_list[i][0],all_list[i][1],all_list[i][2])

def ref_item(item):
    consult_list = consult(item)
    all_list = consult()

    if consult_list:

        print("Elige la opción a actualizar: ")
        
        for i in consult_list:
            print(f"{i}. {consult_list[i][0]} , cant: {consult_list[i][1]}, pre: {consult_list[i][2]}")

        item_to_ref = int(input("Numero: "))
        
        if item_to_ref in consult_list:
            print("Actualizar producto")
            name = input("Ingrese nuevo nombre_producto: ")
            count = input("Ingrese nueva cantidad_vendida: ")
            price = input("Ingrese nuevo precio: ")
            all_list[item_to_ref]=[name,count,price]

        
        else:
            print("Valor invalido")

    f = open("./ventas.txt", "w")
    f.close()
    
    for i in all_list:
        add_to_file(all_list[i][0],all_list[i][1],all_list[i][2])

def menu():

    f = open("./ventas.txt", "w")
    f.close()

    while True:
        print("Gestor de ventas".center(40,"-"))
        print("1. Añadir.".ljust(39),"|")
        print("2. Consultar.".ljust(39),"|")
        print("3. Actualizar".ljust(39),"|")
        print("4. Eliminar".ljust(39),"|")
        print("5. Calcular ventas por productos".ljust(39),"|")
        print("6. Calcular ventas totales".ljust(39),"|")
        print("7. Salir".ljust(39),"|")
        print("-"*40)
        action = input("Opción: ")

# [nombre_producto], [cantidad_vendida], [precio]
        match action:
            case '1':
                print("Añadir producto")
                name = input("Ingrese el nombre_producto: ")
                count = input("Ingrese la cantidad_vendida: ")
                price = input("Ingrese el precio: ")
                add_to_file(name,count,price)
                
            case '2':
                item = input("Indique el producto a buscar: ")
                consult_list = consult(item)
                if consult_list:
                    for i in consult_list:
                        print(f"{i}. {consult_list[i][0]} , cant: {consult_list[i][1]}, pre: {consult_list[i][2]}")
                
            case '3':
                item = input("Indique el producto a actualizar: ")
                ref_item(item)
                    

            case '4':
                item = input("Indique el producto que quiere eliminar: ")
                del_item(item)

            case '5':
                item = input("Indique el producto del cual quiere calcular sus ventas totales: ")
                consult_list = consult(item)
                venta_totales = 0
                for i in consult_list:
                    venta_totales += float(consult_list[i][1]) * float(consult_list[i][2])
                print(f"Ventas totales de {item}: {venta_totales}")
            
            case '6':
                consult_list = consult()
                venta_totales = 0
                for i in consult_list:
                    venta_totales += float(consult_list[i][1]) * float(consult_list[i][2])
                print(f"Ventas totales: {venta_totales}")
            
            case '7':
                print("Saliendo del programa...")
                os.remove("./ventas.txt")
                break
            
            case _:
                print("Coloque un numero del 1 al 7...")

menu()