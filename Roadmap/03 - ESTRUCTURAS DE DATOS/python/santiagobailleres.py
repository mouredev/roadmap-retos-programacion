''' * EJERCICIO:
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
 * - También se debe proponer una operación de finalización del programa.'''

# Creación de estructuras de datos
# Listas
list=[1,2,3,4,5]
print("Lista:",list)
# Inserción
list.append(6)
print("Lista con inserción:",list)
# Borrado
list.remove(6)
print("Lista con borrado:",list)
# Actualización
list[1]=0
print("Lista con actualización:",list)
# Ordenación
list.sort()
print("Lista ordenada:",list)
# Inversión
list.reverse()
print("Lista invertida:",list)
# acceso
print("Elemento en la posición 2:",list[2])
print('Tipo :' , type(list))

# Tuplas
tuple_=(1,2,3,5,4)
print("Tupla:",tuple_)
# No se pueden modificar, borrar o actualizar
# Ordenación
tuple2=sorted(tuple_) # devuelve una lista ordenada
tuple=tuple(sorted(tuple_)) # convierte la lista ordenada en tupla
print("Tupla ordenada:",tuple)
# acceso
print("Elemento en la posición 2:",tuple[2])
print('Tipo :' , type(tuple))

# Diccionarios
dict_={"Nombre":"Santiago","Apellido":"Bailleres"}
print("Diccionario:",dict_)
# Inserción
dict_["Edad"]=25
print("Diccionario con inserción:",dict_)
# Borrado
del dict_["Edad"]
print("Diccionario con borrado:",dict_)
# Actualización
dict_["Nombre"]="Santiago Bailleres"
print("Diccionario con actualización:",dict_)
# Ordenación
dict2=sorted(dict_) # devuelve una lista ordenada
dict3=dict(sorted(dict_.items())) # es necesario poner .items()? 
# si no se pone .items() da error porque no se puede ordenar un diccionario
# convierte la lista ordenada en diccionario
print("Diccionario ordenado:",dict3)
# acceso
print("Valor de la clave 'Nombre':",dict_["Nombre"])
print('Tipo :' , type(dict_))
dicc= {1: 2, 2: 4, 3: 1}
dicc=dict(sorted(dicc.items())) #se puede ordenar un diccionario por clave o por valor
print('Diccionario ordenado por clave:',dicc)
# si se ordena por valor se debe hacer asi:
dicc=dict(sorted(dicc.items(), key=lambda x: x[1])) # x[1] es el valor de cada par clave-valor
print('diccionario ordenado por valor:',dicc)
# si se quieren reestablecer las claves se puede hacer asi:
dicc=dict(enumerate(dicc.values(),1)) # se enumeran los valores empezando en 1
print('diccionario con claves reestablecidas:',dicc)

# Conjuntos
set={1,2,3,4,5} # un conjunto no puede tener elementos duplicados y no tiene orden
# es util para eliminar duplicados de una lista o tupla y para realizar operaciones de conjuntos
# como union, interseccion, diferencia, etc.
print("Conjunto:",set)
# Inserción
set.add(6)
print("Conjunto con inserción:",set)
# Borrado
set.remove(6)
print("Conjunto con borrado:",set)
# Actualización
set.add(0)
print("Conjunto con actualización:",set)
# Ordenación
# no se puede ordenar un conjunto
# acceso
# no se puede acceder a un elemento por su posición
print('Tipo :' , type(set))
# Operaciones de conjuntos
set2={4,5,6,7,8}
print("Conjunto 2:",set2)
print("Union:",set.union(set2))
print("Intersección:",set.intersection(set2))
print("Diferencia:",set.difference(set2)) 
print("Diferencia simétrica:",set.symmetric_difference(set2))
print("Subconjunto:",set.issubset(set2)) # para que sea subconjunto todos los elementos de set deben estar en set2
print("Superconjunto:",set.issuperset(set2)) # para que sea superconjunto todos los elementos de set2 deben estar en set
print("Disjuntos:",set.isdisjoint(set2)) # si no tienen elementos en común

# EXTRA
'''Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.'''
# Agenda de contactos
def mi_agenda():  
    agenda={}
    while True:
        print('')
        print('1. Buscar contacto')
        print('2. Insertar contacto')
        print('3. Actualizar contacto')
        print('4. Eliminar contacto')
        print('5. Mostrar agenda')
        print('6. Salir')
        option=input('\nSeleccione una opción: ')
        if option=='1':
            name=input('Ingrese el nombre del contacto que desea buscar: ')
            if name in agenda:
                print(f'Nombre: {name}, Teléfono: {agenda[name]}')
            else:
                print('Contacto no encontrado')
        elif option=='2':
            name= input('Ingrese el nombre del contacto que desea insertar: ')
            phone=input('Ingrese el teléfono del contacto: ')
            if phone.isdigit() and len(phone)<=11 and len(phone)>0:
                agenda[name]=phone
                print('Contacto insertado')
            else:
                print('El número de teléfono debe ser numérico y tener máximo 11 dígitos')
        elif option=='3':
            name=input('Ingrese el nombre del contacto que desea actualizar: ')
            if name in agenda:
                phone=input('Ingrese el nuevo teléfono del contacto: ')
                if phone.isdigit() and len(phone)<=11 and len(phone)>0:
                    agenda[name]=phone
                    print('Contacto actualizado')
                else:
                    print('El número de teléfono debe ser numérico y tener máximo 11 dígitos')
            else:
                print('Contacto no encontrado')
        elif option=='4':
            name = input('Ingrese el nombre del contacto que desea eliminar: ')
            if name in agenda:
                del agenda[name]
                print('Contacto eliminado')
            else:
                print('Contacto no encontrado')
        elif option=='5':
            print('Agenda de contactos:')
            for name,phone in agenda.items():
                print(f'Nombre: {name}, Teléfono: {phone}')
        elif option=='6':
            print('Saliendo de la agenda...')
            break
        else:
            print('Opción no válida, ingrese un número del 1 al 6')
mi_agenda()




