#LIsts
my_list = ["Tomas","Messi","Ronaldo"]
print(my_list)
my_list.append("Neymar") #Insert
print(my_list)
my_list.remove("Tomas") #Delete
print(my_list)
print(my_list[1]) #Access
my_list[2] = "Mbappe" #Updqate
print(my_list)
my_list.sort() #ordination
print(my_list)
print(type(my_list))

#Tuplas
my_tuple = ("Tomas","Luna","Tomy", "20")
print(my_tuple[1]) #Access
my_tuple = tuple(sorted(my_tuple))#ordination
print(my_tuple)
print(type(my_tuple))

#sets
my_set = {"Tomas","Luna","Tomy", "20"}
print(my_set)
my_set.add("tomlinuxexe@gmail.com")#Insert
print(my_set)
my_set.remove("Luna")#Delete
print(my_set)
my_set = set(sorted(my_set))#It can't be sorted
print(type(my_set))

#Dictionary
my_dict = {"name" :"Tomas",
        "Lastname" : "Luna",
        "alias" : "tomy",
        "age" : "20"
        }
my_dict["emaiol"] = "tomlinuxexe@gmail.com" #insert
print(my_dict)
print(my_dict["name"]) #access
my_dict["age"] = "21" #update
print(my_dict)
del my_dict["Lastname"] #delete
print(my_dict)
my_dict=dict( sorted(my_dict.items())) #order
print( my_dict)
print(type(my_dict))

"""
EXTRA
"""
agenda = {"contacts" : [] }
while True:
    action = input("Desea realizar una accion" \
    " \n1.Agregar" 
    " \n2.Eliminar" 
    " \n3.Actualizar" 
    " \n4.Ordenar "
    " \nSeleccione ")
    
    if action == "1":
                    name = input("ingrese el nombre de contacto: ")
                    number = input("ingrese el numero (solo ingresar 10 digitos) : ")
                    if len(number) == 10 and name != "" and number != "":
                        contacto = {"name" :name,
                                    "number" : number} 
                        agenda["contacts"].append(contacto)
                        print(f"Esta es tu agenda actualmente {agenda}")
                        print("Accion finalizada. Puede seleccionar otra opcion si lo desea")
                        
                    else:
                        print("Los digitos de tu numero sobre pasan o son menores a 10 !Intente de nuevo")
                
                            
    elif action == "2":
        print(f"Estos son tus contactos {agenda}")
        user_drop = input("\ningrese el nombre o numero que desee eliminar ")
        encontrado = False
        for delete in agenda["contacts"]:
            if delete["name"] == user_drop:
                agenda["contacts"].remove(delete)
                print(f"usuario  {delete} se ha elimindado")
                print(f"esta es su agenda actual {agenda}")
                encontrado = True
                break
        if not encontrado :
            print("Uusario no encontrado")
        print("Puede seleccionar otra opcion")
        
    elif action == "3":
        print(f"Estos son tus contactos {agenda}")
        user_ud = input("\ningrese el nombre o numero que desee actualizar ")
        encontrado = False
        for update in agenda["contacts"]:
            if update["name"] == user_ud:
                nameu = input("Ingrese el nuevo nombre: ")
                namberu = input("Ingrese el nuevo numero: ")
                update["name"] = nameu
                update["number"] = namberu
                print(f"usuario  {update} se ha actualizadp")
                print(f"esta es su agenda actual {agenda}")
                encontrado = True
                break
        if not encontrado:
            print("Uusario no encontrado")
        print("Puede seleccionar otra opcion")
    elif action == "4":
        if not agenda["contacts"]:
            print("Su agenda esta vacia")
        else :
            print(f"Esta es su agenda desorneda {agenda["contacts"]}")
            def obtener_name(usuario):
                return usuario["name"]

            agenda["contacts"] = sorted(agenda["contacts"],key=obtener_name)
            print(f"Esta es la agenda ordenada{agenda["contacts"]}")

    else :
        print("Gracias por usar el programa")
        break

"""
Ejercicio de Brais
"""

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
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
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()
