import os

'''
Ejercicio
'''
file_name = "mvidalb.txt"

with open(file_name, "w") as file:
    file.write("Mario\n")
    file.write("40\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)
    

'''
Ejercicio extra
'''
file_txt = "ventas.txt"
open(file_txt, "a")     #a = append, seguir añadiendo

while True:
   print("¡Bienvenido!")
   print("1. Añadir producto.")
   print("2. Consultar producto.")
   print("3. Actualizar producto.")
   print("4. Eliminar producto.")
   print("5. Mostrar productos.")
   print("6. Calcular venta total.")
   print("7. Calcular venta por producto.")
   print("8. Salir.")
   accion = input("Selecciona la acción a realizar: ")

   match accion:
        case "1":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_txt, "a",) as file:   #a = append, seguir añadiendo
                file.write(f"{name}, {quantity}, {price}\n")
        case "2":
            name = input("Nombre: ")
            with open(file_txt, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                        break
                print("Ese producto no existe!\n")
        case "3":
            name = input("Nombre: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_txt, "r") as file:   # Copio todas las líneas
                lines = file.readlines()
            with open(file_txt, "w") as file:  # Escribo todo de nuevo
                for line in lines:
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                        print("Producto actualizado!\n")
                    else:
                        file.write(line)
        case "4":
            name = input("Nombre: ")
            with open(file_txt, "r") as file:   # Copio todas las líneas
                lines = file.readlines()
            with open(file_txt, "w") as file:  # Escribo todo de nuevo
                for line in lines:
                    if line.split(", ")[0] != name:
                        file.write(line)
                    else:
                        print("Ese producto no existe!")
        case "5":
            with open(file_txt, "r") as file:
                print(file.read())
        case "6":
            total_price = 0
            with open(file_txt, "r") as file:
                for line in file.readlines():
                    quantity = int(line.split(", ")[1])
                    price = float(line.split(", ")[2])
                    total_price += quantity*price
                print(f"Venta total: {total_price} €")
        case "7":
            name = input("Nombre: ")
            total_product = 0
            with open(file_txt, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(line.split(", ")[1])
                        price = float(line.split(", ")[2])
                        total_product += quantity*price
                        break
                print(f"Venta producto {name}: {total_product} €")
        case "8":
            print("ventas.txt ha sido borrado. ¡Hasta pronto!")
            os.remove(file_txt)
            break
        case _:
            print("No ha seleccionado ninguna acción entre los números 1 y 5.")

    