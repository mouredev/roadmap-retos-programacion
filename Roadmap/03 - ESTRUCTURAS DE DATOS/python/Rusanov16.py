"""
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
  los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
  (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""

#*-------------------------------------------------------------------------------------------------------------#

"""
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

print("-----------------------------------------------------------------------------------------------------")
#Listas
print("LISTAS")
lista = [1,2,3,4]
print(f"Esto es una lista = {lista}")

#Inserción
lista.append(3)
print(f"Con la función append se añaden nuevos elementos al final de la lista {lista}")

#Borrado
lista.remove(1)
print(f"Con la función remove se eliminan el valor de los elementos que esten dentro de la lista {lista}")

#Actualizacion
lista[2] = 20
print(f"Para actualizar valores de la lista hay que indicar con [el indice que se quiere actualizar] {lista}")

#Ordenacion
lista.sort()
print(f"Para ordenar los valores de los elementos de la lista, se utiliza la función sort {lista}")

print("-----------------------------------------------------------------------------------------------------")

#Set
print("SET")
#Forma uno: Usando la función set()
set_forma_uno = set([1,2,4,5])
print(f"Estos es un set: {set_forma_uno}")
print(f"Una forma de hacer un set es con la función set(): {set_forma_uno}")
#Forma dos: Usando {}
set_forma_dos = {1,2,3,4,5}
print(f"Otra forma de hacer un set es definiendo con: {set_forma_dos}")
#IMPORTANTE: Los elementos de un set deben ser inmutables.

#Inserccion
set_forma_uno.add(8) #Forma uno
set_forma_dos.add(66) #Forma dos
print(f"Para insertar elementos dentro del set, se usa la función add(): {set_forma_uno} y {set_forma_dos}")

#Borrado
set_forma_uno.remove(8) #Forma uno
set_forma_dos.remove(66) #Forma dos
print(f"Una forma de eliminar elementos dentro del set es usando la función remove(): {set_forma_uno} y {set_forma_dos}")

print("-----------------------------------------------------------------------------------------------------")

#Tuplas
print("TUPLAS")
tupla_uno = (1,2,4) #Forma 1
tupla_dos = 1,2,3,4 #Forma 2
print(f"Esto es una tupla {tupla_uno}")
#IMPORTANTE: Los elementos de un set deben ser inmutables.
print("-----------------------------------------------------------------------------------------------------")

#Diccionario
print("DICCIONARIO")
dic_uno = {'Fruta':'Manzana',
           'Hortaliza':'Zanahoria'}
print(f"Esto ez un diccionario: {dic_uno}")

#Actualizar
dic_uno['Fruta'] = "Durazno" 
print(f"Para actualizar valores del diccionario hay que indicar con [elemento que se quiere actualizar]: {dic_uno}")

#*-------------------------------------------------------------------------------------------------------------#
"""
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
  los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
  (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""
#*-------------------------------------------------------------------------------------------------------------#

agenda_contactos = {
    'Carlos': '10985565324',
    'Juan' : '18709253628'}

# INSERTAR CONTACTO
def insertar_contactos():
    nombre = input("Indique su nombre: ")
    telefono = input("Indique su número de teléfono: ")

    if len(telefono) <= 11 and telefono.isdigit() and int(telefono) >= 0:
        agenda_contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado correctamente.")
    else:
        print("Número de teléfono inválido. Debe ser numérico y tener hasta 11 dígitos.")

# BUSCAR CONTACTO
def buscar_contacto():
    nombre = input("Indique el nombre del contacto: ")
    if nombre in agenda_contactos:
        print(f"Contacto {nombre}: {agenda_contactos[nombre]}")
    else:
        print(f"El contacto {nombre} no se encontró en la agenda.")

# ACTUALIZAR CONTACTO
def actualizar_contactos():
    nombre = input("Indique el nombre del contacto que desea actualizar: ")
    if nombre in agenda_contactos:
        nuevo_telefono = input("Indique el nuevo número de teléfono: ")

        if len(nuevo_telefono) <= 11 and nuevo_telefono.isdigit() and int(nuevo_telefono) >= 0:
            agenda_contactos[nombre] = nuevo_telefono
            print(f"Teléfono de {nombre} actualizado correctamente.")
        else:
            print("Número de teléfono inválido. Debe ser numérico y tener hasta 11 dígitos.")
    else:
        print(f"El contacto {nombre} no se encontró en la agenda.")

# ELIMINAR CONTACTOS
def eliminar_contactos():
    nombre = input("Indique el nombre del contacto que desea eliminar: ")
    if nombre in agenda_contactos:
        del agenda_contactos[nombre]
        print(f"El contacto {nombre} ha sido eliminado correctamente.")
    else:
        print(f"El contacto {nombre} no se encontró en la agenda.")

menu = True

while menu:
    print("---------------------------------------------------")
    print("BIENVENIDOS A LA AGENDA DE CONTACTOS")
    print("---------------------------------------------------")
    print("¿QUÉ PROCESO QUIERE REALIZAR?")
    print("-----------------------------")
    print("|1.| BUSCAR CONTACTO         |")
    print("|2.| CREAR CONTACTO          |")
    print("|3.| ACTUALIZAR CONTACTO     |")
    print("|4.| ELIMINAR CONTACTO       |")
    print("|5.| VER AGENDA DE CONTACTOS |")
    print("|6.| SALIR                   |")

    opcion = input("Indique la opción que desea realizar: ")

    if opcion == "1":
        buscar_contacto()
    elif opcion == "2":
        insertar_contactos()
    elif opcion == "3":
        actualizar_contactos()
    elif opcion == "4":
        eliminar_contactos()
    elif opcion == "5":
        print(f"Agenda de Contactos = {agenda_contactos}")
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")



  
  
#"-------------------------------------------------------------------------------------------"#

