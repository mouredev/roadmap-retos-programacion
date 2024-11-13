import os

"""
Ejercicio
"""

file_name = "ipfabio.txt"

with open(file_name, 'w') as archivo:
    archivo.write("Fabio\n")
    archivo.write("40\n")
    archivo.write("Python\n")

with open(file_name, "r") as archivo_a_leer:
    contenido = archivo_a_leer.read()
    print(contenido)

if os.path.exists(file_name):
    os.remove(file_name)
    print(f"El archivo: {file_name} ha sido borrado.\n")
else:
    print(f"El archivo: {file_name} no se encuentra.\n")

"""
Extra
"""

file_name = "ipfabio_shop.txt"

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")
    print(" ")
    option = input("Selecciona una opción: ")
    
    match option:
        case "1": # Añadir producto
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")

            with open(file_name, 'a') as archivo:
                archivo.write(f"{name}, {quantity}, {price}\n")
        case "2": # Consultar producto
            name = input("Nombre: ")
            found = False # Variable para rastrear si se encontró el producto
            
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                        found = True
                        break
            if not found:
                print(f"{name} no se encuentra en la lista. Intenta agregandolo")

        case "3": # Actualizar producto
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            found = False

            # Leer el archivo y almacernarlo en 'lines' 
            with open(file_name, "r") as file:
                lines = file.readlines()

            # Abrir el archivo para sobreescribir
            with open(file_name, "w") as file:
                for line in lines: # Usar la lista 'lines' que ya fue leida
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                        found = True # El producto fue encontrado y actualizado
                    else:
                        file.write(line)

            if not found:
                print(f"Producto {name} no encontrado.")
            else:
                print(f"Producto: {name}. Actualizado correctamente!")
        case "4": # Borrar producto
            name = input("Nombre: ")

            with open(file_name, "r") as file:
                lines = file.readlines()

            with open(file_name, "w") as file:
                for line in lines: # Usar la lista 'lines' que ya fue leida
                    if line.split(", ")[0] != name:
                        file.write(line) # Solo me quedo con lo items que no cumplen con el nombre ingresado.
            print(f"{name} ha sido borrado.")
                    
        case "5": # Mostrar productos
            if os.path.exists(file_name):
                with open(file_name, "r") as productos_a_mostrar:
                    print(productos_a_mostrar.read())
            else:
                print("Todavía no se ha generado la lista de compras. Pruebe agregando productos\n")
        case "6": # Calcular venta total
            total = 0
             
            # Leer el archivo y almacernarlo en 'lines' 
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            print(f"Total a pagar: ${total}")

        case "7": # Calcular venta por producto
            name = input("Nombre: ")
            total = 0
             
            # Leer el archivo y almacernarlo en 'lines' 
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
            print(f"{name} total es: ${total}")

        case "8": # Salir
            print("Saliendo...")
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"El archivo: {file_name} ha sido borrado.")
            else:
                print(f"El archivo: {file_name} no se encuentra.")
            break
        case _:
            print("No es una opción válida.\n")