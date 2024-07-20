
# Listas
lista = [1,2,3,4,5,6,0]
lista.append(7) # Insercion
print(lista)
lista.remove(2) # Borrado
print(lista)
lista.sort() # Ordenar
print(lista)


# Sets
set_1 = set([1,2,3,4,5,6,3,2,3,3])
print(set_1)
set_1.add(17) # Insertar elemento en el set
print(set_1)
set_1.remove(1) # eliminar un elemento del set
print(set_1)
set_2 = set([9,8,7,6,5,5,4,3])
set_1.update(set_2) # actualizar set
print(set_1)
print(sorted(set_1)) # Ordenar set

# Tuple
tupla = (1,2,3,4,5,5,6)
print(tupla)
print(tupla.count(5)) # Devuelve el numero de veces que esta repetido el elemento
print(tupla.index(2)) # Devuelve el indice del objeto

# Diccionario
dic = {'Nombre':'Abel','Apellido': 'Perez', 'Lenguaje': 'Python'}
dic['Edad'] = 40 # Insercion
print(dic)
dic.pop('Edad') # Borrar
print(dic)
dic.clear() # Vaciado de diccionario
print(dic)


# DIFICULTAD EXTRA
print('AGENDA DE CONTACTOS')
print('1 - Busqueda de contacto')
print('2 - Nuevo Contacto')
print('3 - Actualizar contacto')
print('4 - Borrar contacto')
opcion = input('Seleccione la opción deseada (0 para salir): ')

agenda = []


def validar_telefono(num):
    while not num.isdigit() or len(num)>= 11:
        print('El numero debe ser numerico y no superar los 11 digitos.')
        num = input('Vuelve a introducir el numero de telefono:')
    return num

while opcion != '0':
    contacto = {'Nombre':'','Tlfno':''}
    if opcion == '1':
        nombre = input('Introduce el nombre del contacto a buscar: ')
        [print(contacto) for contacto in agenda if contacto['Nombre'] == nombre ]
        
    elif opcion == '2':
        nombre = input('Nombre del contacto: ')
        telefono = input('Número de telefono: ')
        telefono = validar_telefono(telefono)
        contacto['Nombre'] = nombre
        contacto['Tlfno'] = telefono
        agenda.append(contacto)
        
    elif opcion == '3':
        nombre = input('Nombre del contacto a modificar: ')
        for contact in agenda:
            if contact['Nombre'] == nombre:
                telefono = input(f'Nuevo telefono para {nombre}')
                contact['Tlfno'] = validar_telefono(telefono)

            
    elif opcion == '4':
        nombre = input('Nombre del contacto a modificar: ')
        for contact in agenda:
            if contact['Nombre'] == nombre:
                agenda.remove(contact)
                print('Contacto eliminado')
    elif opcion == '0':
        print('MUCHAS GRACIAS POR USAR LA AGENDA DE CONTACTOS')
        break
    else:
        print('Opcion no deseada. Seleccione la opcion correcta.')
    
    print('1 - Busqueda de contacto')
    print('2 - Nuevo Contacto')
    print('3 - Actualizar contacto')
    print('4 - Borrar contacto')
    opcion = input('Seleccione la opción deseada (0 para salir): ')
    