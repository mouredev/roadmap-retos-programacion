"""
Estructuras
"""

"""
#Listas
"""

lista_vacia = []
frutas = ["manzana", "naranja", "mandarina", "durazno"]

for i in range(0, len(frutas)):
    print(frutas[i])

#Agregar un elemento al final

frutas.append("melon")
print("\nagrego melon")
for i in range(0, len(frutas)):
    print(frutas[i])

#Agregar un elemento en el lugar deseado
print("\nagrego Anana")
frutas.insert(2, "anana")
for i in range(0, len(frutas)):
    print(frutas[i])

#Eliminar elemento de la lista
print("\nElimino naranja")
frutas.remove("naranja")
for i in range(0, len(frutas)):
    print(frutas[i])

#Ordeno los items de la lista
print("\nOrdeno los elementos de la lista")
frutas.sort()
for i in range(0, len(frutas)):
    print(frutas[i])

#Invierto el orden de los elementos de la lista
print("\nInvierto el orden de los elementos de la lista")
frutas.reverse()
for i in range(0, len(frutas)):
    print(frutas[i])

#Actualizacion
print("\nActualizo el segundo item")
frutas[1] = "pera"
for i in range(0, len(frutas)):
    print(frutas[i])

#Eliminar todos los elementos de la lista
print("\nVacio la lista")
frutas.clear()
for i in range(0, len(frutas)):
    print(frutas[i])
