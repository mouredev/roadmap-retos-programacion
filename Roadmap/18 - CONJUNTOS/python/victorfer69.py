#EJERCICIO

data = [1, 2, 3, 4, 5]
print(data)

#Añade un elemento al principio.
data.append(6)
print(data)

#Añade un elemento en la posicion que quieras
data.insert(0, 0)
print(data)

#Añade varios elementos en bloque al final.
block = [7, 8, 9]
data.extend(block)
print(data)

#Añade varios elementos en bloque en una posición concreta.
data[3:3] = [-1, -2, -3]
print(data)

# Elimina un elemento en una posición concreta.
data.pop(5)
print(data)

# Actualiza el valor de un elemento en una posición concreta.
data[4] = 10
print(data)

# Comprueba si un elemento está en un conjunto.
print(data.__contains__(3))
print(data.__contains__(1234))

# Elimina todo el contenido del conjunto.
data.clear()
print(data)


#EJERCICIO EXTRA

#Union
def union(a, b):
    c = []
    a.extend(b)
    for i in a:
        if not c.__contains__(i):
            c.append(i)
    return c

a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 7, 9]
print(union(a,b))

#Interseccion
def interseccion(a, b):
    c = []
    for i in a:
        if b.__contains__(i):
            c.append(i)
    return c

a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 7, 9]
print(interseccion(a, b))

#Diferencia 
def diferencia(a, b):
    c = a
    for i in b:
        if a.__contains__(i):
            c.remove(i)
    return c

a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 7, 9]
print(diferencia(a, b))

#Hay operaciones que lo hacen solas
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}
print(f"Unión: {a.union(b)}")
print(f"Intersección: {a.intersection(b)}")
print(f"Diferencia: {a.difference(b)}")