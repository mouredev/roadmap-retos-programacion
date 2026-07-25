"""

EJERCICIO:
  - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
    en tu lenguaje.
  - Utiliza operaciones de inserción, borrado, actualización y ordenación.

"""

''' LISTAS '''
# Creación de una lista
mi_lista = ['Daniel', 'Africa', 'Paco', 'Jhon']
print(mi_lista)

# Inserción
mi_lista.append('Victor')
print(mi_lista)

# Borrado
mi_lista.remove('Paco')
print(mi_lista)

# Actualización
mi_lista[0] = 'Francisco'
print(mi_lista)

# Ordenación    
mi_lista.sort()
print(mi_lista) # Ordenado alfabéticamente


''' TUPLAS '''
# Creación de una tupla
mi_tupla = ('Daniel', 'Quiros', '25', 'Don Benito')
print(mi_tupla)

# Acesso
print(mi_tupla[0]) # Daniel

# Ordenación
mi_tupla = tuple(sorted(mi_tupla))
print(mi_tupla) 

''' SETS '''
# Creación de un conjunto
mi_set = {1, 2, 3, 4, 5}
print(mi_set)

# Acesso
# Los sets no tienen un orden definido, 
# tendriamos que convertirlo en una lista

# Inserción
mi_set.add(6)
mi_set.add(6)  # No se inserta un elemento repetido
print(mi_set)

# Borrado
mi_set.remove(3)
print(mi_set)

# Actualización
mi_set.update({7, 8, 9})
print(mi_set)

# Ordenación
mi_set = set(sorted(mi_set))
print(mi_set)

''' DICCIONARIOS '''
# Creación de un diccionario
mi_diccionario = {
    'nombre': 'Daniel', 
    'edad': 25, 
    'profesion': 'Programador'}
print(mi_diccionario)

# Acesso
print(mi_diccionario['nombre']) # Daniel

# Inserción
mi_diccionario['pais'] = 'España'
print(mi_diccionario)

# Actualización
mi_diccionario['edad'] = 26
print(mi_diccionario)

# Borrado
del mi_diccionario['edad']
print(mi_diccionario)

# Ordenación
mi_diccionario = dict(sorted(mi_diccionario.items())) # Ordenado alfabéticamente por items
print(mi_diccionario)

"""
DIFICULTAD EXTRA (opcional):
  Crea una agenda de contactos por terminal.
  - Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
  - Cada contacto debe tener un nombre y un número de teléfono.
  - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
  - El programa no puede dejar introducir números de teléfono no númericos y con más
    de 11 dígitos (o el número de dígitos que quieras).
  - También se debe proponer una operación de finalización del programa.

"""

print('\n--- EJERCICIO EXTRA ---\n')

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input('Ingrese el número de teléfono del contacto: ')
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
             print('El número de teléfono debe tener menos de 11 digitos y ser numérico.')

    while True:

        print('Selecciona una opción:')
        print('    1. Buscar un contacto')
        print('    2. Agregar un contacto')
        print('    3. Actualizar un contacto')
        print('    4. Eliminar un contacto')
        print('    5. Salir')
        
        opcion = input('\nOpcion: ')

        match opcion:

            case '1': # Buscar contacto
                name = input('Ingrese el nombre del contacto que desea buscar: ')
                if name in agenda:
                    print(f'El número de telefono del contacto {name} es -> {agenda[name]}.')
                else: 
                    print(f'El contacto {name} no existe en la agenda.')

            case '2': # Agregar contacto
                name = input('Ingrese el nombre del contacto: ')
                insert_contact()

            case '3': # Actualizar contacto
                name = input('Ingrese el nombre del contacto a actualizar: ')
                insert_contact()

            case '4': # Eliminar contacto
                name = input('Ingrese el nombre del contacto a eliminar: ')
                if name in agenda:
                    del agenda[name]
                else: print('El contacto no existe en la agenda.')

            case '5': # Salir
                print('Saliendo del programa...')
                break

            case _: # Opcion no valida
                print('Opcion no valida. Elige una opción válida.\n')

my_agenda()
