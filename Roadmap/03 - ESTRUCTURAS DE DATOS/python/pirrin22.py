'''
Estructuras de datos
'''

# Listas.

my_list = ['Pirrin', 'Python', 36, 7.5] # lista origen
print(my_list)

my_list.append('Apple')  # Lista con un elemento añadido al final de la lista
print(my_list)

my_list.remove('Python') # Lista con un elemento eliminado mediante nombre valor
print(my_list)

my_list[0] = 'PirrinDev' # modificacion de elemento mediante indice
print(my_list)

if 'PirrinDev' in my_list: # Comprovacion de pertenencia de un elemento
    print('Si, PirrinDev esta en lista')

my_other_list = [4 , 16, 'Ford']

my_list.extend(my_other_list) # Agregar una lista a otra
print(my_list)

my_integer_list = [5, 16, 24, 98, 4, 12] 

my_integer_list.sort() # Ordenar lista de menor a mayor o en orden alfabetico de la A -> z
print(my_integer_list)

my_integer_list.sort(reverse=True) # Ordenar lista de mayor a menor o en orden alfabetico de la z -> A
print(my_integer_list)

my_list.clear() # Vaciar una lista
print(my_list)

del my_list # Eliminar una lista por completo



# Tuplas

'''
Las tuplas son inmutables, no habra ningun ejemplo con funcion de insercion.
'''

my_tuple = (4, 16 ,200, 84) 


if 16 in my_tuple: # Comprovacion de pertenencia de un elemento
    print('Si, 16 esta en la tupla')

print(len(my_tuple)) # Revision de cuantos elementos tiene la Tupla

sorted_my_tuple = sorted(my_tuple) # Ordenacion de los elementos de la Tupla.
print(sorted_my_tuple)

print(my_tuple.count(16)) # Revision de cuantos elementos del numero '16' hay en la tupla

print(my_tuple.index(200)) # Comprovacion de en que posicion de indice esta el numero '200'

min_my_tuple = min(my_tuple) # Comprovacion del numero menor de la Tupla
print(min_my_tuple)

max_my_tuple = max(my_tuple) # Comprovacion del numero mayor de la Tupla
print(max_my_tuple)

del my_tuple # Eliminar una tupla
#print(my_tuple)



# Sets

'''
Los sets son estructuras desordenadas, por eso nunca se imprimiran en el mismo orden.
En el momento de eliminar deberemos hacerlo por elemento y no por indice.
'''

my_set = {4, 6, 12, 3, 45}

if 12 in my_set: # Comprovacion de pertenencia
    print('Si, 12 esta en el set')

my_set.add('Pirrin') # Añadir un elemento al Set
print(my_set)

my_set.update([10, 300]) # Añadir varios elementos al Set
print(my_set)

my_set.remove(10) # Eliminar un elemento (En el caso de la funcion 'remove()' nos dara un error en el caso que no este el elemnto).
print(my_set)

my_set.discard('Pirrin') # Eliminar un elemento (En el caso de la funcion 'discard()' no salta ningun error en el caso de que no este el elemento).
print(my_set)

print(my_set.pop()) # La funcion 'pop()'  elimina un elemento aleatiorio y te lo muestra. 

my_set.clear() # Vaciar el Set.
print(my_set)

my_set_impares = {1, 3, 5, 7, 9}
my_set_primos = {1, 2, 3, 5, 7, 9}

my_union_sets = my_set_impares.union(my_set_primos) # Union de los dos sets, no permite duplicados.
print(my_union_sets)

my_intersection_sets = my_set_impares.intersection(my_set_primos) # La funcion 'intersection()' nos da los numeros repetidos de cada set que le pidamos.
print(my_intersection_sets)

my_diferencia_sets = my_set_primos.difference(my_set_impares) # La funcion 'difference()' te muestra la diferencia entere los dos sets.
print(my_diferencia_sets)



# Diccionarios

my_dict = {
    'Marca' : 'Seat',
    'Modelo' : 'Leon',
    'Año' : 2016
}

my_dict['City'] = 'New York' # Operacion de insercion poniendo la clave entre corchetes y el valor despues del igual.
print(my_dict)

my_dict['Año'] = 2022 # Operacion para cambiar un valor de los que ya tenemos en el diccionario.
print(my_dict)

my_dict.update({'CP' : 10018, 'Pneumaticos' : 'Michelin'}) # Operacion para añadir varios elementos.
print(my_dict)

my_dict.setdefault('Cambio', 'Automatico') # Operacion para insertar una clave valor que no exista en el diccionario.
print(my_dict)

print(my_dict.pop('Año')) # Operacion de borrado de un elemento del diccionario
my_dict.pop('CP')
print(my_dict)


sorted_my_dict = dict(sorted(my_dict.items())) # Operacion de ordenado del diccionario
print(sorted_my_dict)



# Ejercicio dificultad extra.



def agenda():

    my_agenda = {}

    def comprovacion():
        numero = input(f'Inserta el numero de telefono: ')
        if numero.isdigit() and len(numero) > 0 and len(numero) <= 11:
            my_agenda[nombre] = numero
            print(f'El contacto {nombre} se guardo.')
        else:
            print('El numero debe contener como maximo 11 digitos.')
    
    
    while True:

        print('')
        print('1. Buscar un contacto')
        print('2. Insertar un contacto')    
        print('3. Actulizar un contacto')
        print('4. Eliminar un contacto')
        print('5. Salir')
        
        option = input('Selecciona una opcion: ')

        match option:
            case '1':
                nombre = input('Introduce el nombre a busar: ')
                if nombre in my_agenda:
                    print(f'El numero de {nombre} es {my_agenda[nombre]}')
                else:
                    print(f'El contacto {nombre} no exsiste')
            case '2':
                nombre = input('Inserta el nombre: ')
                comprovacion()
                            
            case '3':
                nombre = input('De que contacto quieres cambier el nombre: ')
                if nombre in my_agenda:
                     comprovacion()
                else:
                    print(f'El contacto {nombre} no existe.')
            case '4':
                nombre = input('Que contacto quieres eliminar: ')
                if nombre in my_agenda:
                    del my_agenda[nombre]
                    print(f'El contacto {nombre} se elimino.')
                else:
                    print(f'El contacto {nombre} no existe.')
            case '5':
                print('Saliendo de la agenda')
                break
            case _:
                print('Elige una opcion entre las que aparecen.')





agenda()