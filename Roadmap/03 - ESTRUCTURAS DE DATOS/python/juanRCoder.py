'''Estructura de datos'''
# Listas -> conjunto de elementos mutables, pueden cambiar sus datos.
lista = ['1', 'a', '2', 'b', '3']
lista.append('c')       # agrega 'c'
lista.remove('2')       # remueve '2'
lista[1] = 'A'          # actualiza 'a' por 'A'
lista = sorted(lista)   # ordena de manera ascendente
# ['1', '3', 'A', 'b', 'c']

# Tupas -> estructura de datos inmutable, no se pueden cambiar sus elementos.
tupla = (2001, 31, 31)
tupla.count(31)         # cuenta elementos 31
tupla.index(31)         # devuelve posicion

# Conjuntos (set) estrcutura de datos mutables y con elementos unicos desordenados.
conjunto = {1, 4, 10, 3, 11}
conjunto.pop()          # elimina elemento aleatorio
conjunto.add(9)         # agrega elemento al conjunto
conjunto.remove(3)      # remueve elemento por el valor


# Diccionarios (set) estructura de datos mutable, son de pares (c-v)
diciconario = {'name': 'juan', 'lastName': 'ramirez'}
diciconario.get('name', 'no encontrado') # buscar elemento por clave, si no mostrar segundo parametro por defecto
diciconario.keys()      # lista de claves
diciconario.values()    # lista de valores
diciconario.items()     # lista de claves y valores


#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.

#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización
#  *   y eliminación de contactos.

#  * - Cada contacto debe tener un nombre y un número de teléfono.

#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.

contactos = [['pepe', 123456789], ['maria', 987645321]]
estatus = True

def buscar():
    print('BUSCAR CONTACTO:')
    estado = True
    while estado:
        print('Buscar por?\n1.Nombre\n2.Numero\n3.Salir')
        option_search = input('Opcion: ')
        if option_search == '1':
            nombre_find = input('Nombre del contacto: ')
            print([contact for contact in contactos if contact[0] == nombre_find] or 'No encontrado')
        elif option_search == '2':
            nombre_find = input('Numero del contacto: ')
            if nombre_find.isdigit(): 
                nombre_find = int(nombre_find)
                print([contact for contact in contactos if contact[1] == option_search] or 'No encontrado')
            else:
                 print('Ingresar numero valido')
        else:
            estado = False
            return 

def agregar():
    estatus_agregar = True
    
    while estatus_agregar:
        print('AGREGAR CONTACTO:\n1.Agregar Contacto\n2.Salir')
        option_add = int(input('opcion: '))
    
        if option_add == 1:
            name = input('Nombre del contacto: ')
            num_contact = input('Número del contacto: ')
            contactos.append([name, num_contact])
            print('Contacto Agregado')
        elif option_add == 2:
            estatus_agregar = False
    return
    
def update():
    estatus_update = True
    while estatus_update:
        print('ACTUALIZAR CONTACTOS:')
        print('1.Lista Contactos\n2.Nombre\n3.Numero\n4.Salir')
        opcion_update = input('opcion: ')
            
        if opcion_update == '1':
            print(contactos);
            
        elif opcion_update == '2':
            name_update = input('Nombre del contacto: ')
            for contacto in contactos:
                if contacto[0] == name_update:
                    name_update = input(f'Actualizar {name_update} por: ')
                    contactos[0][0] = name_update
            print('Nombre no encontrado')
        
        elif opcion_update == '3':
            num_update = int(input('Numero del contacto: '))
            for contacto in contactos:
                if contacto[1] == num_update:
                    num_update = input(f'Actualizar {num_update} por: ')
                    contactos[0][1] = num_update
            print('Numero no encontrado')
            
        else:
            estatus_update = False
    return 

def delete():
    estatus_delete = True
    while estatus_delete:
        print('ELIMINAR CONTACTOS:')
        print('1.Lista Contactos\n2.Eliminar\n3.Salir')
        opcion_update = input('opcion: ')
        
        if opcion_update == '1':
            print(contactos);
            
        elif opcion_update == '2':
            name_delete = input('Nombre del contacto: ')
            encontrado = False
            for contacto in contactos:
                if contacto[0] == name_delete:
                    print(f'Eliminar a {name_delete} de tus contactos? 1.SI 2.NO')
                    name_delete = input('opcion: ')
                    if name_delete == '1':
                        contactos.remove(contacto)
                        print('Contacto eliminado')
                    encontrado = True
                    break
            
            if not encontrado:
                print('Contacto no encontrado')

        else:
            estatus_delete = False
    return 
    
                 
while estatus:
    print('AGENDA DE CONTACTOS:')
    print('Operaciones Principales: \n1. Buscar Contacto\n2. Agregar Contacto\n3. Actualizar Contacto\n4. Eliminar Contacto\n5. Cerrar Programa')
    opcion = int(input('Opcion: '))

    if opcion == 1:
        buscar()
    elif opcion == 2:
        agregar()
    elif opcion == 3:
        update()
    elif opcion == 4:
        delete()
    elif opcion == 5:
        estatus = False