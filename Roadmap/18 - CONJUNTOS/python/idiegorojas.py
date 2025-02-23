"""
Conjuntos
"""

# Son una coleccion desordenada de elementos unicos.
# Son utiles cuando cuandos se necesita almacenar elmentes sin duplicados. 
# Sirve para hacer operaciones matematicas como union, interseccion y diferencia.

"""
Crear un conjunto
"""
# Usando llaves
mi_conjunto = {1,2,3,4,5}
print(mi_conjunto)


print('----------')


# Usando la funcion set()
otro_conjunto = set([1,2,2,3,4,4,5,5,5]) # Se eliminan los duplicados automaticamente
print(otro_conjunto)


print('----------')


"""
Operaciones comunes
"""

# Agregar un elemento: .add()
mi_conjunto = {1,2,3}
mi_conjunto.add(4)
print(mi_conjunto)


print('----------')


# Eliminar elementos: .remove()
mi_conjunto.remove(2)
print(mi_conjunto)


# Union: '|' o '.union()'
conjunto_uno = {1, 2, 3}
conjunto_dos = {3, 4, 5}
union = conjunto_uno | conjunto_dos
print(union)


# Interseccion: Encuentra elementos comunes '&' o intersection()
interseccion = conjunto_uno & conjunto_dos
print(interseccion)


# Diferencia: Elementos de un conjunto pero no en otro '-' o '.difference()'
diferencia = conjunto_uno - conjunto_dos
print(diferencia)


"""
Casos de usos
"""

# Eliminar duplicados de una lista
# Verificar membresias rapidamente
# Operaciones matematicas entre grupos de datos


"""
Ejercicio
"""

datos = [1, 2, 3, 4, 5]
print(f'Estructura inicial: {datos}')

 #Añade un elemento al final.
datos.append(6)
print(datos)

 # Añade un elemento al principio.
datos.insert(0, 0)
print(datos)

 # Añade varios elementos en bloque al final.
datos.extend([7, 8, 9])
print(datos)

 # Añade varios elementos en bloque en una posición concreta.
datos[4:4] = [-1,-2,-3]
print(datos)

 # Elimina un elemento en una posición concreta.
del datos[3]
print(datos)

 # Actualiza el valor de un elemento en una posición concreta.
datos[3:6] = [3,4,5]
print(datos)
 
 # Comprueba si un elemento está en un conjunto.
print(-1 in datos)

 # Elimina todo el contenido del conjunto.
datos.clear()
print(datos)


"""
Extra
"""

datos_uno = {1,2,3,4,5}
datos_dos = {2,3,4,5,6}

# Unión.
union = datos_uno | datos_dos
print(union)

# Intersección.
interseccion = datos_uno & datos_dos
print(interseccion)

# Diferencia.
diferencia_uno = datos_uno - datos_dos
diferencia_dos = datos_dos - datos_uno
print(diferencia_uno)
print(diferencia_dos)

# Diferencia simétrica.
diferencia_simetrica = datos_uno.symmetric_difference(datos_dos)
print(diferencia_simetrica)
