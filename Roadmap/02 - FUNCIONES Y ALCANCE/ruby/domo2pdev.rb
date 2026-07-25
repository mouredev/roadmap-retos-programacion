# frozen_string_literal: true

# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.

# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

# Funciones Definidas por el usuario

# Simple funcions:
def greet
  puts 'Hello, Ruby'
end

greet

# Return functions: Ruby methods return the value of the last evaluated expression by default,
#  so explicitly using return at the end of a method is not recomended for convention.

def return_greet
  puts 'Hello, ReturnedRuby'
end

greet = return_greet
puts greet
puts return_greet

# Functions with parameters or aguments:
def square(number)
  number**2
end

my_square = square(2)
puts my_square
puts square(3)

def add(number_a, number_b)
  number_a + number_b
end

puts add(1, 2)

# Functions with default parameters:
def circle_area(radius, my_pi = 3.1416)
  return 'Radius shuld be a positive number' if radius.negative? # Here you can use a return expression

  my_pi * (radius**2)
end

result_circle_area = circle_area(-5)
puts result_circle_area
puts circle_area(5)

# keyword arguments:
def division(dividend:, divisor:)
  dividend / divisor
end

resul_division = division(divisor: 5, dividend: 10)
puts resul_division
puts division(dividend: 24, divisor: 4)

# multiple return functions:
def return_functions(place_a, place_b)
  puts place_a, place_b
end

puts return_functions(1, 2)

# Variable number of arguments:

def variable_arg_greet(*names)
  names.each { |name| puts "Hola, #{name}" }
end

variable_arg_greet('Juan', 'Pablo', 'Jorge', 'Ringo')

def variable_arg_greet2(*names)
  names.each do |name|
    puts "Hi, #{name}"
  end
end

variable_arg_greet2('John', 'Paul', 'George', 'Ringo')

def sum(*args)
  args.sum
end

puts sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def variable_keyword_arg_greet(**names)
  names.each { |name| puts "Mission, #{name}" }
end

variable_keyword_arg_greet(Name: 'John', Last_name: 'Connor', Target: 'Yes', Location: 'Unknown')

# Nested functions:
# It is a function that is defined inside another function.

# This is a nested function to see an example but not recommended practice
def outer_function
  puts 'Outer function'

  def inner_function
    puts 'Inner function'
  end
end

outer_function
inner_function

# In Ruby Method definitions must not be nested. Use lambda instead.

# Bilt-in functions:
# See https://ruby-doc.org/core-2.7.0/ for more information

def square_root(number)
  Math.sqrt(number)
end

puts square_root(16)

def who_am_i
  puts 'Enter your name'
  firts_name = gets.chomp

  puts 'Enter your last name'
  last_name = gets.chomp

  puts "Your name is #{firts_name} #{last_name}"
end

who_am_i

# Variable scoop in ruby:

# Global variables are accessible from anywhere in the program.
# their use is generally discouraged due to potential side effects
# and reduced code maintainability.

$global_var = 'I am accessible everywhere!'

def some_method
  puts $global_var # Accessible here
end

some_method # Outputs: I am accessible everywhere!
puts $global_var

# Local variables are accessible only within the scope of the method
# where they are declared.

def my_method
  local_variable = 'I am only accessible inside this method'
  puts local_variable
end

my_method

# puts local_variable # This would raise an error as local_variable is not accessible here.

# Instance variables:
# Instance variables are specific to each instance of a class.

class MyClass
  def setting_value(value)
    @instance_var = value
  end

  def getting_value
    @instance_var
  end
end

obj = MyClass.new
obj.setting_value(10)
puts obj.getting_value # Outputs: 10

# Class variables:
# Class variables are shared among all instances of a class.
# They are defined using the @@ prefix.

class MyClass
  @@class_var = 'I am a class variable'

  def self.show_class_var
    puts @@class_var
  end
end

MyClass.show_class_var # Outputs: I am a class variable

# Constants:
# Constants are variables that should not change once assigned.
# They start with an uppercase letter.

PI = 3.1416

puts PI # Outputs: 3.1416

# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.

# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

# Prints numbers from 1 to 100 with specific substitutions:
# - If the number is a multiple of 3, prints the first text parameter.
# - If the number is a multiple of 5, prints the second text parameter.
# - If the number is a multiple of both 3 and 5, prints the concatenation of both text parameters.
# - Otherwise, prints the number itself and increments the count of such numbers.
# Parameters:
# - text1: String to print for multiples of 3.
# - text2: String to print for multiples of 5.
def print_numbers(text1, text2)
  count = 0
  101.times do |number|
    if (number % 3).zero? && (number % 5).zero?
      puts text1 + text2
    elsif (number % 3).zero?
      puts text1
    elsif (number % 5).zero?
      puts text2
    else
      puts number
      count += 1
    end
  end
  count
end

print(print_numbers('Es multiplo de 3', 'Es multiplo de 5'))
