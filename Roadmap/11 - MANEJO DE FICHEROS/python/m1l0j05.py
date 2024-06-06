## Ejercicio

import os

def ejercicio():
    texts = ['Mi nombre\n', 'Mi edad\n', 'Python\n']
    
    with open('m1l0j05.txt', 'w') as file:
        file.write('Mi nombre\n')
        file.write('Mi edad\n')
        file.write('Python\n')
        file.write('+++++\n')
        file.writelines(texts)

    with open('m1l0j05.txt', 'r') as file:
        print(file.read())

    os.remove('m1l0j05.txt')

#ejercicio()

# Extra

def guardar_producto(nombre_archivo, producto):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(producto + '\n')

def mostrar_productos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        print('Productos:')
        print(archivo.read())

def actualizar_producto(nombre_archivo, indice, nuevo_producto):
    with open(nombre_archivo, 'r+') as archivo:
        lineas = archivo.readlines()
        if indice >= len(lineas):
            print('Índice fuera de rango.')
            return
        lineas[indice] = nuevo_producto + '\n'
        archivo.seek(0)
        archivo.writelines(lineas)
        archivo.truncate()

def eliminar_producto(nombre_archivo, indice):
    with open(nombre_archivo, 'r+') as archivo:
        lineas = archivo.readlines()
        if indice >= len(lineas):
            print('Índice fuera de rango.')
            return
        lineas.pop(indice)
        archivo.seek(0)
        archivo.writelines(lineas)
        archivo.truncate()

def calcular_venta_total(nombre_archivo):
    venta_total = 0
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            _, cantidad, precio = linea.strip().split(',')
            venta_total += int(cantidad) * float(precio)
    return venta_total

def calcular_venta_producto(nombre_archivo, producto_buscado):
    venta_producto = 0
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(',')
            if nombre == producto_buscado:
                venta_producto += int(cantidad) * float(precio)
    return venta_producto

def ejercicio_extra():
    nombre_archivo = 'ventas.txt'

    while True:
        print('\n1. Añadir producto')
        print('2. Consultar productos')
        print('3. Actualizar producto')
        print('4. Eliminar producto')
        print('5. Calcular venta total')
        print('6. Calcular venta por producto')
        print('7. Salir')
        opcion = input('Ingrese el número de la opción deseada: ')

        if opcion == '1':
            producto = input('Ingrese el producto en el formato [nombre_producto], [cantidad_vendida], [precio]: ')
            guardar_producto(nombre_archivo, producto)
        elif opcion == '2':
            mostrar_productos(nombre_archivo)
        elif opcion == '3':
            indice = int(input('Ingrese el índice del producto a actualizar: '))
            nuevo_producto = input('Ingrese el nuevo producto en el formato [nombre_producto], [cantidad_vendida], [precio]: ')
            actualizar_producto(nombre_archivo, indice, nuevo_producto)
        elif opcion == '4':
            indice = int(input('Ingrese el índice del producto a eliminar: '))
            eliminar_producto(nombre_archivo, indice)
        elif opcion == '5':
            venta_total = calcular_venta_total(nombre_archivo)
            print(f'Venta total: {venta_total}')
        elif opcion == '6':
            producto_buscado = input('Ingrese el nombre del producto: ')
            venta_producto = calcular_venta_producto(nombre_archivo, producto_buscado)
            print(f'Venta del producto {producto_buscado}: {venta_producto}')
        elif opcion == '7':
            import os
            os.remove(nombre_archivo)
            print('Archivo borrado. Saliendo...')
            break
        else:
            print('Opción no válida. Por favor, ingrese un número válido.')


ejercicio_extra()
