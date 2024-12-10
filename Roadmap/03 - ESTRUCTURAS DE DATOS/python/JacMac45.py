# Estructuras de datos en Python!

# Listas : las listas son estructuras para almacenar datos, estos pueden ser de cualquier tipo, inclusive
# se pueden almacenar listas dentro una lista. Las listas son ordenadas por un índice donde el primer elemento
# tiene el índice 0. Estas pueden tener elementos duplicados

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

# Inserción de elementos a una lista.

my_list_numbers.insert(2,6)         # insert agrega un elemento a una posición indicada en la lista
print (my_list_numbers)
other_list = ["Hola", "Python"]
my_list_numbers.extend(other_list)  # extend extiende la lista agregando cualquier otro tipo de esctructura
print (my_list_numbers)
my_list_numbers.append(7)           # append agrega un elemento al final de la lista
print (my_list_numbers)

# Borrado de elementos de listas.

my_list_numbers.remove(5)  # elimina el primer elemento especificado que encuentre en la lista
print (my_list_numbers)
my_list_numbers.pop(1)     # elimina el elemento que se encuentra en la posición especificada 
print (my_list_numbers)
del my_list_numbers[0]     # este tambien elimina el elemento que se encuentra en la posición especificada
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

# Tuplas : Las tuplas son estructuras para almacenar datos, estas pueden ser de cualquier tipo, inclusive
# se pueden almacenar tuplas dentro una tupla. Las tuplas son ordenadas por un índice donde el primer elemento
# tiene el índice 0. Estas no pueden tener elementos duplicados y son inmutables

# Creación de tuplas

my_tuple = ()                          
print (type(my_tuple))                 # Impresión del tipo de la variable my_tuple: Tuple
my_tuple_numbers = (1,2,3,4,5,5,5)     
print (my_tuple_numbers)

# Accediendo a los elementos de una tupla

print (my_tuple_numbers[0])            # Imprime el primer elemento de la tupla: 1
print (my_tuple_numbers[1])            # Imprime el segundo elemento de la tupla: 2
print (my_tuple_numbers[2])            # Imprime el tercer elemento de la tupla: 3
print (my_tuple_numbers[3])            # Imprime el cuarto elemento de la tupla: 4

# sets : Los sets son estructuras para almacenar datos, estas pueden ser de cualquier tipo, inclusive
# se pueden almacenar sets dentro un set. Los sets son no ordenados y no pueden tener elementos duplicados

# Creación de sets

my_set = {1,2,3,4,5,5,5}
print (type(my_set))                # Impresión del tipo de la variable my_set: Set
print (my_set)

# Inserción de elementos a un set

my_set.add(6)                       # Agrega un elemento al set
print (my_set)

# Borrado de elementos de un set

my_set.remove(5)                    # Elimina el primer elemento especificado que encuentre en el set
print (my_set)
# my_set.remove(5)                    # Error, ya que no puede haber elementos duplicados en un set
my_set.discard(5)                   # Elimina el primer elemento especificado que encuentre en el set
print (my_set)
my_set.clear()                      # Elimina todos los elementos del set
print (my_set)

# Diccionarios : Los diccionarios son estructuras para almacenar datos, estas pueden ser de cualquier tipo, inclusive
# se pueden almacenar diccionarios dentro un diccionario. Los diccionarios son no ordenados y pueden tener elementos duplicados

# Creación de diccionarios

my_dicc = {}            # Crea un diccionario vacío
print (type(my_dicc))
my_dicc_elements = {
    "Nombre": "Jac",
    "Apellido": "Mac",
    "Edad": 20
}

# Inserción de elementos a un diccionario

my_dicc_elements["Profesion"] = "Desarrollador" # Agrega un elemento al diccionario
print (my_dicc_elements)

# Acceso a los elementos de un diccionario

print (my_dicc_elements["Nombre"])   # Accede al primer elemento del diccionario: Jac
print (my_dicc_elements["Apellido"])# Accede al segundo elemento del diccionario: Mac
print (my_dicc_elements["Edad"])    # Accede al tercer elemento del diccionario: 20

# Borrado de elementos de un diccionario

del my_dicc_elements["Profesion"]   # Elimina el primer elemento del diccionario
print (my_dicc_elements)

# Actualización de elementos de un diccionario

my_dicc_elements["Edad"] = 21       # Actualiza el tercer elemento del diccionario
print (my_dicc_elements)

# Ordenación de elementos de un diccionario

my_dicc_elements = {
    "Nombre": "Jac",
    "Apellido": "Mac",
    "Edad": 20
}

my_dicc_elements = dict(sorted(my_dicc_elements.items()))
print (my_dicc_elements)
print (type(my_dicc_elements))
print()

# DIFICULTAD EXTRA
print('*************************')
print('*                       *')
print('*   AGENDA TELEFÓNICA   *')
print('*                       *')
print('*************************')
print()

def agenda():
    
    datos_agenda = {}
    
    while True:
    
        print("\n1. Buscar Contacto")
        print("2. Añadir Nuevo Contacto")
        print("3. Modificar Contacto")
        print("4. Eliminar Contacto")
        print("5. Cerrar")

        operacion = input("\nSeleccione la operación deseada del 1 al 5: ")

        match operacion:
            case "1":
                nombre = input("\nIngrese el nombre del contacto: ")
                if nombre in datos_agenda:
                    print(f"El número de teléfono de {nombre} es {datos_agenda[nombre]}")
                else:
                    print("El contacto no existe")
            case "2":
                nombre = input("\nIngrese el nombre del contacto: ")
                telefono = input("\nIngrese el telefono del contacto: ")
                if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
                    datos_agenda[nombre] = telefono
                else: 
                    print("telefono no valido, por favor escribe un teléfono máximo de 11 digitos" )
            case "3":
                nombre = input("\nIngrese el nombre del contacto a modificar: ")
                if nombre in datos_agenda:
                    telefono = input("\nIngrese el nuevo número de teléfono: ")
                    if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
                        datos_agenda[nombre] = telefono
                    else:
                        print("telefono no valido, por favor escribe un teléfono máximo de 11 digitos" )
                else:
                    print("El contacto no existe")
            case "4":
                nombre = input("\nIngrese el nombre del contacto a eliminar: ")
                if nombre in datos_agenda:
                    del datos_agenda[nombre]
                else:
                    print("El contacto no existe")
                
            case "5":
                print("Cerrarando Agenda")
                break
            case _:
                print("Operación no valida. Elije una de las 5 opciones.")
            
            
agenda()         
                
            
                
            

