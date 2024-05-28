#listas


mi_lista = ["mouredev", "simon", "adrimar"]
print(mi_lista)

mi_lista.append("loengris") #insercion
print(mi_lista)

mi_lista.remove("simon") #eliminacion
print(mi_lista)

print(mi_lista[1]) #acceso
mi_lista[1]= "mouredevillo" #actualizacion
print(mi_lista)

mi_lista.sort() #ordenacion
print(mi_lista)


# tuplas

mi_tupla = ("simon", "torbett", "storbett", "36")
print(mi_tupla[1]) #acceso
print(mi_tupla[3]) 
mi_tupla = tuple(sorted(mi_tupla)) #ordenacion
print(mi_tupla)
print(type(mi_tupla)) 


# set #no se duplican los datos#
#no se puede ordenar#


mi_set = {"simon", "torbett", "storbett", "36"}
print(mi_set)
mi_set.add("simontorbett@gmail.com")
mi_set.remove("storbett") #elimicacion
print(mi_set)

print(type(mi_set))

#diccionario

mi_diccionario: dict = {
    "nombre": "simon",
    "apellido": "torbett",
    "edad": "33"
}

mi_diccionario["email"] = "simontorbett@gmail.com" # insercion
print(mi_diccionario)
del mi_diccionario["apellido"] # elimimcacion
print(mi_diccionario)
mi_diccionario["edad"] = "34" #actualizacion
print(mi_diccionario)
mi_diccionario = dict(sorted(mi_diccionario.items()))
print(mi_diccionario)
print(type(mi_diccionario))