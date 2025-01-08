"""	
10 - MANEJO DE FICHEROS

Autor de la solución: Oriaj3	

Teoría:	
El manejo de ficheros es una de las tareas más comunes en la programación.

Python proporciona una serie de funciones y métodos para trabajar con ficheros.

Para abrir un fichero, se utiliza la función open(), que recibe dos parámetros: el nombre del fichero y el modo de apertura.

El modo de apertura puede ser de lectura (r), escritura (w), o añadir (a). También se puede abrir el fichero en modo binario (b) o en modo texto (t).

Ejemplo:
f = open("archivo.txt", "r")

Una vez abierto el fichero, se pueden leer o escribir datos en él utilizando los métodos read(), write(), readline(), readlines(), etc.

Es importante cerrar el fichero una vez que se ha terminado de trabajar con él, para liberar los recursos que utiliza.
""" 
"""
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
"""
# Crear un archivo con mi usuario de GitHub
f = open("oriaj3.txt", "w")
f.write("Oriaj3\n")
f.write("30\n")
f.write("Python\n")
f.close()

# Leer el contenido del archivo
f = open("oriaj3.txt", "r")
print(f.read())
f.close()

# Borrar el archivo
import os
os.remove("oriaj3.txt")

"""
/*
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
"""

# Clase producto
class Producto:
    def __init__ (self, nombre, cantidad, precio) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self) -> str:
        return f"{self.nombre}, {self.cantidad}, {self.precio}"
    
# Clase gestor de ventas
class GestorVentas:
    def __init__(self) -> None:
        self.archivo = "ventas.txt"

    def anadir_producto(self, producto: Producto) -> None:
        with open(self.archivo, "a") as f:
            str_producto = producto.__str__()
            f.write(f"{str_producto}\n")

    def consultar_producto(self, nombre: str) -> Producto:
        with open(self.archivo, "r") as f:
            for linea in f:
                nombre_producto, cantidad, precio = linea.split(", ")
                if nombre_producto == nombre:
                    return Producto(nombre_producto, cantidad, precio).__str__()
            return None
    def actualizar_producto(self, producto: Producto) -> None:
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
        with open(self.archivo, "w") as f:
            for linea in lineas:
                nombre_producto, cantidad, precio = linea.split(", ")
                if nombre_producto == producto.nombre:
                    str_producto = producto.__str__()
                    f.write(f"{str_producto}\n")
                else:
                    f.write(linea)
    def eliminar_producto(self, nombre: str) -> None:
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
        with open(self.archivo, "w") as f:
            for linea in lineas:
                nombre_producto, cantidad, precio = linea.split(", ")
                if nombre_producto != nombre:
                    f.write(linea) 

    def n_ventas_producto(self, nombre: str) -> int:
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
            for linea in lineas:
                nombre_producto, cantidad, precio = linea.split(", ")
                cantidad = int(cantidad)
                precio = float(precio)
                if nombre_producto == nombre:
                    return cantidad * precio

    def n_ventas_total(self) -> int:
        with open(self.archivo, "r") as f:
            total = 0
            for linea in f:
                nombre_producto, cantidad, precio = linea.split(", ")
                cantidad = int(cantidad)
                precio = float(precio)
                total += cantidad * precio
            return total
        
    def salir(self) -> None:
        os.remove(self.archivo)
    

# Prueba de la clase
gestor = GestorVentas()
producto1 = Producto("Producto1", 10, 100)
producto2 = Producto("Producto2", 20, 200)
producto3 = Producto("Producto3", 30, 300)
producto4 = Producto("Producto4", 40, 400)

gestor.anadir_producto(producto1)
gestor.anadir_producto(producto2)
gestor.anadir_producto(producto3)
gestor.anadir_producto(producto4)

print(gestor.consultar_producto("Producto1"))
print(gestor.consultar_producto("Producto2"))
print(gestor.consultar_producto("Producto3"))
print(gestor.consultar_producto("Producto4"))

producto1 = Producto("Producto1", 20, 100)
gestor.actualizar_producto(producto1)
print(gestor.consultar_producto("Producto1"))

gestor.eliminar_producto("Producto2")
print(gestor.consultar_producto("Producto2"))

print(gestor.n_ventas_producto("Producto1"))
print(gestor.n_ventas_total())

gestor.salir()
