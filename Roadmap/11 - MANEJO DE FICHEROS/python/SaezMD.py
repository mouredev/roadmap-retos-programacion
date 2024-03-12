#11 Manejo de ficheros
"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
"""
import os
abspath = os.path.abspath(__file__) #get the file directory
dname = os.path.dirname(abspath)
os.chdir(dname) #change to file directory

nameOfFile = "SaezMD"
extension = "." + "txt"
myName = "Name: Write your name here: **SMM**"
myAge = "Age: 12"
myFavouriteLanguage = "Language: Java" 

#write
with open(nameOfFile + extension, 'w') as file:
    file.write(myName + '\n' + myAge + '\n' + myFavouriteLanguage)

#read
with open(nameOfFile + extension, 'r') as file:
    myFile = file.read()
    print(myFile)

#delete file
input("press any key to delete the file...")
os.remove(nameOfFile + extension)


#EXTRA
    


