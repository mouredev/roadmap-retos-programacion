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
#  * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.
#  */

import os

# EJERCICIO:
nombre = 'Hernan\n'
edad = '23\n'
lenguaje_favorito = 'Python\n'

with open('agusrosero.txt', 'r+') as file:
    file.write(f'Nombre: {nombre}')
    file.write(f'Edad: {edad}')
    file.write(f'Lenguaje de programacion favorito: {lenguaje_favorito}')
    print(file.read())
    os.remove('agusrosero.txt')
    file.close()
