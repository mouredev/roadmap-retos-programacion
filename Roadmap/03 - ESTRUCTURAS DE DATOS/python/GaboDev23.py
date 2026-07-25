''' - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

'''
Listas
Ordenados: La posición de sus datos importa
Heterogenea: Puede almacenar distintos tipos de datos
Mutable: Se puede agregar, modificar y eliminar datos cuando quieras
'''
lista = [29, True, 3.1415, 'Que onda wacho', 3]

print(lista) # Mostrando todos los elementos de la lista
print(lista[0]) # Mostrando el primer elemento de la lista
# print(lista[4]) # La lista tiene 4 elementos, pero empiezan desde el indice 0, así que va desde el indice 0 al 3, entonces el indice 4 no existe, por lo que genera un error
print(lista[-1]) # Acceder al último elemento de la lista
print(lista[-2]) # Acceder al penúltimo elemento de la lista
print(lista[1:3]) # Muestra los elementos desde el índice 1 al 3

# Métodos de listas
lista.append(3) # Agrega un elemento al final de la lista
print(lista)
print(lista.count(3)) # Cuenta la cantidad de veces que aparece un elemento en la lista
print(lista.index(3.1415)) # Nos muestra el índice del primer elemento encontrado en la lista
lista.remove(3) # Elimina el elemento que tenga el valor pasado por parámetros
print(lista)

'''
Tuplas
Ordenados: La posición de sus datos importa
Heterogenea: Puede almacenar distintos tipos de datos
Inmutable: No se puede agregar, modificar y eliminar datos un vez creada
'''
tupla = ('¿La tierra es plana?', True, False)
print(tupla) # Mostramos los datos de la tupla

# Métodos de tuplas
print(tupla.count(False))
print(tupla.index(True))
print((3, )) # Tupla de un solo elemento

'''
Conjuntos
No ordenados - No importa la posición de los datos
Heterogeneo - Solo con datos inmutables
Mutable - Sin repetir
'''
print(set([5, 2, 5, 1, 1.5])) # Puede guardar listas
print(set((5, 2, 5, 1, 1.5))) # Puede guardar tuplas
print(set('Booooenaaasssss')) # Puede guardar un string (Lo toma como un conjunto de carácteres)
conjunto = set([1, 3, 3, 4]) # No permite datos repetidos
print(conjunto)

# Métodos
conjunto.add(5) # Agrega un elemento al final de la lista
print(conjunto)
conjunto.remove(1)
print(conjunto)

conjunto2 = set([5, 3, 5, 6])
conjunto3 = set([4, 2])
print(conjunto, conjunto2, conjunto3)
print(conjunto.intersection(conjunto2)) # Intersección de conjuntos
print(conjunto & conjunto2) # Otra manera de obtener la intersección
print(conjunto2.issubset(conjunto)) # Comprueba si un elemento está incluído en otro
print(conjunto3.issubset(conjunto))

'''
Diccionario
- No ordenado - No importa la posición de sus datos
- Es heterogeneo - Con clave inmutable
- Mutable - Se puede agregar, modificar y eliminar datos
'''
diccionario = {1: 'Uno', 2: 'Dos'}
print(diccionario)
diccionario[3] = 'Tres'
print(diccionario)
#Otra forma de crear diccionarios
dict_lista_tuplas = dict([(1, 'Uno'), (2, 'Dos'), (3, 'Tres')])
dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
# La key no debe repetirse, si se repite siempre tomara el primer valor

# Metodos
print(diccionario.keys()) # Devuelve las llaves del diccionario
print(diccionario.values()) # Devuelve los valores del diccionario
print(diccionario.items()) # Devuelve una tupla con los datos del diccionario
diccionario.pop(2) # Elimina la segunda clave del diccionario por lo tanto también elimina su valor
print(diccionario)

print()

'''
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos. (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
'''
contactos = {'A': [], 'B': [], 'C': [], 'D': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def esNumerico(num):
    if not num.isnumeric():
        print('El número no es de tipo numérico')
        return False
    elif not len(num) == 12:
        print('El número debe tener 12 carácteres')
        return False
    else:
        return True
    
def buscarContacto(nombre):
    contactoEncontrado = []

    inicial = nombre[0].upper()
    if inicial in contactos:
        for contacto in contactos[inicial]:
            if nombre.lower() == contacto[0].lower():
                contactoEncontrado.append(contacto)
    
    return contactoEncontrado
while True:
    seleccion = input('Elige una opción.\n1. Ingresar contacto.\n2. Modificar contacto.\n3. Mostrar Contactos.\n4. Eliminar contactos.\n0. Salir del programa.\n')
    match seleccion:
        case '1':
            print('Ingresar contacto')
            nombre = input('Ingresa el nombre del contacto: ')
            numero = input('Ingresa el número del contacto: ')
            
            if esNumerico(numero) == False:
                break
            
            for clave in contactos:
                if clave == nombre[0].upper():
                    contactos[clave].append([nombre, numero]) 
                    print(f'Agregado: {contactos[clave]}')
                    break
        case '2':
            print('Modificar contacto')
            nombre = input('Introduce el nombre del contacto que deseas modificar: ')
            encontrados = buscarContacto(nombre)
            
            if encontrados:
                print(f"Contacto encontrado: {encontrados}")
                nuevoNombre = input('Nuevo nombre (deja vacío si no quieres cambiarlo): ')
                nuevoNumero = input('Nuevo número (deja vacío si no quieres cambiarlo): ')

                for contacto in encontrados:
                    inicial = nombre[0].upper()
                    contactos[inicial].remove(contacto)
                    
                    nombreFinal = nuevoNombre if nuevoNombre.strip() else contacto[0]
                    numeroFinal = nuevoNumero if nuevoNumero.strip() else contacto[1]
                    nuevaInicial = nombreFinal[0].upper()

                    contactos[nuevaInicial].append([nombreFinal, numeroFinal])
                    print("Contacto modificado con éxito.")
                    print(contactos[inicial])
            else:
                print("Contacto no encontrado.")
        case '3':
            for letra in contactos:
                if contactos[letra]:
                    print(f'\nContactos con {letra}:')
                    for i, contacto in enumerate(contactos[letra], 1):
                        print(f'  {i}. Nombre: {contacto[0]}, Número: {contacto[1]}')
        case '4':
            print('Eliminar contacto')
            nombre = input('Introduce el nombre del contacto que quiere eliminar: ')
            contactoEncontrado = buscarContacto(nombre)
            if contactoEncontrado == []:
                print('No se encontró el contacto')
            else:
                print(f'Se encontró: {contactoEncontrado}')
                confirmar = input('¿Deseas eliminar este contacto? (s/n): ').lower()
                if confirmar == 's':
                    for contacto in contactoEncontrado:
                        contactos[nombre[0].upper()].remove(contacto)
                    print('Contacto eliminado.')
                else:
                    print('No se eliminó el contacto')
                print(contactos[nombre[0]])
        case '0':
            print('Programa cerrado')
            break
        case _:
            print('Opción incorrecta, vuelva a intentarlo')