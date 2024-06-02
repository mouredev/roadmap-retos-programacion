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

