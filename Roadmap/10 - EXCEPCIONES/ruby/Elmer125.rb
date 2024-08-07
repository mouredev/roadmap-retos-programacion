#  * EJERCICIO:
#  * Explora el concepto de manejo de excepciones según tu lenguaje.
#  * Fuerza un error en tu código, captura el error, imprime dicho error
#  * y evita que el programa se detenga de manera inesperada.
#  * Prueba a dividir "10/0" o acceder a un índice no existente
#  * de un listado para intentar provocar un error.
# Guide: https://www.honeybadger.io/blog/a-beginner-s-guide-to-exceptions-in-ruby/

begin
  #Any exceptions in here...
  10/0
rescue
  #...will be rescued here
  # do something
end

begin
  10/0
  #Ruby has a Exception object that can be used to rescue exceptions
rescue ZeroDivisionError => e
  puts "Exception class: #{ e.class.name }"
  puts "Exception message: #{ e.message }"
  puts "Exception backtrace: #{ e.backtrace }"
end

#Raising your own exceptions
begin
  # raise an ArgumentError with the message
  raise ArgumentError.new("This is an argument error")
rescue ArgumentError => e
  puts e.message
end

begin
  # raise an RuntimeError with the message
  # raise RuntimeError, "This is an error"
  raise RuntimeError.new("This is a runtime error")
rescue RuntimeError => e
  puts e.message
end

begin
  raise "Here's the exception"
  #This use a StandardError
  # rescue StandardError => e
rescue => e
  puts e
end

fruit_list = ["apple", "banana", "cherry"]

begin
  fruit_list[3]
  raise RuntimeError.new("The fruit is not in the list")
rescue RuntimeError => e
  puts e.message
end


#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que sea capaz de procesar parámetros, pero que también
#  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
#  * corresponderse con un tipo de excepción creada por nosotros de manera
#  * personalizada, y debe ser lanzada de manera manual) en caso de error.
#  * - Captura todas las excepciones desde el lugar donde llamas a la función.
#  * - Imprime el tipo de error.
#  * - Imprime si no se ha producido ningún error.
#  * - Imprime que la ejecución ha finalizado.

class CustomError < StandardError
  def initialize(message)
    super(message)
  end
end

def process_params(param)
  if param.class != String
    raise ArgumentError.new("The parameter is not a string")
  elsif param.length < 5
    raise RuntimeError.new("The string is too short")
  elsif param.length > 10
    raise CustomError.new("The string is too long")
  end
end

begin
  process_params("Hello from Ruby")
rescue ArgumentError, RuntimeError, CustomError  => e
  puts "Type error: #{e.class.name}"
  puts e.message
else
  puts "No errors"
ensure
  puts "Execution has finished"
end

