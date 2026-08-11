#lista
from ast import Del
from optparse import Option
from os import name


my_list: list = [1,2,3]
print(my_list)
my_list.append(4) #insercion
print(my_list)
my_list.remove(4) #eliminacion
print(my_list)
print(my_list[1]) #Acceso
my_list[1]= 7 #actualizacion
print(my_list)
my_list.sort() #ordenacion
print(my_list)
print(type(my_list))

#turpias
my_turpias = [1,2,3]
print(my_turpias)
print(my_turpias[1])
print(my_turpias[2])
print(type(my_turpias))
my_tuple = tuple(sorted(my_turpias)) #ordenacion
print(my_tuple)
print(type(my_tuple))


#sets
my_set = {"moure","maria","brais"}
print(my_set)
my_set.add("Brais")#insercio
print(my_set)
my_set.remove("moure")#eliminacion
print(my_set)
print(type(my_set)) 
my_set = set(sorted(my_set))# no se puede ordenar
print(my_set)

print(type(my_set))

#Diccionario
my_dict: dict = {
    "name":"brais",
    "surname":"moure",
    "age":"36"
}

print(type(my_dict))

my_dict["email"] = "mouredev@gmail.com" #insercion 
print(my_dict["name"])
del my_dict["surname"] #eliminacion
print(my_dict)
print(my_dict["name"]) #acceso
my_dict["age"] = "37" #actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # ✅ Correcto
print(my_dict)
print(type(my_dict))


""" 
extra
"""
def insert_contact(agenda):
    phone = input("Introduce el teléfono del contacto: ")
    if phone.isdigit() and len(phone) > 0 and len(phone)<= 11:
        agenda[name] = phone
    else:
        print("debes introducir un numero de telefono un maximo de 11 digitos.")


def my_agenda():
    agenda = {}

    while True:

        print("")
        print("1.insertar contacto")
        print("2.buscar contacto")
        print("3.actualizar contacto")
        print("4.eliminar contacto")
        print("5.salir")

        Option = input("selecciona una opcion:")

        match Option:
            case "1":
                name = input("introduce el nombre de contacto de busqueda:")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")

            case "2":
                name = input("\nIntroduce el nombre del contacto a buscar: ")
                insert_contact(agenda)
                
            case "3":
                name = input("introduce el nombre de contacto actualizar:")
                if name in agenda:
                    insert_contact(agenda)
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("introduce el nombre de contacto a eliminar:")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
                pass
            case "5":
                print("saliendo de la agenda.")
                pass
            
        break

    print("Option no valida.Elige una opcion del 1 al 5.")

my_agenda()