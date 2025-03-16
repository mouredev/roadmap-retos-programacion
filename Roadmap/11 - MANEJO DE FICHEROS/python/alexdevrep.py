'''
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
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
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
'''

#Creamos un archivo de texto
archivo = open("alexdevrep.txt","x")

#Usamos close() para cambiar los modos de acceso a archivos
archivo.close()

#Abrimos el archivo en modo escritura
archivo= open("alexdevrep.txt","w")

#Añadimos contenido al archivo
archivo.writelines(["Alejandro \n", "24 \n", "Python \n"])
archivo.close()


#Abrimos de nuevo el archivo en modo lectura
archivo= open("alexdevrep.txt","r")

#Imprimimos el archivo en la terminal
print(archivo.read())

#Borramos el archivo creado
import os #Importamos las librerias necesarias
archivo= "alexdevrep.txt"
os.remove(archivo)
print("El archivo ha sido eliminado con éxito")


#Dificultad EXTRA

lista = []

def gestion(accion):
    global lista
    if accion == 'añadir':
        print("Añada el producto a la lista")
        nombre_producto = input("Por favor indique el nombre del producto: ")
        cantidad_vendida = input("Por favor indique las unidades vendidas: ")
        precio_unitario = input("Por favor indique el precio unitario: ")
        producto = {
            "Nombre del producto": nombre_producto,
            "Cantidad Vendida": cantidad_vendida,
            "Precio unitario": precio_unitario
        }
        lista.append(producto)

    elif accion == 'consultar':
        print(lista)

    elif accion == 'actualizar':
        producto_actualizar = input("Por favor indique el nombre del producto a actualizar: ")
        for i, prod in enumerate(lista):
            if prod["Nombre del producto"] == producto_actualizar:
                lista.pop(i)
                print("Ingrese la información actualizada del producto")
                cantidad_vendida = input("Por favor indique las unidades vendidas: ")
                precio_unitario = input("Por favor indique el precio unitario: ")
                prod["Cantidad Vendida"] = cantidad_vendida
                prod["Precio unitario"] = precio_unitario
                lista.append(prod)
                break
        else:
            print("El producto no existe")

    elif accion == 'eliminar':
        producto_eliminar = input("Por favor indique el producto a eliminar: ")
        lista = [prod for prod in lista if prod["Nombre del producto"] != producto_eliminar]

    elif accion == 'guardar':
        try:
            with open("gestion_de_ventas.txt", "w") as fichero:
                for prod in lista:
                    fichero.write(f"{prod['Nombre del producto']}, {prod['Cantidad Vendida']}, {prod['Precio unitario']}\n")
            print("Datos guardados con éxito.")
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            
    elif accion == 'salir':
        try:
            os.remove("gestion_de_ventas.txt")
            print("Archivo eliminado con éxito")
        except FileNotFoundError:
            print("El archivo no existe")

while True:
    print("Archivo de la gestión de ventas")
    print("Funciones disponibles: añadir, consultar, actualizar, eliminar, guardar, salir")
    accion = input("Escriba una de las funciones disponibles: ")
    gestion(accion)

    if accion == 'salir':
        break
    





