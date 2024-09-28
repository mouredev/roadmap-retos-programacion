# --- 11-Manejo de Ficheros ---
# --- Javier Molina ---

# Crear Fichero
with open('Jav-mol.txt', 'w') as file:
    name = input('Ingrese su nombre: ')
    age = input('Ingrese su edad: ')
    language = input('Ingrese su lenguaje favorito: ')
    
    file.write(f'Name: {name} \nAge: {age} \nFavorite Language: {language}')
    print(f'Name: {name} \nAge: {age} \nFavorite Language: {language}')

# Borrar Fichero
import os
file = 'Jav-mol.txt'

if os.path.exists(file):
    os.remove(file)

        
# --- Extra ---

import os
index = None
caracteres = lambda:print('-'*25)

def delete_file():
    file = 'Jav-mol.txt'
    if os.path.exists(file):
        #os.remove(file)
        pass
    return True

def add_product():
    
    with open('Jav-mol.txt', 'a+') as file:
        
        caracteres()
        product = input('Ingrese el producto: ')
        stock = input('Ingrese la cantidad: ')
        precio = input('Ingrese el precio: ')
        caracteres()
        
        file.write(f'[{product}], [{stock}], [${precio}]' + '\n')


def listening_product():
    with open('Jav-mol.txt', 'r') as file:
        texto = file.read()
        caracteres()
        print(texto)
        caracteres()
        
list_to_str = lambda lista:f'{lista[0]}, {lista[1]}, {lista[2]}'
def update_product(products, index, lista):
        total = input('Ingrese la cantidad vendida: ')
        products[1] = f'[{total}]'
        price = input('Ingrese el precio: ')
        products[2] = f'[${price}]'
        
        lista_str_products = list_to_str(products)
        lista[index] = lista_str_products
        
        print(lista_str_products)
        caracteres() 
        return lista 
        
def edit_product():    
    with open('Jav-mol.txt', 'r') as file:
        texto = file.read()
        text_list = texto.split('\n')
        lista_final = None
        
        caracteres()
        product = input('Ingrese el producto: ')
        
        for num, lista in enumerate(text_list):
            if product in lista:
                index = num
                products = lista.split(', ')

                lista_final = update_product(products, index, text_list)
            
        if not lista_final:
            print('Producto no encontrado')
            caracteres()
        else:            
            with open('Jav-mol.txt', 'w') as file:
                for produc in lista_final:
                    if produc == '':
                        continue
                    file.write(f'{produc}\n')

def delete_product():
    with open('Jav-mol.txt', 'r') as file:
        texto = file.read()
        text_list = texto.split('\n')
        product = input('Ingrese el producto: ')
        
        for num, lista in enumerate(text_list):
            if product in lista:
                index = num
        
        if index >= 0:
            deleted = text_list.pop(index)
            print(deleted)
            with open('Jav-mol.txt', 'w') as file:
                for produc in text_list:
                    if produc == '':
                        continue
                    file.write(f'{produc}\n')
            caracteres()
                    
        else:
            print('Producto no encontrado')
            caracteres()


delete_caract = lambda x: int(x.replace('[', '').replace(']', '').replace('$', ''))
def ventas_por_producto():    
    with open('Jav-mol.txt', 'r') as file:
        texto = file.read()
        text_list = texto.split('\n')
        
        caracteres()
        product = input('Ingrese el producto: ')        
        
        for lista in text_list:
            if product in lista:
                products = lista.split(', ')

                venta_total = delete_caract(products[1]) * delete_caract(products[2])
        print(f'${venta_total}')
        caracteres()



def ventas_total():    
    with open('Jav-mol.txt', 'r') as file:
        texto = file.read()
        text_list = texto.split('\n')
        venta_total = 0
        
        for lista in text_list:
            if lista:
                products = lista.split(', ')

                venta_total += delete_caract(products[1]) * delete_caract(products[2])

        caracteres()        
        print(venta_total)
        caracteres()

menu = """1-Agregar Producto
2-Listar Productos
3-Actualizar Producto
4-Eliminar Producto
5-Venta por Producto
6-Venta Total
> """

functions = {
    '1':add_product,
    '2':listening_product,
    '3':edit_product,
    '4':delete_product,
    '5':ventas_por_producto,
    '6':ventas_total
}

while True:
    options = input(menu)
    
    option = functions.get(options, delete_file)

    if option():
        break