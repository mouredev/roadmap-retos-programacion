"""
/*
 * EJERCICIO:
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
 * - También se debe proponer una operación de finalización del programa.
 */
"""

#Listas
my_list = []  # creacion lista vacia
my_list = ["alan", "ramirez", 20, 1985, "alan2085@gmail.com" ]
print(my_list)

my_list.append(1.73) #insercion
print(my_list)

del my_list[1] #borra elemento posicion 1
print(my_list)

my_list [2] = 2014 #actualizacion
print(my_list) 

my_list = ["alan", "ramirez", "matheo", "alan2085@gmail.com" ]
my_list.sort() #ordenacion
print(my_list) 

#tuplas
my_tuple = () # creacion tupla vacia
my_tuple = (25, 86, 85, 2014, 5, 2024, 3) #las tuplas son inmutables no se pueden modificar
print(my_tuple)

my_tuple2 = (25,85,47)
print(my_tuple + my_tuple2) #las tuplas se pueden concatenar 



#Set
my_set = {} #creacion set vacio
my_set = {"Alan", "Nicolle", "Giselle", "Matheo"}
print(my_set)

my_set.add("Shakir") #insercion
print(my_set)

my_set.update(["ramirez"]) #actualizacion de la lista
print(my_set)

my_set.remove("Alan") #borrado
print(my_set)

#Diccionario
my_dictionary = dict() #creacion diccionario vacio
my_dictionary = {"name":"alan", "surname": "ramirez", "age": 39, "email": "alan2085@gmail.com"}
print(my_dictionary)

my_dictionary["address"] = "Chile" #insercion
print(my_dictionary)

my_dictionary["age"] = 38  #actualizacion
print(my_dictionary)

my_dictionary.pop("surname") #borrado por clave
print(my_dictionary)
del my_dictionary["age"] #borrado por clave
print(my_dictionary)
my_dictionary.popitem() #borra ultimo elemento
print(my_dictionary)

###### DIFICULTAD EXTRA ##########
print("vamos a crear la agenda de contacto.!")
count_contact = int(input("ingrese la cantidad de contactos de desea crear: "))
print(type(count_contact))
my_contacts = dict()
#creacion lista de contactos
while count_contact > 0:
    contact = input("ingrese el nombre del contacto: ")
    number = input("ingrese el numero del contacto, debe ser menor a 11 digitos: ")
    if len(number) > 11:
        number = input("ingrese el numero del contacto, debe ser menor a 11 digitos: ")
    else:
        my_contacts[contact] = number
    count_contact-= 1
print(my_contacts)
#Operaciones de la agenda
while True:
    print("Si desea actualizar numero de contacto presione 1: ")
    print("Si desea eliminar numero de contacto presione 2:   ")
    print("Si desea buscar numero de contacto presione 3:     ")
    print("Si desea salir del sistema presione 4:             ")

    option = int(input("Seleccione una opcion: "))

    if option == 1:
        contact = input("ingrese el nombre del contacto: ")
        if contact in my_contacts:
             number = int(input("ingrese el numero del contacto, debe ser menor a 11 digitos: "))
             my_contacts[contact] = number
        else:
            print("Contacto no existe")
    elif option == 2:
        contact = input("ingrese el nombre del contacto: ")
        if contact in my_contacts:
             del my_contacts[contact]
        else:
            print("Contacto no existe")
    elif option == 3:
        contact = input("ingrese el nombre del contacto: ")
        if contact in my_contacts:
             print(my_contacts[contact]) 
        else:
            print("Contacto no existe")
    elif option == 4:
        print("Hasta Luego")
        break
