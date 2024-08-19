"""
* EJERCICIO:
* Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
* operaciones (debes utilizar una estructura que las soporte):
* - Añade un elemento al final.
* - Añade un elemento al principio.
* - Añade varios elementos en bloque al final.
* - Añade varios elementos en bloque en una posición concreta.
* - Elimina un elemento en una posición concreta.
* - Actualiza el valor de un elemento en una posición concreta.
* - Comprueba si un elemento está en un conjunto.
* - Elimina todo el contenido del conjunto.
*
* DIFICULTAD EXTRA (opcional):
* Muestra ejemplos de las siguientes operaciones con conjuntos:
* - Unión.
* - Intersección.
* - Diferencia.
* - Diferencia simétrica.
"""

my_list = ["Python", "Java", "Kotlin"]

my_list.append("Php")                # Añade un elemento al final de la lista
print(my_list)

my_list.insert(0, "JavaScript")      # Añade un elemento en un especifico indice de la lista en esta caso al principio
print(my_list)

my_list.extend(["C++", "Html", "Ruby"])   # Añade varios elementos en bloque al final
print(my_list)

index_pos = 2
my_list[index_pos:index_pos]= ["swift", "typescript"]  # Añade elementos en bloque en una posicion concreta
print(my_list)

del my_list[3]                              # Elimina un elemento en una posicion concreta
print(my_list)

my_list[1] = "Html"                         # Actualiza el valor de un elemento en una posición concreta.
print(my_list)

item_to_check = "Python"
in_list = item_to_check in my_list          # Comprueba si un elemento esta en un conjunto
print(f"El elemento {item_to_check} esta en la lista? {in_list}")

my_list.clear()                             # Elimina todos los elementos de una lista
print(my_list)



########### -------------------------- EXTRA --------------------------------- ####################

# Union

my_set = {"orange", "banana", "apple"}
my_other_set = {"mango", "lemon", "pineapple"}
result = my_set.union(my_other_set)
print(result)

# Interseccion

python = {'p', 'y', 't', 'h', 'o','n'}
typescript = {'t', 'y', 'p', 'e', 's','c','r','i','p','t'}
print(python.intersection(typescript))

# Diferencia

set_one = {"elem1", "elem2", "elem3", "elem4"}
set_two = {"elem2", "elem3"}

print(set_one.difference(set_two))
print(set_two.difference(set_one))

# Diferencia simetrica

python = {'p', 'y', 't', 'h', 'o','n'}
typescript = {'t', 'y', 'p', 'e', 's','c','r','i','p','t'}
print(python.symmetric_difference(typescript))

# se actualiza para contener la diferencia simétrica entre typescript y python

typescript.symmetric_difference_update(python)
print(typescript)