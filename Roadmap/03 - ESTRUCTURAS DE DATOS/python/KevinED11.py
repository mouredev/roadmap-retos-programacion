diccionario = {"nombre": "Kevin", "apellido": "Elias", "edad": 23}
diccionario["direccion"] = "Calle falsa 123"
diccionario["edad"] = 24
del diccionario["direccion"]
diccionario.sort()
print(diccionario)

lista = [1, 2, 3, 4, 5]
lista += [6, 7, 8, 9, 10]
lista.append(11)
lista.extend([12, 13, 14, 15, 16])
lista.insert(0, 0)
lista.remove(0)
lista.pop()
lista.clear()
tupla = (1, 2, 3, 4, 5)
set1 = {1, 2, 3, 4, 5}
