# Listas

my_list: list = ["Angel", "Brais", "Wolfy"]
print(my_list)
my_list.append("Castor")  # Insercion
print(my_list)
my_list.remove("Brais")  # Emininacion
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Cuervillo"  # Actualizacion
print(my_list)
my_list.sort()  # Ordenacin
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Angel", "Curup", "@curup", "25")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenacion
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Angel", "Curup", "@curup", "25"}
print(my_set)
my_set.add("curup.angel53@gmail.com")  # Insercion
my_set.add("curup.angel53@gmail.com")
print(my_set)
my_set.remove("Curup")  # Eliminacion
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar

print(type(my_set))

# Diccionario
my_dic: dict = {
    "name": "Angel",
    "surname": "Curup",
    "alias": "@curup",
    "age": "25",
}
my_dic["email"] = "curup.angel53@gmai.com"  # Insercion
print(my_dic)
del my_dic["surname"]  # Eliminacion
print(my_dic)
print(my_dic["name"])  # Acceso
my_dic["age"] = "26"  # Actualizacion
print(my_dic)
my_dic = dict(sorted(my_dic.items()))
print(my_dic)
print(type(my_dic))


"""
Extra
"""

def my_agenda():

    agenda = {}


    def is_digit():
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 8:
            agenda[name] = phone
        else:
            print("Debes introducir numero de telefono con menos de 9 digitos")


    while True:
        print("\nAgenda de contactos")
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\n Seleccione una opcion: ")

        match option:
            case "1":
                print("\nBuscar contacto")
                if not agenda:
                    print("Agenda vacia")
                else: 
                    name = input("Introduzaca el nombre del contacto: ")
                    if name in agenda:
                        print(f"El numero del contacto de telefono de {name} es {agenda[name]}.")
                    else:
                        print(f"El contacto {name} no existe")
            case "2":
                print("\nAgregar nuevo contacto")
                name = input("Introduce el nombre del contacto: ")
                phone = input("Introdeuce el telefono del conatacto: ")
                is_digit()
                print("Contacto agregado!")
            case "3":
                print("\nActualizar contacto")
                name = input("introduce nombre del contacto a actulizar: ")
                if name in agenda:
                    phone = input("Introdeuce el nuevo numero de telefono del conatacto: ")
                    is_digit()
                    print("Contacto actualizado!")
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                print("\nEliminar contacto")
                name = input("introduce nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print("Contacto eliminado!")
                else:
                    print(f"El contacto {name} no existe")
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion invalida, Elige una opcion del 1 al 5.")                

my_agenda()
