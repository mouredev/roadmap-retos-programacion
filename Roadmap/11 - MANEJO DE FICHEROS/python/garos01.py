import os

# Obtener el nombre de usuario de GitHub
username = "GAROS01"

# Crear el archivo con extensión .txt
filename = f"{username}.txt"

# Escribir en el archivo
with open(filename, "w") as file:
    file.write("Nombre: Oscar Garzon\n")
    file.write("Edad: 29\n")
    file.write("Lenguaje de programación favorito: Python y JavaScript\n")

# Leer el contenido del archivo y imprimirlo
with open(filename, "r") as file:
    content = file.read()
    print("Contenido del archivo:")
    print(content)

# Borrar el archivo
os.remove(filename)
print(f"El archivo {filename} ha sido borrado.")


# Ejercicio extra


def leer_archivo():
    try:
        with open("ventas.txt", "r") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print("No hay ventas registradas.")
        return []


def guardar_venta(nombre_producto, cantidad, precio):
    with open("ventas.txt", "a") as archivo:
        archivo.write(f"{nombre_producto}, {cantidad}, {precio}\n")


def mostrar_ventas():
    ventas = leer_archivo()
    if ventas:
        print("Ventas realizadas:")
        for venta in ventas:
            print(venta.strip())
    else:
        print("No hay ventas registradas.")


def actualizar_venta(nombre_producto, nueva_cantidad, nuevo_precio):
    ventas = leer_archivo()
    with open("ventas.txt", "w") as archivo:
        for venta in ventas:
            producto, cantidad, precio = venta.strip().split(", ")
            if producto == nombre_producto:
                cantidad = nueva_cantidad
                precio = nuevo_precio
            archivo.write(f"{producto}, {cantidad}, {precio}\n")


def eliminar_venta(nombre_producto):
    ventas = leer_archivo()
    with open("ventas.txt", "w") as archivo:
        for venta in ventas:
            producto, _, _ = venta.strip().split(", ")
            if producto != nombre_producto:
                archivo.write(venta)


def calcular_venta_total():
    ventas = leer_archivo()
    total = 0
    for venta in ventas:
        _, cantidad, precio = venta.strip().split(", ")
        total += int(cantidad) * float(precio)
    return total


def calcular_venta_producto(nombre_producto):
    ventas = leer_archivo()
    for venta in ventas:
        producto, cantidad, precio = venta.strip().split(", ")
        if producto == nombre_producto:
            return int(cantidad) * float(precio)
    return 0


def main():
    while True:
        print("\nMenú:")
        print("1. Añadir venta")
        print("2. Consultar ventas")
        print("3. Actualizar venta")
        print("4. Eliminar venta")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir y borrar archivo")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad vendida: ")
            precio = input("Ingrese el precio unitario: ")
            guardar_venta(nombre_producto, cantidad, precio)
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad vendida: ")
            nuevo_precio = input("Ingrese el nuevo precio unitario: ")
            actualizar_venta(nombre_producto, nueva_cantidad, nuevo_precio)
        elif opcion == "4":
            nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_venta(nombre_producto)
        elif opcion == "5":
            total = calcular_venta_total()
            print(f"Venta total: {total}")
        elif opcion == "6":
            nombre_producto = input(
                "Ingrese el nombre del producto para calcular su venta: "
            )
            venta_producto = calcular_venta_producto(nombre_producto)
            print(f"Venta de {nombre_producto}: {venta_producto}")
        elif opcion == "7":

            os.remove("ventas.txt")
            print("Archivo borrado. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
