#LISTAS

my_list = ["Victor", "Brais", "Carl"]   #Lista inicial (mutable)
print(my_list)

my_list.append("Jorge")     #Añadimos a Jorge
print(my_list)

my_list.remove("Carl")      #Eliminamos a Carl
print(my_list)

my_list[1] = "Mouredev"     #Acceso y modificacion de Brais
print(my_list)

my_list.sort()              #Ordena la lista (alfabéticamente, menor -> mayor)
print(my_list)


#TUPLAS

my_tuple = ("Victor", "Juan", "32")     #Tupla inicial (inmutable)
print(my_tuple)

print(my_tuple[2])          #Acceso

my_tuple_2 = sorted(my_tuple)           #Ordena una tupla y ...
print(type(my_tuple_2))     #ahora es una lista en vez de una tupla
print(my_tuple_2)


#SET
my_set = {"Victor", "Juan", "32"}       #Set inicial (estructura desordenada)
print(my_set)

my_set.add("Hola")          #Añadimos pero no sabemos la posicion de Hola
print(my_set)

#print(my_set[0])           No hay operacion de acceso

my_set.remove("32")         #Eliminamos 32
print(my_set)

my_set_2 = set(sorted(my_set))          #No se puede ordenar
print(my_set_2)


#DICCIONARIO
my_dict: dict = {
    "name": "Victor",
    "age": "32",
    "alias": "Jose"
}

print(my_dict)

print(my_dict["name"])      #Acceso

my_dict["email"] = "qwerty" #Añadir nueva clave/valor
print(my_dict)

my_dict["email"] = "asdf"   #Acceso y modificacion del email
print(my_dict)

del my_dict["age"]          #Eliminamos la edad
print(my_dict)

my_dict_2 = dict(sorted(my_dict.items()))   #Diccionario ordenado
print(my_dict_2)


#EJERCICIO EXTRA

def my_agenda():

    salir = False
    agenda = {}

    def insert_tel():
        tel = input("Dime el telefono: ")
        if tel.isdigit() and len(tel) > 0 and len(tel) <= 11:
            agenda[name] = tel
        else:
            print("Telefono invalido")

    while not salir:

        print("\n1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSeleccione la opcion: ")

        match option:
            case "1":
                
                name = input("Dime el nombre: ")
                if name in agenda:
                    print(f"Nombre: {name} y telefono {agenda[name]}.")
                else:
                    print(f"El nombre {name} no existe")

            case "2":

                name = input("Dime el nombre: ")
                insert_tel()
                
            case "3":

                name = input("Dime el nombre: ")
                if name in agenda:
                    insert_tel()
                else:
                    print(f"Usuario {name} no existe")

            case "4":

                name = input("Dime el nombre: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Usuario {name} eliminado")
                else:
                    print(f"El nombre {name} no existe")

            case "5":

                print("Saliendo de la agenda")
                salir = True

            case _:
                
                print("Operación no válida")



print("**********************")
print("Bienvenido a la agenda")
my_agenda()