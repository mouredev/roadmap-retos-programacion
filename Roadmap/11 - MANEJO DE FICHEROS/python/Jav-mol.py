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

# Crear Fichero
#with open('Jav-mol.txt', 'w') as file:
#   
#    file.write(f'[Jabon], [10], [23] \n')
#    file.write(f'[Arroz], [20], [10] \n')
#    file.write(f'[Fideos], [20], [10]')



list_to_str = lambda lista:f'{lista[0]}, {lista[1]}, {lista[2]}'

def update_product(products, index, lista):
        total = input('Ingrese la cantidad vendida: ')
        products[1] = f'[{total}]'
        price = input('Ingrese el precio: ')
        products[2] = f'[${price}]'
        
        products_fin = list_to_str(products)
        lista[index] = products_fin
        
        return lista 
        
def edit_product():    
    with open('Jav-mol.txt', 'r') as file:
        texto = file.read()
        lista = texto.split('\n')
        lista_final = None
        product = input('Ingrese el producto: ')
        
        for a,i in enumerate(lista):
            if product in i:
                index = a
                products = i.split(', ')

                lista_final = update_product(products, index, lista)
            
        if not lista_final:
            print('Producto no encontrado')
        else:            
            with open('Jav-mol.txt', 'w') as file:
                for produc in lista_final:
                    if produc == '':
                        continue
                    file.write(f'{produc}\n')
