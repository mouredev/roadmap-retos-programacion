# #11 MANEJO DE FICHEROS
#### Dificultad: Media | Publicación: 11/03/24 | Corrección: 18/03/24

## Ejercicio


'''
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 
'''
 
import os
import re
def main():
    # Directorio donde deseas crear el archivo
    target_directory = "C:/Users/Dan/Desktop/Coding/ficheros sin merge en mouredev/11 - MANEJO DE FICHEROS"
    # Si no existe se crea
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Directorio de trabajo actual
    # current_directoy = os.getcwd()
    # print(f"Directorio de trabajo actual: {current_directoy}")

     # Nombre del archivo
    file_name = "danielhdzr.txt"

    # Crear la ruta completa
    file_path = os.path.join(target_directory, file_name)

    # Crear y escribir en el archivo
    with open(file_path, "w") as file:
        file.write("Daniel\n")
        file.write("33\n")
        file.write("Python")

    # Verificar si el archivo existe
    if os.path.exists(file_path):
        print(f"El archivo: '{file_name}' ha sido creado en '{target_directory}'")
    else:
        print(f"No se pudo crear el archivo '{file_name}'")

    # Leer y mostrar el contenido del archivo
    with open(file_path, "r") as file:
        print(file.read())

    # Eliminar el archivo
    os.remove(file_path)
    print(f"Se elimino el archivo {file_name} de {file_path}")


    
    # ----- Extra -----
    '''* DIFICULTAD EXTRA (opcional):
    * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
    * archivo .txt.
    * - Cada producto se guarda en una línea del archivo de la siguiente manera:
    *   [nombre_producto], [cantidad_vendida], [precio].
    * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
    *   actualizar, eliminar productos y salir.
    * - También debe poseer opciones para calcular la venta total y por producto.
    * - La opción salir borra el .txt.'''


    # Directorio donde deseas crear el archivo
    target_directory = "C:/Users/Dan/Desktop/Coding/ficheros sin merge en mouredev/11 - MANEJO DE FICHEROS"
    # Si el directorio no existe se crea
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Directorio de trabajo actual
    # current_directoy = os.getcwd()
    # print(f"Directorio de trabajo actual: {current_directoy}")

     # Nombre del archivo
    file_name = "daniel_tienda.txt"

    # Concatena el archivo a la ruta del directorio
    # C:/Users/Dan/Desktop/Coding/ficheros sin merge en mouredev/11 - MANEJO DE FICHEROS/ daniel_tienda.txt
    file_path = os.path.join(target_directory, file_name)

    while True:
        
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Borrar producto")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Consultar lista de productos y precios")
        print("8. Salir")

        option = int(input("Selecciona la opcion que deseas: "))
        # Agregar producto
        if option == 1:
            print()
            print("Agrega un producto")
            product = input("Nombre del producto: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")

           # Escribimos una nueva linea en el archivo txt sin borrar la existente
                            # "a" = append
            with open(file_path, "a") as file:
                file.write(f"Producto: {product}, Cantidad: {quantity}, Precio: ${price}\n")
        
        # Consultar producto
        elif option == 2:
            print()
            product = input("Nombre del producto: ")
            with open(file_path, "r") as file:
                for line in file.readlines():
                    if product in line:
                        pro, qua, pri = product, quantity, price
            print(f"Nombre: {pro}, Cantidad: {qua}, precio {pri}")

        # Actualizar producto
        elif option == 3:
            print()
            product = input("Nombre del producto: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if product in line:
                    # Si el producto esta en la linea, escribe el nuevo valor
                        file.write(f"Producto: {product}, Cantidad: {quantity}, Precio: ${price}\n")
                    else:
                    # Si no esta, escribe la linea como estaba
                        file.write(line)

        # Borrar producto
        elif option == 4:
            print()
            product = input("Nombre del producto: ")
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                # Si producto NO ESTA en la linea, se reescribe la linea
                # Por lo tanto, SI ESTA en la linea, no se reescribe
                    if product not in line:
                        file.write(line)

        # Calcular venta total
        elif option == 5:
            print()
            total = 0
            with open(file_path, "r") as file:
                for line in file.readlines():
                    # Excluye no numericos
                    numbers_only = re.findall(r'\d+', line)
                    quantity = int(numbers_only[0])
                    price = float(numbers_only[1])
                    total += quantity * price
            print(f"Total vendido: {total}")
            print()

        # Calcular venta por producto
        elif option == 6:
            print()
            product = input("Nombre del producto: ")
            total = 0
            with open(file_path, "r") as file:
                for line in file.readlines():
                    if product in line:
                        # Excluye no numericos
                        numbers_only = re.findall(r'\d+', line)
                quantity = int(numbers_only[0])
                price = float(numbers_only[1])
                total += quantity * price
            
            print(f"Total vendido de {product}: {total}")
            print()

        # Consultar lista de productos y precios
        elif option == 7:
            print()
            with open(file_path, "r") as file:
                print(file.read())
            
        elif option == 8:
            # os.remove(file_path)
            break
        else:
            print("Selecciona una de las opciones disponibles")
            
            


    # # Crear y escribir en el archivo
    # with open(file_path, "w") as file:
    #     file.write(input("nombre del producto: \n"))
    #     file.write(input("cantidad vendida: \n"))
    #     file.write(input("precio: "))

    # # Verificar si el archivo existe
    # if os.path.exists(file_path):
    #     print(f"El archivo: '{file_name}' ha sido creado en '{target_directory}'")
    # else:
    #     print(f"No se pudo crear el archivo '{file_name}'")

    # # Leer y mostrar el contenido del archivo
    # with open(file_path, "r") as file:
    #     print(file.read())

if __name__=="__main__":
    main()
