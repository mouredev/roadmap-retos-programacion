# frozen_string_literal: true

#
# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#

puts '### OPERADORES ###'

# Operadores Aritméticos
puts "\n--- Aritméticos ---"
a = 10
b = 3
puts "Suma: 10 + 3 = #{a + b}"
puts "Resta: 10 - 3 = #{a - b}"
puts "Multiplicación: 10 * 3 = #{a * b}"
puts "División: 10 / 3 = #{a / b}"
puts "Módulo: 10 % 3 = #{a % b}"

# Operadores Lógicos
puts "\n--- Lógicos ---"
puts "AND (true && false): #{true && false}"
puts "OR (true || false): #{true || false}"
puts "NOT (!true): #{!true}"

# Operadores de Comparación
puts "\n--- Comparación ---"
puts "Igualdad (10 == 3): #{10 == 3}"
puts "Desigualdad (10 != 3): #{10 != 3}"

# Operadores de Asignación
puts "\n--- Asignación ---"
x = 5
x += 2
puts "Suma y asignación: x += 2 -> x = #{x}"

# Operador de Pertenencia (rangos)
puts "\n--- Pertenencia (Rangos) ---"
rango = (1..5)
puts "¿El rango 1..5 incluye 3? #{rango.include?(3)}"

# Operadores de Bits
puts "\n--- Bits ---"
p = 10 # 1010
q = 3  # 0011
puts "AND a nivel de bits (10 & 3): #{p & q}"
puts "OR a nivel de bits (10 | 3): #{p | q}"

#
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
#

puts "\n### ESTRUCTURAS DE CONTROL ###"

# Condicionales
puts "\n--- Condicionales (if, else) ---"
edad = 18
if edad < 18
  puts 'Eres menor de edad.'
else
  puts 'Eres mayor de edad.'
end

# Iterativas
puts "\n--- Iterativas (for) ---"
(1..3).each do |i|
  puts i
end

puts "\n--- Iterativas (while) ---"
contador = 3
while contador > 0
  puts contador
  contador -= 1
end

# Excepciones
puts "\n--- Excepciones (begin, rescue) ---"
begin
  raise 'Este es un error de ejemplo'
rescue StandardError => e
  puts "Se capturó una excepción: #{e.message}"
end

#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#

puts "\n### DIFICULTAD EXTRA ###"
(10..55).each do |numero|
  if numero.even? && numero != 16 && (numero % 3 != 0)
    puts numero
  end
end
