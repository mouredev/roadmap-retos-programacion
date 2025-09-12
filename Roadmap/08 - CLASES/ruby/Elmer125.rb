#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos utilizando su función.

class SayHello
  def initialize(name, age)
    @name = name
    @age = age
  end

  def print_name
    puts "Hello #{@name}"
  end

  def print_age
    puts "You are #{@age} years old"
  end
end

hello_ruby = SayHello.new('Ruby', 10)

hello_ruby.print_name
hello_ruby.print_age

#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  */

class WebNavigation
  def initialize
    @stack = []
  end

  def navigate(option)
    unless option == 'exit'
      case option
      when 'back'
        remove_web
        puts "You are in #{@stack.first}"
      when 'forward'
        puts "You are in #{@stack[1]}"
      else
        add_web(option)
      end
    end
  end

  def add_web(web)
    @stack.unshift(web)
  end

  def remove_web
    @stack.shift
  end
end

browser = WebNavigation.new

browser.navigate('google')
browser.navigate('facebook')
browser.navigate('twitter')
browser.navigate('back')
browser.navigate('back')
browser.navigate('exit')

class SharedPrinter
  def initialize
    @queue = []
  end

  def print_document
    document = @queue.pop
    puts "Printing #{document}"
  end

  def add_document(document)
    puts "Adding #{document} to the queue"
    @queue.push(document)
  end
end

printer = SharedPrinter.new

printer.add_document('Document 1')
printer.add_document('Document 2')
printer.add_document('Document 3')
printer.print_document
printer.print_document
printer.print_document
