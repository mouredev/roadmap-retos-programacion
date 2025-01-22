'''
Estructuras
'''
# Listas se crea con []
list_A=["Dani", "Rojas", "DaniRojasDev"]
print (type(list_A))
print(list_A)
        # Indice
print(list_A[0])
print(list_A[1])
print(list_A[2])
        #Reemplazo
list_A[2]="danirojas@gmail.com"
print(list_A)
list_A[2]="DaniRojasDev"
        #Inserción
list_A.append("34") # Al final de la lista
list_A.insert(3, "danirojas@gmail.com") #En la posición que le indicamos
print(list_A)
        #Borrado
list_A.remove("danirojas@gmail.com")
print (list_A)
        #ordenación
list_A.sort()
print(list_A)

print (type(list_A))

# Tuplas se crea con ()
tuple_A=("Dani", "Rojas", "DaniRojasDev")
print (type(tuple_A))
print (tuple_A)
        # Indice
print(tuple_A[0])
print(tuple_A[1])
print(tuple_A[2])
        #Reemplazo
#tuple_A[2]="danirojas@gmail.com"     no se puede realizar en una tupla

        #Inserción
#tuple_A.append("34") # Al final de la lista    no se puede realizar en una tupla
#tuple_A.insert(3, "danirojas@gmail.com") #En la posición que le indicamos       no se puede realizar en una tupla

        #Borrado
#tuple_A.remove("danirojas@gmail.com")     no se puede realizar en una tupla

        #ordenación
tuple_A=(sorted(tuple_A))
print(tuple_A)

print (type(tuple_A))

# Diccionario se crea con {} y hay que añadir "key":"valor"
dictionary_A={"Name": "Dani", "Surname":"Rojas", "Alias":"DaniRojasDev"}
print (type(dictionary_A))
print (dictionary_A)
        # Indice
print(dictionary_A["Name"])   #En lugar de buscar por posición se busca por palabra clave (key)
print(dictionary_A["Surname"])    #En lugar de buscar por posición se busca por palabra clave (key)
print(dictionary_A["Alias"])    #En lugar de buscar por posición se busca por palabra clave (key)
        #Reemplazo
dictionary_A["Alias"]="danirojas@gmail.com"
print(dictionary_A)
dictionary_A["Alias"]="DaniRojasDev"
        #Inserción
dictionary_A["Email"] = "danirojas@gmail.com" # En orden alfabetico
print(dictionary_A)
        #Borrado
del dictionary_A["Email"]
print (dictionary_A)
        #ordenación
dictionary_A=dict(sorted(dictionary_A.items()))
print(dictionary_A)

print (type(dictionary_A))


# Set da igual el orden al meter los datos porque los ordena como quiere se crea también con {}
set_A={"Dani", "Rojas", "DaniRojasDev"}
print (type(set_A))
print (set_A)
        #Inserción
set_A.add("34") 
print(set_A)
        #Borrado
set_A.remove("34")
print (set_A)
        #ordenación
set_A = set(sorted(set_A))  # No se puede ordenar
print(set_A)

print(type(set_A))

print(" ")
print(" ")
'''
Extra
'''
print("Esta es la parte extra")
print(" ")

def agenda():

    agenda={}

    while True:
        
        print ("\nQue quieres hacer?")
        print ("1. Buscar contacto")
        print ("2. Insertar contacto")
        print ("3. Actualizar contacto")
        print ("4. Eliminar contacto")
        print ("5. Salir") 

        option=input("\nSelecciona una opción:")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto que quieres buscar: ")
                if name in agenda:
                    print(f"El número de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe") 

            case "2":
                name =input("Introduce el nombre del contacto: ")
                phone =input("Introduce el telefono del contacto: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                    print("el contacto se ha guardado")
                else:
                    print("Error. Introduce un número correcto")            
            case "3":
                pname = input("Introduce el nombre del contacto que quieres actualizar: ")
                if name in agenda:
                    phone =input("Introduce el telefono del contacto: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                        print("el contacto se ha guardado")
                    else:
                        print("Error. Introduce un número correcto") 
                else:
                    print(f"El contacto {name} no existe") 
                
            case "4":
                name = input("Introduce el nombre del contacto que quieres eliminar: ")
                if name in agenda:
                    del agenda [name]
                    print(f"El contacto de {name} ha sido eliminado")
                else:
                    print(f"El contacto {name} no existe") 
            case "5":
                print("Cerrando agenda")
                break 
            case _:
                print("Elige una opción válida")

agenda()

