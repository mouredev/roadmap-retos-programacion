# 03 ESTRUCTURAS DE DATOS
# Mónica Vaquerano
# https://monicavaquerano.dev
import os, time

os.system("clear")
"""
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
"""
print("\nEstructuras de datos (Data Structures):\n")
# Lists
lista = [1, 2, 3, 4, 5]
print(f"- List: esta es una lista: {lista}")
# Tuples
tupla = (1, 2, "hola")
print(f"- Tuple: este un tuple: {tupla}")
# Sets o conjuntos
conjunto = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(
    f'- Set: este es un ejemplo de set("apple", "orange", "apple", "pear", "orange", "banana") = {conjunto}'
)
# Dictionaries
diccionario = {"monica": 123, "tanya": 456}
print(f"- Dictionary: este es un ejemplo de dictionary -> {diccionario}")


"""
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

print("\nOperaciones de inserción, borrado, actualización y ordenación:")


# Lists o listas
print("\n- En lists o listas:")

# list.append(x)
print(
    f"\nlist.append(x):\npara agregar une elemento a una lista usamos lista.append(x): {lista}",
    end=" ",
)
lista.append(6)
print(f"-> lista.append(6) = {lista}")
# list.extend(iterable)
print(
    f"\nlist.extend(iterable):\npara extender con más elementos usamos list.extend(iterable): {lista}",
    end=" ",
)
lista.extend([7, 8, 9])
print(f"-> lista.extend([7, 8, 9]) = {lista}")
# list.insert(i, x)
print(
    f"\nlist.insert(i, x):\npara insertar un elemento usamos list.insert(i, x): {lista}",
    end=" ",
)
lista.insert(0, 5)
print(f"-> lista.insert(0, 5) = {lista}")
# list.remove(x)
print(
    f"\nlist.remove(x):\npara remover el primer elemento que coincida con x usamos list.remove(x): {lista}",
    end=" ",
)
lista.remove(5)
print(f"-> lista.remove(5) = {lista}")
# list.pop([i])
print(
    f"\nlist.pop([i]):\npara remover un elemento según su posición en la lista usamos list.pop([i]): {lista}",
    end=" ",
)
lista.pop(0)
print(f"-> lista.pop(0) = {lista}")
# list.clear()
print(
    f"\nlist.clear():\npara remover todos los elementos en la lista usamos list.clear(): {lista}",
    end=" ",
)
lista.clear()
print(f"-> lista.clear() = {lista}")

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

# list.index(x[, start[, end]])
print(
    f"\nlist.index(x[, start[, end]]):\npara buscar el índice de un elemento, desde una posición hasta otra o el final en la lista usamos list.index(x[, start[, end]]):\n{fruits}",
    end=" ",
)
print(f"-> fruits.index('banana', 4) = {fruits.index('banana', 4)}")

# list.count(x)
print(
    f"\nlist.count(x):\npara saber el número de veces que x aparece en la lista usamos list.count(x): {fruits}",
    end=" ",
)
print(f"-> fruits.count('apple') = {fruits.count('apple')}")
# list.sort(*, key=None, reverse=False)
print(
    f"\nlist.sort(*, key=None, reverse=False):\nordenar la lista usamos list.sort(*, key=None, reverse=False): {fruits}",
    end=" ",
)
fruits.sort()
print(f"-> fruits.sort() = {fruits}")
# list.reverse()
print(
    f"\nlist.reverse():\npara revertir la lista usamos list.reverse(): {fruits}",
    end=" ",
)
fruits.reverse()
print(f"-> fruits.reverse() = {fruits}")
# list.copy()
print(
    f"\nlist.copy():\npara hacer una copia superficial de la lista usamos list.copia():\nfruits = {fruits}",
    end=" ",
)
copia = fruits.copy()
print(f"-> copia = fruits.copy() -> copia = {copia}")


# Tuples o tuplas
print("\n- En tuples o tuplas:")
print(
    "Una tupla no admite cambios y por lo tanto, es inmutable. Solo puede ser cambiada si se convierte a lista y devuelta a tuple."
)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(
    f"x = ('apple', 'banana', 'cherry')\ny = list(x)\ny[1] = 'kiwi'\nx = tuple(y)\nx = {x}"
)


# Sets o conjuntos
print("\n- En sets o conjuntos:")
print(
    "Los items de un Set son inmutables, pero se pueden remover items y agregar nuevos."
)

#  Add
periodic_table = set()
metals = ("Fe", "Mg", "Au", "Au", "Zn")
periodic_table.add(metals)
non_metals = ("C", "H", "O", "F", "Cl")
periodic_table.add(non_metals)
print(
    f"\nset.add(x): agrega un item a un set.\nperiodic_table = set()\nmetals = ('Fe', 'Mg', 'Au', 'Au', 'Zn')\nperiodic_table.add(metals)\nnon_metals = ('C', 'H', 'O', 'F', 'Cl')\nperiodic_table.add(non_metals)"
)
print(f"periodic_table = {periodic_table}")

# Update
mylist = ["kiwi", "orange"]
periodic_table.update(mylist)
print(
    f"\nset.update(iterable): agrega cualquier iterable a un set.\nmylist = ['kiwi', 'orange']\nperiodic_table.update(mylist)"
)
print(f"periodic_table = {periodic_table}")

# Remove o discard
thisset = {"apple", "banana", "cherry", "mango"}
thisset.remove("banana")
print(
    f"\nset.remove(x) o discard(x): remueve cualquier item de un set.\nthisset = set('apple', 'banana', 'cherry', 'mango')\nthisset.remove('banana')"
)
print(f"thisset = {thisset}")

# Pop
x = thisset.pop()
print(
    f"\nset.pop(): este método remueve un item al azar.\nthisset.pop() = {x}\nthisset = {thisset}"
)

# Clear
thisset.clear()
print(f"\nset.clear(): este método vacía el set.\nthisset.clear()\nthisset = {thisset}")

# Del
del thisset
try:
    print(thisset)
except NameError:
    print(
        "\ndel set: este método elimina por completo el set.\ndel thisset\nprint(thisset) -> genera un error ya que 'thisset' ya no existe"
    )


# Dictionaries o diccionarios
print("\n- En dictionaries o diccionarios:")

# Update
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(
    f"\ndict.update(k, v): se puede cambiar un valor específico solo refiriéndose a su key o usando update(key, valor).\nthisdict = {thisdict}\nthisdict['year'] = 2018"
)
thisdict["year"] = 2018
print(f"thisdict = {thisdict}")
thisdict.update({"year": 2020})
print("thisdict.update({'year'': 2020})")
print(f"thisdict = {thisdict}")

# Add
print(
    f"\ndict.add(k, v): se puede agregar un item usando un nuevo valor de key y asignándole un valor o usando update(key, valor) de igual forma.\nthisdict['color'] = 'red' o ",
    end="",
)
print("thisdict.update({'color': 'red'})")
thisdict.update({"color": "red"})
print(f"thisdict = {thisdict}")

# Remove
# Pop
print(
    f"\ndict.pop(k): remueve el item con esa key específica.\nthisdict = {thisdict}\nthisdict.pop('model')",
)
thisdict.pop("model")
print(f"thisdict = {thisdict}")

# Popitem
print(
    f"\ndict.popitem(): remueve el item con úlitma key agregada.\nthisdict = {thisdict}\nthisdict.popitem()",
)
thisdict.popitem()
print(f"thisdict = {thisdict}")

# del dict[k]
print(
    f"\ndel dict[k]: remueve el item con esa key específica.\nthisdict = {thisdict}\ndel thisdict('year')",
)
del thisdict["year"]
print(f"thisdict = {thisdict}")

# del dict
del thisdict
try:
    print(thisdict)
except NameError:
    print(
        "\ndel dict: este método elimina por completo el diccionario.\ndel thisdict\nprint(thisdict) -> genera un error ya que 'thisdict' ya no existe"
    )


"""
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""


contacts = {
    "monica": {"phone": 1234567890, "address": "avenida 123"},
    "ana": {"phone": 1234567890, "address": "calle 123"},
}


def showContacts():
    os.system("clear")
    print(f"{'========================= Contact List =========================':^60}")
    if len(contacts) == 0:
        print("\nContact list is empty.")
    else:
        title = f"|{'Name':^20}|{'Phone':^20}|{'Address':^20}|"
        print(title)
        for key, value in contacts.items():
            print(f"| {key.capitalize():<19}", end="|")
            for subvalue in value.values():
                print(f" {str(subvalue).capitalize():<19}", end="|")
            print()
        print(
            f"{'================================================================':^60}"
        )


def searchContact():
    os.system("clear")
    print("=== Search ===")
    nameInput = input("Input contact's name: > ").strip().lower()
    if nameInput in contacts.keys():
        print("\n--- Contact Info ---")
        print(
            f"Name: {nameInput.capitalize()}\nPhone: {contacts[nameInput]['phone']}\nAddress: {contacts[nameInput]['address'].capitalize()}"
        )
    else:
        print("\nContact not found.")


def addContact():
    os.system("clear")
    print("=== Add ===")
    name = input("Input contact's name: > ").strip().lower()
    while True:
        try:
            phone = int(input("Input contact's phone: > "))
            break
        except ValueError:
            print("Phone must be a number.")
    address = input("Input contact's address: > ").strip().lower()
    if name not in contacts.keys():
        if len(str(phone)) <= 11:
            contacts[name] = {"phone": phone, "address": address}
            print("\nContact has been successfuly added.")
        else:
            print("\nPhone number can't have more than 11 digits.")
    else:
        print("\nContact already exists.")


def updateContact():
    os.system("clear")
    print("=== Update ===")
    name = input("Input contact's name: > ").strip().lower()
    if name in contacts.keys():
        print(f"\n--- {name.capitalize()}'s new info ---")
        while True:
            try:
                newPhone = int(input("Update phone: > "))
                break
            except ValueError:
                print("Phone must be a number.")
        newAddress = input("Update address: > ").strip().lower()
        if len(str(newPhone)) <= 11:
            contacts[name] = {"phone": newPhone, "address": newAddress}
            print("\nContact successfully updated.")
        else:
            print("\nPhone number can't have more than 11 digits.")
    else:
        print("\nContact not found.")


def deleteContact():
    os.system("clear")
    print("=== Delete ===")
    if len(contacts) == 0:
        print("\nContact list is empty.")
    else:
        name = input("Input contact's name: > ").strip().lower()
        if name in contacts.keys():
            sureInput = (
                input(
                    f"\nAre you sure you want to delete {name.capitalize()}'s contact info? y/n? > "
                )
                .strip()
                .lower()
            )
            if sureInput[0] == "y":
                del contacts[name]
                print(f"\n{name.capitalize()}'s contact info was successfully deleted.")
            else:
                print(f"\n{name.capitalize()}'s contact info was not deleted.")
        else:
            print("\nContact not found.")


goInput = input("\nIr a DIFICULTAD EXTRA (opcional): y/n? > ").strip().lower()
if goInput[0] == "y":
    while True:
        os.system("clear")
        print("\nDIFICULTAD EXTRA (opcional):\n")
        print("=== Contact List ===")
        menuInput = (
            input("1: View all\n2: Search\n3: Add\n4: Update\n5: Delete\n6: Exit\n> ")
            .strip()
            .lower()
        )
        if menuInput == "1" or menuInput[0] == "v":
            while True:
                showContacts()
                againInput = input("\nGo back to main menu? y/n? : > ").strip().lower()
                if againInput == "":
                    continue
                elif againInput[0] == "y":
                    break
                else:
                    continue
        elif menuInput == "2" or menuInput[0] == "s":
            while True:
                searchContact()
                againInput = input("\nSearch other contact? y/n? : > ").strip().lower()
                if againInput == "":
                    continue
                elif againInput[0] == "y":
                    continue
                else:
                    break
        elif menuInput == "3" or menuInput[0] == "a":
            addContact()
            time.sleep(2)
        elif menuInput == "4" or menuInput[0] == "u":
            updateContact()
            time.sleep(2)
        elif menuInput == "5" or menuInput[0] == "d":
            deleteContact()
            time.sleep(2)
        elif menuInput == "6" or menuInput[0] == "e":
            break
        else:
            continue
else:
    pass
