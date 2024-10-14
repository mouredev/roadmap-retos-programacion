# Listas

my_list = list()
my_list: list = ['Brais','Bl4ck','Wolfy','Liner','Hanny']
print(my_list)

my_list.append('Yamid') # INSERCIÓN  ---> Añadir un elemento al final de la lista
my_list.append('Yamid') 
print(my_list)

my_list.insert(0,'Celeste') # INSERCIÓN  ---> Añadir un elemento en la lista deacuerdo al indice  
print(my_list)

my_list.remove('Brais') # ELIMINACIÓN  ---> Eliminar un elemento en la lista deacuerdo al valor dado  
print(my_list)

print(my_list[1]) # Acceso

my_list[1] = 'Cuervillo' # Actualización
print(my_list) 

my_list.sort()# Ordeanación
print(my_list)

# Tuplas

my_tuple = tuple()
my_tuple: tuple = ('Liner','LanderDev','@landerdev','24')

print(my_tuple[1]) # Acceso
print(my_tuple[3])

my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)
print(type(my_tuple))

# set 

my_set = set()
my_set = {'Liner','LanderDev','@landerdev','24'} 
print(my_set)

my_set.add('linerlander@gmail.com') # Inserción

my_set.add('linerlander@gmail.com') # Evita duplicado
my_set.remove('Liner') # Eliminación
print(my_set)

my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario

my_dict = dict()
my_dict: dict = {
    'name':'Liner',
    'surname':'LanderDev'
    ,'alias':'@landerdev',
    'age':'24'
}
my_dict['email'] = 'linerlander@gmail.com' #Inserción
print(my_dict)

print(my_dict['alias']) # Acceso

my_dict['age'] = '37' # Actualización
print(my_dict)

del my_dict['name'] # Eliminación
print(my_dict)

my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)

print(type(my_dict))

'''
Dificultad Extra
'''

def my_agenda():
    agenda = {}

    def inser_contact():
        phone = input('Introduce el teléfono del contacto: ')
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print('Debes introducir un número de teléfono con un máximo de 12 dígitos.')
    def no_existe():
        print(f'El contacto {name} no existe.')
    
    while True:
        print('\n')
        print('#### AGENDA ######')
        print('\n1. Buscar contacto')
        print('2. Insertar contacto')
        print('3. Actualizar contacto')
        print('4. Eliminar contacto')
        print('5. Salir')

        option = input('\nSeleciona una opción: ')
        print(option)

        match option:
            case '1':
                name = input('Introduce el nombre del contacto a buscar: ')
                if name in agenda:
                    print(f'El número de teléfono de {name} es {agenda[name]}.')
                else:
                    no_existe()
                pass
            case '2':
                name = input('Introduce el nombre del contacto a insertar: ')
                inser_contact()
            case '3':
                name = input('Introduce el nombre del contacto a actualizar: ')
                if name in agenda:
                   inser_contact() 
                else:
                    no_existe()
            case '4':
                name = input('Introduce el nombre del contacto a eliminar: ')
                if name in agenda:
                    del agenda[name]
                else:
                    no_existe()

            case '5':
                print('Saliendo de la agenda.')
                break
            case _:
                print('Opción no válida. ELige una opción del 1 al 5')

my_agenda()