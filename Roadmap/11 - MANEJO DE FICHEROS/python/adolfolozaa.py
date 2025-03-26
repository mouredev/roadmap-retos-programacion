''' 
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
 * - La opción salir borra el .txt.'''

import os

def create_file():
    with open('adolfolozaa.txt', 'w') as file:
        file.write('Adolfo Loza Almeida\n')
        file.write('Edad: 56\n')
        file.write('Lenguaje de programación favorito: Python\n')

    with open('adolfolozaa.txt', 'r') as file:
        print(file.read())

    os.remove('adolfolozaa.txt')

create_file()


'''
DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 - La opción salir borra el .txt.
 '''

import os
from os import path

def elim_reg(item):
    with open("ventas.txt", "r") as input_file:
        with open("temp.txt", "w") as output_file:
            for line in input_file:
                if item not in line.strip("\n"):
                    output_file.write(line)
    os.replace("temp.txt", "ventas.txt")    

def ventas():
    while True:
        print('---------------------')
        print('Gestión de ventas')
        print('1. Añadir producto')
        print('2. Consultar producto')
        print('3. Actualizar producto')
        print('4. Eliminar producto')
        print('5. Venta total')
        print('6. Salir')
        print('---------------------')
        action = input('Ingrese la acción deseada: ')

        if action == '6':           #salir
            print('Saliendo del programa')
            os.remove(file_name)
            break
        elif action == '1':     #anadir
            nombre_producto = input('ingrese el nombre del producto: ')
            cantidad_vendida = input('ingrese la cantidad vendida: ')
            precio = input('Ingrese precio: ')
            with open(file_name, "a") as file:
                file.write(nombre_producto + ', ')
                file.write(cantidad_vendida + ', ')
                file.write(precio +'\n')

        elif action == '2':     #consulta
            if path.exists(file_name):

                with open(file_name, "r") as file:
                    for linea in file:
                        print(linea)  
                        
            else:
                print('no existen registros aun!!!')
                

        elif action == '3':         #actualizar
            with open('ventas.txt', 'r') as file:
                print(file.read())
            item = input('Ingrese el producto que desea actualizar: ')
            
            elim_reg(item)
             
            with open(file_name, "a") as file:
                cantidad_vendida = input('ingrese la nueva cantidad vendida: ')
                precio = input('Ingrese el nuevo precio: ')
                
                file.write(item + ', ')
                file.write(cantidad_vendida + ', ')
                file.write(precio +'\n')
            with open('ventas.txt', 'r') as file:
                print(file.read())



        elif action == '4':         #eliminar
            with open('ventas.txt', 'r') as file:
                print(file.read())
            item = input('Ingrese el producto que desea Borar: ')
            elim_reg(item)

        elif action == '5':         #total
            if path.exists(file_name):
                with open(file_name, "r") as file:
                    total = 0
                    for linea in file:
                        linea = linea.split(',')
                        item = linea[0]
                        total1 = int(linea[1]) * int(linea[2]) 
                        print(f'EL total del producto {item} es: {total1}')
                        total = total + total1
                    print(f'la venta total es: {total}')
            else:
                print('no existen registros aun!!!')
                

global file_name
file_name = 'ventas.txt'
ventas()


