# @Author Mhayhem

# EJERCICIO:
# Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
# operaciones (debes utilizar una estructura que las soporte):

my_list = [1, 2, 3]

# - Añade un elemento al final.

my_list.append(4)

# - Añade un elemento al principio.

my_list.insert(0, 0)

# - Añade varios elementos en bloque al final.

my_list.extend([7, 8]) # otra opciones seria my_list += [7, 8], my_list[len(my_list): ] = [7, 8]

# - Añade varios elementos en bloque en una posición concreta.

my_list[5:5] = [5, 6]

# - Elimina un elemento en una posición concreta.

my_list.pop(2)

# - Actualiza el valor de un elemento en una posición concreta.

my_list[3] = 10

# - Comprueba si un elemento está en un conjunto.

is_in = 7 in my_list

# - Elimina todo el contenido del conjunto.

my_list.clear()

# DIFICULTAD EXTRA (opcional):
# Muestra ejemplos de las siguientes operaciones con conjuntos:

s1 = {1, 2, 3}
s2 = {"a", "b", "c"}

# - Unión.

s_union = s1.union(s2)

# - Intersección.

s3 = s1.intersection({"a", 2, "d", 6})

# - Diferencia.

diff = s1.difference(s3)

# - Diferencia simétrica.

s1.symmetric_difference({1, 2, 4, 5})