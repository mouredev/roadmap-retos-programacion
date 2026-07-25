"""
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
  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
  *   (o el número de dígitos que quieras)
  * - También se debe proponer una operación de finalización del programa.
"""

### lsita ###

""" my_list = ["Juan", "Rodriguez", "34", "juserdev"]
print(my_list)

my_list.append("laura")
print(my_list)

my_list.remove("laura")
print(my_list)

my_list_copy = my_list.copy() # Esta funcion crea un acopia de la variable original
my_list_copy.append("laura")
print(my_list_copy)

print(my_list.count("hola")) # esta funcion cuanta cuntas veces se repite lo que esta dentro de los parentesis 
print(my_list.count("34"))

my_list.pop() # Elemina el ultimo indice de la lista
print(my_list)

my_list.remove("Juan") # Elimna el elemento que tenga escrito dentro de los paretesis
print(my_list)

my_list.reverse() # devuele la listra de tras pa lante
print(my_list)

print(my_list[0]) # selecciona el valor en el indice declarado entre corchetes

edad, nombre = my_list # destructurar

print(edad)
print(nombre)

print(my_list)

my_list.append("juan")
print(my_list)

my_list.insert( 2, "juserdev") # agrega un valor en la posicion indicada
print(my_list)

my_list.sort() # ordena
print(my_list)

my_list.clear() # con esta funcion limpa la lista
print(my_list)

### Tupla ###

my_tupla = (34, 1.70, "juan", "rodriguez", "juan")
print(my_tupla)

print(my_tupla.index(34)) # Busca y nos devuelve el indice del valor dentro de los parentesis
print(my_tupla.count("juan"))
my_tupla = list(my_tupla) # lo transforme en lista para poder modificarlo
my_tupla[4] = "juserdev"
print(type(my_tupla))
print(my_tupla)
my_tupla = tuple(my_tupla) # lo transforme en tupla nuevamente
print(type(my_tupla))
print(my_tupla)

### Set

my_set = {"juan", "rodriguez", 34, 1.70}
print(type(my_set))
print(my_set) # muestra el contenido en desorden

my_set.add("juserdev") # Agrega contenido al set
print(my_set) 
print(len(my_set)) # esta funcion sirve con todos para contantar la cantidad de elementos que hay

print("juserdev" in my_set) # confima si existe el elemento #-> true
print("juserdeve" in my_set) # confima si existe el elemento #-> false

my_set.remove("juserdev")
print(my_set)

my_other_set = {"juserdev", "colombia"}

my_set = my_set.union(my_other_set).union({"python"})
print(my_set)

# my_set.clear() # -> elimina el contenido del set
# print(my_set) 
# del my_set # -> borra el set


### dictcionary

my_dict = {
  "nombre": "juan",
  "apellido": "rodirguez",
  "edad": 34,
  "lenguajes": {
    "python",
    "typescript",
    "css"
  }
}

print(my_dict)
print(my_dict["nombre"])

my_dict["nombre"] = "Sebastian"
print(my_dict)
print(my_dict["nombre"])
# print(my_dict[1])

my_dict["calle"] = "monda" # agregue una clave llamada calle y le puse de nombre monda
print(my_dict)

print( "Sebastian" in my_dict)
print( "nombre" in my_dict) # Busca por clave y no por valor

del my_dict["calle"] # Borra un elemento especifico
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values()) """


### Dificultad extra

def my_agenda():
  
  agenda = {}

  def insert_contact():
    phone = input("Escriba el numero de contacto: ")
    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
      agenda[name] = phone
    else:
      print("Debes introducir un numero de telefono con maximo 11 digitos")
    
  while True:

    print("")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Mostrar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

    option = input("\nSelecciona una option: ")

    match option:
      case "1":
        name = input("Intruce el nombre del contacto a buscar: ")
        if name in agenda:
          print(f"El numero de telefono de {name} es {agenda[name]}")
        else:
          print(f"El contacto {name} no existe")
      case "2":
        name = input("Introduce el nombre del contacto: ")
        insert_contact()
      case "3":
        name = input("Introduce el nombre del contacto a actualizar: ")
        if name in agenda:
          insert_contact()
        else:
          print(f"El contacto {name} no existe.")
      case "4":
        print(agenda)
      case "5":
        name = input("Introduce el nombre del contact a eliminar: ")
        if name in agenda:
          del agenda[name]
        else:
          print(f"El contacto {name} no existe")
      case "6":
        print("Saliendo de la agenda.")
        break
      case _:
        print("Opcion no valida. Elige una opcion del 1 al 5.")

my_agenda()