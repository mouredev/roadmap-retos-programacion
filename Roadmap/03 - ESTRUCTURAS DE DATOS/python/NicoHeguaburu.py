#ESTRUCTURA DE DATOS
#lista (list)
lista = [1,2,3,4,5]
lista.append(6) #agregar un elemento a la lista
print(lista)
lista.remove(2) #eliminacion del elemento
print(lista)
lista[0] = 7 #actualizacion del elemento
print(lista)
lista.sort() #orden de los elementos
print(lista)

#tupla (tuple)
tupla = (1,2,3,4) #son inmutables no se pueden modificar
print (tupla)

#diccionario (dict)
diccionario = {
    "Nombre": "Nicolás",
    "Edad": 22,
    "Estatura": 1.87
    }
diccionario["Ciudad"] = "Montevideo"   #agregar un elemento clave-valor
print(diccionario)
diccionario["Edad"] = 23    #actualizacion del valor
print(diccionario["Edad"])
del diccionario["Estatura"]   #eliminacion de clave-valor
print(diccionario)

#Conjunto (set)
conjunto = {1,2,3,4,5} #estructuras desordenadas sin duplicados
conjunto.add(9) #agregar un elemento
print(conjunto)
conjunto.remove(4)
print(conjunto)




# DIFICULTAD EXTRA
# AGENDA

mi_agenda = {}

def agendar():
    nombre = input("nombre:")
    numero = int(input("numero:"))
    while len(str(numero)) != 8:
        print("numero incorrecto")
        numero = int(input("numero:"))
    agendado = {"Nombre": nombre, "Numero": numero}
    mi_agenda[nombre] = agendado
    print("se a agendado correctamente el contacto")



def actualizar():
    nombre_actualizar = input("nombre de contacto a actualizar: ")
    if nombre_actualizar in mi_agenda:
        nuevo_numero = input("Nuevo numero:")
        if len(str(nuevo_numero)) == 8:
            mi_agenda[nombre_actualizar]["Numero"] = nuevo_numero
        else:
            print("numero incorrecto")
    else:
        print("no existe el contacto")


def eliminar():
    nombre_eliminar = input("nombre de contacto a eliminar: ")
    if nombre_eliminar in mi_agenda:
        del mi_agenda[nombre_eliminar]
        print(f"Se a elmiminado el contacto {nombre_eliminar}")
    else:
        print("no existe el contacto")
        
def busqueda():
    nombre_buscar = input("nombre de contacto a buscar: ")
    if nombre_buscar in mi_agenda:
        print(mi_agenda[nombre_buscar])
    else:
        print("no existe el contacto")


def menu():
    print("Menu de la agenda")
    print("1----------Agendar contacto")
    print("2----------Eliminar contacto")
    print("3----------Buscar contacto")
    print("4----------Actualizar contacto")
    print("5----------Salir")

    accion = input()
    if accion == "1":
        agendar()
    elif accion == "2":
        eliminar()
    elif accion == "3":
        busqueda()
    elif accion == "4":
        actualizar()
    elif accion == "5":
        exit()
    else:
        print("Digite un numero valido")
    menu()


menu()


