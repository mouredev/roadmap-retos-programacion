#Listas
print("----LISTAS----")

lista = [1, 2, 3, 4, "hola"]
print(lista)

#Eliminación  de datos de una lista
del lista[4]
print(f"Hemos eliminado un dato de la lista {lista}")

#Añadir elementos al final de una lista
lista.append(28)
print(f"Elemento añadido al final de la lista {lista}")

#Añadir una lista a la lista inicial
lista.extend([6,100])
print(f"Nueva lista añadida a la lista inicial {lista}")

#Añadir un dato en el indice indicado
lista.insert(1, 255)
print(f"Elemento añadido en la posicion [1] de la lista {lista}")

#Borrado de un elemento de una lista
lista.remove(3)
print(f"Borrado de un elemento de la lista {lista}")

#Eliminación por defecto del último elemento de una lista
lista.pop()
print(f"Eliminación por defecto del último elemento de la lista {lista}")

#Invertir el orden de la lista
lista.reverse()
print(f"Lista en orden inverso {lista}")

#Ordena los elementos de la lista de menor a mayor por defecto
lista.sort()
print(f"Ordenados los elementos de la lista de menor a mayor {lista}")

#Ordena los elementos de la lista de mayor a menor
lista.sort(reverse=True)
print(f"Ordenados los elementos de la lista de menor a mayor {lista}")

print("----SET----")

conjunto = {5, 4, 6, 8, 8, 1}
print(conjunto)

#Añadir elemento
conjunto.add("Python")
print(f"Añadir elemento en un set {conjunto}")

#Eliminar elemento indicado
conjunto.remove(5)
print(f"Eliminación del elemento indicado {conjunto}")

#Eliminación aleatoria de un elemento
conjunto.pop()
print(f"Eliminación aleatoria de un elemento {conjunto}")

#Actualización de los elementos
conjunto.update({"Manzana", 34, True})
print(f"Actualización de los elementos del set {conjunto}")

#Eliminación de todos los elementos
conjunto.clear()
print(f"Eliminación de todos los elementos {conjunto}")

print("----TUPLAS----")

tupla = (1, 2, 3)
print(f"{tupla}\n Las tuplas son una lista de valores inmutables, con lo cual no se le pueden hacer ninguna operación de insercción, borrado, actualización y ordenación")  

print("----DICCIONARIOS----")

diccionario = {
    "nombre": "Mario",
    "edad": 33,
    "altura": 1.80,
    "developer": True 
}
print(diccionario)

#Inserción de valores del diccionario
diccionario["telefono"] = 123456789
print(f"Se ha modificado el valor de la clave nombre del diccionario {diccionario}")

#Eliminar la key indicada del diccionario
diccionario.pop("altura")
print(f"Se elimina una key del diccionario {diccionario}")

#Eliminar de forma aleatoria un elemento del diccionario
diccionario.popitem()
print(f"Eliminación aleatoria de un elemento del diccionario {diccionario}")

#Actualizar diccionario con otro diccionario
diccionario1 = {
    "lenguajes": ["python", "js", "html", "css"]
}

diccionario.update(diccionario1)
print(f"Actualizado de un diccionario con otro diccionario {diccionario}")

#Eliminar todo el contenido del diccionario
diccionario.clear()
print(f"Eliminamos todo el contenido del diccionario {diccionario}")

print("----EXTRA----")

def contact_list():
    
    #Creamos un diccionario, que contendra el nombre y el teléfono de los contactos
    agenda = {
    "Mario": 123456678,
    "Sara": 1423423435
    }

    #Creamos un variable booleana para poder controlar el bucle del menu de opciones
    leave = True

    #Creamos bucle que contentra el menu de opciones
    while leave == True:

        #Mostramos las opciones del menu y preguntamos al usuario que desea hacer
        print("1 - Búsqueda de contacto\n2 - Añadir contacto\n3 - Actualizar contacto\n4 - Eliminar contacto\n5 - Salir")
        ask = input("¿Qué desea hacer? ")
        answer = int(ask)

        #Dependiendo de la opción seleccionada el menu entrará en dicha opción
        if answer == 1:
            #Se introduce por consola el nombre del usuario a buscar
            search = input("Introduce el nombre del contacto a buscar ")
            try:
                print(agenda[search])
            except KeyError:
                print("Usuario no encontrado")
        elif answer == 2:
            #Añadimos el nombre y el número de teléfono del nuevo contacto
            add = input("Añade el nombre del nuevo contacto ")
            condition = True
            #Si el número de teléfono no tiene 9 dígitos o no es un número, se le pedirá al usuario que vuelva a introducir el número
            while condition == True:
                number = input("Añade el número de teléfono ")
                if len(number) == 9:
                    try:
                        agenda[add] = int(number)
                        print("Añadido el contacto")
                        condition = False
                    except ValueError:
                        print("No has introducido un número")
                else:
                    print("La longitud del número es menor o superior a 9 dígitos")
        elif answer == 3:
            #Se pide por consola el nombre del contacto y el número de teléfono que se actualizará
            update_name = input("Añade el nombre del contacto ")
            update_phone = input("Añade el número de teléfono a actualizar ")
            agenda[update_name] = update_phone
            print("Actualizado el número de teléfono del contacto")
        elif answer == 4:
            #Se pide por consola el nombre del contacto a eliminar
            remove = input("Añade el nombre del contacto a eliminar ")
            agenda.pop(remove)
            print(f"Eliminado el contacto de {remove}")
        elif answer == 5:
            #Finaliza el programa
            leave = False
        else:
            print("Introduce un número entre 1 y 5")

contact_list()

