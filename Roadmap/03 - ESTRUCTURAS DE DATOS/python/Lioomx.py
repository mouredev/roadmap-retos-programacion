
''' Las estructuras de datos son una forma de organizar y 
almacenar datos de manera que podamos acceder y modificarlos 
de manera eficiente.
Algunos ejemplos comunes de estructuras de datos son 
listas, pilas, colas, conjuntos y diccionarios. 
'''

''' Listas (list) ''' 
'''
Colecciones ordenadas y mutables (Pueden cambiar sus elementos)
''' 

list = [1, 2, 3, 4, 5] # Pueden ser de tipo númerico, mixto ó vacía
print(list[0]) # Accede al primer elemento

# Modificar una lista 
list.append(6) # Agrega un elemento al final
list[1] = 20 # Cambia el elemento 1 por el número 20
list.insert(3, 6) # Agrega un elemento en un indice específico
print(list) 

# Elimina elementos
list.remove(5) # Elimina el primer elemento que coincida
list.pop (1) # Elimina un elemento por índice (o el último si no se especifica)
del list[0] # Elimina un elemento o un rango de la lista
print(list)

# Cortar listas (Slicing)
list_1 = [10, 20, 30, 40, 50]
print(list_1[1:4]) # [20, 30, 40]
print(list_1[:3]) # [10, 20, 30]
print(list_1[2:1]) # [30, 40, 50]
print(list_1[::-1]) # [50, 40, 30, 20, 20] # lista invertida

# Operaciones comunes
print(len(list_1)) # Número de elementos

list_2 = [1, 2]
list_3 = [3, 4]
print(list_2 + list_3) # Concatencación

print([0] * 5) # Repetición

numbers = [10, 20, 30]
print(20 in numbers) # Busqueda
print(numbers.index(20))

# Métodos utiles de listas
numeros = [4, 2, 3, 1]
numeros.sort() # Ordenar en orden ascendente
print(numeros)  # [1, 2, 3, 4]
numeros.reverse() # Invertir el orden la lista
print(numeros)  # [4, 3, 2, 1]
print(numeros.count(2))  # 1 # Contar las apariciones de un elemento
copia = numeros.copy() # Crear una copia de la lista
print(copia)  # [4, 3, 2, 1]

''' Tuplas (tuple)'''
'''
Son colecciones ordenadas pero inmutables 
(no pueden cambiar sus elementos después de crearlas)
'''

my_tupla = (1, 2, 3, 4, 5)
print(my_tupla[1])

# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5)
otra_tupla = "a", "b", "c"  # También válido
tupla_vacia = ()
una_tupla = (42,)  # Tupla de un solo elemento, con una coma al final

# Acceder a los elementos
mi_tupla = (10, 20, 30, 40, 50)
print(mi_tupla[0])   # 10
print(mi_tupla[-1])  # 50


# Inmutabilidad. 
# No puedes modificar una tupla después de crearla. Esto significa que los siguientes intentos darán error
mi_tupla = (1, 2, 3)
# mi_tupla[1] = 10  # Esto da error
# mi_tupla.append(4)  # Esto también da error
# Sin embargo, si la tupla contiene elementos mutables como listas, puedes modificar esos elementos internos.
tupla_con_lista = (1, [2, 3], 4)
tupla_con_lista[1][0] = 99
print(tupla_con_lista)  # (1, [99, 3], 4)

# Unión de tuplas
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)  # (1, 2, 3, 4, 5, 6)

# Repetición de tuplas
t = (1, 2)
print(t * 3)  # (1, 2, 1, 2, 1, 2)

# Verificar si un elemento está en una tupla
t = (10, 20, 30)
print(20 in t)  # True
print(50 in t)  # False

# Metodos utiles
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # 3 (el 2 aparece tres veces)
print(t.index(3))  # 2 (el índice del primer 3)

# Desempaquetado de tuplas
# Puedes "desempaquetar" los elementos de una tupla directamente en variables.

t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # 1 2 3

# También puedes usar el operador * para desempacar el resto de los elementos:
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

''' Conjuntos (set)'''

mi_conjunto = {1, 2, 3, 3, 4}
print(mi_conjunto)  # {1, 2, 3, 4}
mi_conjunto.add(5)  # Agregar un elemento
mi_conjunto.remove(2)  # Eliminar un elemento

''' Diccionarios (dict)'''

mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(mi_diccionario["nombre"])  # Acceder al valor asociado a una clave
mi_diccionario["edad"] = 26      # Modificar un valor
mi_diccionario["pais"] = "España"  # Agregar un nuevo par clave-valor









