#Estructuras de datos
"""
Listas
"""
Mi_lista: list = ["Gallo", "Jose","Miguel","Zuno"]
print(Mi_lista)
Mi_lista.append("Michel") #Inserción
print(Mi_lista)
Mi_lista.remove("Michel") #Eliminación
print(Mi_lista)
print(Mi_lista[0]) #Acceso
Mi_lista[0] = "Gallolobo" #Actualización
Mi_lista.sort() #Ordenación
print(Mi_lista)
print(type(Mi_lista))

"""
Tuplas
"""
Mi_tupla: tuple = ("Melchor","Gazpar","Baltazar")
print(Mi_tupla[1]) #Acceso
my_tuple = tuple(sorted(Mi_tupla)) #Ordenación
#Se pone tuple antes del sorted por que el sorted convierte en lista
print(Mi_tupla)
print(type(Mi_tupla))

"""
Sets
"""
mi_set: set= {"Gallolobo","Gallitofast","Tacosricos","MESSI"}
print(mi_set)
mi_set.add("messigallito") # Insercion
print(mi_set)
mi_set.add("messigallito")
print(mi_set)
mi_set.remove("Gallolobo") #Eliminacion
print(mi_set)
mi_set = set(sorted(mi_set)) #No se puede ordenar
print(mi_set)
print(type(mi_set))


#Diccionario
Mi_diccionario: dict = {
    "Nombre": "Jose",
    "Apellido": "Gallo",
    "Alias": "Gallolobo",
    "edad": "23"
}
Mi_diccionario["email"] = "MessigallitoQgmail.com" #Insercion
print(Mi_diccionario)
del Mi_diccionario["Alias"] #Eliminacion
print(Mi_diccionario)
print(Mi_diccionario["Nombre"])
Mi_diccionario["edad"] = "24" #Actualizacion
print(Mi_diccionario)
Mi_diccionario = dict(sorted(Mi_diccionario.items()))
print(Mi_diccionario)
print(type(Mi_diccionario))

"""
Extra
"""
def MI_AGENDA():

    agenda = {}

    def  insert_contact():
        num_tel = input("Introduce el numero telefonico del contacto: ")
        if num_tel.isdigit() and len(num_tel) > 0 and len(num_tel) <=11:
            agenda[name] =num_tel
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
                    print(f"el numero de telefono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto de {name} no existe")
            case "2":
                name = input("Introduce el nombre del contacto")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto que quieres actualizar")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar")
                if name in agenda: 
                    del agenda[name]
                else: 
                    print(f"El contacto que buscas eliminar no existe")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5")
MI_AGENDA()