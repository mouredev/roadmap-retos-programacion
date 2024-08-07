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

# Creación de estructuras de datos
# List
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Insertion
my_list.remove(1)  # Deletion
my_list[0] = 7  # Update
my_list.sort()  # Sorting

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Dictionary
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
del my_dict['one']  # Deletion
my_dict['two'] = 22  # Update
sorted_dict = dict(sorted(my_dict.items()))  # Sorting

# Set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Insertion
my_set.remove(1)  # Deletion
# Update is not applicable for sets as they only contain unique values
my_sorted_set = sorted(my_set)  # Sorting


# Extra difficulty
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactBook:
    def __init__(self):
        self.contacts = []

    def insert(self, name, phone):
        self.contacts.append(Contact(name, phone))

    def delete(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def update(self, name, phone):
        for c in self.contacts:
            if c.name == name:
                c.phone = phone

    def search(self, name):
        for c in self.contacts:
            if c.name == name:
                return c
        return None


def main():
    book = ContactBook()

    while True:
        operation = input("Enter operation (insert, delete, update, search, quit): ")

        if operation == "quit":
            break

        if operation == "insert":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            if not phone.isdigit() or len(phone) > 11:
                print("Invalid phone number")
                continue
            book.insert(name, phone)

        elif operation == "delete":
            name = input("Enter name: ")
            book.delete(name)

        elif operation == "update":
            name = input("Enter name: ")
            phone = input("Enter new phone: ")
            if not phone.isdigit() or len(phone) > 11:
                print("Invalid phone number")
                continue
            book.update(name, phone)

        elif operation == "search":
            name = input("Enter name: ")
            contact = book.search(name)
            if contact:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("Contact not found")


if __name__ == "__main__":
    main()
