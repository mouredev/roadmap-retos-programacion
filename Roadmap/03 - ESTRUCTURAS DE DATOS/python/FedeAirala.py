# Reto #03 ESTRUCTURAS DE DATOS

"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *

 """

# Estructuras de datos en Python!

""" Listas : las listas son estructuras para almacenar datos, estos pueden ser de cualquier tipo, inclusive
    se pueden almacenar listas dentro una lista. Las listas son ordenadas por un índice donde el primer elemento
    tiene el índice 0. Estas pueden tener elementos duplicados
"""

# Creación de listas.

my_list = []                                            # Lista vacía
my_list_numbers = [1,2,3,4,5]                           # Lista de números
my_list_strings = ["Hola", "Python"]                    # Lista de strings
my_list_several = ["Hola", 1,2,3, ["Python", "Java"]]   # Lista con elementos varios

print (type(my_list))            # Impresión del tipo de la variable my_list: List
print (my_list_numbers)
print (my_list_strings)
print (my_list_several)
print (my_list_several[4][1])    # Imprime el segundo elemento de la lista dentro de la lista: Java


# Inserción de un elemento a una lista.

my_list_numbers.append(5)           # append agrega un elemento y lo coloca en el último lugar
print (my_list_numbers)
my_list_numbers.insert(2,6)         # insert agrega un elemento a una posición indicada en la lista
print (my_list_numbers)
other_list = ["Hola", "Python"]
my_list_numbers.extend(other_list)  # extend extiende la lista agregando cualquier otro tipo de esctructura
print (my_list_numbers)

# Borrado de elementos de listas.

my_list_numbers.remove(5)  # elimina el primer elemento especificado que encuentre en la lista
print (my_list_numbers)
my_list_numbers.pop(1)     # elimina el elemento que se encuentra en la posición especificada
print (my_list_numbers)
del my_list_numbers[0]     # este también elimina el elemento que se encuentra en la posición especificada
print (my_list_numbers)
# del my_list_numbers      # elimina lista completa
my_list_numbers.clear()    # vacía la lista
print (my_list_numbers)

# Actualización de listas

my_list_strings[1]="Mundo" # Actualiza el índice 1 de la lista: cambia Python por Mundo
print(my_list_strings)

# Ordenación de listas

my_list_order = [4,65,8,4,26,95,1]
my_list_order.sort()                # ordena la lista en forma ascendente
print (my_list_order)
my_list_order.sort (reverse=True)   # ordena la lista en forma descendente
print (my_list_order)


# Tuplas 

""" Las tuplas permiten almacenar muchos tipos de datos, estos están indexados pero tienen la particularidad de 
    de que son ordenadas e inmutables. Al igual que las listas pueden tener cualquier tipo de elementos.
"""
# Creación de tuplas

my_tuple = ()                          # Tupla vacía
print (type(my_tuple))
my_tuple_numbers = (1,2,3,4,5,5,5)     # Tupla de números
print (my_tuple_numbers)

# Inserción de elementos a una tupla

# Para ello hay que convertir la lista en una lista, agregar el elemento y luego convertirlo en tupla nuevamente

my_tuple_numbers = (1,2,3,4,5,5,5)
tuple_list = list ( my_tuple_numbers)
tuple_list.append (6)
my_tuple_numbers = tuple(tuple_list)
print (my_tuple_numbers)


# Borrado de Tuplas

# Para eliminar un elemento de una tupla también se debe convertir en una lista, borrar el elemento y volver a tupla.

my_tuple_numbers = (1,2,3,4,5,5,5)
tuple_list = list ( my_tuple_numbers)
tuple_list.remove(5)
my_tuple_numbers = tuple(tuple_list)
print (my_tuple_numbers)

# Eliminar una tupla

# del my_tuple_numbers
# print (my_tuple_numbers)

# Conjuntos

""" Los conjuntos también se utilizan para almacenar elementos, ellos no están ordenados, no admiten duplicados
    y no son indexados, por lo tanto no se pueden ordenar
"""

# Creación de conjuntos

my_set = {""}           # Conjunto vacío
print (type(my_set))
my_set_elements = {"Hola",1,2,3,3,3,"Python"}
print(my_set_elements)  # Al imprimir se ve como aparece el elemento 3 una sola vez

# Inserción de un elemento a un conjunto

my_set_elements.add("Mundo")
print (my_set_elements) # Al imprimir se ve como lo agraga al elemento en cualquier posición

# Eliminar un elemento de un conjunto

"""Para ello no se puede indicar el índice, y al no permitir duplicados, busca el elemento a eliminar
y lo saca del conjunto
"""

my_set_elements.remove("Python")
print (my_set_elements)


# Diccionarios

""" Este tipo de estructura se utiliza para almacenar datos en pares clave:valor.
    Es una estructura ordenada, se puede modificar y no permite duplicados

"""

# Creación de un diccionario

my_dicc = {}            # Crea un diccionario vacío
print (type(my_dicc))
my_dicc_elements = {
                    "name" :"María",
                    "surname":"López",
                    "age": 25}
print (my_dicc_elements)

# Agregar un elemento a un diccionario

my_dicc_elements ["email"]= "marialopez@lopez.com"
print (my_dicc_elements)

# Actualizar elementos de un diccionario

my_dicc_elements["age"]= 30
print (my_dicc_elements)

# Eliminar elementos de un diccionario

my_dicc_elements.pop ("age")
print (my_dicc_elements)

print ("\n")
print ("\n")
print ("\n")

"""
 * DIFICULTAD EXTRA (opcional):

 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 
 """

print ("**********Agenda de Contactos***********")
print ("                                         ")
   

contacts = {}
try:
    def agregar():
        name = input ( "Ingrese nombre del contacto a agregar: ")
        num =  input("Ingrese número de teléfono del contacto: ")
        while True:
            if num.isdigit() and len(num) < 12 :
                contacts[name]= num
                print (contacts)
                print (f"El contacto {name} se ha ingresado correctamente")
                break
            else:
                print ("Número incorrecto")
                num =  (input("Ingrese número de teléfono del contacto: "))


    def buscar():
        name = input (" Ingrese el nombre del contacto que desea buscar: ")
        if name in contacts:
                print (f"{name} : {contacts[name]}")
        else:
            print (" El contacto no se encuentra en la agenda")
            ag = input ("Desea agregarlo S/N: ")
            if ag == "S":
                agregar()
            elif ag == "N":
                pass

            

    def actualizar():
        name = input ("Ingrese el contacto que desea actualizar: ")
        if name in contacts:
            num = input ("Ingrese nuevo número: ")
            
            while True:
                if num.isdigit() and len (num) < 12 :
                    contacts[name]= num
                    print (f"El contacto {name} se ha actualizado correctamente")
                    break
                else:
                    print ("Número incorrecto")
                    num =  (input("Ingrese número de teléfono del contacto: "))
        else:
            print ("El contacto no existe")

    def eliminar ():
        name = input("Ingrese nombre de contacto a eliminar:")
        if name in contacts:
            contacts.pop(name)
            print (f"Se eliminó el contacto {name}")
        else:
            print ("El contacto no existe en la agenda")
    

    def agenda():
        
        while True:
            print ("1 ! Buscar , 2 ! Agregar , 3 ! Actualizar, 4 ! Eliminar, 5 ! Lista, 6 ! Salir ")
            opcion = int(input ("Ingrese opción: "))

            if opcion == 1:
                buscar()
            elif opcion == 2:
                agregar()
            elif opcion == 3:
                actualizar()
            elif opcion == 4:
                eliminar()
            elif opcion == 5:
                print ("Contactos     Número")
                for i in contacts:
                    print (f"  {i}        {contacts[i]}")
            elif opcion == 6:
                print ("Ha salido de la agenda")
                break
            else:
                opcion = input("Opción incorrecta, vuela a elegir: ")

    agenda()
      
except Exception as e:
    print (e)





