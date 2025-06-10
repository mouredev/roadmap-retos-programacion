#Listas
mi_lista :list = ["Miriam", "Iban", 25, "Futbol"]

mi_lista.append("Analista") #Importante el orden de inserción 
print(mi_lista)

mi_lista.remove(25) #Borrado de elementos
print(mi_lista)

mi_lista[1] = "Gil" #Actualización
print(mi_lista)

mi_lista.sort()
print(mi_lista) #Ordenación

#Tuplas
mi_tupla :tuple = ("Miriam", "Iban", "miban", "25")
print(mi_tupla[1])

mi_tupla = tuple(sorted(mi_tupla)) #El sorted cambia a lista una tupla
print(type(mi_tupla))
print(mi_tupla)


#Diccionarios
mi_dict : dict = {
    "name": "Miriam", 
    "apellido": "Iban", 
    "alias":"miban", 
    "edad":"25"
}

print(mi_dict["name"]) #Acceso
print(type(mi_dict))

mi_dict["email"] = "miriamiban@gmail.com" #Inserción
print(mi_dict)

mi_dict["edad"] = "26" #Actualización
print(mi_dict)

del mi_dict["apellido"] #Eliminar
print(mi_dict)

mi_dict = dict(sorted(mi_dict.items())) #Ordenación
print(mi_dict)

#Sets
mi_set : set= {"Miriam", "Iban", "miban", "25"}
print(type(mi_set))

mi_set.add("miriamiban@gmail.com")
print(mi_set)
#Estructura no ordenada, evita duplicados

mi_set.remove("Miriam") #Eliminar
print(mi_set)

mi_set = set(sorted(mi_set)) #No se puede ordenar


#Extra
def my_agenda():
    
    agenda :dict = {}
    
    def insertContact():
        number = input("Introduce el número: ")
        if number.isdigit() and len(number) > 0 and len(number) <=11:
            agenda[name] = [number]
        else:
            print("Debes introducir un número correcto.")
    
    while True:

        print("1.Buscar contacto")
        print("2.Insertar contacto")
        print("3.Actualizar contacto")
        print("4.Borrar contacto")
        print("5.Salir")
        
        option = input("\n Selecciona una opción: ")
        
        match option:
            case "1":
                name = input("Introduce el nombre que quieres buscar: ")
                if name in agenda:
                    print(f"El numero de teléfono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre: ")
                insertContact()
            case "3":
                name = input("Introduce el nombrea actualizar: ")
                if name in agenda:
                    insertContact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombrea eliminar: ")
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