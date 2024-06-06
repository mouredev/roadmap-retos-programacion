# 03 Estructuras de Datos

# Listas
from asyncio.windows_events import NULL
from os import system


my_list = [0, 1, 2]
my_list.append(1) # Insercion
my_list[1] = 3    # Actualizacion
my_list.remove(2) # Borrado
my_list.sort()    # Ordenacion
print("Lista:",my_list)


# Tuplas
my_tuple = (0, 1, 2)      # Las tuplas no pueden ser editadas
print("Tupla:",my_tuple)


# Set
my_set = {0, 1, 2} 
my_set.add(3)       # Insercion
my_set.remove(1)    # Borrado
print("Sets:",my_set)


# Dicts
my_dict = {"Nombre": "Empty", "Edad": 21}
my_dict["Nombre"] = "Gabriel" # Actualizacion
del my_dict["Edad"]           # Borrado
my_dict["Ocupacion"] = "Estudiante" # Insercion
print("Diccionario:",my_dict)

###  Agenda  ###
agenda = list()
def menu():
    entrada = int()
    while True:
        try:
            system("cls")
            print("Seleciona una opcion 1-Agregar 2-Actualizar 3-Eliminar 4-Ver Contactos 5-Salir ")
            entrada = int(input())
        except ValueError or entrada <= 5 or entrada < 1:
            print("Ingrese un numero valido")
        if entrada == 1:
            agregar()
        elif entrada == 2:
            actualizar()
        elif entrada == 3:
            eliminar()
            pass
        elif entrada == 4:
            system("cls")
            if len(agenda) == 0:
                print("Agenda sin contactos")
                system("pause")
            else: 
                for contacto in agenda:
                    print(f"Nombre: {contacto["Nombre"]}")
                    print(f"Numero de Telf: {contacto["Numero de Telf"]}")
                system("pause")
        else:break

def agregar():
    system("cls")
    nuevo_contacto = dict()
    nombre = input("Escribe el nombre de tu contacto: ")
    num_telf = int()
    try:
        num_telf = int(input("Introduzca el numero de telefono: "))
    except ValueError or len(str(num_telf)) > 11:
        print("Por favor, ingresa un número válido.")
    nuevo_contacto["Nombre"] = nombre
    nuevo_contacto["Numero de Telf"] = num_telf
    print("Contacto Agregado")
    system("pause")
    agenda.append(nuevo_contacto)
    return

def actualizar():
    system("cls")
    if len(agenda) == 0:
        print("Agenda sin contactos")
        system("pause")
        return
    while True:
        system("cls")
        for contacto in agenda:
            print(f"Nombre: {contacto["Nombre"]}")
            print(f"Numero de Telf: {contacto["Numero de Telf"]}")
        nombre = input("Que contacto desea actualizar: ")
        encontrado = False
        for contacto in agenda:
            if nombre == contacto["Nombre"]:
                num_telf = int()
                try:
                    system("cls")
                    num_telf = int(input("Introduzca el nuevo numero de telefono: "))
                except ValueError or len(str(num_telf)) > 11:
                    print("Por favor, ingresa un número válido.")
                contacto["Numero de Telf"] = num_telf
                encontrado = True
                return
        if not encontrado:
            system("cls")
            print("No se ha encontrado el contacto")
            system("pause")

def eliminar():
    system("cls")
    if len(agenda) == 0:
        print("Agenda sin contactos")
        system("pause")
        return
    while True:
        system("cls")
        for contacto in agenda:
            print(f"Nombre: {contacto["Nombre"]}")
            print(f"Numero de Telf: {contacto["Numero de Telf"]}")
        nombre = input("Que contacto desea eliminar: ")
        encontrado = False
        for contacto in agenda:
            if nombre == contacto["Nombre"]:
                system("cls")
                print("Contacto eliminado")
                system("pause")
                agenda.remove(contacto)
                encontrado = True
                return
        if not encontrado:
            system("cls")
            print("No se ha encontrado el contacto")
            system("pause")
                    

        
menu()