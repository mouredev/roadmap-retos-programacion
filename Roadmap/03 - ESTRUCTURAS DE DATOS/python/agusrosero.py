# Estructuras de Datos

# LISTAS
listas = [1, 2, 3, 4, 5]
listas.append(1)
listas.insert(1, 2)
lista = listas.copy()
lista[1] = 10
lista.sort()
print(lista)

# TUPLAS
mi_tupla = (1, 2, 3, 4)
elemento = mi_tupla[1]
tupla_nueva = mi_tupla + (5, 6, 7)
print(mi_tupla)

# Conjuntos
mi_conjunto = {'hello', 'world', 'python'}
mi_conjunto.add('java')
conjuntos = mi_conjunto.copy()
conjuntos.remove('world')
conjuntos.discard('hello')
conjuntos.update({'hello', 'world'})
conjuntos.clear()
conjuntos.add('python')
print(conjuntos)

# Diccionarios
mi_diccionario = {'clave': 'valor', 'color': 'rojo'}
mi_diccionario['edad'] = 23
diccionario = mi_diccionario.copy()
diccionario.pop('color')
del diccionario['clave']
diccionario.update({'edad': 23})
diccionario.clear()
print(diccionario)
