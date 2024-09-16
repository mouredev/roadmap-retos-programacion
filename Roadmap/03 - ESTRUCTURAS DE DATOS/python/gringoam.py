# Listas
my_list: list = ["Brais", "Bl4ck", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor")  # Inserción
my_list.append("Castor")
print(my_list)
my_list.remove("Brais")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Cuervillo"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[0])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
my_set.add("mouredev@gmail.com")  # Inserción
my_set.add("mouredev@gmail.com")
print(my_set)
my_set.remove("Moure")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
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

"""
Extra
"""
#Agenda

agenda={}

def insert_contact():
    phone = input("Introduce el teléfono del contacto: ")
    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
        agenda[nombre] = phone
    else:
        print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")
  
       

while True:
     print("Agenda:")
     print("Ingrese operaci+on a realizar")
     print("1) Aregar contacto.")
     print("2) Borrar contacto.")
     print("3) Buscar contacto.")
     print("4) Actualizar contacto.")
     print("5) Salir.")

     op=input()
     match op:
        case "1":
          nombre=input("Ingrese nombre del contacto: ")
          insert_contact()
        case "2":
         nombre=input("Ingrese nombre del contacto: ")
         if nombre in agenda:
            del agenda[nombre]
            print(f"El contacto {nombre} fue eliminado")
         else:
              print("El contacto no existe")
        case "3":
         nombre=input("Ingrese nombre del contacto: ")
         if nombre in agenda:
           print(f"Contacto  encontrado nombre: {nombre} teléfono: {agenda[nombre]} ")
         else:
              print("El contacto no existe")
        case "4":
         nombre=input("Ingrese nombre del contacto: ")  
         if nombre in agenda:
           insert_contact()
         else:
           print("El contacto no existe")  
        case "5":
          break

print(agenda)

