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


with open('Jav-mol.txt', 'a+') as file1:
    file1.seek(0)
    texto = file1.read()
    
    product = input('Ingrese el producto: ')
    
    
    inicio = texto.find(product) - 1
    
    print(inicio)
    
    
    fin = inicio + len(product) + 14
    
    print(fin)
    
    lista = texto[inicio:fin] #.split(', ')
    print(lista)
