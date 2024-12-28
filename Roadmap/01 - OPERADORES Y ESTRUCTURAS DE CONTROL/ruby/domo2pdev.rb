# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
# que representen todos los tipos de estructuras de control que existan en tu lenguaje:
# Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

# Aritmetic Operators:

# Addition Operator (+)
first_number = 15
second_number = 5

addition = first_number + second_number
puts "The result of the addition #{first_number} + #{second_number} is #{addition}"

# Subtraction Operator (-)
subtraction = first_number - second_number
puts "The result of the subtraction #{first_number} - #{second_number} is #{subtraction}"

# Multiplication Operator (*)
multiplication = first_number * second_number
puts "The result of the multiplication #{first_number} * #{second_number}2 is #{multiplication}"

# Division Operator (/)
division = first_number / second_number
puts "The result of the division #{first_number} / #{second_number} is #{division}"

# Modulo Operator (%)
modulo = first_number % second_number
puts "The result of the modulo #{first_number} % #{second_number} is #{modulo}"

# Exponentiation Operator (**)
exponentiation = first_number**second_number
puts "The result of the exponentiation #{first_number} ** #{second_number} is #{exponentiation}"

# Increment Operator (++)
increment = first_number + 1
puts "The result of the increment #{first_number} + 1 is #{increment}"

# Decrement Operator (--)
decrement = first_number - 1
puts "The result of the decrement #{first_number} - 1 is #{decrement}"

# Assignment Operators:

# (=) assigns a value to a variable
my_shoes = 'a pair of shoes'
my_size = 42
puts "I have #{my_shoes} size #{my_size}"

# (+=) adds a value to a variable
my_size += 1
puts "I have #{my_shoes} size #{my_size}"

# (-=) subtracts a value from a variable
my_size -= 1
puts "I have #{my_shoes} size #{my_size}"

# (*=) multiplies a value to a variable
my_size *= 2
puts "I have #{my_shoes} size #{my_size}"

# (/=) divides a value to a variable
my_size /= 2
puts "I have #{my_shoes} size #{my_size}"

# (%=) divides a value to a variable
my_size %= 2
puts "I have #{my_shoes} size #{my_size}"

# (**=) exponentiates a value to a variable
my_size = 6
my_size **= 2
puts "I have #{my_shoes} size #{my_size}"

# Comparison Operators:

name = 'Mateo'
last_name = 'Lombana'
# Equal to (==)
puts "Is #{name} equal to #{last_name}? #{name == last_name}" # false

# Not equal to (!=)
puts "Is #{name} not equal to #{last_name}? #{name != last_name}" # true

# Equal to (===)
puts "Is #{name} equal to #{last_name}? #{name == last_name}" # false

young_age = 18
adult_age = 21
child_age = 8

# Greater than (>)
puts "Is #{young_age} greater than #{adult_age}? #{young_age > adult_age}" # false

# Less than (<)
puts "Is #{young_age} less than #{adult_age}? #{young_age < adult_age}" # true

# Greater than or equal to (>=)
puts "Is #{young_age} greater than or equal to #{adult_age}? #{young_age >= adult_age}" # false

# Less than or equal to (<=)
puts "Is #{young_age} less than or equal to #{adult_age}? #{young_age <= adult_age}" # true

# Combined comparison: Returns -1 if less, 0 if equal, 1 if greater
puts young_age <=> adult_age

# Logical Operators:

# Logical AND (&&)
puts "is #{child_age} less than #{adult_age} and #{adult_age}
greater than #{young_age}? #{child_age < adult_age && adult_age > young_age}" # true

# Logical OR (||)
puts "is #{child_age} less than #{adult_age} or #{adult_age}
greater than #{young_age}? #{child_age < adult_age || adult_age > young_age}" # true

# Logical NOT (!)
puts !(child_age < adult_age || adult_age > young_age)

# Range Operators:

# Range Operator (..) - The .. operator creates a range
# that includes both the start and the end values.
range = 1..5
puts range.to_a

# Range Operator (...) - The ... operator creates
# a range that includes the start value but excludes
# the end value.

range = 1...5
puts range.to_a

# Regular Expression Operators:

# Match Operator (=~):
# The =~ operator is used to check if a string
# matches a regular expression. It returns the
# index of the first match or nil if there is no match
puts 'Jhon' =~ /on/

# Not Match Operator (!~):
# The !~ operator is used to check if a string
# does not match a regular expression. It returns
# true if the string does not match the regular
# expression and false if it does.
puts 'Jhon' !~ /Mary/

# Bitwise Operators:

# Bitwise AND (&)
bitwise_return = 5 & 3
puts "Bitwise AND (&) (5 & 3) = #{bitwise_return}"

# Bitwise OR (|)
bitwise_return = 5 | 3
puts "Bitwise OR (|)  (5 | 3) = #{bitwise_return}"

# Bitwise XOR (^)
bitwise_return = 5 ^ 3
puts "Bitwise XOR (^) (5 ^ 3) = #{bitwise_return}"

# Bitwise NOT (~)
bitwise_return = ~5
puts "Bitwise NOT (~) (~5) = #{bitwise_return}"

# Bitwise Left Shift (<<)
bitwise_return = 5 << 3
puts "Bitwise Left Shift (<<) (5 << 3) = #{bitwise_return}"

# Bitwise Right Shift (>>)
bitwise_return = 5 >> 3
puts "Bitwise Right Shift (>>) (5 >> 3) = #{bitwise_return}"

# Unary Operators:

# Unary Plus (+)
puts '+5 = 5'

# Unary Minus (-)
puts '-5 = -5'

# Membership Operators:

# Membership Operator include?:
# The include? operator is used to check if an object
# is included in an array or a string. It returns true
# if the object is included and false if it is not.

puts %w[a b c].include?('b')
puts 'jhon Doe'.include?('Doa')

# Ternary Operator:
age = 10
can_drive_vehicle = age >= 18 ? 'Yes' : 'No'
puts "the subject age is #{age}. Can drive vehicle? #{can_drive_vehicle}"

# Ternary Operator with multiple conditions:
age = 17
can_drive_vehicle = if age >= 18
                      'Yes'
                    else
                      (age >= 16 ? 'Maybe' : 'No')
                    end
puts "the subject age is #{age}. Can drive vehicle? #{can_drive_vehicle}"

# Control statements:

# if statement
# Executes a block of code if a specified condition is true.
age = 19
is_male = true
is_female = true

puts 'You are an adult male' if age >= 18 && is_male == true

age = 15
puts 'You are a little girl' if age <= 18 && is_female == true

# if else statement:
# Executes one block of code if a condition
# is true and another block if the condition is false.

age = 15
name = 'Mateo'
confirm_name = 'Mateo'
last_name = 'Lombana'
confirm_last_name = 'Lombana'

if name == confirm_name && last_name == confirm_last_name # condition
  puts "Hello #{name} #{last_name}"
else
  puts "You are not #{name} #{last_name}"
end

# elsif statement:
# Allows for multiple conditions to be checked in sequence.

if name == confirm_name && last_name == confirm_last_name # condition 1
  puts "El usuario es: #{name} #{last_name}"
elsif age >= 18 # condition 2
  puts "La edad del usuario es: #{age}"
else
  puts 'Debes ser mayor de edad para ingresar'
end

if age == 18
  then
  puts 'You are an adult'
end

# Unless statement:
# Executes a block of code if a specified condition is false.

unless name == confirm_name && last_name == confirm_last_name
  puts 'You are not the right user'
end

unless name != confirm_name && last_name != confirm_last_name
  puts 'You are not the right user'
else
  puts 'You are the right user'
end

# case statement:
# Executes different blocks of code based on the value of a variable.

case age
when 0..5
  puts 'You are a baby'
when 6..12
  puts 'You are a child'
when 13..17
  puts 'You are a teenager'
else
  puts 'You are an adult'
end

# Looping Statements

# while loop:
# Repeats a block of code as long as a specified condition is true.

age = 0
while age <= 18
  puts 'You are a kid'
  age += 1
end

# until loop:
# Repeats a block of code as long as a specified condition is false.

age = 0
until age >= 18
  puts 'You are another kid'
  age += 1
end

# for loop:
# Iterates over each element in a collection.

for square in 0..5
  puts square * 2
end

# Each Method:
# Iterates over each element in a collection using a block.
numbers = [5, 4, 3, 2, 1]
numbers.each do |sqaure|
  puts sqaure * 2
end

# Times Method:
# Executes a block of code a specified number of times
5.times do |i|
  puts "Iteration #{i}"
end

# Upto Method:
# Iterate over a range of numbers from start to end

6.upto(10) do |i|
  puts "Square is #{i * 2}"
end

# Downto Method:
# Iterates over a range of numbers from start to end in descending order
10.downto(5) do |i|
  puts "Square is #{i * 2}"
end

# Loop Method:
# Executes a block of code indefinitely until a break statement is encountered.
count = 0
loop do
  puts "Count is #{count}"
  count += 1
  break if count >= 5
end

# Jump Statements:

# Break Statements:
# Exits a loop prematurely.

count = 0
while true
  puts "Count is #{count}"
  count += 1
  break if count <= 7
end

# Next Statements:
# Skips the current iteration of a loop and moves to the next iteration.
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_array.each do |element|
  next if element.even?

  puts "odd element is #{element}"
end

# Redo Statements:
# Restarts the current iteration of a loop without checking the loop condition.
count = 0
loop do
  puts "Count is #{count}"
  count += 1
  redo if count < 5
  break
end

# Retray Statements:
# Restarts a begin-rescue block from the beginning.
begin
  puts 'Trying to divide by zero'
  1 / 0
rescue ZeroDivisionError
  puts 'Caught an exception, retrying...'
  # retry
end

# Return Statements:
# Exits a method and optionally returns a value.
def greet(name)
  return "Hello, #{name}!"
end
puts greet('Alice')

# Exception Handling:

# Begin-rescue-ensure Statement
# Handles exceptions and ensures that certain code is executed
# regardless of whether an exception occurs.

begin
  puts 'Dividing by zero'
  1 / 0
rescue ZeroDivisionError => e
  puts "Caught an exception: #{e.message}"
ensure
  puts 'This will always be executed.'
end

# Raise Statement
# Raises an exception.

def check_age(age)
  raise 'Age must be a positive number' if age <= 0

  puts "Age is #{age}"
end

begin
  check_age(-1)
rescue => e
  puts "Caught an exception: #{e.message}"
end

# DIFICULTAD EXTRA:
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

range = 10..55
range.each do |number|
  if (number % 2).zero? && number != 16 && number % 3 != 0
    puts number
  end
end

for number in range
  if (number % 2).zero?
    if number != 16 && number % 3 != 0
      puts number
    end
  end
end