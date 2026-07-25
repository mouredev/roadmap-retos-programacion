# Estructuras de datos

list = [1, 2, 3, 4] #Lista, mutable y ordenada
print(list)

my_tuple = (1, 2, 3, 4) #Tupla, inmutables
print(my_tuple)

my_set = {1, 2, 3, 4} #Conjunto, mutable, no ordenada
print(my_set)

mi_diccionario = {
    'Nombre': 'Daniel',
    'Apellido': 'Pineda',
    'Edad': 24
} # Diccionario
print(mi_diccionario)

# Metodos para modificar listas

list.append('Phobos')
print(list)

list.remove('Phobos')
print(list)

list[1] = 'Hola'
print(list)

list[1] = 6

list.sort()
print(list)

# Metodos para tuplas

my_tuple = tuple(sorted(my_tuple))

# Metodos para set

print(type(my_set))

my_set.add('Phobos')
print(my_set)

my_set.remove('Phobos')
print(my_set)

#Metodos para diccionarios

print(type(mi_diccionario))
print(mi_diccionario['Nombre'])

mi_diccionario['Email'] = 'danielpineda@gmail.com'
print(mi_diccionario)

mi_diccionario['Edad'] = 25
print(mi_diccionario)

del mi_diccionario['Apellido']
print(mi_diccionario)

'''
Dificultad extra
'''

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

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
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
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
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()