# @author: Mhayhem

# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.

""" list """
# crear una lista

my_list = ["Dany", "Mhayhem", "Python", "Valladolid"]
my_list_2 = list([21, 3, 99, 1, 0, 10])

# acceder a un elemento dentro de la lista

print(my_list[2]) # se accede através de su índice (en programción el primero es el 0) => python

# añadir un elemento al final de la lista

my_list.append("España")
print(my_list) # ['Dany', 'Mhayhem', 'python', 'valladolid', 'España']

# insertar un elemento en una posición concreta

my_list.insert(0, "Humano")
print(my_list) # ['humano', 'Dany', 'Mhayhem', 'python', 'valladolid', 'España']

# actualizar un elemento

my_list[0] = "Alien"
print(my_list) # ['Alien', 'Dany', 'Mhayhem', 'python', 'valladolid', 'España']

# eliminar un elemento

my_list.remove("España")
print(my_list) # ['Dany', 'Mhayhem', 'python', 'valladolid'] 

# eliminar el ultimo elemento

my_list.pop() # también podrias elegir el índice a eliminar => my_list.pop(2)
print(my_list) # ['Dany', 'Mhayhem', 'python'] 

# eliminar toda la lista

my_list.clear() 
print(my_list) # []

# ordenar una lista

my_list_2.sort() 
print(my_list_2) # [0, 1, 3, 10, 21, 99] si usamor sort(reverse=True) se ordenaría al contrario

""" tuple """
# crear una tupla

my_tuple = ("Dany", 42)
my_tuple_2 = tuple(["Mhayhem", "Python"])

# acceder a un elemento dentro de la tupla
print(my_tuple[0]) # Dany

""" las tuplas son inmutables, por lo que no se puede ni añadir ni eliminar elementos 
ni actualizarlas, para eso habría que convertirlas a listas y retornarlas a tuplas """

""" set """
# crear un set
my_set = {"Dany", "Mhayhem", "Valladolid"}
my_set_2 = set(["Python", "Java", "C++"])

""" los set no tienen orden especifico, no se puede acceder a los elementos através de índices, tampoco se pueden duplicar elementos """

# añadir un elemento

my_set.add("España") # se añade un elemento al final, no se puede elegir la posición
print(my_set) # se imprime sin orden 

# eliminar un elemento

my_set.remove("España")
print(my_set) 
my_set_2.discard("Go") # discard() no daría error si el elemento ha borrar no existe, remove() si daría error
print(my_set_2)
my_set_2.pop() # pop() borraría un elemento al azar, ya que no estan ordenados
print(my_set_2)

# actualizar mediante asignación no se podría, podiamos usar update() para actualizarlo con otra estructura iterable
my_set_2.update(my_set)
print(my_set_2)

# elimminar todo el set

my_set_2.clear()
print(my_set_2) 

""" dict """
# crear un dict
my_dict = {"name": "Dany", "alias":"Mhayhem"}
my_dict_2 = dict([("name", "Dany"),("alias", "Mhayhem")])
my_dict_3 = dict(name="Dany", alias="Mhayhem")

# acceder a un valor

print(my_dict["alias"])

# añadir elemento
my_dict["city"] = "Valladolid"
print(my_dict) # {"name": "Dany", "alias":"Mhayhem", "city": "Valladolid"}

# actualizar elemento

my_dict["city"] = "Madrid"
print(my_dict) # {"name": "Dany", "alias":"Mhayhem", "city": "madrid"}
my_dict_2.update({"city":"Valladolid"})
print(my_dict_2) # {"nombre": "Dany", "alias":"Mhayhem", "city": "Valladolid"}

my_dict_2.pop("alias")
print(my_dict_2) # {"name": "Dany"} 

# eliminar todo el dict

my_dict_3.clear()
print(my_dict_3) # {}
""""""

""" hay una plabra reservada para hacer una eliminación completa, incluida la referencía en memoría, del: del my_dict"""
# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.

""" Extra """

# comprobar que la longitud del número sea 11 y que sean solo dígitos
def checking_phone_num():
    while True:
        try:
            num = int(input("Número de telélefono: \n"))
            lenError = len(str(num)) != 11
        except ValueError:
            print("Solo admite números")
        if not lenError:
            break
        else:
            print("La longitud del número debe ser de 11 dígitos")
    return num
            
# guardar nombre delccontacto
def contact_name():
    return input("Nombre del contacto: \n").capitalize()
        

# crear contacto e insertarlo a la agenda
def create_contact(book_contact):
    name = contact_name()
    phone_num = checking_phone_num()
    book_contact.update({name: phone_num})
    print("contacto creado") 
    return book_contact
    
 # actualizar contacto   
def update_contact(book_contact):
    name = contact_name()
    if name not in book_contact.keys():
        print("El contacto no existe")
    else:    
        phone_num = checking_phone_num()
        book_contact[name] = phone_num
        print(f"Contacto actualizado: {name}: {book_contact[name]}")
    return book_contact

# buscar contacto
def serching_contact(book_contact):
    name = contact_name()
    if name in book_contact.keys():
        print(f"{name}: {book_contact[name]}")
    else:
        print("El contacto no existe")
         
# borrar contacto
def delete_contact(book_contact):
    name = contact_name()
    if name not in book_contact.keys():
        print("El contacto no exisate")
    else:
        book_contact.pop(name)
        print(f"Contacto {name} ha sido elíminado")
    return book_contact

def contact_phone():
    book_contact= {}
    if not book_contact:
        print("La agenda esta vacía, cree un nuevo contacto")
        create_contact(book_contact)
    while True:
        option = input("Que operación quiere realizar: [C]rear, [A]ctualizar, [B]uscar, [E]liminar, [S]alir\n").lower()
        match option : # es el switch de JS
            case "s":
                print("Cerrando prógrama")
                break
            case "c":
                create_contact(book_contact)
            case "a":
                update_contact(book_contact)
            case "b":
                serching_contact(book_contact)
            case "e":
                delete_contact(book_contact)
            case _: # seria como un else
                print("Opción no válida")
            
    
    print(book_contact)

        
contact_phone()