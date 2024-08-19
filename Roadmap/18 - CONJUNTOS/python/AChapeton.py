letters = ['a', 'b', 'c', 'd']
print('Original', letters)

# Añade un elemento al final.
letters.append('e')
print('Añade un elemento al final', letters)

# Añade un elemento al principio.
letters.insert(0, '-')
print('Añade un elemento al principio', letters)

# Añade varios elementos en bloque al final.
newLetters = ['x', 'y', 'z']
letters.extend(newLetters)
print('Añade varios elementos en bloque al final', letters)

# Añade varios elementos en bloque en una posición concreta.
newLetters2 = ['f', 'g', 'h']
for letter in reversed(newLetters2):
  letters.insert(6, letter)
print('Añade varios elementos en bloque en una posición concreta', letters)

# Elimina un elemento en una posición concreta.
letters.pop(5)
print('Elimina un elemento en una posición concreta', letters)

# Actualiza el valor de un elemento en una posición concreta.
letters[1] = '#'
print('Actualiza el valor de un elemento en una posición concreta', letters)

# Comprueba si un elemento está en un conjunto.
try:
  print('Comprueba si el elemento -a- está en el conjunto letters (buscar posicion)', letters.index('a'))
except ValueError:
  print('El elemento -a- no existe')

try:
  print('Comprueba si el elemento -b- está en el conjunto letters (buscar posicion)', letters.index('b'))
except ValueError:
  print('El elemento -a- no existe')

# Elimina todo el contenido del conjunto.
letters.clear()
print('Elimina todo el contenido del conjunto', letters)


# DIFICULTAD EXTRA\

# Union
first ={1, 2, 3, 4}
second = {3, 4, 5, 6}
union = first.union(second)
print('Union', union)

# Interseccion
interseccion = first.intersection(second)
print('Interseccion', interseccion)

# Diferencia
interseccion = first.difference(second)
print('Diferencia', interseccion)

# Diferencia simetrica
interseccion = first.symmetric_difference(second)
print('Diferencia simetrica', interseccion)