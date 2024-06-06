import os

archivo_usuario = "pyramsd.txt"

if os.path.exists(path=archivo_usuario):
    os.remove(path=archivo_usuario)

with open(archivo_usuario, 'w') as archivo:
    archivo.write("Nombre: Sergio Ruiz\n")
    archivo.write("Edad: 18\n")
    archivo.write("Lenguaje de programación favorito: Python\n")

with open(archivo_usuario, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

os.remove(archivo_usuario)
print("El archivo %s ha sido eliminado." % (archivo_usuario))


'''
EXTRA
'''
archivoDeVentas = 'registroDeVentas.txt'
def mostrar_menu():
    print("\nMenú de gestión de ventas:")
    print("1. Añadir producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")


def añadir_producto():
    nombre_producto = input("Introduce el nombre del producto: ")
    cantidad_vendida = input("Introduce la cantidad vendida: ")
    precio = input("Introduce el precio del producto: ")
    with open(archivoDeVentas, 'a') as archivo:
        archivo.write("%s, %s, %s\n" % (nombre_producto, cantidad_vendida, precio))
    print("Producto añadido correctamente.")


def consultar_productos():
    with open(archivoDeVentas, 'r') as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.split(', ')
        print(partes[0])
    

def actualizar_producto():
    nombre_producto = input("Introduce el nombre del producto a actualizar: ")
    nueva_cantidad = input("Introduce la nueva cantidad vendida: ")
    nuevo_precio = input("Introduce el nuevo precio: ")
    with open(archivoDeVentas, 'r') as archivo:
        lineas = archivo.readlines()
    with open(archivoDeVentas, 'w') as archivo:
        for linea in lineas:
            if nombre_producto in linea:
                archivo.write("%s, %s, %s\n" % (nombre_producto, nueva_cantidad, nuevo_precio))
                print("Producto actualizado correctamente.")
            else:
                archivo.write(linea)


def eliminar_producto():
    nombre_producto = input("Introduce el nombre del producto a eliminar: ")
    with open(archivoDeVentas, 'r') as archivo:
        lineas = archivo.readlines()
    with open(archivoDeVentas, 'w') as archivo:
        for linea in lineas:
            if nombre_producto not in linea:
                archivo.write(linea)
        print("Producto eliminado correctamente.")


def calcular_venta_total():
    with open(archivoDeVentas, 'r') as archivo:
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
    with open(archivoDeVentas, 'r') as archivo:
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
            if os.path.exists(archivoDeVentas):
                os.remove(archivoDeVentas)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == '__main__':
    main()
