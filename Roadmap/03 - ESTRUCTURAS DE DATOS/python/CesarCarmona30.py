'''
  ESTRUCTURAS DE DATOS
'''

# Listas
my_list = [0, 5, 6, 2, 7, 2, 6, 8, 9, 4, 3, 3]
print(f'Mi lista = {my_list}') 
my_list.append("texto") # Inserción
my_list.append(True) # Inserción
print(f'Mi lista = {my_list}')
my_list.remove(True) # Borrado
print(f'Mi lista = {my_list}')
my_list[-1] = 10 # Actualización
print(f'Mi lista = {my_list}')
my_list.sort() # Ordenación
print(f'Mi lista = {my_list}')


# Tuplas
my_tuple = ("Carne", "Verduras", "Frutas", "Legumbres")
print(f"Mi tupla: {my_tuple}")
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(f"Mi tupla: {my_tuple}")
print(type(my_tuple))

# Sets
my_set = {"Mexico, España, Argentina, Colombia, Chile, Peru"}
print(f"Mi set: {my_set}") 
my_set.add("Brasil") # Inserción
print(f"Mi set: {my_set}")  
my_set.remove("Brasil") # Borrado
print(f"Mi set: {my_set}") 

# Diccionario
my_dict = {
  "name": "César",
  "surname": "Carmona",
  "age": "19",
  "country": "Mexico",
  "city": "Guadalajara"
}
print(f"Mi diccionario: {my_dict}")
my_dict["gender"] = "Male" # Inserción
print(f"Mi diccionario: {my_dict}")
del my_dict["gender"] # Borrado
print(f"Mi diccionario: {my_dict}")
my_dict["city"] = "Mexico City" # Actualización
print(f"Mi diccionario: {my_dict}")
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(f"Mi diccionario: {my_dict}")


'''
  EXTRA
'''

def my_contacts():

  agenda = {}
  name = ''

  def insert_contact():
    number = input("Introduce el número: ")
    if number.isdigit() and len(number) > 0 and len(number) <= 10:
      agenda[name] = number
    else:
      print("Introduce un número válido de 10 dígitos.")

  while True:

    print("\n - AGENDA TELEFÓNICA -\n")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Listar contactos")
    print("6. Salir\n")

    option = input("Selecciona una opción: ")

    match option:
      case "1":
        name = input("Introduce el nombre del contacto a buscar: ").lower()
        if name in agenda:
          print(f"{name} - {agenda[name]}")
        else:
          print(f"{name} no existe.")
      case "2":
        name = input("Introduce el nombre del nuevo contacto: ").lower()
        insert_contact()
        print(f"{name} creado.")
      case "3":
        name = input("Introduce el nombre del contacto a actualizar: ").lower()
        if name in agenda:
          insert_contact()
          print(f"{name} actualizado.")
        else:
          print(f"{name} no existe.")
      case "4":
        name = input("Introduce el nombre del contacto a a eliminar: ").lower()
        if name in agenda:
          del agenda[name]
          print(f"{name} eliminado.")
        else:
          print(f"{name} no existe.")
      case "5":
        if agenda:
          print('Contactos - Números')
          for contact, phone in agenda.items():
            print(f'{contact} - {phone}')
        else:  
          print('Agenda vacía, agrega nuevos contactos.')
      case "6":
        print("Saliendo de la agenda.")
        break
      case _:
        print("Elige una opción del 1 al 5.")

my_contacts()