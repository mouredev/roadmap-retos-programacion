#Manejo de Ficheros
"""
El manejo de ficheros en Python se realiza utilizando las funciones integradas open(), read(), write() y close().
Estas funciones permiten abrir, leer, escribir y cerrar archivos de manera sencilla.
El proceso básico para manejar ficheros en Python es el siguiente:
1. Abrir el archivo utilizando la función open(). Esta función toma dos argumentos: el nombre del archivo y el modo en que se va a abrir
(por ejemplo, 'r' para leer, 'w' para escribir, 'a' para añadir, etc.).
2. Realizar operaciones de lectura o escritura en el archivo utilizando los métodos read(), readline(), readlines() para leer y write(), writelines() para escribir.
3. Cerrar el archivo utilizando el método close() para liberar los recursos asociados al archivo.
Es importante cerrar el archivo después de haber terminado de trabajar con él para evitar problemas de memoria y asegurar que los datos se guarden correctamente.
"""
# Abrir un archivo en modo escritura (crea el archivo si no existe)
import os
file_name = "Paprikaiskrieg.txt"
#with open(file_name, "w") as file :  # Crea un archivo vacío (write mode "w" crea el archivo si no existe)
    #file.write("Ivan RN\n")  # Escribe una línea en el archivo (\n para nueva línea)
    #file.write("26\n")  # Escribe otra línea en el archivo
    #file.write("python\n")  # Escribe otra línea en el archivo

#with open(file_name, "r") as file :  # Abre el archivo en modo lectura
      # Lee todo el contenido del archivo
    #print(file.read())  # Imprime el contenido del archivo

  # Elimina el archivo creado


#XTRAJ

while True:
    try:
        print("1.- añadir producto")
        print("2.- consultar producto")
        print("3.- actualizar producto")
        print("4.- eliminar producto")
        print("5.- calcular venta total")
        print("6.- calcular venta por producto")
        print("7.- Mostrar inventario")
        print("8.- salir")

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            with open(file_name, "a") as file:
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                file.write(f"{nombre},{precio},{cantidad}\n")
                print("Producto añadido exitosamente.")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto a consultar: ")
            encontrado = False
            with open(file_name, "r") as file:
                for line in file:
                    datos = line.strip().split(",")
                    if datos[0] == nombre:
                        print(f"Producto: {datos[0]}, Precio: {datos[1]}, Cantidad: {datos[2]}")
                        encontrado = True
                        break
            if not encontrado:
                print("Producto no encontrado.")
        elif opcion == 3:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            actualizado = False
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    datos = line.strip().split(",")
                    if datos[0] == nombre:
                        file.write(f"{nombre},{precio},{cantidad}\n")
                        actualizado = True
                    else:
                        file.write(line)
            if actualizado:
                print("Producto actualizado exitosamente.")
            else:
                print("Producto no encontrado para actualizar.")
        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminado = False
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    datos = line.strip().split(",")
                    if datos[0] != nombre:
                        file.write(line)
                    else:
                        eliminado = True
            if eliminado:
                print("Producto eliminado exitosamente.")
            else:
                print("Producto no encontrado para eliminar.")
        elif opcion == 5:
            total_venta = 0
            with open(file_name, "r") as file:
                for line in file:
                    datos = line.strip().split(",")
                    if len(datos) == 3:
                        try:
                            total_venta += float(datos[1]) * int(datos[2])
                        except ValueError:
                            continue
            print(f"Venta total: {total_venta}")
        elif opcion == 6:
            nombre = input("Ingrese el nombre del producto a consultar: ")
            encontrado = False
            with open(file_name, "r") as file:
                for line in file:
                    datos = line.strip().split(",")
                    if datos[0] == nombre:
                        try:
                            venta = float(datos[1]) * int(datos[2])
                            print(f"Venta de {nombre}: {venta}")
                        except ValueError:
                            print("Datos inválidos para el producto.")
                        encontrado = True
                        break
            if not encontrado:
                print("Producto no encontrado.")
        elif opcion == 7:
            with open(file_name, "r") as file:
                contenido = file.read()
                if contenido.strip() == "":
                    print("Inventario vacío.")
                else:
                    print("Inventario:\n" + contenido)
        elif opcion == 8:
            if os.path.exists(file_name):
                os.remove(file_name)
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número.")
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    