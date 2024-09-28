'''
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
 '''

print('-----------------------------------------------------------')
print('Ejemplo de tuplas')
print('-----------------------------------------------------------')
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tup)

print('- Seleccionando un elemento')
print(tup[2])
print('- Agregando elementos a una tupla')
print(tup + (100, 200))
print('- Actualizando elementos de una tupla')
try:
    tup[2] = 300
except:
    print('- No se pueden eliminar elementos porque una tupla es inmutable ')
print('- Eliminando elementos de una tupla')
print('No se pueden eliminar elementos porque una tupla es inmutable')
print('- Ordenando elementos de una tupla')
print(tuple(sorted(tup, reverse=True)))

print('-----------------------------------------------------------')
print('Ejemplo de listas')
print('-----------------------------------------------------------')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

print('- Seleccionando un elemento')
print(list[2])
print('- Agregando elementos a una lista')
list.append(200)
print(list)
print('- Actualizando elementos a una lista')
list[0] = -100
print(list)
print('- Eliminando elementos a una lista')
del list[0]
print(list)
print('- Ordenando elementos de una lista')
list.sort(reverse=True)
print(list)


print('-----------------------------------------------------------')
print('Ejemplo de diccionarios')
print('-----------------------------------------------------------')
dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
print(dict)

print('- Seleccionando un elemento')
print(dict[2])
print('- Agregando elementos a una dict')
dict[11] = 'eleven'
print(dict)
print('- Actualizando elementos a una dict')
dict[2] = 'dos'
print(dict)
print('- Eliminando elementos a una dict')
val_eliminado = dict.pop(1)
print(val_eliminado)
print(dict)
print('- Ordenando elementos de una dict')
dict_2 ={x: dict[x] for x in sorted(dict, reverse=True)}
print(dict_2)


print('-----------------------------------------------------------')
print('Ejemplo de set')
print('-----------------------------------------------------------')
v_set = {1, 2, 3, 4, 100}
print(v_set)

print('- Seleccionando un elemento')
print('Los elementos no se pueden consultar directamente solo se puede usar in')
print(2 in v_set)
print('- Agregando elementos a un set')
v_set.add(200)
print(v_set)
print('- Actualizando elementos a un set')
print('No se puede modificar un valor de un set')
print('- Eliminando elementos a un set')
v_set.remove(100)
print(v_set)
print('- Ordenando elementos de un set')
v_set_2 = sorted(v_set, reverse=True)
print(v_set_2)

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
'''
# Funciones
def f_inicio():
    print('-----------------------PANTALLA DE INICIO------------------')
    print('-- 1. Consultar un contacto')
    print('-- 2. Agregar un contacto')
    print('-- 3. Editar un contacto')
    print('-- 4. Eliminar un contacto')
    print('-- 5. Salir')
    print('-----------------------PANTALLA DE INICIO------------------')

def f_input_telf():
    flag = 0
    while flag == 0:
        telefono = input('Ingrese el número del contacto [Màximo 9 digitos]: ')
        try:
            if int(telefono) >= 100000000 and int(telefono) <= 1000000000:
                return telefono
        except:
            pass
        print('-- !El número debe tner 9 dígitos ...')

def f_consultar(dict):
    if not dict:
        print('-- !Agenda vacía...')
    for nom in dict.keys():
        print('-- ' + nom + ': ' + dict[nom])

def f_editar(nom_con, dict, opc=100):
    if opc == '3':
        if nom_con not in dict:
            input('El contacto no existe...')
            return 
    
    tel_con = f_input_telf()
    dict[nom_con] = tel_con

def f_agregar(nom_con, dict):
    if nom_con in dict:
        opcion_sn = input('El contacto ya existe desea modificarlo (S/N)?...: ')
        if opcion_sn.upper() == 'N':
            return        
    
    f_editar(nom_con, dict)    

def f_eliminar(nom_con, dict):
    if nom_con in dict:
        del dict[nom_con]
        print('Contacto eliminado ...')

        return
    print('Contacto no existe ...')
    
    
# Variables iniciales
agenda = {}

while True:
    f_inicio()
    opcion = input('Ingree una opción: ')

    if opcion == '1':
        f_consultar(agenda)
    elif opcion == '2':
        nom_contacto = input('Ingrese el nombre del contacto: ')
        f_agregar(nom_contacto, agenda)
    elif opcion == '3':
        nom_contacto = input('Ingrese el nombre del contacto: ')
        f_editar(nom_contacto, agenda, opcion)
    elif opcion == '4':
        nom_contacto = input('Ingrese el nombre del contacto: ')
        f_eliminar(nom_contacto, agenda)
    elif opcion == '5':
        print('-- !Saliendo del programa ...')
    else:
        print('--!Opción no válida ...')
        

