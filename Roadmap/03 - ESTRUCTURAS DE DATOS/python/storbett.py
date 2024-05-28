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


# set 

mi_set = {"simon", "torbett", "storbett", "36"}
print(mi_set)
mi_set.add("simontorbett@gmail.com")
print(mi_set)
print(type(mi_set))