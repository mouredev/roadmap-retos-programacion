'''EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como
tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.
DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.'''

# Solución: 
import os
filename = 'santiagobailleres.txt'
with open(filename, 'w') as file:
    file.write('Santiago Bailleres\n')
    file.write('25\n')
    file.write('Python\n')

with open(filename, 'r') as file:
    print(file.read())

os.remove(filename)

# EXTRA
filename = 'ventas.txt'
open(filename, 'a') # 'a' para añadir al final del archivo

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")
    
    option = input("Selecciona una opción: ")
    if option == "1": # Añadir producto
        name = input("Nombre del producto: ")
        quantity = input("Cantidad vendida: ")
        price = input("Precio: ")
        with open(filename, 'a') as file:
            file.write(f'{name}, {quantity}, {price}\n')
    elif option == "2": # Consultar producto
        name = input("Nombre del producto: ")
        with open(filename, 'r') as file:
            for line in file.readlines(): # Lee todas las lineas
                if line.split(', ')[0] == name:
                    print(line)
                    break
    elif option == "3": # Actualizar producto
        name = input("Nombre del producto: ")
        quantity = input("Cantidad vendida: ")
        price = input("Precio: ")
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(filename, 'w') as file:
            for line in lines:
                if line.split(', ')[0] == name:
                    file.write(f'{name}, {quantity}, {price}\n')
                else:
                    file.write(line)
    elif option == "4": # Eliminar producto
        name = input("Nombre del producto: ")
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(filename, 'w') as file:
            for line in lines:
                if line.split(', ')[0] != name: # este if es para no escribir la linea que se quiere eliminar
                    file.write(line) # Escribe todas las lineas menos la que se quiere eliminar
    elif option == "5": # Mostrar productos
        with open(filename, 'r') as file:
            print(file.read())
    elif option == "6": # Calcular venta total
        tot = 0
        with open(filename, 'r') as file:
            for line in file.readlines():
                tot += int(line.split(', ')[1]) * float(line.split(', ')[2])
        print(f'Venta total: {tot}')
    elif option == "7": # Calcular venta por producto
        name = input("Nombre del producto: ")
        tot = 0
        with open(filename, 'r') as file:
            for line in file.readlines():
                if line.split(', ')[0] == name:
                    tot += int(line.split(', ')[1]) * float(line.split(', ')[2])
                    break
        print(f'Venta de {name}: {tot}')
    elif option == "8": # Salir
        os.remove(filename)
        break
    else:
        print("Opción no válida")