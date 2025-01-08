"""
estructuras de datos 
"""

# listas: varios elementos ordenados.

mi_lista = ["Brais", "Nombre2", "sunjamer"] # entre corchetes
print (mi_lista)

mi_lista.append("Cristina")   # inserción dato
print(mi_lista)

mi_lista.remove("sunjamer")  #eliminar dato
print(mi_lista)

print(mi_lista[1])  # acceder a una posicion

mi_lista[1] = "patatatuelas"  # actualizaion
print(mi_lista)

mi_lista.sort()   # ordenación, si es texto, ordenación alfabética
print(mi_lista)
print(type(mi_lista))


# tuplas

mi_tupla: tuple = ("sunjamer", "Pedro", "@canal_sunjamer", "47")
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[2])
print(mi_tupla[3])   # acceso a datos de la tupla

mi_tupla = tuple(sorted(mi_tupla))    # ordenación de la tupla
print(mi_tupla)
print(type(mi_tupla))

# sets

mi_set = {"sunjamer", "Pedro", "@canal_sunjamer", "47"}

print(mi_set)
print(type(mi_set))

mi_set.add("sunjamer@gmail.com")  # inserción
print(mi_set)  # no se puede acceder a una posición concreta
mi_set.add("sunjamer@gmail.com")
print(mi_set) # no se puede añadir elementos si estan duplicados

mi_set.remove("Pedro")  # eliminación
print(mi_set)

mi_set = set (sorted(mi_set))  # no se puede ordenar
print(mi_set)


# Diccionario

mi_dict: dict = {
    "nombre":"Pedro",
    "apellido":"Pérez",
    "nick":"sunjamer",
    "edad":"47"
}

print(mi_dict)
print(type(mi_dict))

mi_dict["email"] = "sunjamer@gmail.com"  # inserción 
print(mi_dict)

del mi_dict["apellido"]  # eliminación
print(mi_dict)

print (mi_dict["nombre"])  # acceso

mi_dict["edad"] = 48    # actualización
print(mi_dict)

mi_dict = dict(sorted(mi_dict.items())) # ordenación
print(mi_dict)
print(type(mi_dict))

# extra

def mi_agenda():

    agenda = {}
    
    while True:
    
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case "1":
                nombre = input("entra el nombre del contacto a buscar: ")
                if nombre in agenda:
                    print(f"el telefono de {nombre} es {agenda[nombre]}.")
                else:
                    print("el nombre no existe en la agenda")
                    
            case "2":
                nombre = input("entra el nombre del contacto: ")
                telefono = input("entra el teléfono del contacto: ")
                if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
                    agenda[nombre] = telefono
                else:
                    print ("debes introducir un número de 11 digitos como máximo")
            case "3":
                pass
            case "4":
                nombre = input("entra el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print(f"el contacto {nombre} se ha eliminado")
                else:
                    print("el nombre no existe en la agenda")
            case "5":
                print ("saliendo del programa Agenda")
                break
            case _:
                print("Opción no válida. Escoge una opción del 1 al 5.")
    


mi_agenda()






