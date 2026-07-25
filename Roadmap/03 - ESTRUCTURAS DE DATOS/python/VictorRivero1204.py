# Listas

my_list: list= ["Victor", "Jose", "Maria"]
print (my_list)
my_list.append("Daysi") #Inserción
my_list.append("Daysi")
print (my_list)
my_list.remove("Victor") # Eliminacion
print (my_list)
print(my_list[1]) #Acceso
my_list[1] = "Victor" #Actualizacion
print (my_list)
my_list.sort() #Ordenacion
print (my_list)

# Tuplas
my_tuple: tuple = ("Victor", "VictorRivero1204", "23")
print(my_tuple[1]) #Acceso
my_tuple = tuple(sorted(my_tuple)) #Ordenacion
print(my_tuple)

# Sets

my_set: set = {"Victor", "VictorRivero1204", "23"}
print(my_set)
my_set.add("Victor.rivero1204@gmail.com") #Insecion
my_set.add("Victor.rivero1204@gmail.com")
print(my_set)
my_set.remove("Victor") #Eliminacion
print(my_set)
my_set = sorted(my_set) #No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario

my_dict: dict = {
    "name":"Victor", 
    "username":"VictorRivero1204", 
    "correo":"victor.rivero1204@gmail.com", 
    "edad":23
}
print(my_dict)
my_dict["alias"] = "Vitico" #insercion
del my_dict["username"] #Eliminacion
print(my_dict)
print(my_dict["name"]) #Acceso
my_dict["edad"] = 24 #Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items())) #Ordenacion
print(my_dict)
print(type(my_dict))

"""
 EXTRA
"""

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el numero del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <=11:
                agenda[name] = phone
        else:
            print("" \
            "El numero de telefono no puede superar los 11 digitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. insertar contacto")
        print("3. actualizar contacto")
        print("4. eliminar contacto")
        print("5. salir")

        option = input("\nSelecciona una opcion: ")
    
        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"el numero de telefono de contacto {name} es: {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe. ")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input ("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe: ")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto no existe: ")
                pass
            case "5":
                print("Saliendo de la agenda")
                break 
            case _:
                print("Opcion no valida, elija una valida")

my_agenda()