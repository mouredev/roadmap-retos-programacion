### 1 - LISTAS ###
print('## 1 - LISTAS ##')
# Creación de listas
print('# Creación de listas #')
lista_nombres= ['Ana', 'Mario', 'Olga', 'Marco']
print(lista_nombres)

# añadir un elemento a la lista
print('# añadir un elemento a la lista #')
lista_nombres.append('Maria')
print(lista_nombres)

# borrar un elemento
print('# borrar un elemento #')
lista_nombres.remove('Ana')
print(lista_nombres)

# Acceso a un elemeto de la lista
print('# Acceso a un elemeto de la lista #')
print(lista_nombres[1])

# Actualizar un elemento
print('# Actualizar un elemento #')
lista_nombres[1]= 'Luis'
print(lista_nombres)

# Ordenar elementos
print('# Ordenar elementos #') 
print(f'Ordenado como lo hemos creado --> {lista_nombres}')
lista_nombres.sort()
print(f'Ordenado con SORT() ------------> {lista_nombres}') # ordena por orden alfabetico de la 'a' a la 'z'
lista_nombres.reverse()
print(f'Ordenado con REVERSE() ---------> {lista_nombres}') # ordena por orden alfabetico de la 'z' a la 'a'

### 2 - TUPLAS ###
print('### 2 - TUPLAS ###')
# Creación de Tuplas
print('# Creación de Tuplas #')
tupla_nombres= ('Harold', 'Ana','Olga', 'Mario', 666)
print(tupla_nombres)

# Acceso a un elemeto de la Tupla
print('# Acceso a un elemeto de la Tupla #')
print(tupla_nombres[1])

# Desempaquetado de Tuplas
print('# Desempaquetado de Tuplas #')
persona_tupla = ("Ana", "Conejos", 47)
nombre, apellido, edad = persona_tupla
print(nombre)
print(apellido)
print(edad)

### 3 - SETS ###
print('### 3 - SETS ###')
# Creación de Sets
print('## Creación de Sets ##')
set_num1= {2, 5, 1, 9}
print(set_num1)
list_num= [10, 90, 50]
set_num2= set(list_num)
print(set_num2)

# añadir un elemento a un Set
print('# Agregar elementos #')
set_num1.add(7)
print(set_num1)

# borrar un elemento de un Set
print('# borrar un elemento de un Set#')
set_num1.remove(2) # Si el elemento no está en el Set, el interprete lanzará un error
print(set_num1)
set_num2.discard(30) # No arrojará un error si el elemento no está presente en el conjunto
print(set_num2)
set_num2.pop() # Elimina un elemento al azar
print(set_num2)

# Acceso a un elemeto del Set
print('# Acceso a un elemeto del Set #')
print("No se puede acceder a los elementos de un Set mediante indice,\npero si podemos recorrerlo con un bucle 'for'\no preguntar si un valor está presente con un 'in'")
for x in set_num1:
    print(x)
if 90 in set_num2:
    print(f'90 si está')

### 4 - DICCIONARIOS ###
print('### 4 - DICCIONARIOS ###')

# Creación de un diccionario
print('# Creación de un diccionario #')
dict_Usuario= {
    'Nombre' : 'Mario',
    'Apellidos' : 'Albiñana',
    'Alias' : 'Marito',
    'Edad' : 7
}
print(dict_Usuario) 

# añadir un elemento a un Diccionario
print('# Añadir un elemento a un Diccionario#')
dict_Usuario['email'] = 'marioalb@gmail.com'
print(dict_Usuario)

# Acceso a un elemento de un Diccionario
print('# Acceso a un elemento de un Diccionario #')
print(dict_Usuario['Nombre'])

# Actualizar un elemento de un Diccionario
print('# Actualizar un elemento de un Diccionario #')
dict_Usuario['Apellidos'] = 'Albiñana Conejos'
print(dict_Usuario)

# Borrar un elemento de un Diccionario
print('# Borrar un elemento de un Diccionario #')
del dict_Usuario['Alias']
print(dict_Usuario)

valorBorrado= dict_Usuario.pop('email') # Elimina y devuelve el valor de la clave eliminada
print(f'{valorBorrado} ha sido eliminado del diccionario\nAhora hay {dict_Usuario}')

### EJERCICIO EXTRA OPCIONAL ###
print('### EJERCICIO EXTRA OPCIONAL ###')

ejecucion= True
menu= ''' ##### AGENDA DE CONTACTOS #####
[A]ñadir contacto
[B]uscar contacto
[E]liminar contacto
a[C]tualizar contacto
[S]alir de la aplicación'''

def añadir_contacto(name, tlf):
    global agenda
    agenda.append({'nombre':name, 'tlf':tlf})

def buscar_contacto(busqueda):
    for x in agenda:
        if x ['nombre'] == busqueda:
            print(f'{x['nombre']} : {x['tlf']}')

def borrar_contacto(nombre_borrar):
    count= 0
    for contacto in agenda:
        if contacto ['nombre'] == nombre_borrar:
            agenda.pop(count)
            print(f'{nombre_borrar} fue borrado con exito!')
            break
        else:
            count += 1

    if count == len(agenda):
        print(f'{nombre_borrar} no se haya en la agenda')

def actualizar_contacto(busqueda, clave):
    global agenda
    count= 0
    for nombre in agenda:
        if nombre['nombre'] == busqueda:
            if clave == 'n':
                nombre_actualizar= input(f'Actualizar el nombre de \'{busqueda}\' a: ')
                agenda[count]['nombre'] = nombre_actualizar
                print(agenda[count])
            elif clave == 't':
                tlf_actualizar= input(f'Actualizar el tlf de \'{busqueda}\' a: ')
                agenda[count]['tlf'] = tlf_actualizar
                print(agenda[count])
            elif clave == 'a':
                nombre_actualizar= input(f'Actualizar el nombre de \'{busqueda}\' a: ')
                tlf_actualizar= input(f'Actualizar el tlf de \'{nombre_actualizar}\' a: ')
                agenda[count]['nombre'] = nombre_actualizar
                agenda[count]['tlf'] = tlf_actualizar
                print(agenda[count])
        count += 1

while ejecucion:
    print(menu)
    char=input('Introduce opción: ')
    end= True

    if char == 'a' or char == 'A': # añadir contacto
        Nombre= input('Introduce el nombre del contacto: ')

        while end:
            Tlf= input('Introduce el teléfono del contacto: ')
            if Tlf.isnumeric() and len(Tlf) < 10:
                añadir_contacto(Nombre, Tlf)
                end= False

    elif char == 'b' or char == 'B': # buscar contacto
        nombre_busqueda= input('Indica el nombre a buscar:')

        buscar_contacto(nombre_busqueda)

    elif char == 'e' or char == 'E': # borrar contacto
        nombre_eliminar= input('Indica el nombre a borrar: ')

        borrar_contacto(nombre_eliminar)

    elif char == 'c' or char == 'C': # actualizar contacto
        nombre_busqueda= input('Introduce nombre contacto a actualizar: ')
        clave_actualizar= input('Que quiere actualizar:\n[n]ombre\n[t]eléfono\n')

        actualizar_contacto()

    elif char == 's' or char == 'S': # salir aplicación
        print('Adios!')
        ejecucion= False

    else: # opción incorrecta
        print('Opción incorreceta. Vuelva a introducir opción')


# Timing del video por donde me he quedado (EJERCICIO EXTRA OPCIONAL) -> 2.23.00