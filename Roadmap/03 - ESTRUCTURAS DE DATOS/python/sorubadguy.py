"""
Estructuras
"""

"""
#Listas
"""

lista_vacia = []
frutas = ["manzana", "naranja", "mandarina", "durazno"]
print(lista_vacia)
print(type(frutas))
print(frutas)

#Agregar un elemento al final

frutas.append("melon")
print("\nagrego melon")
print(frutas)

#Agregar un elemento en el lugar deseado
print("\nagrego Anana")
frutas.insert(2, "anana")
print(frutas)

#Eliminar elemento de la lista
print("\nElimino naranja")
frutas.remove("naranja")
print(frutas)

#Ordeno los items de la lista
print("\nOrdeno los elementos de la lista")
frutas.sort()
print(frutas)

#Invierto el orden de los elementos de la lista
print("\nInvierto el orden de los elementos de la lista")
frutas.reverse()
print(frutas)

#Actualizacion
print("\nActualizo el segundo item")
frutas[1] = "pera"
print(frutas)

#Eliminar todos los elementos de la lista
print("\nVacio la lista")
frutas.clear()
print(frutas)

"""
Tuplas
"""

tupla_vacia = ()
animales = ("gato", "perro", "oso")
print(type(animales))
print(tupla_vacia)
print(animales)
print(animales[2]) #acceder

#Ordenar
animales = tuple(sorted(animales))
print(animales)

"""
Set
"""
set_vacio = {}
nombres = {"Lucas","Carlos","Alfredo","Ramon"}
print(set_vacio)
print(type(nombres))
print(nombres)
print(len(nombres))

#Agrego elemento
nombres.add("Alejandro")
print(nombres)

#Quito Elemento
nombres.remove("Carlos")
print(nombres)


"""
Diccionario
"""

diccionario = {
    "nombre" : "Lucas",
    "Apellido" : "Martinez",
    "nick" : "Sorubadguy",
    "edad" : "30"
}

print(f"Diccionario\n{diccionario}")
print(diccionario["nombre"])#Acceso
diccionario["edad"] = 31 #actualizacion
print(diccionario)
diccionario["idioma"] = "español" #Agregar item
print(diccionario)
diccionario.pop("edad") #Eliminar item
print(diccionario)
diccionario.clear() #Limpiar diccionario
print(diccionario)

"""
Extra
"""

def agenda():
    op = 0

    while(op != 5):
        print(f"Ingrese la opcion deseada")
        print(f"1: Buscar contacto")
        print(f"2: Agregar contacto")
        print(f"3: Eliminar contacto")
        print(f"4: Actualisar Contacto")
        op = input("Ingrese la opcion deseada\n")

        match op:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case _:
                print("Opcion no encontrada")
    

def agregar_contacto(nombre, numero):
    pass

def eliminar_contacto():
    pass

def buscar_contacto():
    pass

def actualizar_contacto():
    pass