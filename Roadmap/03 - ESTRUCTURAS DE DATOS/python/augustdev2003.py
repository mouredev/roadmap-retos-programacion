"""Estructuras de datos"""

# LISTAS

list()  # Crea una lista vacía

empty_list = []

languages = ['Python', 'JavaScript', 'Go', 'PHP']

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

data = ['Tenerife', {"cielo": "limpio", "temp": 25},
        453, (28.1283971, -16.57372)]

# Conversión desde cadena de texto

print(list('Python'))

# Conversión a partir de un rango

print(list(range(0, 10)))

# Operaciones en listas

data.append('Python')  # Inserción
data.append(12)
print(data)
data.insert(1, 'Argentina')  # Inserción mediante índice
data[1] = 'España'  # Actualización
print(data)
# Cuatro formas de borrar elementos de ua lista
del data[2]  # Por su índice
print(data)
data.remove('España')  # Por su valor
print(data)
# Por índice(extracción) - .pop() no solo borra un elemento sino que nos ayuda a recuperar el elemento
element = data.pop()
print(element)
print(data)
data[1:3] = []  # Por su rango
print(data)
# Ordenación - sorted() NO modifica la lista original, crea una nueva.
sorted(languages)
print(languages)
languages.sort()  # .sort() SI modifica la lista original
# Tanto .sort() como sorted() aceptan un parámetro 'reverse' para indicar la forma en que se ordena
sorted(languages, reverse=True)
print(languages)

# TUPLAS

empty_tuple = ()

tenerife_geoloc = (28.46824, -16.25462)

three_countries = ('Argentina', 'España', 'Chile')

# Para crear una tupla con un único elemento, tendremos que hacerlo de la siguiente forma:

one_item_tuple = ('Python',)

# Las tuplas son inmutables, esto quiere decir que no podemos modificarlas,
# eliminar elementos, ni agregar.

print(tuple(sorted(three_countries)))  # Ordenación

# DICCIOONARIOS

empty_dict = {}

my_dict = {
    "name": 'Augusto',
    "surname": 'Ojeda Rosso',
    "age": 20,
}
print(my_dict)

person = dict(
    name='Juan',
    surname='Rodriguez',
    age=30,
)
print(person)

# Es posible crear un diccionario especificanod sus claves y un valor único

unique_value = dict.fromkeys('abcdef', 1)
print(unique_value)

# Operaciones en diccionarios

person['job'] = 'Data scientist'  # Inserción
print(person)
person['job'] = 'Backend Developer'  # Actualización
del person['surname']  # Eliminación
print(person)
sorted_dict = dict(sorted(person.items()))  # Ordenación
print(sorted_dict)

# SETS

lottery = {32, 10, 23, 1, 8}
print(lottery)

# La única forma de crear un set vacío es de la siguiente manera:
my_set = set()
print(my_set)

# Operaciones con sets

lottery.add(14)  # Inserción
print(lottery)
lottery.remove(1)  # Eliminación
print(lottery)
sorted(lottery)  # No se puede ordenar
print(lottery)

"""
Extra
"""


def agenda():
    agenda = {}

    def insert_contact():
        phone_number = input("Introduce tu número de teléfono: ")
        if phone_number.isdigit() and len(phone_number) > 0 and len(phone_number) <= 11:
            agenda[insert_name] = phone_number
        else:
            print('Introduce un número de teléfono con un máximo de 11 digitos')

    while True:
        print(
            """
            1- Buscar contacto.
            2- Insertar contacto.
            3- Actualizar contacto.
            4- Eliminar contacto.
            5- Salir.
            """
        )
        option = input("\nSelecciona una opción: ")
        print(option)

        match option:
            case "1":
                insert_name = input(
                    "Introduce el nombre del contácto a buscar: ")
                if insert_name in agenda:
                    print(
                        f'El número de teléfono de {insert_name} es {agenda[insert_name]}.')
                else:
                    print(
                        f'El número de teléfono de {insert_name} no está registrado.')

            case "2":
                insert_name = input(
                    "Introduce el nombre del contácto a registrar: ")
                if insert_name == "":
                    print(insert_name)
                else:
                    insert_contact()

            case "3":
                insert_name = input(
                    "Introduzca el nombre del contácto para actualizar: ")
                if insert_name in agenda:
                    insert_contact()
                else:
                    print(f'El contacto {insert_name} no existe.')

            case "4":
                insert_name = input(
                    "Introduce el nombre del contácto a eliminar: ")
                if insert_name in agenda:
                    del agenda[insert_name]
                else:
                    print(f'El contacto {insert_name} no existe')

            case "5":
                print("Saliendo de la agenda.")
                break

            case _:
                print("Opción no válida, elige una opción correcta.")


agenda()
