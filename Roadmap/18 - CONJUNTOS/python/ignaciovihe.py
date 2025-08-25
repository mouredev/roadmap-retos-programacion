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
"""

my_list = [i for i in range (1,11)]
print(my_list)

#Añadir elemento al final

my_list.append("a")
print(my_list)

#Añadir elemento al principio

my_list.insert(0, "b")
print(my_list)

#Añadir elementos en bloque al final.

my_second_list = ["c", "d"]
my_list.extend(my_second_list)
print(my_list)

#Añade elementos en bloque en posición concreta

my_empty_list = []
my_third_list = ["e", "f"]
my_list[2:2] = my_third_list #inserta los valores en el índice indicado
print(my_list)
my_list[2:4] = my_empty_list # Sustituye los valores entre los indices por los nuevos. EN este caso los borra porque la listga esta vacia.
print(my_list)

#Eliminar un elemento de posición concreta

element = my_list.pop(6) # Tambien del my_list[6]
print(element)
print(my_list)

#Actualiza el elemento de una posición

my_list[4] = "e"
print(my_list)

# Comprobar si u elemento esta en un conjunto

element= 10
print(f" {element} Esta en la lista: {element in my_list} --> Posición: {my_list.index(element) if element in my_list else "-"}")

# Eliminar el contenido de un conjunto

my_list.clear()
print(my_list)


"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

set_a = {"j", "g", "i", "f", "p", "a", "r"}
set_b = {"g", "l", "r", "f", "b", "i"}

#Unión
print(set_a | set_b) # Une los elementos de ambos conjuntos (sin duplicados).


#Initersección
print(set_a & set_b) # Devuelve los elementos comunes entre ambos conjuntos.


#Diferencia

print(set_a - set_b) # Elementos que están en A pero no en B (Como una resta)
print(set_b - set_a) #Elementos que están en B pero no en A (Como una resta)

#Diferencia simetrica
print(set_a ^ set_b) #Elementos que están en A o en B, pero no en ambos.