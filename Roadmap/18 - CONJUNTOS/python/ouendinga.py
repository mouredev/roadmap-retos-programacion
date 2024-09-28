# 1. Crear una lista
lista = ['elemento1', 'elemento2', 'elemento3']
print(f'1.: {lista}')

# 2. Añadir un elemento al final de la lista
lista.append('elemento4')
print(f'2.: {lista}')

# 3. Añadir un elemento al principio de la lista
lista.insert(0, 'elemento0')
print(f'3.: {lista}')

# 4. Añadir varios elementos en bloque al final de la lista
lista.extend(['elemento5', 'elemento6', 'elemento7'])
print(f'4.: {lista}')

# 5. Añadir varios elementos en bloque en una posición concreta de la lista
lista[2:2] = ['elemento1.5', 'elemento1.75']
print(f'5.: {lista}')

# 6. Eliminar un elemento en una posición concreta de la lista
del lista[1]
print(f'6.: {lista}')

# 7. Actualizar el valor de un elemento en una posición concreta de la lista
lista[0] = 'elemento0.5'
print(f'7.: {lista}')

# 8. Comprobar si un elemento está en la lista
if 'elemento0.5' in lista:
	print('elemento0.5 está en la lista')
print(f'8.: {lista}')

# 9. Eliminar todo el contenido de la lista
lista.clear()
print(f'9.: {lista}')

print('DIFICULTAD EXTRA')

# 1. Crear dos conjuntos de datos
conjunto1 = set(['a', 'b', 'c', 'd'])
conjunto2 = set(['c', 'd', 'e', 'f'])

# 2. Realizar la unión de los dos conjuntos
union = conjunto1.union(conjunto2)
print(f'Unión: {union}')

# 3. Realizar la intersección de los dos conjuntos
interseccion = conjunto1.intersection(conjunto2)
print(f'Intersección: {interseccion}')

# 4. Realizar la diferencia de los dos conjuntos
diferencia = conjunto1.difference(conjunto2)
print(f'Diferencia: {diferencia}')

# 5. Realizar la diferencia simétrica de los dos conjuntos
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(f'Diferencia simétrica: {diferencia_simetrica}')