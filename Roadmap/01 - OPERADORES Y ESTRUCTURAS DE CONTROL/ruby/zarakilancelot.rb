# Operadores aritméticos en Ruby
# '+', '-', '*', '/', '%', '**'

primer_numero = 5.0   # Lo coloco como float para que de un resultado sobre cero en la división
segundo_numero = 10

# SUMA +
suma = primer_numero + segundo_numero                   # 15.0
puts "El resultado de la suma es #{suma}"

# RESTA -
resta = primer_numero - segundo_numero                  # -5.0
puts "El resultado de la resta es #{resta}"

# MULTIPLICACIÓN *
multiplicacion = primer_numero * segundo_numero         # 50.0
puts "El resultado de la multiplicacion es #{multiplicacion}"

# DIVISIÓN /
division = primer_numero / segundo_numero               # 0.5
puts "El resultado de la division es #{division}"

# MÓDULO %
modulo = primer_numero % segundo_numero                 # 5.0
puts "El resultado de modulo es #{modulo}"

# EXPONENTE **
exponencial = primer_numero ** segundo_numero           # 9765625.0
puts "El resultado del exponencial es #{exponencial}"

# ====================================================================================

# Operadores lógicos (booleanos) en Ruby
# '&&', '||', '!', 'and', 'or', 'not'
# && (and): Devuelve true si ambos operandos son true.
# || (or): Devuelve true si al menos uno de los operandos es true.
# !  (not): Devuelve true si el operando es false.

# AND
puts true && false  # Devuelve false

# OR
puts true || false  # Devuelve true

# NOT
puts !true  # Devuelve false

# Ejemplo con variables
x = true
y = false

# AND
puts x && y  # Devuelve false

# OR
puts x || y  # Devuelve true

# NOT
puts !x  # Devuelve false
puts !y  # Devuelve true

# AND y OR tienen la misma precedencia por lo que se evalúa de izquierda a derecha
# && y || no tienen la misma precedencia, se evalúa primero &&

# ====================================================================================

# Operadores de comparación en Ruby
# '<', '<=', '>', '>=', '<=>'

a = 5
b = 7
c = 5

puts "Es A menor a B? #{a < b}"
puts "Es A mayor a B? #{a > b}"
puts "Es A mayor o igual a C? #{a >= c}"
puts "Es A diferente a C? #{a <=> c}"

# ====================================================================================

# Operadores de igualdad en Ruby
# '==', '!=', '=~', '!~', '==='

puts "Es A igual a c? #{a == c}"
puts "Es A diferente a B? #{a != b}"

# =~ Se utiliza para verificar si una cadena coincide con una RegEx
cadena = "Hola mundo"
if cadena =~ /mundo/
  puts "Se encontró la palabra 'mundo'"
else
  puts "No se encontró la palabra 'mundo'"
end

puts "Es A estrictamente igual a C? #{a === c}"

# ====================================================================================

# Operador condicional en Ruby
# '?'

mensajes = 3
puts "Tienes #{mensajes} #{mensajes == 1 ? 'mensaje' : 'mensajes'}"

# ====================================================================================

# Operador de asignación en Ruby
# '='

g = h = i = 0               # Le asigna 0 a las tres variables
puts "#{g} - #{h} - #{i}"

g = (h = (i = 0))           # Sucede lo mismo que arriba
puts "#{g} - #{h} - #{i}"

# ====================================================================================

# Estructuras de control condicionales en Ruby

# IF
x = 6

# Como bloque
if x < 10
  x += 1
end
puts x

# Una línea con THEN como separador
if x < 10 then x += 1 end
puts x

# Como bloque con THEN
if x < 10 then
  x += 1
end
puts x

# If como modificador
puts mensajes if mensajes

# ELSE
data = []

if data
  data << x+1
else
  data = [x+2]
end
puts data

# ELSIF
if x == 1
  name = "one"
elsif x == 2
  name = "two"
elsif x == 3 then name = "three"
elsif x == 4; name = "four"
else
  name = "other"
end
puts name

# UNLESS
unless x == 0
  puts "x no es cero (0)"
end

# CASE
name = case
  when x == 1 then puts "one"
  when x == 2 then puts "two"
  when x == 3 then puts "three"
  when x == 4 then puts "four"
  else puts "many"
end

# ====================================================================================

# Estructuras de control iterativas en Ruby

# WHILE
x = 10                    # Inicializamos una variable para el bucle
while x >= 0 do           # Mientras x sea mas o igual a 0 se repetirá
  puts x                  # Se imprimie el valor de x en esa iteración
  x = x - 1               # Se resta 1 de x
end                       # Se finaliza el bucle

# UNTIL
x = 0                     # Inicializamos una variable para el bucle
until x > 10 do           # Se ejecutará hasta que x sea mayor a 10
  puts x                  # Se imprime el valor de x en esa iteración
  x = x + 1               # Se suma 1 a x
end                       # Se finaliza el bucle

x = 10                    # Inicializamos una variable para el bucle
begin                     # Se inicia el bucle
  puts x                  # Se imprime el valor de x en esa iteración
  x = x - 1               # Se resta 1 de x
end until x == 0          # Se finaliza el bucle hasta que x sea igual a cero

# FOR IN
animales = ['perro', 'gato', 'loro', 'pez']
for animal in animales do
  puts animal
end

hash = {:a=>1, :b=>2, :c=>3}
for key,value in hash
  puts "#{key} => #{value}"
end

# ITERADOR NUMÉRICO UPTO
4.upto(8) {|n| print n}   # Imprime "45678"
puts

# ITERADOR NUMÉRICO TIMES
3.times {|x| print x}     # Imprime "012"
puts

# EACH
[10, 20, 30].each {|x| print x}   # Imprime "102030"
puts
(1..3).each {|x| print x}         # Imprime "123"
puts

# COLLECT
cuadrados = [1, 2, 3].collect {|x| print x*x}
puts

# SELECT
pares = (1..10).select {|x| print x if x%2 == 0}   # Imprime [2,4,6,8,10]
puts

# REJECT
impares = (1..10).reject {|x| print x if x%2 != 0}   # Imprime [1,3,5,7,9]
puts

# EXCEPCIONES
n = 0
raise ArgumentError, "Expected argument >= 1. Got #{n}" if n < 1

n = "s"
raise TypeError, "Integer argument expected" if not n.is_a? Integer

def factorial(n)
  raise "bad argument" if n < 1
  return 1 if n == 1
  n * factorial(n-1)
end

begin
  x = factorial(-1)
rescue => ex
  puts "#{ex.class}: #{ex.message}"
end

# ====================================================================================

# EXTRA
extra = (10..55).select {|x| x%2 == 0 and x != 16 and x%3 != 0}
print extra
