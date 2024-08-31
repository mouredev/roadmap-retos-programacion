""" 
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
 """
 
def data_structures():
    # Create list, dict, set and tuple
    my_list = []
    my_dict = {}
    my_set = set()
    my_tuple = ('a',6,0,6,'a',(5,9))
    # Frozenset receive an interable
    my_frozenset_1 = (5,6,9,'a',(8,9,7))
    my_frozenset_1 = frozenset(my_frozenset_1)
    my_frozenset_2 = (5,7,9,'b',(8,1,7))
    my_frozenset_2 = frozenset(my_frozenset_2)
    
    ''' Insert element '''
    # List at the end
    my_list.append(5)
    my_list.append(6)
    my_list.append('p')
    
    # List at specific index
    my_list.insert(2,4) 
    my_list.insert(0,9)
    
    # Dict at specific key
    my_dict['a'] = 1
    my_dict['b'] = 2
    # Update dict
    my_dict['a'] = 6
    
    # Sets are unordered and unindexed
    my_set.add(5)
    my_set.add(3)
    my_set.add(9)
    my_set.add('a')
              
    ''' Remove element '''
    # List
    my_list.pop() # At the end
    my_list.pop(0) # At index
    my_list.remove(6) # Remove specific element
    
    # Dict
    my_dict.pop('a')
    my_dict.pop('c',0) # Return default value
    del my_dict['b']
    
    # Set
    my_set.pop() # Random element
    my_set.remove(3) # Error if element doesn't exist
    my_set.discard(5) # No error if element is not present
    
    ''' Sort '''
    # List
    my_list.sort()
    
    # Dict. We need method sorted. We organized keys and then create a new dictionary with the keys organized
    keys_my_dict = my_dict.keys()
    sorted_keys = sorted(keys_my_dict)
    new_my_dict = {}
    for key in sorted_keys:
        new_my_dict[key] = my_dict[key]
        
    ''' Clear '''
    # List
    my_list.clear() # or my_list = []
    
    # Dict
    my_dict.clear()
    
    # Set
    my_set = set()
        
    # Tuple are immutable. This are some operations:
    my_tuple.count('a') 
    my_tuple.index(6)
    my_tuple.index(6,2) # Initialize search index at 2
    my_tuple = () # Clear
    
    # Frozenset are also immutable.
    my_new_frozenset = my_frozenset_1.copy()
    my_frozenset_1.difference(my_frozenset_2)
    my_frozenset_1.intersection(my_frozenset_2)

data_structures()

agenda = {}
def my_agenda():
    option = int(input(f'''
        ****** BIENVENIDO ******
        1. Nuevo contacto
        2. Buscar contacto
        3. Actualizar contacto
        4. Borrar contacto
        5. Visualizar agenda
        6. Salir 
        Ingrese una opcion para operar: '''))
 
    while option != 6:
        if option == 1:
            name = input('Por favor ingrese el nombre del contacto: ')
            if name in agenda:
                print('El contacto ya se encuentra en la agenda')
            else:
                telephone = int(input('Ingrese el numero telefonico (maximo 11 digitos): '))
                
                while len(str(telephone)) > 11 or telephone == 0:
                    telephone = int(input('Por favor, ingrese un numero valido: '))
                agenda[name] = telephone
                print('Contacto agregado correctamente')
            
        if option == 2:
            name_search = input('Ingrese el nombre del contacto a buscar: ')
            if name_search in agenda:
                print(f'El contacto es {name_search} y el telefono {agenda[name_search]}')
            else:
                print('El contacto no se encuentra en la agenda')
                
        if option == 3:
            update = input('Ingrese el contacto a actualizar: ')
            if update in agenda:
                response = int(input('Si desea actualizar nombre ingrese 1, si lo que desea actualizar es telefono ingrese 2 '))
                if response == 1:
                    update_name = input('Ingrese el nombre nuevo: ')
                    agenda[update_name] = agenda[update]
                if response == 2:
                    update_telephone = int(input('Ingrese el nuevo telefono, maximo 11 digitos: '))
                    while len(str(telephone)) > 11 or telephone == 0:
                        update_telephone = int(input('Por favor, ingrese un numero valido: '))
                    agenda[update] = update_telephone
                    print(f'El contacto se modifico correctamente')
            else:
                print('El contacto no se encuentra en la agenda')
                    
        if option == 4:
            delete_contact = input('Ingrese el contacto a eliminar: ')
            if delete_contact in agenda:
                del agenda[delete_contact]
                print('Contacto eliminado')
            else:
                print('El contacto no se encuentra en la agenda')
        
        if option == 5:
            for key,value in agenda.items():
                print(f'Nombre: {key} - Telefono: {value}')  
                
        option = int(input(f'''
        ****** BIENVENIDO ******
        1. Nuevo contacto
        2. Buscar contacto
        3. Actualizar contacto
        4. Borrar contacto
        5. Visualizar agenda
        6. Salir 
        Ingrese una opcion para operar: '''))
        
my_agenda()  
    