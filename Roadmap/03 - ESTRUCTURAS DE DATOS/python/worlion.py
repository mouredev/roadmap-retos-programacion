# List
my_list = [5, 3, 1, 4, 2]
print ("\n\n____ LISTAS____");

print(f" - Lista:\t\t\t{my_list}")
my_list.append(8)
print(f" - Lista (añado el 8):\t\t{my_list}")
my_list.remove(3)
print(f" - Lista (borro el 3):\t\t{my_list}")
my_list[2] = 99
print(f" - Lista (actualizo la pos 3):\t{my_list}")
my_list.sort()
print(f" - Lista (ordenada):\t\t{my_list}")

# Tuple
my_tuple = (5, 3, 1, 4, 2)
print ("\n\n____ TUPLAS ____");

print(f" - Tuple:\t\t\t{my_tuple}")
print(" - Tuple: Las tuplas son inmutables, no se pueden insertar, borrar, actualizar o ordenar elementos.")

# Set
my_set = {5, 3, 1, 4, 2}
print ("\n\n____ SETS ____");

print(f" - Set:\t\t\t\t{my_set}")
my_set.add(8)
print(f" - Set (añado el 8):\t\t{my_set}")
my_set.remove(3)
print(f" - Set (borro el 3):\t\t{my_set}")

print(" - Set: los sets son conjuntos no ordenados y sin elementos repetodos, no se pueden actualizar ni ordenar elementos.")


# Dictionary
my_dict = {'j': 'value1', 'g': 'value2', 'a': 'value3'}
print ("\n\n____ DICTIONARY ____");
print(f" - Diccionario:\t\t\t\t\t{my_dict}")
my_dict['d'] = 'value4'
print(f" - Diccionario (añado el 'f'):\t\t\t{my_dict}")

my_dict.pop('a')
print(f" - Diccionario (borro el 'a' (del o pop)):\t{my_dict}")

my_dict['a'] = 'NUEVO VALOR'
print(f" - Diccionario (actualizo el 'j'):\t\t{my_dict}")

print(" - Diccionario (ordenado):")
for key in sorted(my_dict):
    print(f"\t\t\t - {key}: {my_dict[key]}")  

"""
DIFICULTAD EXTRA (opcional): AGENDA
"""
def agenda():
    
    # Clase Agenda (Dictionary)
    agenda = {}
    
    # Búsqueda de un contacto	
    def search_contact():
        name = input("Introduce el nombre del contacto a buscar: ")
        if name in agenda:
            print(f" -> Contacto encontrado. Nombre: {name} - Teléfono: {agenda.get(name)}")
        else:
            print("El contacto no existe")
    
    # Añadir/Actualizar un contacto
    def insert_contact(update = False):
        if(update):
            name_msg = "Introduce el nombre del contacto a actualizar: "
            tlfn_msg = "Introduce el nuevo teléfono del contacto: "
        else:
            name_msg = "Introduce el nombre del contacto: "
            tlfn_msg = "Introduce el teléfono del contacto: "
            
        name = input(name_msg)
        valid = False
        while(not(valid)):
            phone = input(tlfn_msg)
            if(phone.isdigit() and len(phone) == 9):
                print("Teléfono correcto")
                agenda[name] = phone
                valid = True
            else:
                retry = input(" # Teléfono no valido # ¿Desea volver a intentarlo? (s/n): ")
                if(retry.lower == "n"):
                    valid = True
                else:
                    print("Vuelva a intentarlo...")
    
    # Borrar un contacto
    def delete_contact():
        name = input("Introduce el nombre del contacto a borrar: ")
        if name in agenda:
            agenda.pop(name)
            print(f"Contacto '{name}' borrado")
        else:
            print("El contacto no existe")

    def show_agenda():
        print("Listado de contactos: ")
        for key in agenda:
            print(f"\t - {key}: {agenda[key]}")
        

    # Mostrar menú de la agenda
    def menu():
        print("\n AGENDA DE CONTACTOS\n")
        print("\t 1.- Búsqueda de un contacto")            
        print("\t 2.- Añadir un contacto")            
        print("\t 3.- Actualización de un contacto")            
        print("\t 4.- Borrar un contacto")         
        print("\t 5.- Mostrar agenda (extra)")         
        print("\t 0.- Salir")         
    
        option = input("\nSelecciona una opción: ")
        return option
    
    # Procesar la opción seleccionada
    def process_option(option):
        if(option == "1"):
            search_contact()
        elif(option == "2"):
            insert_contact()
        elif(option == "3"):
            insert_contact(True)
        elif(option == "4"):
            delete_contact()
        elif(option == "5"):
            show_agenda()
        elif(option == "0"):
            print("Saliendo de la agenda...")
        else:
            print("Opción no válida loco!")
        return option
        
    def main():
        option = ""
        while(option != "0"):
            option = menu()
            process_option(option)
        
    main()
    
agenda()

