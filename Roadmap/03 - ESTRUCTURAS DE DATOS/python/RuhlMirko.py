import os

print("Listas")
number_list = [0, 1, 2, 3, 4, 5]  # Crea una lista con Ints
string_list = ["A", "B", "C", "D"]  # Crea una lista con Strings
print(f"{number_list}\n{string_list}")

string_list.append("E")  # Agrega un elemento a una lista creada
string_list.remove("A")  # Remueve un elemento buscado por coincidencias
number_list.pop(5)  # Remueve un elemento buscado por indice
string_list[1] = "F"  # Accede y actualiza un item de la lista por indice
string_list.sort()  # Ordena la lista de forma alfabetica. Tambien util para lista de numeros
print(f"nuevas listas:\n{number_list} \n{string_list}")

print("\nTuplas")

tupla = ("Python", "Ejercicio 03", "Estructura de datos", "RuhlMirko.py")
print(tupla)
print(tupla[2])  # Devuelve el valor de la tupla buscado por indice
print(tuple(sorted(tupla)))  # Ordena la tupla por orden alfabetico. Tambien util para tupla de numeros

print("\nSets")
my_set = {"Python", "Ejercicio 03", "Estructura de datos", "RuhlMirko.py"}
print(my_set)
my_set.add("Java")  # Agrega un elemento a un set
my_set.remove("Python")  # Remueve un elemnto del set
print(my_set)

print("\nDiccionarios")
my_dict = {
    "#00": "Sintaxis, variables, tipos de datos y hola mundo",
    "#02": "Funciones",
    "#01": "Operadores y estructuras de control"
}

print(my_dict["#01"])  # Acceso de datos por clave
my_dict["#03"] = "Estructuras de datos"  # Agrega un elemento al diccionario
my_dict["#02"] = "Funciones y alcance"  # Actualiza un elemnto ya declarado
my_dict["#03"] = "Estructuras de datos"  # Agrega un elemento al diccionario
print(my_dict)

my_dict.pop("#03")  # Una manera de eliminar un elemento
my_dict["#03"] = "Estructuras de datos"
del my_dict["#03"]  # Otra manera de eliminar un elemento

my_dict = dict(sorted(my_dict.items()))
print(my_dict)

print("\nDificultad extra: ")
contact_dict = {}
while True:
    user_choice = int(input("\nBienvenido a tu agenda de contactos"
                            "\n1) Ingresar nuevo contacto"
                            "\n2) Buscar contacto"
                            "\n3) Actualizar contacto"
                            "\n4) Eliminar contacto"
                            "\n5) Mostrar lista de contactos"
                            "\n\n0) Salir del programa"
                            "\nElija la operacion: "))
    match user_choice:
        case 0:
            break
        case 1:
            while True:
                name = input("Enter the new contact name: ").lower()

                while True:
                    try:
                        number = int(input("Enter the cellphone number: "))
                        number_length = len(str(number))
                        break
                    except ValueError:
                        print("Enter a valid number")

                while True:
                    if number_length > 11:
                        number = input("You can only enter 11 digits, Enter the number again: ")
                        number_length = len(number)
                    else:
                        break

                contact_dict[name] = number
                break
        case 2:
            search_term = input("Ingrese el nombre del contacto: ").lower()
            try:
                print(f"Cellphone number of {search_term}: {contact_dict[search_term]}")
            except KeyError:
                print(f"{search_term} not available in your contact list.")

        case 3:
            search_term = input("Ingrese el nombre del contacto a actualizar : ").lower()

            if search_term in contact_dict:
                contact_dict[search_term] = input("Enter the new number: ")
            else:
                print(f"{search_term} not available in your contact list.")
        case 4:
            search_term = input("Ingrese el nombre del contacto a eliminar: ")
            if search_term in contact_dict:
                del contact_dict[search_term]
            else:
                print(f"{search_term} not available in your contact list.")
        case 5:
            print(contact_dict)
        case _:
            print("\nEnter a valid option\n")

