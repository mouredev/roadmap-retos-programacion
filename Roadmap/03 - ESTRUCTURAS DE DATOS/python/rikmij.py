import os
import re

print('*'*7, 'ESTRUCTURAS DE DATOS EN PYTHON', '*'*7)
print('\t--> LISTAS')
lista_ejemplo = ["Yoda", "Qui Gon Jinn", "Obi Wan", "Mace Windu"]
print(lista_ejemplo)

print("\n-> Agregar elementos a una lista")
lista_ejemplo.append("Anakin")
print(lista_ejemplo)

lista_ejemplo.insert(4, "Ahsoka Tano")
print(lista_ejemplo)

lista_ejemplo.extend(["Luke", "Rey"])
print(lista_ejemplo)

print("\n-> Borrar elementos de una lista")
lista_ejemplo.remove("Qui Gon Jinn")
print(lista_ejemplo)

lista_ejemplo.pop(2)
print(lista_ejemplo)

print("\n-> Ordenar la lista")
lista_ejemplo.sort()
print(lista_ejemplo)

print("\n-> Invertir la lista")
lista_ejemplo.reverse()
print(lista_ejemplo)

print("\n-> Borrar toda la lista")
lista_ejemplo.clear()
print(lista_ejemplo)


print('\n\t--> SETS')
set_ejemplo = set(["Aragorn", "Légolas", "Gimli", "Gandalf"])
print(set_ejemplo)

print("\n-> Agregar elementos a un set")
set_ejemplo.add("Frodo")
print(set_ejemplo)

print("\n-> Combinar sets")
hobbits = {"Sam", "Frodo"}  # {} también declara sets
comunidad_anillo = set_ejemplo.union(hobbits)
print(comunidad_anillo)

gollum_saruman = {"Gollum", "Saruman"}
comunidad_anillo.update(gollum_saruman)
print(comunidad_anillo)


print("\n-> Borrar elementos a un set")
comunidad_anillo.remove("Gollum")
comunidad_anillo.discard("Saruman")
comunidad_anillo.pop()
print(comunidad_anillo)

print("\n-> Borrar un set")
comunidad_anillo.clear()
print(comunidad_anillo)


print('\n\t--> TUPLES')
tuple_ejemplo = ("Mario", "Luigi", "Peach")
print(tuple_ejemplo)

print('\n-> "Agregar" elementos a un tuple (concatenar tuplas)')
toad_yoshi = ("Toad", "Yoshi")
print(tuple_ejemplo + toad_yoshi)


print('\n\t--> DICCIONARIOS')
dicc_ejemplo = {"Charmander": "Fuego",
                "Squirtle": "Agua",
                "Bulbasaur": "Planta",
                "Pikachu": "Eléctrico"}
print(dicc_ejemplo)

print('\n-> Agregar elementos a un diccionario')
dicc_ejemplo["Pidgey"] = "Volador"
print(dicc_ejemplo)

print('\n-> Borrar elementos a un diccionario')
dicc_ejemplo.pop("Pidgey")
print(dicc_ejemplo)

dicc_ejemplo.popitem()
print(dicc_ejemplo)

print('\n-> Actualización de un diccionario')
dicc_2 = {"Nidoran": "Veneno", "Beedrill": "Bicho", "Abra": "Psíquico"}

dicc_ejemplo.update(dicc_2)

print(dicc_ejemplo)

print("\n-> Borrar un diccionario")
dicc_ejemplo.clear()
print(dicc_ejemplo)


print('\n\t','*'*13, "EXTRA", '*'*13)

contact_list = {}

def inicio():
    print("\n\t~~ Agenda telefónica ~~")

    try:
        option = int(input('''¿Qué quieres hacer?:
            1.- Buscar contacto
            2.- Añadir contacto
            3.- Actualizar listado
            4.- Borrar contacto
            5.- Mostrar contactos
            6.- Salir\n-> '''))

        if option == 1:
            lookfor_contact()
        
        elif option == 2:
            add_contact()
        
        elif option == 3:
            update_contacts()
        
        elif option == 4:
            delete_contacts()
        
        elif option == 5:
            show_contacts()
        
        elif option == 6:
            pass
        
        else:
            print("Opción no válida")
            inicio()
    
    except ValueError:
        print("Ingrese una opción válida")
        inicio()


def end_funct():
    print(input("\nPulsa cualquier tecla para volver al inicio"))
    os.system("cls")
    inicio()


def lookfor_contact():
    if len(contact_list) == 0:
        print("La lista de contactos está vacía")
    
    else:
        look_for = input("¿Quieres buscar por contacto (C) o por número (Num)?: ").lower()

        while look_for != "c" and look_for != "num":
            look_for = input("Opción no válida. ¿Por contacto (C) o por número(Num)?: ").lower()

        if look_for == "c":
            contact = input("¿Qué contacto quieres buscar?: ")
        
            if contact in contact_list:
                print(f"\nAquí está el contacto que buscaba:\n{contact} : {contact_list[contact]}")
                end_funct()
            
            else:
                print("Ese contacto no está en la lista")

        elif look_for == "num":
            contact_num = input("¿Cuál es el número del contacto?: ")

            if contact_num in contact_list.values():
                for name, number in contact_list.items():
                    if str(number) == contact_num:
                        print(f"\nEl número \"{number}\" pertenece a: {name}")
            else:
                print("Ese número no coincide con ningún contacto")
            
            end_funct()


def add_contact():
    name = input("Ingrese nombre del contacto: ")
    number = input("Ingrese el número del contacto: ")

    if re.match("\d{9}", number):
        contact_list[name] = number
    else:
        print("El formato de número no es válido. Introduce un número de 9 cifras")
    
    end_funct()


def update_contacts():
    update = input("Quieres actualizar algún contacto?: Sí(s) / No(n)").lower()

    if update == "s":
        contact = input("¿Qué contacto quieres actualizar?")

        if contact in contact_list:
            new_number = int(input("ingrese su número de teléfono"))

            if re.match("\d{9}", new_number):
                contact_list[contact] = new_number
        else:
            print("No existe ese contacto")
        end_funct()
    
    elif update == "n":
        end_funct()
    
    else:
        while update != "s" or update != "n":
            print("Opción no válida. Ingrese \"s\" o \"n\"")
            update_contacts()

def delete_contacts():
    contact = input("¿Qué contacto quieres borrar?: ")

    if contact in contact_list:
        contact_list.pop(contact)
    else:
        print("Este usuario no existe")
    
    end_funct()


def show_contacts():
    for contact in contact_list.items():
        print(contact)
    
    end_funct()


inicio()
