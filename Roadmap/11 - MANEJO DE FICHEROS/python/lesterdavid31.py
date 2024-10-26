import os

# def write_file():
#     name = 'Lester David'
#     age = "25 de edad"
#     lenguage = 'python'

#     return f''' Nombre del estudiante: {name} 
#                 Edad: {age}
#                 lenguaje favorito : {lenguage}'''

# def file(name_file):
#     file = open(name_file, "r+")
#     #file.write(write_file())
#     print(file.read())
#     file.close()

# #file('estudiante.txt')

def delete_file(name_file):
    if os.path.exists(name_file):
        os.remove(name_file) 
    else:
        print('El archivo no existe')

# delete_file('estudiante.txt')



def writeFile(nameFile,product):
    with open(nameFile,'a') as file:
        file.write(product)

def addProduct():
    name = input('Nombre del producto: ')
    quantity = int(input('Cantidad vendida: '))
    price = int(input('Precio del producto: '))

    newProduct = f'Nombre Producto: {name}, Cantidad vendida: {quantity}, Precio Producto: {price} \n'
    writeFile('venta.txt',newProduct)

# addProduct()

def readFile(nameFile):
    with open(nameFile,'r')as file:
        print(file.read())

#readFile('venta.txt')

def update(nameFile,nombre_producto,nuevo_nombre, nueva_cantidad, nuevo_precio):
    with open(nameFile,'r')as file:
        lineas = file.readlines()
        for i, linea in enumerate(lineas):
            if nombre_producto in linea:
                partes = linea.split(", ")
                partes[0] = f'Nombre: {nuevo_nombre}' 
                partes[1] = f'Cantidad : {nueva_cantidad}'
                partes[2] = f'Precio: {nuevo_precio}'
                lineas[i] = ", ".join(partes)
                break
    with open(nameFile, 'w') as file:
        file.writelines(lineas)
    print(f'producto {nuevo_nombre} actualizado con éxito')

#update('venta.txt')

def calcularVenta(namefile,productName):
    
    with open(namefile, 'r') as file:
        lineas = file.readlines()
        
        for linea in lineas:
            if productName in linea:
                partes = linea.split(", ")
                
                # Validamos que las partes tengan el formato correcto
                if len(partes) == 3:
                    # Extraer la cantidad
                    cantidad_str = partes[1].split(": ")
                    if len(cantidad_str) == 2:
                        cantidad = int(cantidad_str[1])  # Convertir a entero
                    else:
                        print("Formato de cantidad incorrecto en la línea:", linea)
                        continue
                    
                    # Extraer el precio
                    precio_str = partes[2].split(": ")
                    if len(precio_str) == 2:
                        precio = float(precio_str[1])  # Convertir a flotante
                    else:
                        print("Formato de precio incorrecto en la línea:", linea)
                        continue
                    # Calcular el total
                    resultado = cantidad * precio
                    return resultado
    print(f'Producto {productName} no encontrado.')

def NameProduct(fileName):
    list_name_products = []
    with open(fileName, 'r') as file:
        lineas = file.readlines()
        
        for linea in lineas:
            partes = linea.split(", ")
            if len(partes) == 3:
                productName = partes[0].split(": ")
                if len(productName) == 2:
                    nombres = productName[1]
                    list_name_products.append(nombres)
    return list_name_products


while True:
    print('\n')
    print('1. Añadir producto')
    print('2. Consultar producto')
    print('3. Actualizar producto')
    print('4. calcular venta total por poroducto')
    print('5. calcular venta total')
    print('6. Salir')
    print('\n')

    try:
        option = int(input('Ingrese la opción: '))
        print('\n')

        if option == 1:
            addProduct()
            print('¿Producto agregado exitosamente!')
        elif option == 2:
            readFile('venta.txt')
        elif option == 3:
            
            name = input('Nombre del producto a actualizar: ')
            newName = input('Nombre: ')
            newQuantity = input('Cantidad: ')
            newPrice = input('Precio: ')
            update('venta.txt',name,newName,newQuantity,newPrice)

        elif option == 4:
            productName = input('Ingrese el nombre del producto a calcular: ')
            result = calcularVenta('venta.txt',productName)
            print(f'El total de ventas del producto {productName} es: {result}')

        elif option == 5:
            nombres = NameProduct("venta.txt")
            resultado = 0
            for nombre in nombres:
                venta_producto = calcularVenta("venta.txt",nombre)
                resultado += venta_producto 
            print(f'El monto total de los productos vendidos es de: {resultado}')

        elif option == 6:
            delete_file('venta.txt')
        else:
            print('Solo puedes seleccionar las opciones del 1 al 7 por foavor ingrese nuevamente: ')
    except ValueError as e:
        print('Ingrese solamente los numeros del 1 - 6')
