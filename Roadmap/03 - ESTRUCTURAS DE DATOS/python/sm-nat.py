#ESTRUCTURAS DE DATOS

#listas
mi_lista = ["en", "las",3,"listas","se pueden", "mezclar", "tipos de datos",5.4,True]
print(mi_lista[0])
mi_lista[0] = "son mutables"
print(mi_lista[0])

#tuplas
mi_tupla = ("son como las listas","pero","son inmutables",55,False)
print(mi_tupla)
print(mi_tupla[2])

#conjuntos
mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.add(6)
print(mi_conjunto) 
mi_conjunto.remove(1)
print(mi_conjunto)  

#diccionarios
mi_diccionario = {"nombre": "Natalia", "edad": 21, "ciudad": "Gold Coast"}
print(mi_diccionario["nombre"]) 
mi_diccionario["edad"] = 31
print(mi_diccionario)  


