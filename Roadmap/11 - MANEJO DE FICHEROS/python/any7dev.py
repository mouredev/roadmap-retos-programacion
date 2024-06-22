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
#  */

#EJERCICIO
import os

def crea_archivo(nombre, contenido):
    if not os.path.exists(nombre): #Para saber si ya existe el archivo
        with open (nombre, 'w') as archivo: #Crea el archivo abriéndolo y cerrándolo
            archivo.write(contenido)
    else:
        print("El archivo ya existe")
    if os.path.exists(nombre):
        with open (nombre, 'r') as archivo: #Abre el archivo abriéndolo y cerrándolo
            print(archivo.read())
    else:
        print("El archivo no existe")
    os.remove(nombre) #Elimina el archivo.

crea_archivo("any7dev.txt", "Ana\n36\nPython")

#DIFICULTAD EXTRA
def gestor_ventas():
    archivo = "gestion_ventas.txt"
    open(archivo, 'w').close()
    while True:
        opcion = input("\nDime tu opción: \n\t1-Añadir producto vendido \n\t2-Consultar archivo \n\t3-Actualizar \n\t4-Eliminar \n\t5-Totales \n\ts-Salir \nOpción--> ")
        match opcion:
            case "1":
                añadir(archivo)
            case "2":
                if os.stat(archivo).st_size == 0:
                    print("El archivo está vacío")
                else:
                    consultar(archivo)
            case "3":
                if os.stat(archivo).st_size == 0:
                    print("El archivo está vacío")
                else:
                    actualizar(archivo)
            case "4":
                if os.stat(archivo).st_size == 0:
                    print("El archivo está vacío")
                else:
                    eliminar(archivo)
            case "5":
                if os.stat(archivo).st_size == 0:
                    print("El archivo está vacío")
                else:
                    totales(archivo)
            case "s":
                print("Saliendo...")
                os.remove(archivo)
                break
            case _:
                print("Opción incorrecta")

def añadir(archivo):
    producto = ""
    nombre = input("Dime el nombre: ")    
    try:
        cantidad = int(input("Cantidad vendida: "))
        precio = float(input("Precio: "))
        producto = f"{nombre}, {cantidad}, {precio}\n"
        with open (archivo, 'a') as a:
            a.write(producto)
        print("Producto añadido")
    except ValueError:
        print("La cantidad debe ser un número entero y el precio entero o decimal")  


def consultar(archivo):
    with open (archivo, 'r') as a:
        print(a.read())

def actualizar(archivo):
    buscar = input("Dime el valor del campo a actualizar: ")
    cambiar = input("Dime lo que quieres poner: ")

    contenido = open(archivo, 'r').read()
    contenido = contenido.replace(buscar, cambiar)

    with open (archivo, 'w') as a:
        a.write(contenido)
    print("Cambio realizado")

def eliminar(archivo):
    producto = input("Dime el nombre del producto a eliminar: ")
    encontrado = False
    contador = 0

    with open (archivo, 'r') as a:
        for linea in a:
            if producto in linea:
                encontrado = True
                break                
            else:
                contador += 1
    
    if encontrado:
        a = open (archivo, 'r')
        lineas = a.readlines()
        a.close()
        with open (archivo, 'w') as a:
            linea = lineas[contador]
            lineas.remove(linea)
            for linea in lineas:
                a.write(linea)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")
        
def totales(archivo):
    lista = []
    suma = 0
    total = 0

    with open (archivo, 'r') as a:
        lista = [linea.split(", ") for linea in a]
        for linea in lista:
            suma += float(linea[1]) * float(linea[2]) 
            print(f"Cantidad ganada con ventas de {linea[0]}: {suma}")
            total += suma
    print(f"Cantidad total ganada por las ventas: {total}")       


gestor_ventas()