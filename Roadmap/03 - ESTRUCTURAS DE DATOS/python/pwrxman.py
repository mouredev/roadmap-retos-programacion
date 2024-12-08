"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""
# Creando LISTA Usando Brackets
my_list: list = ["Brais", "Black", 4 , True, 3.1416, ["a", "b", "c", "d"]]   

# Creando LISTA Using the list() constructor to make a List:
thislist = list(("xerox", "tomas", "apple", "banana", "cherry")) # note the double round-brackets
print(thislist)                    
print(my_list)

empty_list = list() # this is an empty list, no item in the list

my_list.append("Castor")  # Inserción
print(my_list)
my_list.remove("Brais")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso al segundo elemento, recuerda que empieza en cero
my_list[1] = "Cuervillo"  # Actualización
print(my_list)

thislist.sort()
print(thislist)

lst = ['item1','item2','item3', 'item4', 'item5']
f_item, s_item, t_item, *rest = lst  # Hace un emparejamiento de cada nombre de estos con el correspondiente elemento de la lista
                        # El *rest crea una lista con los elementos restantes 
print(f_item)     # item1
print(t_item)    # item2
print(s_item)     # item3
print(rest)           # ['item4', 'item5']
print(type(my_list))


# Creando TUPLE con parentesis
my_tuple: tuple = ("Andrei", "Med", "@amed", "66")
print(my_tuple)

# Creando TUPLE usando el constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))


# Creando un SET usando llaves {}
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)

# Creando un SET usando e constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 


my_set.add("mouredev@gmail.com")  # Inserción
print(my_set)
my_set.remove("Moure")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
print(type(my_set))

# Creando un Diccionario usando {}
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
print(my_dict)

# Creating a Dictionary Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


my_dict["email"] = "mouredev@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))


# Diccionario anidado
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

print(child1)
print(child2)
print(child3)
print(myfamily)


"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

agenda = {}

def searching():
    print("\nBuscando contactoF")
    nombre = input("Dime el nombre a Buscar: ")
    if nombre in agenda.keys():
        print(f"Encontre el nombre {nombre} solicitado y su teléfono es {agenda[nombre]}\n")
      
    else:
        print(f"No existe el contacto {nombre}\n")    


def adding():
    print("\nAñadiendo contactoF")
    nombre = input("Dime el nombre del nuevo contacto: ")
    if nombre in agenda.keys():
        print(f"Ya existe un contacto con el nombre -> {nombre} y telefono {agenda[nombre]}\n\n")
              
    else:
        # print(f"Nombre no Duplicado  ============>  nombre = {nombre}")
        tel = input("Introduce el número telefónico del contacto: ")
        if tel.isdigit() and len(tel) > 0 and len(tel) <= 11:
            agenda[nombre] = tel
            print(f"Se añadió nuevo contacto nombre: {nombre} y telefono {agenda[nombre]}\n\n")

        else:
            print("Debes introducir un teléfono solo con números y un máximo de 11 dígitos.\n\n")   

def updating():
    print("Modificar contactoF")
    nombre = input("Dime el nombre del contacto que deseas actualizar: ")
    if nombre in agenda.keys():
        tel = input("Dime el nuevo telefono  para este contacto: ")
        agenda[nombre] = tel
        print(f"Se actualizó el contacto {nombre} con el telefono {agenda[nombre]}\n\n")
    else:
        print(f"No existe el contacto {nombre}\n")

def deleting():
    print("Eliminando contactoF")      
    nombre = input("Dime el nombre del contacto que deseas eliminar: ")
    if nombre in agenda.keys():
        agenda.pop(nombre)
        print(f"Se eliminó el contacto {nombre}")
    else:
        print(f"No existe el contacto {nombre}\n")

def my_agenda():

    operacion = "0"
    
    while operacion != "5": 
        print("1. Buscar Contacto")
        print("2. Añadir Nuevo Contacto")
        print("3. Modificar Contacto")
        print("4. Eliminar Contacto")
        print("p. Genrra Lista de Contactos")
        print("5. Terminar")

        operacion = input("Seleccione la operación deseada: ")

        match operacion:
          case "1":
              searching()
          
          case "2":
              adding()
          
          case "3":
              updating()

          case "4":
              deleting()
          
          case "p":
              for x, y in agenda.items():
                  print(x, y) 

          case "5":
            print("Terminar")  
            break

          case _:
            print("Opcion seleccionada NO válida.")               

my_agenda()

