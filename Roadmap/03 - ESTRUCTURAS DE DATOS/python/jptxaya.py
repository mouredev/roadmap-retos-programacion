#Estructuras de datos

#Listas
print("Listas")
my_list = [3,4,"Lista"]

#CRUD on List
my_list2 = list()
#Insert
my_list2.insert(0,"Dato_0")
print(my_list2)
my_list2.append("Dato Final")
print(my_list2)
my_list2.insert(1,"Dato_1")
print(my_list2)
#Update
my_list2[1] = "Dato_1_update"
print(my_list2)
#Remove
my_list2.remove("Dato Final")
print(my_list2)
#Read
print(my_list2[0])
#Sort
my_list2.append("Aa")
my_list2.sort()
print(my_list2)

#Tuplas
print("Tuplas")
#Create
my_tupla = ("dato1","dato2","aato3")
print(my_tupla)
#Read
print(my_tupla[1])
#No permite operaciones Insert,Append,Delete ni Sort

#Set
print("Sets")
my_set = {"set1","set2","set3"}
print(my_set)
#Insert
my_set.add("set4")
print(my_set)
my_set.add("set4") #Solo permite valores unicos
print(my_set)
#Read
for elem in my_set:
    print(elem)
#Remove
my_set.remove("set4")
print(my_set)
#No update

#Dictionaries
print("Dictionaries")

my_dict = {"k0":"value0","k1":"value1","k2":"value2"}
print(my_dict)

#Read
print(my_dict["k1"])
print(my_dict.get("k1"))

#Insert
my_dict["k4"] = "new_value1"
print(my_dict)

#Update
my_dict.update({"k5":"new_value5"}) #Es un insert
print(my_dict)

my_dict.update({"k5":"update_value5"}) #Es un update
print(my_dict)

#Delete
del my_dict["k4"]
print(my_dict)
#or
my_dict.pop("k5") #Devuelve el valor
print(my_dict)

#Dificultad Extra
import re


def validar_numtlfno( num ):
    if re.search("^[0-9]{1,11}$",num):
        return True
    else:
        return False


my_contact = {}
while True:
    print("AllContacts")
    print(my_contact)
    print("Introducir la opcion seleccionada:")
    print("1- Añadir Contacto")
    print("2- Consultar Contacto")
    print("3- Modificar Contacto")
    print("4- Borrar Contacto")
    print("5- Salir")
    option = input("Selecciona una opcion:")
    match option:
        case "5":
            break
        case "1":
            num_tlfno = input("Introducir numero de telefono:")
            if validar_numtlfno(num_tlfno):
                nombre = input("Introducir nombre:")
                my_contact[num_tlfno] = nombre
            else:
                print("Formato incorrecto. El numero de telefono tiene que ser un numero de 1 a 11 digitos")
        case "2":
            print("Que desea realizar:")
            print("1-Buscar por numero de telefono")
            print("2-Buscar por nombre de contacto")
            find_option = input("Seleccione la opcion:")
            match find_option:
                case "1":
                    find_num_tlfno = input("Introduce el número de telefono a buscar:")
                    if my_contact.get(find_num_tlfno):
                        print(f"***Telefono:{find_num_tlfno} Nombre:{my_contact.get(find_num_tlfno)}")
                    else:
                        print("Ningun contacto encontrado")
                case "2":
                    find_contact = input("Introduce el nombre del contacto:")
                    cont = 0
                    for elem in my_contact.items():
                        if elem[1] == find_contact:
                            cont += 1
                            print(f"***Telefono:{elem[0]} Nombre:{elem[1]}")
            
                    print(f"Telefonos encontrados: {cont}")
        case "3":
            find_num_tlfno = input("Introduce el número de telefono a modificar:")
            if my_contact.get(find_num_tlfno):
                new_contact = input("Introduce nuevo nombre de contacto")
                my_contact[find_num_tlfno] = new_contact
            else:
                print("Ningun contacto encontrado para modificar")
        case "4":
            find_num_tlfno = input("Introduce el número de telefono a borrar:")
            if my_contact.get(find_num_tlfno):
                 my_contact.pop(find_num_tlfno)
            else:
                print("Ningun contacto encontrado para borrar")












