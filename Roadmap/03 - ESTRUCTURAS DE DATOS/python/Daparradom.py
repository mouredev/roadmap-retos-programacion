### Estructuras de Datos ###


mi_list = ["David","Parrado", 28 , False] # Lista esta compuesta por elementos ordenados, heterogeneos y mutables

mi_tupla = ("David","Parrado", 28 , False) # Compuesta por datos ordenados, heterogeneos pero no mutables

mi_set = set(["David","Parrado", 28 , False, False]) # Compuesto por datos no ordenados, heterogeneos, mutable, sin repeticion

mi_dict = {"Nombre":"David", "Apellido" :"Parrado","Edad":28, "Casado" : False} # datos No ordenados, Heterogenea , Mutable, clave : valor

print(mi_list)

# Metodos y modificaciones para listas

mi_list[0] = "Alexander" #Cambia el valor de la posicion 0 de la lista
mi_list.append("Mora") #Agrega un elemento al final de la lista
mi_list.count("David") #CUenta el numero de veces que se repite un elemento
mi_list. index("Parrado") #Devuelve el indice de la primera aparicion de un elemento
mi_list.remove(28) #Elimina la primera aparicion de un elemento
mi_list.insert(4,"Azul") #Agrega elemento en el indice dado
mi_list.pop() #Elimina el ultimo dato de la lista y lo retorna
#mi_list.sort() #Ordena la lista de acuerdo a parametros de ordenacion
other_list = [6,7,2,3,5,1,9,-4]
other_list.sort()
print(other_list)
other_list.reverse() #Ordena la lista al reves
print(other_list)

#Metodos y modificaciones para tuplas

mi_tupla.count(False)
mi_tupla.index(False)
mi_tupla[2] #Acceso al elemento ubicado en el indice 2

#Metodos y modificaciones para sets

mi_set.add(10)
mi_set.remove(False)
mi_set.clear()

#Metodos y modificaciones para diccionarios

mi_dict.keys() #Devuelve una lista con las claves
mi_dict.values() #Devuelve una lista con los valores
mi_dict.items() # Devueleve una lista de tuplas con clave y valor
mi_dict.pop("Casado")
print(mi_dict)

def mis_contactos():
    mis_contactos = {}
    while True :
        print ("Bienvenido al menu de tus contactos")
        opcion = input("Escoge la opcion  que desees llevar a cabo:\n b : Buscar contacto\n a: Agregar contacto\n ac : Actualizar contacto\n e : eliminar contacto\n S: Salir\n")
        if opcion == "a" :
            print ("Usted ha seleccionado agregar contacto, el numero debe ser de diez digitos")
            name= input("Ingrese nombre del contacto nuevo: ")
            number= input("Ingrese el numero: ")
            if len(number) != 10 and type(number) != int:
                print("Debe ingresar un numero tipo int de 10 digitos")
            else :
                mis_contactos[name] = number
                print("El contacto se ha agregado con exito" , mis_contactos)
        elif opcion == "b" :
            print ("Usted ha seleccionado buscar contacto")
            name= input("Ingrese nombre del contacto: ")
            validacion = name in mis_contactos 
            if validacion == True :
                print(f"El numero de {name} es {mis_contactos[name]}")
            else :
                print("El contacto no existe")
        elif opcion == "ac" :
            print ("Usted ha seleccionado actualizar contacto")
            name = input("Ingrese el nombre del contacto a actualizar: ")
            validacion = name in mis_contactos 
            if validacion == True :
                number= input("Ingrese numero nuevo: ")
                mis_contactos[name] = number
                print("El contacto se ha modificado con exito" , mis_contactos)
            else :
                print("El contacto no existe")
        elif opcion == "e" :
            print ("Usted ha seleccionado eliminar contacto")
            name= input("Ingrese el nombre del contacto a eliminar: ")
            validacion = name in mis_contactos 
            if validacion == True :
                del mis_contactos[name]
                print("El contacto se ha eliminado con exito" , mis_contactos)
            else :
                print("El contacto no existe")
        elif opcion == "S":
            print("Has salido de tu agenda exitosamente, a continuacion se muestra tu agenda")
            print(mis_contactos)
            break
        else : 
            print("No ha ingresado la opcion correctamente")

        




mis_contactos()

