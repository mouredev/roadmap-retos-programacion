#listas  (como un array)
mi_lista = [1, 2, 3, 4, 5]
print(f"mi_lista: {mi_lista}")

#agrega un elemento
mi_lista.append(6)
print(f"mi_lista: {mi_lista}")

#elimina un elemento
mi_lista.remove(3)
print(f"mi_lista: {mi_lista}")  

#agrega un elemento en la posicion 2
mi_lista.insert(2, 3)
print(f"mi_lista: {mi_lista}")

#toma el primer valor
mi_lista.pop()
print(f"mi_lista: {mi_lista}")

#asignaun valor a un elemento del array
mi_lista[2] = 10
print(f"mi_lista: {mi_lista}")

#ordena
mi_lista.sort()
print(f"mi_lista: {mi_lista}")  

#elimina
mi_lista.remove(10)
print(f"mi_lista: {mi_lista}")

#amplia los datos que ya estan en el set
#mi_lista.update ([7, 8, 9])
print(f"mi_lista: {mi_lista}")


#diccionario
mi_diccionario = {"nombre": "Juan", 
                "edad": 30, 
                "ciudad": "Madrid"}
print(f"mi_diccionario: {mi_diccionario}")

#tipo de datos
print(type(mi_diccionario))

#update de un valor dando una clave
mi_diccionario["edad"] = 31
print(f"mi_diccionario: {mi_diccionario}")




