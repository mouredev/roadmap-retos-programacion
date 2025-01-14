#/*
# * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
# * 
# * EJERCICIO:
# * Desarrolla un programa capaz de crear un archivo que se llame como
# * tu usuario de GitHub y tenga la extensión .txt.
# * Añade varias líneas en ese fichero:
# * - Tu nombre.
# * - Edad.
# * - Lenguaje de programación favorito.
# * Imprime el contenido.
# * Borra el fichero.

import os

nombre_archivo = "evilpotato04.txt"

archivo = open(nombre_archivo, "w") # "w" = write/overwrite
texto = ["Nombre: Samy\n", "Edad: 19 años\n", "Lenguajes de programación favoritos: Python y C#\n"]
archivo.writelines(texto)
archivo.write("Pasatiempo: jugar videojuegos")
archivo.close()

archivo = open(nombre_archivo, "r") # "r" = read
print(archivo.read())
archivo.close()

if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
else:
    print(f"no hay ningún archivo llamado {nombre_archivo}")

# *
# * DIFICULTAD EXTRA (opcional):
# * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
# * archivo .txt.
# * - Cada producto se guarda en una línea del archivo de la siguiente manera:
# *   [nombre_producto], [cantidad_vendida], [precio].
# * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
# *   actualizar, eliminar productos y salir.
# * - También debe poseer opciones para calcular la venta total y por producto.
# * - La opción salir borra el .txt.
# */

class gestion_de_ventas:
    def iniciar_sistema(self):
        print("\n===== Empezando el sistema =====\n")
        registro = 1
        total_cantidad = 0
        total_precio = 0
        arc = open("reporte_de_ventas.txt", "w")
        arc.write("Nombre, Cantidad, Precio\n")
        arc.write(f"-----------------------------------------\n")
        
        while registro == 1:
            novo_producto = input("¿Quieres agregar un nuevo producto? (si/no) ").upper()

            if novo_producto == "SI":
                nombre = input("Nombre del nuevo producto: ")
                cantidad = input("Cantidad del nuevo producto: ")
                precio = input("Precio del nuevo producto: ")

                total_cantidad += int(cantidad)
                total_precio += float(precio) * int(cantidad)

                arc.write(f"{nombre}, {cantidad}, {precio}\n")
            else:
                registro = 0
        
        arc.close()
        arc = open("reporte_de_ventas.txt", "a")
        arc.write(f"-----------------------------------------\n")
        arc.write(f"Total, {total_cantidad}, {total_precio}\n")
        arc.close()

        print("\n===== Cerrando el sistema =====\n")
        

sistema = gestion_de_ventas()

sistema.iniciar_sistema()
