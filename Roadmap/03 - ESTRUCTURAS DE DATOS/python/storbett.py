#listas


mi_lista = ["mouredev", "simon", "adrimar"]
print(mi_lista)

mi_lista.append("loengris") #insercion
print(mi_lista)

mi_lista.remove("simon") #eliminacion
print(mi_lista)

print(mi_lista[1]) #acceso
mi_lista[1]= "mouredevillo" #actualizacion
print(mi_lista)

mi_lista.sort() #ordenacion
print(mi_lista)


# tuplas

mi_tupla = ("simon", "torbett", "storbett", "36")
print(mi_tupla[1]) #acceso
print(mi_tupla[3]) 
mi_tupla = tuple(sorted(mi_tupla)) #ordenacion
print(mi_tupla)
print(type(mi_tupla)) 


# set #no se duplican los datos#
#no se puede ordenar#


mi_set = {"simon", "torbett", "storbett", "36"}
print(mi_set)
mi_set.add("simontorbett@gmail.com")
mi_set.remove("storbett") #elimicacion
print(mi_set)

print(type(mi_set))

#diccionario

mi_diccionario: dict = {
    "nombre": "simon",
    "apellido": "torbett",
    "edad": "33"
}

mi_diccionario["email"] = "simontorbett@gmail.com" # insercion
print(mi_diccionario)
del mi_diccionario["apellido"] # elimimcacion
print(mi_diccionario)
mi_diccionario["edad"] = "34" #actualizacion
print(mi_diccionario)
mi_diccionario = dict(sorted(mi_diccionario.items()))
print(mi_diccionario)
print(type(mi_diccionario))

# extra

def mi_agenda():

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
            case "2":
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
mi_agenda()