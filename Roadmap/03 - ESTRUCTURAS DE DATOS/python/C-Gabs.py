#Reto 03

'''EJERCICIO:
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
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.'''


#Creación de listas

lista_1 = []

lista_2 = list()

#Inserción de elementos
lista_1 = ["JavaScript"]
print(lista_1)
lista_1.append("Python")
print(lista_1)
lista_1.append("Kotlin")
print(lista_1)
lista_1.insert(1,"Swift")
print(lista_1)
lista_1.extend(["C#","C++","Java"])
print(lista_1)

lista_2 = lista_1[:]
print()
#Borrado de elementos

lista_1.pop()
print(lista_1)
lista_1.pop(0)
print(lista_1)
lista_1.remove("C++")
print(lista_1)
lista_1.clear()
print(lista_1)
print()

#ordenacón de elementos

lista_2.sort()
print(lista_2)
lista_2.reverse()
print(lista_2)
print()

#actualización de elementos

lista_2[3] = "Html"
print(lista_2)
print("\n")

#Creación de tuplas

tupla_1 = ()
tupla_2 = tuple()

#inserción de elementos

tupla_1 = ("Python")
print(tupla_1)
tupla_1 = ("Python", "Java")
print(tupla_1)
print()

'''Las tuplas son estructuras no mutables,
estas no se pueden modificar'''
#tupla_1[1] = "Html"

#Borrado de elementos

tupla_1 = ()
print(tupla_1)
print("\n")

#Creación de sets

set_1 = set()
set_2 = set()

#Inserción de elementos

set_2.add("Python")
print(set_2)
set_2.add("Kotlin")
print(set_2)
set_1.add("JavaScript")
print(set_1)
set_1.add("Java")
print(set_1)
set_1.add("Swift")
print(set_1)
set_1.add("HTML")
print(set_1)
print()

#Borrado de elementos

set_1.discard("Java")
print(set_1)

set_1.remove("HTML")
print(set_1)

set_1.clear()
print(set_1)
print()

#Actualización de elementos
set_2.update({"Java","Swift","SQL"})
print(set_2)
set_2.intersection_update({"Pandas","Python","SQL","Java","HTML"})
print(set_2)
set_2.symmetric_difference_update({"Python","Kotlin","SQL","HTML","Java","Pandas","Numpy"})
print(set_2)
print("\n")

'''Los set son estructuras no ordenadas,
por lo que no tienen operaciones de ordenación
asociadas'''

#Creación de diccionarios

dict_1 = {}
dict_2 = dict()

#Inserción de elementos

dict_1["Nombre"] = "Brais"
print(dict_1)
dict_1["Apellido"] = "Moure"
print(dict_1)
dict_1 = {"Nombre":"Brais","Apellido":"Moure","Alias":"MoureDev"}
print()
#Borrado de elementos

retorno = dict_1.pop("Apellido")
print(retorno)
print(dict_1)
retorno = dict_1.popitem()
print(retorno)
print(dict_1)
dict_1.clear()
print(dict_1)
print()

#Actualización de elementos
dict_1 = {"Nombre":"Brais","Apellido":"Moure","Alias":"MoureDev","Lenguaje":"Kotlin"}
print(dict_1)
dict_1.update({"Lenguaje":"Python","Librerias":["Pandas", "Numpy"]})
print(dict_1)
print("\n")

#Reto Extra

contactos = {}
opcion_menu = 1
import os
while opcion_menu != 0:
    print("AGENDA DE CONTACTOS")
    try:
        opcion_menu = int(input('''
            Elija una opción\n
            1- Buscar contactos
            2- Agregar contacto
            3- Actualizar contacto
            4- Eliminar contacto
            5- Imprimir agenda                 
            0- Finalizar programa                   
            '''))
        if opcion_menu < 0 or opcion_menu > 5:
            raise ValueError
    except ValueError:
        print("Debe ingresar un caracter numérico entre el 0 y el 5\n")
    else:
        if opcion_menu == 1:
            os.system("cls")
            print("BUSCAR CONTACTO")
            opcion_1 = "SI"
            while opcion_1.upper() != "NO":
                try:
                    nombre = str(input("Ingrese el nombre del contacto \n"))
                except ValueError:
                    print("Valor no válido, debe ingresar una cadena de texto\n")
                else:    
                    print(f"{nombre}:", contactos.get(nombre, "No se encontró el contacto solicitado\n"))
                finally:    
                    opcion_1 = str(input("Desea buscar otro contacto? SI/NO\n"))

        elif opcion_menu == 2:
            os.system("cls")
            print("AGREGAR CONTACTO")
            opcion_2 = "SI"
            while opcion_2.upper() != "NO":
                try:
                    nombre = str(input("Ingrese el nombre del contacto\n"))
                    telefono = int(input("Ingrese el número telefonico del contacto\n"))
                    if len(str(telefono)) > 11:
                        raise ValueError
                except ValueError:
                    print('''
                    Valor no válido
                    El nombre de contacto debe ser una cadena de texto
                    El número de telefono debe ser compuesto solo por caracteres numéricos
                    y no contener mas de 11 caracteres\n''')
                else:
                    contactos[nombre] = telefono
                    print(contactos)
                finally:
                    opcion_2 = str(input("Desea agregar otro contacto? SI/NO\n"))
        elif opcion_menu == 3:
            os.system("cls")
            print("ACTUALIZAR CONTACTO")
            opcion_3 = "SI"
            while opcion_3.upper() != "NO":
                try:
                    nombre = str(input("Ingrese el nombre del contacto que desea actualizar\n"))
                    nuevo_nombre = str(input("Ingrese el nuevo nombre del contacto\n"))
                    telefono = int(input("Ingrese el nuevo número telefonico del contacto\n"))
                    if len(str(telefono)) > 11:
                        raise ValueError              
                except ValueError:
                    print('''
                    Valor no válido
                    El nombre de contacto debe ser una cadena de texto
                    El número de telefono debe ser compuesto solo por caracteres numéricos
                    y no contener mas de 11 caracteres\n''')
                else:
                    if nombre in contactos.keys():
                        contactos.pop(nombre)
                        contactos.update({nuevo_nombre:telefono})
                        print(contactos)
                    else:
                        print("El contacto no fue encontrado")
                finally:
                    opcion_3 = str(input("Desea actualizar otro contacto? SI/NO\n"))
        elif opcion_menu == 4:
            os.system("cls")
            print("ELIMINAR CONTACTO")
            opcion_4 = "SI"
            while opcion_4.upper() != "NO":    
                try:
                    nombre = str(input("Ingrese el nombre del contacto que desea eliminar\n"))
                except ValueError:
                    print("Valor no válido, debe ingresar una cadena de texto\n")
                else:
                    if nombre in contactos.keys():
                        contactos.pop(nombre)
                        print(contactos)
                    else:
                        print("El contacto no fue encontrado")
                finally:
                    opcion_4 = str(input("Desea eliminar otro contacto? SI/NO\n"))
        elif opcion_menu == 5:
            os.system("cls")
            print("CONTACTOS\n")
            print(contactos)
            input("presione una tecla para continuar: ")
        elif opcion_menu == 0:
            print("Adios")
        else:
            print("Esta opción no es válida")