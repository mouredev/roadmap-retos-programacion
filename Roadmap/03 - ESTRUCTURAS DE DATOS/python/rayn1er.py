# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
#  *   en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización
#  *   y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más
#  *   de 11 dígitos (o el número de dígitos que quieras).
#  * - También se debe proponer una operación de finalización del programa.
#  */

# listas 
# en python podemos crear listas creando una variable y asignandole a ella corchetes o utilizando el metodo list, las listas son mutables, por lo que podemos agregar y eliminar elementos de ella

my_list = [1,2,3,4,5] # creando con corchetes
my_list_2 = list(['i','am','a','list']) # ccreando utilizando list
my_list_3 = [1,'string',True] # las listas pueden almacenanr diferentes tipos de datos

print(my_list,my_list_2,my_list_3)

print(my_list_2[1]) # podemos obtener un dato individual si utilizamos corchetes luego de la misma junto con su indice
print(my_list_2[-1]) # tambien podemos obtener un dat utilizando indices negativos para empezar a contar desde el final de la lista
print(my_list_2[1:3]) # tambien se puede obtener una sublista separando dos indices con 2 puntos

my_list_2[2] = 'A' #podemos cambiar un elemento escribiendo junto a corchetes el indice del elemento que se quiere cambiar junto a su nuevo valor
print(my_list_2) # imprime la nueva lista modificada

my_list_2.append('of elements') # el metodo append nos sirve para agregar elementos al final de la lista
print(my_list_2)
my_list_2.pop() # el metodo pop nos sirve para eliminar elementos al final de la lista
print(my_list_2.count('i')) # el metodo count nos sirve para contar la cantidad de veces que se repite un elemento
print(my_list_2.index('i')) # el metodo index nos devuelve la posicion de la primera aparicion de un elemento
my_list_2.remove('i') #el metodo remove elimina la primera aparicion de un elemento
print(my_list_2)
my_list_2.sort() # las listas tambien poseen el metodo sort, el cual nos sirve para ordenar la lista de manera alfabetica
print(my_list_2)

# tuplas
# podemos crear tuplas utilizando parentesis o mediante el metodo tuple, las tuplas no son mutables, lo que significa que no podemos modificarlas una vez creadas

my_tuple_1 = ('element 1','element 2','element 3')
my_tuple_2 = tuple(('element 1','element 2','element 3'))
my_tuple_3 = ('elementstring',True,2000) #al igual que las listas, las tuplas pueden contener elementos de distintos tipos
print(my_tuple_1,my_tuple_2,my_tuple_3)

print(my_tuple_1[1]) #para aceder a sus elementos usamos corchetes igual que en las listas

print(my_tuple_1.count('element 1')) # se puede contar la cantidad de veces que aparece un elemento
print(my_tuple_1.index('element 3')) # tambien nos muestra el indice de un elemento

# conjuntos
# para crear conjuntos en python podemos utilizar llaves o el metodo set, los conjuntos pueden contener multiples tipos de datos, pero no puede contener datos repetidos

my_set = set([1,1,2,2,3,3,4,4])
my_set_2 = set([3,4,5,6])
print(my_set) #al imprimir observamos que solo tenemos un dato a pesar de que hemos colocado dos de ellos al crear el conjunto
my_set.add(5) #podemos anadir elementos utilizando el metodo add
print(my_set)
my_set.remove(5) # se pueden eliminar elementos utilizando el metodo remove
print(my_set)
print(my_set.intersection(my_set_2)) # el metodo intersection nos devuelve los elementos que se encuentren en dos conjuntos
print(my_set_2.issubset(my_set)) #issubset nos sirve para verificar si los elementos de un conjunto estan en otro

# diccionarios 
# los diccionarios nos permiten agregar elementos con una clave y un valor, estos se crean mediante los corchetes, tambien se pueden crear utilizando el metodo dict, los diccionarios son mutables, lo que significa que podemos agregar y eliminar valores

my_dict = {"name" : 'raul', 'age' : 25, 'country' : 'venezuela'}

print(my_dict)
print(my_dict['name']) # podemos ver el valor de una llave utlizando corchetes 
my_dict['name'] = 'rayn1er' # podemos cambiar el valor de una llave con un = 
print(my_dict)
my_dict['hobby'] = 'programming' # si le agregamos un valor a una llave que no existe, se agregara al final del diccionario
print(my_dict)
print(my_dict.keys()) # el metodo key nos devuelve una lista con las claves
print(my_dict.values()) # el metodo value nos devuelve una lista con los valores
print(my_dict.items()) # el metodo items devuelve una lista con los pares de datos clave y valor
my_dict.pop('country') # podemos eliminar una clave y su valor utilizando el metodo pop
print(my_dict)




agenda = {}    

while True:

      
    print('''
        Bienvenido a la agenda
        
        Ingrese la operacion que desea realizar:
          
          1 - Buscar contacto
          2 - Agregar contacto
          3 - Actualizar contacto
          4 - Eliminar contacto
          5 - Ver contactos
          6 - Cerrar agenda

''')
    
    option = int(input("Ingrese una opcion -> "))
    if option == 1:
        value = input("Ingrese el nombre del contacto -> ")
        if value in agenda:
            print()
            print(f'{value} - {agenda[value]}')
        else:
            print()
            print("Este contacto no se encuentra en la agenda")

    if option == 2:
        value = input("Ingrese el nombre del contacto -> ")
        if value in agenda:
            print()
            print("Este contacto ya esta en la agenda")
        else:
            number = int(input("Ingrese el numero del contacto -> "))
            agenda[value] = number
    if option == 3:
        value = input("Ingrese el nombre del contacto -> ")
        if value in agenda:
            number = int(input("Ingrese el nuevo numro del contacto -> "))
            agenda[value] = number
            print()
            print(f'su contacto {value} ha sido actualizado con exito!')
        else:
            print()
            print("Este contacto no se encuentra en la agenda")
    
    if option == 4:
        value = input("Ingrese el nombre del contacto -> ")
        if value in agenda:
            agenda.pop(value)
            print()
            print(f'Su contacto ha sido eliminado con exito!')
        else:
            print(f'Su contacto no se encuentra en la agenda')
    if option == 5:

        if len(agenda) == 0:
            print()
            print(f"No hay contactos en la agenda")
        else:
            for key, value in agenda.items():
                print(f'{key} - {value}')
    if option == 6:
        print('Cerrando agenda')
        break
    
    