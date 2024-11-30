
=begin 
EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
=end

# This is the official Ruby website.: https://www.ruby-lang.org/es/

# Comment Syntax in Ruby:

# This is a single-line comment.

=begin 
This is another comment, but 
this time it spans multiple lines
=end

# Variable Definition: Variables can be defined and assigned values dynamically using the assignment operator (=).
greet = "hello"
name = "world"

# Constant Definition: Constants are variables that cannot be modified once assigned.
# Constants are defined with the first letter in uppercase.

PI = 3.1416
My_constant = "Hi"

# Print to screen.:
puts "#{greet}, #{name}"

greet = "hola" # It is possible to change the value of a previously defined variable.
name = "mundo"

puts "#{greet}, #{name}"

my_number = 8
puts my_number

# Data types in Ruby:

# Strings:
my_string = "This is a string."

# Integers: Whole numbers without decimals, like 42 or -7.
my_integer = 42

# Floats: Numbers with decimals, like 3.14 or -0.5
my_float = 3.14

# Booleans: Logical values that can be either true or false.
my_boolean = true
another_boolean = false

# Symbols: Immutable and unique values, like :name or :age, commonly used for labels or identifiers.
my_symbol = :name

# Nil: Nil: Represents the absence of a value or "nothing," it is a special value in Ruby, similar to null in other languages.
my_nil = nil

# Printinng to screen the language name we are learning:
language_name = "Ruby"
puts "¡Hola, #{language_name}!" # interpolation uses #{variable_name} to insert the value of the variable into the string

# Printing to screen data types:
puts "String: #{my_string}"
puts "Integer: #{my_integer}"
puts "Float: #{my_float}"
puts "Boolean: #{my_boolean}"
puts "Another Boolean: #{another_boolean}"
puts "Symbol: #{my_symbol}"
puts "Nil: #{my_nil}"

