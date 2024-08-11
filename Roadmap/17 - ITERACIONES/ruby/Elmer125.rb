#  * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
puts "Iterating numbers from 1 to 10 using each"
(1..10).each { |i| puts i }

puts "Iterating numbers from 1 to 10 using times"
10.times { |i| puts i + 1 }

puts "Iterating numbers from 1 to 10 using for"
for i in 1..10
  puts i
end

puts "Iterating numbers from 1 to 10 using while"
n = 0
while n < 10
  puts n + 1
  n += 1
end

#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
puts "Iterating numbers from 1 to 10 using recursion"
def iterate(n)
  puts n
  return n < 10 ? iterate(n + 1) : n
end
puts iterate(1)

puts "Iterating numbers from 1 to 10 using upto"
1.upto(10) { |i| puts i }

puts "Strings"
string = "Ruby on Rails"
string.each_char { |c| puts c }
string.split("").each { |c| puts c }
string.scan(/./) { |c| puts c }

puts "Arrays"
array = [1, 2, 3, 4, 5]
array.each { |i| puts i }
array.each_index { |i| puts array[i] }
array.each_with_index { |i, index| puts i }

puts "Hashes"
hash = { a: 1, b: 2, c: 3 }
hash.each { |k, v| puts "#{k}: #{v}" }
hash.each_key { |k| puts k }
hash.each_value { |v| puts v }
