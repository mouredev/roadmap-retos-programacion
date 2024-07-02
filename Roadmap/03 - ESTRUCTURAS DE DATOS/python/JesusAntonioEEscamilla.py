# #02 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
#---LISTA---
# Creando Lista
print("LISTA")
lista = ["Antonio", "Fatima", "Maria", "Lizette"]
print(lista)
# INSERCIÓN
print("INSERCIÓN")
lista.append("Rosa")
print(lista)
# ELIMINACIÓN
print("ELIMINACIÓN")
del lista[2]
print(lista)
# ACTUALIZACIÓN
print("ACTUALIZACIÓN")
lista[0] = "Jesus"
print(lista)
# ORDENAMIENTO
print("ORDENAMIENTO")
lista.sort()
print(lista)


#---DIRECTORIO---
# Creando Directorio
print("DIRECTORIO")
diccionario = {
    "Papas": 3,
    "Tortas": 5,
    "Queso": 2,
    "Pan": 1,
}
print(diccionario)
# INSERCIÓN
print("INSERCIÓN")
diccionario["Pepsi"] = 4
print(diccionario)
# ELIMINACIÓN
print("ELIMINACIÓN")
del diccionario["Papas"]
print(diccionario)
# ACTUALIZACIÓN
print("ACTUALIZACIÓN")
diccionario["Tortas"] = 6
print(diccionario)
# ORDENAMIENTO
print("ORDENAMIENTO")
mi_dicc = dict(sorted(diccionario.items()))
print(mi_dicc)


#---SETS---
# Creando Set
print("SET")
conjunto = {"A", "B", "C"}
print(conjunto)
# INSERCIÓN
print("INSERCIÓN")
conjunto.add("D")
print(conjunto)
# ELIMINACIÓN
print("ELIMINACIÓN")
conjunto.remove("B")
print(conjunto)
# ACTUALIZACIÓN
print("ACTUALIZACIÓN")
print("No se puede eliminar directamente pero hay otra forma")
conjunto.remove("C")
conjunto.add("E")
print(conjunto)
# ORDENAMIENTO
print("ORDENAMIENTO")
print("No Existe una forma de ordenamiento")



"""
EXTRA
"""
#Pendiente