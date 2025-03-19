""" ESTRUCTURAS """
# LISTAS
lenguages = ['C', 'Python', 'C#', 'Java', 'JavaScript', 'Visual Basic']
print(lenguages[0]) # Access 
print(lenguages[1])

lenguages.insert(1, 'C++') # Insertion
print(lenguages)
lenguages.append('Cobol')

lenguages.pop() # Remove
print(lenguages)
lenguages.remove('Cobol') 
print(lenguages)

lenguages[1] = 'C--' # Update
print(lenguages)

lenguages.reverse() # Ordering 
print(lenguages)
lenguages.sort()
print(lenguages)

print(type(lenguages))

# TUPLAS
frameworks = ('Angular', 'React', 'Svelte', 'Vue')
print(frameworks[0]) # Access
print(frameworks[1]) 

frameworks = tuple(sorted(frameworks)) # Ordering
print(frameworks)

print(type(frameworks)) 

# CONJUNTOS
me = {'Julian', 'Enrique', 'juls@developer.com', 17}
print(me)

me.add('u20212001@university.edu.co') # Insertion
print(me)

me.remove('u20212001@university.edu.co') # Remove
print(me)

print(type(me))

# DICCIONARIOS
me = {
    'name' : 'Julien',
    'surname' : 'Enrique',
    'alias' : 'Kike',
    'age' : 17,
    'developer' : ['fronted', 'backend']
}

print(me['name']) # Access

me['name'] = 'Julian' # Insertion
print(me)

del me['alias'] # remove
print(me)

me['age'] = 18 # Update
print(me)

me = dict(sorted(me.items())) # Ordering

print(type(me))
def agenda():
    agenda = {}
    
    def ingresar_contacto(nombre):
        numero = input('Ingresa el numero de telefono:\n')
        if numero.isdigit() and (len(numero) <= 11) and (len(numero) > 0):
            agenda[nombre] = numero
        else:
            print('Ingresa un número máximo de 11 dígitos\n')

    while True:
        choice = input("""\nOperación a realizar en la agenda de contactos:
        1. Insertar
        2. Buscar
        3. Actualizar 
        4. Eliminar
        5. Salir\n
        """)

        if choice == '1':
            name_contact = input('\nIngresa el nombre del contacto:\n')
            ingresar_contacto(name_contact)
        elif choice == '2':
            name_contact = input('\nIngresa el contacto a buscar:\n')
            if name_contact in agenda:
                print(f'\nEl número de teléfono de {name_contact} es: {agenda[name_contact]}')
            else:
                print(f'\nEl contacto {name_contact} no existe en la agenda')
        elif choice == '3':
            name_contact = input('\nIngresa el nombre del contacto a actualizar:\n')
            if name_contact in agenda:
                ingresar_contacto(name_contact)
            else:
                print(f'\nEl contacto {name_contact} proporcionado no existe')
        elif choice == '4':
            name_contact = input('\nIngresa el nombre del contacto a eliminar:\n')
            if name_contact in agenda:
                del agenda[name_contact]
                print(f'\nEl contacto {name_contact} ha sido eliminado de la agenda')
            else:
                print(f'\nEl contacto {name_contact} proporcionado no existe')
        elif choice == '5':
            break
        else:
            print('\nElige una opción válida\n')

agenda()