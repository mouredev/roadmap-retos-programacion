mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
mi_conjunto = {1, 2, 3, 4, 5}
mi_cadena = "Hola, mundo!"
mi_entero = 42
mi_flotante = 3.14
mi_booleano = True


"""

# PROGRAM EXERCISE

"""

contacts = {}
contacts.update({'Nicolas': 96697572})
contacts.update({'Nicole': 2312312312})
contacts.update({'Francisca': 112223334})

def check_input(celular):
    if isinstance(celular, str) and len(str(celular)) <= 11:
        return True
    else:
        return False

def search_contact():
    entry = input("\n Escribe el nombre del contacto o ALL para ver todos los contactos => ")
    if entry == 'all' or entry == 'ALL':
        for name, celular in contacts.items():
            print ("\nNombre: ", name)
            print ("Celular: ", celular)
    elif entry.lower() in (key.lower() for key in contacts):
        entry = entry[0].upper() + entry[1:]
        print ("\nNombre: " , entry)
        print ("Celular: " , contacts.get(entry))
    else:
        print ("\n!!!!!!!!!!!No se ha podido encontrar el contacto!!!!!!!!!!!")

def insert_contact():
    nombre = input("Nombre: ")
    if nombre.lower() in (key.lower() for key in contacts):
        print ("\nEl contacto " , nombre , " ya existe")
    else:
        celular = input("Celular: ")
        if(check_input(celular) == True):
            contacts.update({nombre: celular})
            print("\nCONTACTO ANIADIDO SATISFACTORIAMENTE OK!\n")
        else:
            print ("\nEl número de teléfono no es válido - ingrese solo numeros (11 max)")
    
def delete_contact():
    entry = input("\n Escribe el nombre del contacto que quiere eliminar => ")
    if entry.lower() not in (key.lower() for key in contacts):
        print ("\nEl contacto " , entry , " no existe")
    else:
        key_correct_case = next(key for key in contacts if key.lower() == entry.lower())
        contacts.pop(key_correct_case)
        print("\nCONTACTO ELIMINADO SATISFACTORIAMENTE OK!\n")
    
def update_contact():
    entry = input("\n Escribe el nombre del contacto que quieres actualizar => ")
    entry_lower = entry.lower()
    if entry_lower in (key.lower() for key in contacts):
        celular = input("Celular: ")
        if(check_input(celular) == True):
            key_correct_case = next(key for key in contacts if key.lower() == entry_lower)
            contacts[key_correct_case] = celular
            print("\nCONTACTO ACTUALIZADO SATISFACTORIAMENTE OK!\n")
        else:
            print ("\nEl número de teléfono no es válido - ingrese solo numeros (11 max)")
    else:
        print ("\n!!!!!!!!!!!No se ha podido encontrar el contacto!!!!!!!!!!!")

def sort_contacts():
    return sorted(contacts.items())

print("------------- Agenda de contactos -------------")
def contactos():
    end_pogram = True
    while end_pogram == True:

        print("\nQue operacion desea realizar?")
        option = input("Crear (C), Borrar (B) , Actualizar (A), Buscar (S), Ordenar (O) => ")
        if option == "C" or option == "c":
            insert_contact()
        elif option == "B" or option == "b":
            delete_contact()
        elif option == "A" or option == "a":
            update_contact()
        elif option == "S" or option == "s":
            search_contact()
        elif option == "O" or option == "o":
            print("\nContactos: ", sort_contacts())

        finish = input("\nDesea finalizar el programa? Yes(Y) No(N): ")
        if finish == "Y" or finish == "y":
            end_pogram = False
            break
        elif finish == "N" or finish == "n":
            end_pogram = True
        else:
            print("\n!!!!!!!!!!!Por favor ingrese una opcion valida!!!!!!!!!!!")    

contactos()