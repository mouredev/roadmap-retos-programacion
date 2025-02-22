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
    
        print("")
        print("Bienvenido a la agenda ¿que quieres hacer?")
        print("")
        print("Buscar")
        print("Insertar")
        print("Actualizar")
        print("Borrar")
        print("Salir")
        print("")

        option=input ("Selecciona una opción: ")

        match option:
                case "Buscar":
                        name=input("Introduce el nombre del contacto que quieres buscar: ")
                        if name in agenda:
                            print("")
                            print(f"El número de {name} es {agenda[name]}")   
                        else:
                               print("")
                               print("El contacto no existe")
                case "Insertar":
                        name=input("Inserte nombre del contacto: ")
                        phone=input("Inserte número de telefono: ")
                        if phone.isdigit() and len(phone)>0 and len(phone)<=11:
                               agenda[name] = phone
                               print("")
                               print("Contacto guardado.")                             
                        else:
                               print("")
                               Print("Error, introduce un número de teléfono correcto")

                case "Actualizar":
                         name=input("Introduce el nombre del contacto que quieres actualizar: ")
                         if name in agenda:
                            phone=input("Inserte nuevo número de telefono: ")
                            if phone.isdigit() and len(phone)>0 and len(phone)<=11:
                               agenda[name] = phone
                               print("")
                               print("Contacto modificado.")                             
                            else:
                               print("")
                               Print("Error, introduce un número de teléfono correcto")  
                         else:
                               print("")
                               print("El contacto no existe")
                case "Borrar":
                         name=input("Introduce el nombre del contacto que quieres borrar: ")
                         if name in agenda:
                            del agenda[name]
                            print("")
                            print("El contacto ha sido borrado")   
                         else:
                               print("")
                               print("El contacto no existe")
                case "Salir":
                         print("")
                         print("Cerrando agenda.")
                         break
                        
                case _:
                        print("")
                        print("Seleccione una opción válida")

agenda()