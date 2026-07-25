"""
/*
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
 */
"""
""" Descomentar si se quieren ver resultados. Comentado no molesta a la ejecucion de la agenda
# Listas
mi_lista = list() #Contructor
segunda_lista = [] #Declaracion directa (Se podrian añadir directametne los elementos de la lista)

segunda_lista = ["Manolo", 57, "Visual Basic"]
print(type(segunda_lista))

# Tuplas
mi_tupla = tuple() #Contructor
segunda_tupla = () #Declaracion directa (Se podrian añadir directametne los elementos de la lista)

mi_tupla = (1, 45, 23, 57, 42)
print(type(mi_tupla))

# Set
mi_set = set() #Contructor
segundo_set = {} #Para que esto sea un set y no un diccionario, hay que poner sus elementos como se indica abajo

segundo_set = {"Hola papa", "Quiero ser developer", 12, "Sigue soñando"}
print(type(segundo_set))

# Diccionario
mi_dict = dict() #Contructor
segundo_dict = {} #Para que esto no sea un set sino un diccionario, hay que poner sus elementos como se indica abajo

segundo_dict = {
  "Saludo": "Hola papa",
  "Objetivo": "Quiero ser developer",
  "Tiempo": 12, "Golpe": "Sigue soñando"}
print(type(segundo_dict))

#Funciones de inserción

segunda_lista.insert(0, "Patata")
print(segunda_lista)
segunda_lista.append("puerro")
print(segunda_lista)
segunda_lista[1] = "Me' Colao"
print(segunda_lista)
mi_lista = [1, 45, 23, 57, 42]

#Funciones de borrado

segunda_lista.remove("puerro")
print(segunda_lista)
print(segunda_lista.pop())
print(segunda_lista)
del segunda_lista
#print(segunda_lista) da error porque ya no existe segunda_lista

#Funciones de ordenado

mi_lista.sort()
print(mi_lista)
mi_lista.reverse()
print(mi_lista)
"""

"""
DIFICULTAD EXTRA (opcional):
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

agenda = list()

#Crear aqui el menu de la agenda
def menu():
  print("-------------------")
  print("Agenda de contactos")
  print(agenda)
  print("Elija una opcion")
  print("-------------------")
  opcion = input("""  1 Añadir contacto
  2 Modificar contacto
  3 Buscar contacto
  4 Eliminar contacto
  5 Cerrar la agenda (se perderan los contactos)
  Su opcion aqui:                 
  """)
  if (opcion == "1"):
    add_contact()
  elif (opcion == "2"):
    edit_contact()
  elif (opcion == "3"):
    search_contact()
  elif (opcion == "4"):
    delete_contact()
  elif (opcion == "5"):
    print("Hasta otra!")
    print("__________________________________________________________")
    exit()
  else: 
    print("Elije una opcion valida")
    menu()

def add_contact():
  name = input("Introduce un Nombre: ")
  number = input("Introduce un Telefono: ")
  contacto = {
    "nombre": name,
    "telefono": number
  }
  agenda.append(contacto)
  print(name, "a sido añadido a tus contactos")
  menu()

def edit_contact():
  i = input("¿Que contacto quieres editar?: ")
  contact = next((contact for contact in agenda if contact["nombre"] == i), None)
  if contact is None:
    print("No se encontró el contacto")
    menu()

  confirmado = input("Usted va a editar el contacto elegido, confirme pulsando enter")
  if (confirmado == ""):
    new_name = input("Introduce el nuevo Nombre: ")
    new_number = input("Introduce el nuevo numero: ")
    
    for i, old_contact in enumerate (agenda):
      if old_contact == contact:
        agenda[i] = {"nombre": new_name, "telefono": new_number}
        print("Se a actualizado el contacto correctamente")
        break
      else: print("Hubo algun error")  

  else:
    print("Regresando al menu principal")
  menu()    

def search_contact():
  contact = input("Introduce el nombre a buscar: ")
  found = False
  for asked_contact in agenda:
      if asked_contact["nombre"] == contact:

        print("-------------------------------------")
        print("Nombre:", asked_contact["nombre"])
        print("Telefono:", asked_contact["telefono"])
        print("-------------------------------------")
        
        found = True
        break
  if not found:
    print("Contacto no encontrado")
  menu()

  

  menu()

def delete_contact():
  contact = input("¿Que contacto desea eliminar?: ")

  confirmado = input("Usted va a eliminar el contacto elegido, confirme pulsando enter")
  if (confirmado == ""):    
    for i, del_contact in enumerate (agenda):
      if del_contact["nombre"] == contact:
        del agenda[i]
        print(agenda)
        print(f"{contact} ha sido eliminado")
        break
      else: print("Hubo algun error")  

  else:
    print("Regresando al menu principal")
  menu()

menu()
