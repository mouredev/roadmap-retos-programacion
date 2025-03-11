"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

# Listas
print('LISTS')
my_list: list = ['Adolfo','Gaby', 'Adolfi', 'Manuela', 'Tomas', 'Josemaria']
print(my_list)
my_list.append('Francisco')  #Insercion
print(my_list)
my_list.remove('Francisco')  #borrado
print(my_list)
print(my_list[1])     #Acceso
my_list[1] = 'Gabriela'   #actualizacion
print(my_list[1])
my_list.sort()      #Ordenacion
print(my_list)
print(type(my_list))

# Tuplas  son inmutables
print('TUPLES')
my_tuple: tuple = ('Adolfo', 'Loza', 'ALA', '56')
print(my_tuple[1])
print(type(my_tuple))
#para que sirve?
my_tuple = tuple(sorted(my_tuple))  #sorted la ordena y convierte en lista, con tuple lo covertimos en tupla nuevamente
print(type(my_tuple))
print(my_tuple)

# Sets   No conservan la posicion, se evitan duplicados, no se puede ordenar
print('SETS')
my_set = {'Adolfo', 'Loza', 'ALA', '56'}
print(my_set)
print(type(my_set))
my_set.add('adolfolozaa@gmail.com')   # Insercion
my_set.add('adolfolozaa@gmail.com')   # Insercion duplicado
print(my_set)
my_set.remove('ALA')   #elimiar
print(my_set)

# Diccionario
my_dict: dict = {'Nombre': 'Adolfo',
                 'Apellido': 'Loza',
                 'Alias': 'ALA',
                 'Edad': '56'}
print(my_dict)
print(type(my_dict))

print(my_dict['Nombre']) # se accede por clave
my_dict['Email'] = 'adolfolozaa@gmail.com'  # Insercion
my_dict['Edad'] = '57'  # Actualizacion
print(my_dict)

del my_dict['Alias']   # Eliminacion
print(my_dict)
my_dict1 = sorted(my_dict) # al ordenar solo aparecen claves y como una lista
print(my_dict1)
print(type(my_dict1))

my_dict2 = sorted(my_dict.items()) # al ordenar con items una lista de tuplas
print(my_dict2)
print(type(my_dict2))

my_dict3 = dict(sorted(my_dict.items())) # convertimos a dict la lista de tuplas
print(my_dict3)
print(type(my_dict3))

'''
DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''

agenda: dict= {'Adolfo': '22233344'}
# funciones
def val_num():
    if  telefono.isdigit() and len(telefono) <= 11:
        print('numero valido')
        return
    else:
        print('Numero no valido')
        if seleccion == '2':
            insercion()
        else:
            actualizacion()


def menu_gen():
    print('Menu General')
    print('Que desea hacer? 1. Busqueda, 2. Insercion, 3. Actualizacion, otro. salir')
    global seleccion
    seleccion = input('Ingrese su seleccion? ')
    seleccion = str(seleccion)
    if seleccion == '1' or seleccion == '2' or seleccion == '3':
        print ('Usted ha seleccionado: '+ dict_selec[seleccion])
    else:
        print('Opcion no valida')

    if seleccion == '1':
        busqueda()
    elif seleccion == '2':
        insercion()
    elif seleccion == '3':
        actualizacion()
    else:
        print('Gracias por utilizar nuestro servicio de agenda!!!')


def menu2():
    seleccion2 = input('Desea continuar en: 1. '+  dict_selec[seleccion]+ '?' + ' o ir a 2. Menu General? ' )
    if seleccion2 == '1':
        if  dict_selec[seleccion] == 'Busqueda':
            busqueda()
        elif  dict_selec[seleccion] == 'Insercion':
            insercion()
        elif  dict_selec[seleccion] == 'Actualizacion':
            actualizacion()
        else:
            print('opcion no valida')

    elif seleccion2 == '2':
        menu_gen()
    else:
        print('Gracias por utilizar nuestro servicio de agenda!!!')

def busqueda():
    contacto = input('Ingrese nombre del contacto? ')
    print('Contacto ingresado es ' + contacto)
    try:
        print('su telefono es: '+ agenda[contacto])
    except:
        print('Contacto no encontrado')
    finally:
        menu2()

def insercion():
    nombre = input('Ingrese nombre del contacto nuevo? ')
    global telefono
    telefono = input('Ingrese telefono del contacto? ')
    val_num()
    agenda[nombre] = telefono
    print(agenda)
    menu2()

def actualizacion():
    nombre = input('Ingrese nombre del contacto a actualizar? ')
    if nombre not in  agenda:
        print('No es contacto ')
        actualizacion()
    else:
        global telefono
        telefono = input('Ingrese telefono nuevo del contacto? ')
        val_num()
        agenda[nombre] = telefono
        print(agenda)
        menu2()


print('Agenda por Terminal')
dict_selec = {'1': 'Busqueda', '2': 'Insercion', '3': 'Actualizacion'}
global telefono
menu_gen()





