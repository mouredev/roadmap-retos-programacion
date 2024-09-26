#  * EJERCICIO:
#  * Explora el concepto de funciones de orden superior en tu lenguaje
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
# Doc: https://medium.com/@jeffcoh23/eloquent-ruby-achieving-higher-order-functionality-933267a01f36
#      https://www.rubyguides.com/2016/02/ruby-procs-and-lambdas/
# Ruby hasn't Higher Order Functions, but it has blocks, procs and lambdas.

# pass a lambda to a method
def add_stuff(a, b, my_lambda)
  c = a + b
  my_lambda.call(c)
end
example_lambda = lambda { |c| puts "The sum is #{c}" }
add_stuff(1, 2, example_lambda)

def multiply_stuff(a, b, my_proc)
  c = a * b
  my_proc.call(c)
end
multiply_stuff(2, 3, ->(c) { puts "The product is #{c}" })

def divide_stuff(a, b, &block)
  c = a / b
  block.call(c)
end

divide_stuff(6, 3) { |c| puts "The division is #{c}" }

#  * DIFICULTAD EXTRA (opcional):
#  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
#  * lista de calificaciones), utiliza funciones de orden superior para
#  * realizar las siguientes operaciones de procesamiento y análisis:
#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.
#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.
#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.
#  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

# students = [
#   { name: 'Alice', birthdate: '1990-01-01', grades: [9, 8, 7, 10, 9] },
#   { name: 'Bob', birthdate: '1991-01-01', grades: [8, 7, 6, 9, 8] },
#   { name: 'Charlie', birthdate: '1992-01-01', grades: [7, 6, 5, 8, 7] },
# ]

students = [ :name => 'Alice', :birthdate => '1990-01-01', :grades => [9, 8, 9, 10, 9] ] +
          [ :name => 'Bob', :birthdate => '1991-01-01', :grades => [8, 10, 6, 9, 5] ] +
          [ :name => 'Charlie', :birthdate => '1992-01-01', :grades => [7, 6, 5, 8, 7] ]

def average_grades(grades)
  grades.sum / grades.length
end

puts "Average grades:"
puts students.map { |student| "#{student[:name]}: #{average_grades(student[:grades])}" }

puts "Best students:"
puts students.select { |student| average_grades(student[:grades]) >= 9 }.map { |student| student[:name] }

puts "Youngest students:"
puts students.sort_by { |student| student[:birthdate] }.map { |student| student[:name] }.reverse

puts "Highest grade:"
puts students.map { |student| student[:grades].max }.max