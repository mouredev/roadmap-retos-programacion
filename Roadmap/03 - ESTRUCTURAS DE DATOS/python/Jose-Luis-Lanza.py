# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# Listas
# Creacion
frutas = ["manzana", "platano", "naranja"]
print(frutas)

# Acceso
print(frutas[1])

# Inserción
frutas.append("piña")
print(frutas)

# Borrado
frutas.remove("platano")
print(frutas)

# Actualización
print(frutas)
frutas[1] = "cereza"
print(frutas)

# Ordenación
frutas.sort()
print(frutas)

# Tipo
print(type(frutas))

# Tuplas
# Las tuplas son inmutables, lo que significa que no podemos cambiar, añadir o eliminar elementos
# una vez creada la tupla.

# Creacion
personal_data = ("Diego", "Velazco", "d_velazco@gmail.com", "25")
print(personal_data)

# Acceso
print(personal_data[2])

# Ordenación
personal_data = tuple(sorted(personal_data))
print(personal_data)

# Sets
# Creacion
car_brands = {"Mercedes", "Ferrari", "Audi", "Porsche", "Toyota", "Nissan"}
print(car_brands)

# Acceso
# No se puede acceder directamente a un elemento de un set haciendo referencia a un índice o a una clave.

# Inserción
car_brands.add("Pagani")
print(car_brands)

# Borrado
car_brands.remove("Mercedes")
print(car_brands)

# Actualización
# No se puede actualizar directamente un elemento de un set, pero si se puede eliminar y añadir:
car_brands.remove("Toyota")
car_brands.add("Subaru")
print(car_brands)

# Ordenación
# No se puede ordenar

# Diccionarios
# Creacion
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
    }
print(car)

# Inserción
car["motor"] = "V8"
print(car)

# Borrado
del car["motor"]
print(car)

# Actualización
car["year"] = "1969"
print(car)

# Ordenación
# No se puede ordenar

# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.

def my_agenda():

    agenda = {}

    def search(contact_name):
        try:
            print(f"The phone number of {contact_name} is {agenda[contact_name]}")
        except KeyError:
            print(f"The contact {contact_name} doesn't exists in the agenda.")

    def add(contact_name, contact_number):
        if 1 <= len(contact_number) <= 11:
            agenda[contact_name] = contact_number
            print("New contact added!")
        else:
            print("Wrong phone number, please enter a phone number of a maximum size of 11 digits.")

    def update(contact_name, contact_number):
        if contact_name in agenda:
            if 1 <= len(contact_number) <= 11:
                agenda[contact_name] = contact_number
                print("Contact updated successfully!")
            else:
                print("Wrong phone number, please enter a phone number of a maximum size of 11 digits.")
        else:
            print(f"The contact {contact_name} doesn't exists in the agenda.")

    def delete(contact_name):
        try:
            del agenda[contact_name]
            print("Contact deleted successfully!")
        except KeyError:
            print(f"The contact {contact_name} doesn't exists in the agenda.")

    while True:
        option = input("Type an option: search | add | update | delete | show | exit : ").lower().strip()

        if option == "search":
            name = input("Enter contact name: ")
            search(name)

        elif option == "add":
            name = input("Please enter a new contact name: ")
            number = input("Please enter a new phone number: ")
            add(name, number)

        elif option == "update":
            name = input("Enter a contact name to update: ")
            number = input("Enter the new phone number: ")
            update(name, number)

        elif option == "delete":
            name = input("Enter the name of the contact to delete: ")
            delete(name)

        elif option == "show":
            for name, number in agenda.items():
                print(f"Name: {name}, Phone: {number}")

        elif option == "exit":
            print("Closing agenda, goodbye!")
            break

        else:
            print("Wrong name option, try with: search | add | update | delete | show | exit")

my_agenda()
