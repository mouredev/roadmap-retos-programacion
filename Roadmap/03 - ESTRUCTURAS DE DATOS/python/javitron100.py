# ESTRUCTURAS DE DATOS

# Listas
mi_lista = [1, 35, 23, 11, 34]
print(mi_lista[3])

mi_lista.append(5)
print(mi_lista)

mi_lista.insert(1, 12)
print(mi_lista)

mi_lista.remove(12)
print(mi_lista)

mi_lista.pop()
print(mi_lista)

mi_lista.sort()
print(mi_lista)

mi_lista.reverse()
print(mi_lista)

# Tuplas
mi_tupla = (1, 56, 14, 77, 6, 13)
print(mi_tupla)

# Sets
mi_set = {1, 2, 3, 4, 5, 6, 7}
print(type(mi_set))
print(mi_set)
print(mi_set)
print(mi_set)

mi_set.add(14)
print(mi_set)

mi_set.remove(3)
print(mi_set)

# Diccionarios

mi_diccionario = {
    "Nombre" : "Javier", 
    "Edad" : 50, 
    "Telefono" : "642123487"

}

print(mi_diccionario)
print(mi_diccionario["Nombre"])

# Dificultad Extra
opcion = ""
agenda = [
            {"Nombre" : "javi", "Telefono" : "11111"}, 
            {"Nombre" : "pepe", "Telefono" : "22222"}, 
            {"Nombre" : "toni", "Telefono" : "33333"}, 
            {"Nombre" : "carla", "Telefono" : "44444"}
        ]

def insertar_contacto():

    contacto = {"Nombre" : "", "Telefono" : ""}

    nom = input("Nombre: ")
    tel = input("Teléfono: ")
    if tel.isdigit() and len(tel) in range(1, 12):
        contacto["Nombre"] = nom
        contacto["Telefono"] = tel
        agenda.append(contacto)
    else:
        print("El número de teléfono no es válido, no se ha grabado la entrada.")

def borrar_contacto(busqueda):
    for contacto in agenda:
            if contacto["Nombre"] == busqueda:
                agenda.remove(contacto)

def actualizar_contacto(busqueda):
    for contacto in agenda:
            if contacto["Nombre"] == busqueda:
                tel = input("Nuevo número de teléfono: ")
                if tel.isdigit() and len(tel) in range(1, 12):
                    contacto["Telefono"] = tel
                else: 
                    print("Teléfono no válido. No se actualiza.")

def buscar_contacto(busqueda):
    for contacto in agenda:
        if contacto["Nombre"] == busqueda:
            print(contacto)

    

while opcion != "0":
    
    if opcion == "1":
       insertar_contacto()

    if opcion == "2":
        borrar_contacto(input("Nombre a borrar de la agenda: "))

    if opcion == "3":
        actualizar_contacto(input("Nombre a actualizar: "))

    if opcion == "4":
        buscar_contacto(input("Nombre a buscar: "))

    if opcion == "5":
        print(agenda)

    print("1.- Insertar contacto")
    print("2.- Borrar contacto")
    print("3.- Actualizar contacto")
    print("4.- Buscar contacto")
    print("5.- Mostrar agenda")
    opcion = input("Elige una opcion (0 para terminar el programa): ")
    

