"""
Estructuras
"""

"""
#Listas
"""

lista_vacia = []
frutas = ["manzana", "naranja", "mandarina", "durazno"]
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
print(animales)
print(animales[2]) #acceder

#Ordenar
animales = tuple(sorted(animales))
print(animales)
