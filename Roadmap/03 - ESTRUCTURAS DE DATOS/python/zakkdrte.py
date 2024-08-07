
# ESTRUCTURAS DE DATOS

#   EJERCICIO:
#   - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#   - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  
#   DIFICULTAD EXTRA (opcional):
#   Crea una agenda de contactos por terminal.
#   - Debes implementar funcionalidades de búsqueda, inserción, actualización
#    y eliminación de contactos.
#   - Cada contacto debe tener un nombre y un número de teléfono.
#   - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#     y a continuación los datos necesarios para llevarla a cabo.
#   - El programa no puede dejar introducir números de teléfono no númericos y con más
#     de 11 dígitos (o el número de dígitos que quieras).
#   También se debe proponer una operación de finalización del programa.
 
# LISTS #


my_list:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"MY LIST:\n{my_list}")
print(f"Su length: {len(my_list)}")
print(f"Su type: {type(my_list)}")

# OPERATIONS WITH LIST #

# add a item in the list
my_list.append(11) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(my_list)

# count times that it's in the list     # [1{0}, 2{1}, 3{2}, 4{3}, 5{4}, 6{5}, 7{6}, 8{7}, 9{8}, 10{9}, 11{10}]       position ==> {}
print(my_list.count(5)) #   ==> 1

# search index of item  # [1{0}, 2{1}, 3{2}, 4{3}, 5{4}, 6{5}, 7{6}, 8{7}, 9{8}, 10{9}, 11{10}]       position ==> {}
print(my_list.index(5)) # ==> 4

# extend a list adding another list in its
my_list.extend(my_list)
print(my_list)      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# insert a item in a position and move all items to the right
my_list.insert(0,0) # # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(my_list)

# Do a pop to a item for a index
my_list.pop(-1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

# reverse the list
my_list.reverse()   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(my_list)

# remove one item
my_list.remove(0)   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(my_list)

# delete item or items from a list
del my_list[:11]    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(my_list)

# sorted a list
my_list.sort()  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

# clear a list 
my_list.clear() # []
print(my_list)

## CREATING A LIST COMPREHENSION ## 

# creatind with fot into the list
list_with_for:list = [i for i in range(1,21)]
print(list_with_for)
print(f"Su length: {len(list_with_for)}")
print(f"Su type: {type(list_with_for)}")

# creating without for into the list

other_list_with_for:list = []

for i in range(1, 21):
    other_list_with_for.append(i)

print(other_list_with_for)
print(f"Su length: {len(other_list_with_for)}")
print(f"Su type: {type(other_list_with_for)}")


## TUPLES ##

my_tuple:tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_other_tuple:tuple = (1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10)
print(my_tuple)
print(f"Su length: {len(my_tuple)}")
print(f"Su type: {type(my_tuple)}")

print(f"Searching which ocurrences there is in the tuple with the item ==> (5)\nMy First Tuple: {my_tuple.count(5)}\nMy Second Tuple:  {my_other_tuple.count(5)}")

print(my_tuple.index(7))


## SETS ##

my_set:set= {2, 5, "rodrigo","ricardo"}
print(type(my_set))

my_set.add("roberto")
print(my_set)

my_set_comprehension:set = {i for i in range(1, 21)}
print(my_set_comprehension)

print(my_set.difference(my_set_comprehension))

my_set.remove("ricardo")
print(my_set)

print(my_set.intersection(my_set_comprehension))

my_set.clear()
print(my_set)


## DICITONARIES ## 
my_dict = {"username":"roberto","email":"robertogzz@gmail.com","password":"roberto123456789","url_site":"https://www.robertogzz.com/home/"}
print(f"Su type: {type(my_dict)}")

print(f"obteniendo el email: {my_dict.get("email")}")

print(my_dict.items())

print(my_dict.values())

print(my_dict.keys())

print(my_dict.fromkeys(my_dict,"jajajajaja XD"))

my_dict.popitem()
print(my_dict)
my_dict.popitem()
print(my_dict)

my_dict.pop("email")
print(my_dict)

my_dict.clear()
print(my_dict)


## EXTRA ## 




contacts_agenda: list = [{"name":"Juan","phone_number":8125562398},
                        {"name":"Gerardo","phone_number":8123489756},
                        {"name":"Lucas","phone_number":8153846379},
                        {"name":"Rodrigo","phone_number":8158251008}]

def check_number(number: int):
    if type(number) == int:
        number = str(number)
        if len(number) == 10:
            number = int(number)
            return True
    else:
        return False
    
def verification_user(phone_number: str):
    for i in contacts_agenda:
        if phone_number in i.values() :
            
            return False
        else:
            return True

def creat_function(name: str = None, phone_number: str = None):
    name = input("WRITE NAME:\n")
    phone_number = input("WRITE PHONE NUMBER:\n")
    phone_number = int(phone_number)
    def checking_contact(contacts_agenda):    
        if verification_user(phone_number):
            contacts_agenda.append({"name":name,"phone_number":phone_number})
            return contacts_agenda
        else:
            print("THERE'S A USER WITH THIS PHONE NUMBER")
            return do_it()
    if check_number(phone_number):
        return checking_contact(contacts_agenda)   
    else:
        return print("THE NUMBER IS BIGGER THAN NORMAL, OR ISN'T OF TYPE INT")

def read_function(number_or_name: str = None, data: str = None):
    number_or_name = input("write how do you wanna find the contact:==> [name/phone]\n")
    number_or_name.lower()
    
    if number_or_name == "phone":
        data = input("WRITE THE PHONE NUMBER'S CONTACT THAT DO YOU WANNNA FIND:\n")
        data = int(data)
        try:
        
            contact = (filter(lambda number: number["phone_number"] == data, contacts_agenda))
            contact_list = list(contact)
            return contact_list
        except:    
            return "NO SE ENCONTRO NINGUN USUARIO", do_it()
        
    elif number_or_name == "name":
        data = input("WRITE THE NAME'S CONTACT THAT DO YOU WANNNA FIND:\n")
        data = data.capitalize()
        try:
        
            contact = (filter(lambda name: name["name"] == data, contacts_agenda))
            contact_list = list(contact)
            return contact_list
        except:    
            return "NO SE ENCONTRO NINGUN USUARIO", do_it()
    else:
        print("You don't write the correct word or you write nothing")
        input("sou yo stil want to find some contact? ==> [yes/not]\n")
        if "yes":
            return read_function()
        elif"not":
            return do_it()

def update_function():
    data = input("write the phone number from the contact that do you want to edit:\n")
    data = int(data)
    contact = (filter(lambda number: number["phone_number"] == data, contacts_agenda))
    contact = list(contact)
    if contact:
        print(f'This is the contact:\n{contact}')
        choice_value = input("what do you want to edit in this contact: ==> [name/phone/both]\n")
        if choice_value == "name":
            name = input("What will be your new name?:\n")
            contact[0].update({"name":name})
            return contact 
        
        elif choice_value == "phone":
            phone = input("What will be your new phone?:\n")
            contact[0].update({"phone_number":phone})
            return contact
        elif choice_value == "both":
            name = input("What will be your new name?:\n")
            phone = input("What will ber your new phone?:\n")
            contact[0].update({"name":name,"phone_number":phone})
            return contact

            
        print("There's not this contact")
        return do_it()

def delete_function():
    data = input("write the phone number from the contact that do you want to delete:\n")
    data = int(data)
    
    for item in contacts_agenda:
        if data in item.values():
            contacts_agenda.remove(item)
            return contacts_agenda
        else:
            print("there is not a contact's number with this phone number")
            return delete_function()
        
def do_it(parameter:str=None):
    yes_or_not:str = None
    parameter = input("WHAT DO YOU WANNA DO?:   ==> CRUD(Creat, Read, Update, Delete)\n")
    parameter = parameter.capitalize()
    if parameter == "Creat":
        return creat_function()
    elif parameter == "Read":
        return read_function()
    elif parameter == "Update":
        return update_function()
    elif parameter == "Delete":
        return delete_function()
    else:
        print("PLEASE WRITE THE FUNCTION THAT DO YOU WANNA DO\n IF YOU WANNA WRITE AGAIN WRITE (YES) AND IF YOU DON'T WANT WRITE (NOT) OR JUST IGNORE IT")
        yes_or_not = input("")
        if yes_or_not == "yes":
            return do_it()
        else:
            pass
            
   
print(do_it())