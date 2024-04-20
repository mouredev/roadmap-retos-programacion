# Listas
my_list = ["Brais", "Bl4ck", "Wolfy", "Visions"]
print(my_list)

my_list.append("Angel") # Inserción
my_list.append("Angel")
print(my_list)

my_list.remove('Angel') # Eliminación
print(my_list)

print(my_list[1]) # Acceso
my_list[1] = 'Cuervillo' # Modificación
print(my_list)

my_list.sort() # Ordenación
print(my_list)

# Tuplas
my_tuple = ('Moure', 'Dev', '@mouredev', '36')
print(my_tuple[1])# Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(type(my_tuple))
print(my_tuple)

# Sets
my_set = {'Moure', 'Dev', '@mouredev', '36'}
print(my_set)
my_set.add('angel@gmail.com') # Inserción
my_set.add('angel@gmail.com')
my_set.remove('Moure') # Eliminación
print(my_set)
#print(my_set[0])
my_set = set(sorted(my_set)) # No se puede ordenar, set no es una estructura ordenada
print(my_set)
print(type(my_set))

# Diccionarios
my_dict: dict = {
   'name':'Moure',
   'surname':'Dev',
   'alias':'@mouredev',
   'edad':'36'
   }
my_dict['email'] = 'mouredev@gmail.com' # inserción
print(my_dict)
del my_dict['surname'] # Eliminación
print(my_dict)
print(my_dict['name']) # Acceso
my_dict['edad'] = '37' # Modificación
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación 
print(my_dict)
print(type(my_dict))

"""
EXTRA
"""

def my_agenda():

   agenda = {}

   def insert_contact():
      phone = input("Introduce el teléfono del contacto: ")
      if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
         agenda[name] = phone
      else:
         print("Debes introducir un número de teléfono con menos de 11 dígitos.")

   while True:

      print("")
      print("1. Buscar contacto")
      print("2. Insertar contacto")
      print("3. Actualizar contacto")
      print("4. Eliminar contacto")
      print("5. Salir")

      option = input("\nSelecciona una opción: ")

      match option:
         case "1":
            name = input("Introduce el nombre del contacto a buscar: ")
            if name in agenda:
               print(f"El número de teléfono de {name} es {agenda[name]}")
            else:
               print(f"El contacto {name} no existe")
         case "2":
            name = input("Introduce el nombre del contacto a insertar: ")
            insert_contact()
         case "3":
            name = input("Introduce el nombre del contacto a actualizar: ")
            if name in agenda:
               insert_contact()
            else:
               print(f"El contacto {name} no existe")
         case "4":
            name = input("Introduce el nombre del contacto a eliminar: ")
            if name in agenda:
               del agenda[name]
            else:
               print(f"El contacto {name} no existe")
         case "5":
            print("Saliendo de la agenda.")
            break
         case _:
            print("Opción no válida, Elige una opción del 1 al 5.")


my_agenda()