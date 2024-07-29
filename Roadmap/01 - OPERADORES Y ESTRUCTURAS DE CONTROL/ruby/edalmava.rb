# Operadores aritméticos, de comparación, a nivel de bits, lógicos

a, b, c, d, e = 10, 20, 30, 40, 5 # Asignación paralela

puts "***Operadores Aritméticos***"
puts "Suma:  10 + 20 = #{ a + b }"
puts "Resta: 40 - 20 = #{ d - b }"
puts "Multiplicación: 10 * 20 = #{ a * b }"
puts "División: 40 / 5  = #{ d / e }"
puts "Módulo: 10 % 2  = #{ a % 2 }"     # Módulo
puts "Exponente: 10 ** 5 = #{ a ** e }" # Exponente
puts ""
puts "Operador de Asignación ="
puts ""
puts "***Operadores de Comparación***"
puts "Testear igualdad:  1 == 2 se evalua como #{ 1 == 2 } (falso)"
puts "Testear desigualdad: 1 != 2 se evalua como #{ 1 != 2 } (verdadero)"
puts "Mayor que: 10 > 9 se evalua como #{ 10 > 9 }"
puts "Menor que: 10 < 9 se evalua como #{ 10 > 9 }"
puts "Mayor o igual que: 10 >= 10 se evalua como #{ 10 >= 10 }"
puts "Menor o igual que: 10 <= 10 se evalua como #{ 10 <= 10 }"
puts "Operador de comparación combinada: 10 <=> 10 devuelve #{ 10 <=> 10 } lo que significa que los operandos son iguales"
puts "10 <=> 9 devuelve #{ 10 <=> 9 } lo que significa que el primer operando es mayor que el segundo"
puts "9 <=> 10 devuelve #{ 9 <=> 10 } lo que significa que el primer operando es menor que el segundo"
puts ""
puts "***Operadores a nivel de bits(bitwise)***"
puts "Bitwise NOT: ~"
puts "Bitwise OR:  |"
puts "Bitwise AND: &"
puts "Bitwise Exclusive OR: ^"
puts "Bitwise Shift Left: <<"
puts "Bitwise Shift Right: >>"
puts ""
puts "***Operadores Lógicos o booleanos***"
puts "a = #{ a }, b = #{ b }, c = #{ c }, d = #{ d }"
puts "Operador and(Y lógico): (a < b) and (c < d) se evalua como #{ (a < b) and (c < d) }" # También se puede usar &&
puts "Operador or(O lógico): (a > b) or (c > d) se evalua como #{ (a > b) or (c > d) }" # También se puede usar ||
puts "Operador NOT: !(a > b) se evalua como #{ !(a > b) }"

puts ""
puts "***Estructuras de Control***"
print "Sentencia if-elsif-else: "
if a < b then
  print "#{a} es menor que #{b}"
else
  print "#{a} es mayor que #{b}"
end
print "\nOperador ternario: [condition] ? [true expression] : [false expression]\n"
puts b > a ? "#{b} es mayor que #{a}" : "#{a} es mayor que #{b}"
puts "Sentencia case: "
carro = "Patriot"

fabricante = case carro
   when "Focus" then "Ford"
   when "Navigator" then "Lincoln"
   when "Camry" then "Toyota"
   when "Civic" then "Honda"
   when "Patriot" then "Jeep"
   when "Jetta" then "VW"
   when "Ceyene" then "Porsche"
   when "Outback" then "Subaru"
   when "520i" then "BMW"
   when "Tundra" then "Nissan"
   else "Unknown"
end

puts "El " + carro  + " es fabricado por "  + fabricante
puts ""
puts "Ciclo while"
i = 0
while i < 5 do
   puts i
   i += 1
end
puts "Ciclo until"
i = 0
until i == 5
   puts i
   i += 1
end
puts "Ciclo for"
for i in 1..5 do
  puts i
end

puts ""
puts "***RETO EXTRA***"
puts ""
for i in 10 .. 55
  puts i if (i % 2 == 0) && (i != 16) && (i % 3 != 0)
end
