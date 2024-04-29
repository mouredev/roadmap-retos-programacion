#Estructura de Datos

#List
lista: list = [1,3,4,5,7]
lista.append(6) #Inserción
print(lista)
lista.remove(7) #Delete
print(lista)
print(lista[2]) #Acceso
lista[1] = 9    #Actualización
print(lista)
lista.sort()    #Ordenacion
print(type(lista))


#Tuplas (No se pueden agregar ni eliminar)
mytuple: tuple = (1,2,3)
print(mytuple[1]) # Acceso
mytuple = tuple(sorted(mytuple)) # Ordenación
print(mytuple)
print(type(mytuple))


#Sets(No se puede ordenar)
myset: set ={1,2,4,5,6}
myset.add(29) #Inserción
myset.add(29)
print(myset)
myset.remove(2) #Eliminación
print(myset)
print(type(myset))


#Diccionario
mydict:dict = {
    "age": "18",
    "name": "Yenner"
}

mydict["hobby"] = "futbol" #Inserción
print(mydict)
del mydict["age"] #Eliminación
print(mydict)
print(mydict["name"])#Acceso
mydict["age"] = "21" #Actualización
print(mydict)
mydict = dict(sorted(mydict.items())) #Ordenación
print(mydict)
print(type(mydict))



def myagenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el número de contacto:   ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Introduce un número de telefono de almenos 11 digitos")


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

myagenda()



    




 


