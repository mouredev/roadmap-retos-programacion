"""
Listas
Son colecciones ordenadas y mutables de elementos
"""

# Creacion de listas
mi_lista = [1,2,3,4,5]

# Inserccion
mi_lista.append(5) # Inserta el numero 5 al final de la lista
mi_lista.insert(2, 2.5) # Inserta el numero 2.5 en la posicion 2

# Borrado
mi_lista.remove(2.5) # Elimina el primer elemento con valor 2.5
del mi_lista[0] # Elimina el elemento en la posicion numero 0

# Actualizacion
mi_lista[1] = 10 # Actualiza el elemento en la posicion 1 a 10

# Ordenacion
mi_lista.sort() # Ordena la lista de forma ascendente
mi_lista.sort(reverse=True) # Ordena la lista de forma descendente

print(mi_lista)


"""
Tuplas
Son colecciones ordenadas e inmutables de elementos
Para modificar una tupla, se debe crear una nueva
"""

# Creacion
mi_tupla = (1,2,3,4,5)

# Ordenacion
lista_ordenada = sorted(mi_tupla)
mi_tupla_ordenada = tuple(lista_ordenada)
print(mi_tupla_ordenada)


"""
Conjuntos
Son colecciones no ordenadas y mutables de elementos unicos
"""

# Creacion
mi_conjunto = {1,2,3,4,5}

# Inserccion
mi_conjunto.add(6) # Añade un elemento al conjunto

# Borrado
mi_conjunto.remove(2) # Elimina el elemento 2 del conjunto
mi_conjunto.discard(3) # Elimina el elemnto 3 si esta presente

# Actualizacion
# Los conjuntos no poseen index por lo cual para actualizar un elemento, primero se debe eliminar y luego añadir el nuvo elemento

# Ordenacion
lista_ordenada = sorted(mi_conjunto) # Ordena el conjunto y devuelve una lista
print(mi_conjunto)


"""
Diccionarios
Son colecciones no ordenadas de pares clave - valor
"""

# Creacion
mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Inserccion 
mi_diccionario['f'] = 6 # Añade un nuevo par clave -valor

# Borrado
del mi_diccionario['b'] # Elimina el par con la clave 'b'
mi_diccionario.pop('a') # Elimina y devuelve el valor asociado con la clave 'a'

# Actualizacion
mi_diccionario['c'] = 30 # Actualiza el valor asociado a la clave 'c' por 30

# Ordenacion
# Los diccionarios no tienen un orden, pero se puede ordenar por clave o valor
dict_ordenado_por_clave = dict(sorted(mi_diccionario.items()))
dict_ordenado_por_valor = dict(sorted(mi_diccionario.items(), key=lambda item: item[1]))

print(dict_ordenado_por_clave)
print(dict_ordenado_por_valor)


"""
Extra
"""

def agenda_contactos():

    agenda = {}

    def insertar():
        nombre = input('Por favor ingrese el nombre del contacto: ')
        while True:
            numero = input('Por favor ingresa el numero del contacto:')
            if numero.isdigit() and 5 <= len(numero) <= 11:
                agenda[nombre] = numero
                print(f'Contacto {nombre} agregado correctamente.')
                break
            else:
                print('Numero de contacto invalido. Debe tener entre 5 a 11 Digitos.')

    def eliminar():
        nombre = input('Por favor ingrese el nombre del contacto que desea eliminar: ')
        if nombre in agenda:
            del agenda[nombre]
            print(f'Contacto {nombre} eliminado correctamente.')
        else:
            print(f'Contacto {nombre} no encontrado.')

    def actualizar():
        nombre = input('Por favor ingresa el nombre del contacto que deseas actualizar: ')
        if nombre in agenda:
            print(f"""Seleccione una de las siguientes opciones:
                a. Actualizar nombre de contacto
                b. Actualizar numero de contacto""")
            actualizacion = input('Inserte la opcion a elegir: ')
            if actualizacion == 'a':
                nuevo_nombre = input('Por favor ingrese el nuevo nombre de contacto: ')
                agenda[nuevo_nombre] = agenda.pop(nombre)
            elif actualizacion == 'b':
                nuevo_numero = input('Por favor ingrese el nuevo numero de contacto: ')
                agenda[nombre] = nuevo_numero
        else:
            print(f'Contacto {nombre} no encontrado.')

    def buscar():
        nombre = input('Por favor ingrese el nombre del contacto que desea buscar: ')
        if nombre in agenda:
            print(f'El numero de {nombre} es {agenda[nombre]}.')
        else:
            print(f'El contacto {nombre} no encontrado.')
    
    while True:
        print('Bienvenido a tu agenda')
        print(f"""Que operacion deseas realizar: 
            a. Inserta contacto
            b. Eliminar contacto
            c. Actualizar contacto
            d. Buscar contacto
            e. Salir
            """)
        
        opcion_usuario = input('Por favor ingresa la opcion a seleccionar: ')

        if opcion_usuario == 'a':
            insertar()
        elif opcion_usuario == 'b':
            eliminar()
        elif opcion_usuario == 'c':
            actualizar()
        elif opcion_usuario == 'd':
            buscar()
        elif opcion_usuario == 'e':
            print('Saliendo de la agenda...')
            break
        else:
            print('Opcion no valida, por favor intenta de nuevo.')

agenda_contactos()