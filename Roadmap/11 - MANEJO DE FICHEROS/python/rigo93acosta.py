'''
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
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
'''

## Libraries
import os

'''
Ejercicio
'''

filename = 'rigo93acosta.txt'

with open(filename, 'w') as open_file:
    open_file.write('Rigo Acosta\n')
    open_file.write('30\n')
    open_file.write('Python\n') 

with open(filename, 'r') as open_file:
    print(open_file.read())

os.remove(filename)

'''
Extra
'''

filename = 'ventas.txt'
open(filename, 'a').close()

while True:
    print('1. Añadir producto')
    print('2. Consultar producto')
    print('3. Mostrar productos')
    print('4. Actualizar producto')
    print('5. Eliminar producto')
    print('6. Venta total')
    print('7. Venta por producto')
    print('8. Salir')

    option = int(input('Opción: '))
    
    if option == 1:
        producto = input('Nombre del producto: ')
        cantidad = input('Cantidad vendida: ')
        precio = input('Precio: ')
        with open(filename, 'a') as open_file:
            open_file.write(f'{producto}, {cantidad}, {precio}\n')

    elif option == 2:
        producto = input('Nombre del producto: ')

        with open(filename, 'r') as open_file:
            for line in open_file.readlines():
                if line.split(', ')[0] == producto:
                    temp = line.split(', ')
                    print(f'Producto: {temp[0]} - Cantidad: {temp[1]} - Precio: {temp[2]}')     
    
    elif option == 3:
        with open(filename, 'r') as open_file:
            for line in open_file.readlines():
                temp = line.split(', ')
                print(f'Producto: {temp[0]} - Cantidad: {temp[1]} - Precio: {temp[2]}')
    
    elif option == 4:
        producto = input('Nombre del producto: ')
        cantidad = input('Cantidad vendida: ')
        precio = input('Precio: ')
       
        with open(filename, 'r') as open_file:
            lines = open_file.readlines()
        
        with open(filename, 'w') as open_file:
            for line in lines:
                if line.split(', ')[0] == producto:
                    open_file.write(f'{producto}, {cantidad}, {precio}\n')
                else:
                    open_file.write(line)

    elif option == 5:
        
        producto = input('Nombre del producto: ')
        
        with open(filename, 'r') as open_file:
            lines = open_file.readlines()
        
        with open(filename, 'w') as open_file:
            for line in lines:
                if line.split(', ')[0] != producto:
                    open_file.write(line)

    elif option == 6:
        
        with open(filename, 'r') as open_file:
            lines = open_file.readlines()
        total = 0
        
        for line in lines:
            total += int(line.split(', ')[1]) * float(line.split(', ')[2])
        print(f'Venta total: {total}')

    elif option == 7:
        
        producto = input('Nombre del producto: ')
        
        with open(filename, 'r') as open_file:
            lines = open_file.readlines()
        for line in lines:
            if line.split(', ')[0] == producto:
                print(f'Venta de {line.split(", ")[0]}: {int(line.split(", ")[1]) * float(line.split(", ")[2])}')

    elif option == 8:
        os.remove(filename)
        break
    
    else:
        print('Opción no válida, intenta de nuevo.')