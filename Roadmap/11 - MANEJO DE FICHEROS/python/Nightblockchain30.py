# ```
# /*
#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  * 
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.
#  */

import os

file_name = "Nightblockchain30.txt"

with open(file_name,'w') as file:
    file.write("Alonso\n")
    file.write("26\n")
    file.write("Python\n")

with open(file_name,'r') as file:
    print(file.read())

os.remove(file_name)

#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.

def message_option(option):
    match option:
        case 1:
            return "Agregando..."
        case 2:
            return "Consultando un producto deseado.."
        case 3:
            return "Actualizando..."
        case 4:
            return "Eliminando..."
        case 5:
            return "Saliendo..."
        case 6:
            return "Eliminando de forma definitiva el archivo..."
        case 7:
            return "Mostrando todos los productos..."

file_name_shop = "Nightblockchain30_shop" 

while True:

    print("1. Agregar producto.")
    print("2. Consultar producto.")
    print("3. Actualizar producto.")
    print("4. Eliminar producto.")
    print("5. Salir.")
    print("6. Eliminar el archivo_shop")
    print("7. Mostrar productos")

    print("")

    try:

        option = int(input("<<< Selecciona la opción que deseas >>>\n" ))

        print(message_option(option)) #Call message_option function
        
        if option == 1:
            name = input("Introduce el nombre: \n")
            name.lower() #case sensitive
            quantity = input("Introduce la cantidad: \n")
            price = input("Introduce el precio: \n")

            with open(file_name_shop,"a") as file:
                file.write(f"{name.capitalize()} | Cantidad: {quantity} | Precio: {price}$\n")

        elif option == 2:
            name = input("¿Cuál es el nombre del producto que deseas consultar?\n").capitalize()

            with open(file_name_shop,"r") as file:
                contenido = file.read()
                
                if name in contenido:
                    with open(file_name_shop,"r") as file:
                        for line in file.readlines():
                            if name == line.split(" | ")[0]:
                                print(f"▶ {line}")
                                break
                else:
                    print("❌ Producto no encontrado")

        elif option == 3:
            name = input("Introduce el nombre: \n")
            quantity = input("Introduce la cantidad: \n")
            price = input("Introduce el precio: \n")

            # Antes de actualizar el producto gaurdo el contenido en un variable
            with open(file_name_shop,"r") as file:
                contenido = file.readlines()

            with open(file_name_shop,"w") as file:
                for line in contenido:
                    if name == line.split(" | ")[0]:
                        file.write(f"{name.capitalize()} | Cantidad: {quantity} | Precio: {price}$\n")
                    else:
                        file.write(line)

            
        elif option == 4:
            name = input("Introduce el nombre: \n")
            
            with open(file_name_shop,"r") as file:
                contenido = file.readlines()

            with open(file_name_shop,"w") as file:
                for line in contenido:
                    if name != line.split(" | ")[0]:
                        file.write(line)


        elif option == 5:
            break
        
        elif option == 6:
            os.remove(file_name_shop)
        
        elif option == 7:
            with open(file_name_shop,"r") as file:
                print("")
                print("<<<  Datos Productos Vendidos  >>>  ")
                print(" -------------------------------- ")
                print(file.read())


    except Exception as e:
        print("")
        print(f"💥 Ha ocurrido un error: {e} TIPO: {type(e).__name__}")

print("HASTA PRONTO!")
