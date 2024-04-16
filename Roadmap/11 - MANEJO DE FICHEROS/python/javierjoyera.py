import os

usuario_github = "javierjoyera"
nombre_archivo = ("%s.txt") % (usuario_github)


# Crear y escribir en el archivo
with open(nombre_archivo, 'w') as archivo:
    archivo.write("Nombre: Javier Joyera\n")
    archivo.write("Edad: 27\n")
    archivo.write("Lenguaje de programación favorito: Python\n")

# Leer e imprimir el contenido del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

# Borrar el fichero
os.remove(nombre_archivo)
print("El archivo %s ha sido eliminado." % (nombre_archivo))


##Ejercicio Extra
# Nombre del archivo donde se guardan los datos
archivo_datos = 'ventas.txt'
def mostrar_menu():
    print("\nMenú de gestión de ventas:")
    print("1. Añadir producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")

##Cada producto lo guardaremos como [nombre_producto], [cantidad_vendida], [precio].
def añadir_producto():
    nombre_producto = input("Introduce el nombre del producto: ")
    cantidad_vendida = input("Introduce la cantidad vendida: ")
    precio = input("Introduce el precio del producto: ")
    with open(archivo_datos, 'a') as archivo:
        archivo.write("%s, %s, %s\n" % (nombre_producto, cantidad_vendida, precio))
    print("Producto añadido correctamente.")

def consultar_productos():
    #Solamente debemos sacar el nombre del producto
    with open(archivo_datos, 'r') as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.split(', ')
        print(partes[0])
    
def actualizar_producto():
    nombre_producto = input("Introduce el nombre del producto a actualizar: ")
    nueva_cantidad = input("Introduce la nueva cantidad vendida: ")
    nuevo_precio = input("Introduce el nuevo precio: ")
    with open(archivo_datos, 'r') as archivo:
        lineas = archivo.readlines()
    with open(archivo_datos, 'w') as archivo:
        for linea in lineas:
            if nombre_producto in linea:
                archivo.write("%s, %s, %s\n" % (nombre_producto, nueva_cantidad, nuevo_precio))
                print("Producto actualizado correctamente.")
            else:
                archivo.write(linea)

def eliminar_producto():
    nombre_producto = input("Introduce el nombre del producto a eliminar: ")
    with open(archivo_datos, 'r') as archivo:
        lineas = archivo.readlines()
    with open(archivo_datos, 'w') as archivo:
        for linea in lineas:
            if nombre_producto not in linea:
                archivo.write(linea)
        print("Producto eliminado correctamente.")

def calcular_venta_total():
    with open(archivo_datos, 'r') as archivo:
        lineas = archivo.readlines()
    venta_total = 0
    for linea in lineas:
        partes = linea.split(', ')
        cantidad_vendida = int(partes[1])
        precio = float(partes[2])
        venta_total += cantidad_vendida * precio
    print("La venta total es de %.2f" % venta_total)

def calcular_venta_producto():
    nombre_producto = input("Introduce el nombre del producto a consultar: ")
    with open(archivo_datos, 'r') as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.split(', ')
        if nombre_producto in partes:
            cantidad_vendida = int(partes[1])
            precio = float(partes[2])
            venta_producto = cantidad_vendida * precio
            print("La venta total del producto %s es de %.2f" % (nombre_producto, venta_producto))
            return
    print("Producto no encontrado.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            calcular_venta_total()
        elif opcion == '6':
            calcular_venta_producto()
        elif opcion == '7':
            #Eliminamos el fichero al salir del programa
            if os.path.exists(archivo_datos):
                os.remove(archivo_datos)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == '__main__':
    main()