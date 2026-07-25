import os
"""
 * EJERCICIO:
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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

#En Python se pede usar Listas Tuplas Set  y Diccionarios. asi com archivos externos para alamcenar estructuras
# que ya
# hoy
# en dia estan integradas en el lenguaje de forma nativa como sqlite, json, etc
#en estos ejemplos usaremos en Tuplas Diccionarios Sets y listas


#Ejemplo de lista
lista = [1,3,'Hola Mundo',5,7]
print ('lista original')
print (lista)
print ('\n')
"""Las listas son una estructura de datos que permite almacenar una coleccion de elementos
de cualquier tipo de dato, las listas son mutables, es decir que pueden cambiar su contenido y puede tener valores duplicados
y se declara con corchetes []"""

#Ejemplo de tupla
tupla = (1,3,'Hola Mundo',5,7)
print ('tupla original')
print (tupla)
print ('\n')
"""Las tuplas son una estructura de datos que permite almacenar una coleccion de elementos
de cualquier tipo de dato, las tuplas son inmutables, es decir que no pueden cambiar su contenido y puede tener valores duplicados
y se declara con parentesis ()"""

#Ejemplo de diccionario
diccionario = {'clave1': 1, 'clave2': 'Hola Mundo', 'clave3': 3, 'clave4': 5, 'clave5': 7}
print ('diccionario original')
print (diccionario)
print ('\n')
"""Los diccionarios son una estructura de datos que permite almacenar una coleccion de elementos
de cualquier tipo de dato, los diccionarios son mutables, es decir que pueden cambiar su contenido
Los diccionarios se caracterizan por tener una clave y un valor, es decir que la clave es un identificador y el valor es lo que vamos a almacenar
y puede tener valores duplicados pero la clave debe ser unica
y se declara con llaves {}"""

#Ejemplo de set
set = {1,3,'Hola Mundo',5,7}
print ('set original')
print (set)
print ('\n')
"""Los sets son una estructura de datos que permite almacenar una coleccion de elementos
de cualquier tipo de dato, los sets son mutables, es decir que pueden cambiar su contenido
Los sets se caracterizan por tener elementos unicos, es decir que no se pueden repetir elementos
y se declara con llaves {}"""

#Manejo de listas
print("\nManejo de listas")
#agregamos un elemento a la lista
lista.append(6)
print ('lista con append')
print (lista)
#borramos un elemento de la lista
lista.remove(6)
print ('lista con remove')
print (lista)
#ordenamos la lista
print ('para ordenar la lista se usa el metodo sorted iterando la lista todos los elementos deben ser comparables si '
       'hay alguno que no lo sea se da error')
def funcionOrder(l):
    try:
        sorted(l)
        return 'ordenada'
    except Exception as e:
        return f'{e}'
print (funcionOrder(lista))
print('cambiamos el valor de la lista que contiene string y ordenamos nuevamente')
lista[2] = 8
print ('lista con update')
print (lista)
lista.sort()
print ('lista con sort')
print (lista)
#modificamos un elemento de la lista
lista[0] = 7
print ('lista con update, se cambia el valor de un elemento en la posicion 0')
print (lista)
#borramos todos los elementos de la lista
lista.clear()
print ('lista con clear')
print (lista)


#Manejo de tuplas
print("\nManejo de tuplas")
print('como son inmutables no podemos agregar o borrar elementos u ordenar')
#como son inmutables no podemos agregar o borrar elementos


#Manejo de diccionarios
print("\nManejo de diccionarios")
#agregamos un elemento a la diccionario
diccionario['clave4'] = 'valor4'
print ('diccionario con append')
print (diccionario)
#borramos un elemento de la diccionario
del diccionario['clave4']
print ('diccionario con remove')
print (diccionario)
#ordenamos la diccionario
#para ordenar la diccionario se usa el metodo sorted iterando la diccionario todos los elementos deben ser comparables si
#hay alguno que no lo sea se da error
def ordenar_diccionario(d):
    try:
        new_d = dict(sorted(d.items(), key=lambda item: item[1]))
        print( 'ordenada')
        print (new_d)
        diccionario.clear()
        diccionario.update(new_d)
    except Exception as e:
        print( f'{e}')
print('intentamos ordenar el diccionario con el string')
print (ordenar_diccionario(diccionario))
#modificamos un elemento de la diccionario
print('cambiamos el valor de la diccionario que contiene string y ordenamos nuevamente')
diccionario['clave2'] = 9
print (ordenar_diccionario(diccionario))
#Modificamos un elemento de la diccionario
print ('diccionario con update')
print('')
diccionario['clave1'] = 999
print (diccionario)
#borramos todos los elementos de la diccionario
diccionario.clear()
print ('diccionario con clear')
print (diccionario)

#Manejo de sets
print("\nManejo de sets")
#agregamos un elemento a la set
print ('Al agregar y si son iguales a otro elemento lo ignora')
set.add(6)
print ('set con el item agredado')
print (set)
#borramos un elemento de la set
set.remove(6)
print ('set con remove')
print (set)
#modificamos un elemento y ordenamos la set
print ('el set no permite modificar los elementos y si intentamos ordernar un set no nos sirve por que al orderna '
       'retorna una lista y no un set')
#unir dos sets
print('una unir dos sets se usa el metodo union')
set1 = set.copy()
set2 = {10,20,16}
set3 = set1.union(set2)
print ('set con union')
print (set3)
#interseccion de dos sets
print('otra forma de unir dos sets es con el metodo intersection, une los set y devuelve solo los elementos en comun '
      'y lo retorna eordenado')
set4 = set.intersection(set3)
print ('set con intersection')
print (set4)
#diferencia de dos sets
print('otra forma de unir dos sets es con el metodo difference, une los set y devuelve solo los elementos que estan '
      'en el set 1 y no en el set 2 y lo retorna eordenado')
set5 = set2.difference(set4)
print ('set con difference')
print (set5)
#borramos todos los elementos de la set
set.clear()
print ('set con clear')
print (set)


"Crea una agenda de contactos por terminal."
print('\n\nAgenda de contactos, que usa el nombre como clave y el telefono como valor y se guarda en un diccionario')
print('-'*100)
print('\n\n')
agenda = {}

def telefonoValido():
    telefono = input("Introduzca el telefono: ")
    while True:
        if len(telefono) > 11 and len(telefono) < 9:
            print("Telefono no valido, intenta de nuevo\n")
            telefono = input("Telefono: ")
        elif not telefono.isdigit():
            print("Telefono no valido, intenta de nuevo\n")
            telefono = input("Telefono: ")
        else:
            break
    return telefono

def limpiar_pantalla():
    """Limpia la consola."""
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux, macOS, etc.
        os.system('clear')

while True:
    print("1. Nuevo contacto")
    print("2. Buscar un contacto")
    print("3. Ver agenda")
    print("4. Editar un contacto")
    print("5. Eliminar un contacto")
    print("6. Terminar")
    opcion = input("Selecciona una opcion: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = telefonoValido()
        agenda[nombre.upper()] = telefono
        limpiar_pantalla()
    elif opcion == "2":
        nombre = input("Nombre: ")
        nombre = nombre.upper()
        limpiar_pantalla()
        if nombre in agenda:
            print(f"Telefono: {agenda[nombre]} \n\n")
        else:
            limpiar_pantalla()
            print("Contacto no encontrado\n\n")
    elif opcion == "3":
        limpiar_pantalla()
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
        print("\n\n")
    elif opcion == "4":
        nombre = input("Introduce el Nombre a editar: ")
        nombre = nombre.upper()
        if nombre in agenda:
            telefono = telefonoValido()
            agenda[nombre] = telefono
            limpiar_pantalla()
            print(f"{nombre} actualizado \n\n")
        else:
            limpiar_pantalla()
            print("Contacto no encontrado\n\n")
    elif opcion == "5":
        nombre = input("Introduce el Nombre a eliminar: ")
        nombre = nombre.upper()
        if nombre in agenda:
            del agenda[nombre]
            limpiar_pantalla()
            print(f"{nombre} eliminado \n\n")
        else:
            limpiar_pantalla()
            print("Contacto no encontrado\n\n")
    elif opcion == "6":
        limpiar_pantalla()
        print("Hasta pronto\n\n")
        break
    else:
        limpiar_pantalla()
        print("Opcion no valida, elige una opcion del 1 al 6 \n")


