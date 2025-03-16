#  * EJERCICIO:
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.
data = [1, 2, 3, 4, 5]
puts "Initial data: #{data}"

data.push(6)
puts "Add an element at the end: #{data}"

data.unshift(0)
puts "Add an element at the beginning: #{data}"

data.concat([7, 8, 9])
puts "Add multiple elements at the end: #{data}"

data.insert(5, 10, 11, 12)
puts "Add multiple elements at a specific position: #{data}"

data.delete_at(5)
puts "Delete an element at a specific position: #{data}"

data[5] = 13
puts "Update the value of an element at a specific position: #{data}"

puts "Check if an element is in the set: #{data.include?(13)}"

data.clear
puts "Delete all the content of the set: #{data}"


#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.
set_a = [1, 2, 3, 4, 5]
set_b = [4, 5, 6, 7, 8]

puts "Union: #{set_a | set_b}"

puts "Intersection: #{set_a & set_b}"

puts "Difference: #{set_a - set_b}"

puts "Symmetric difference: #{set_a - set_b | set_b - set_a}"