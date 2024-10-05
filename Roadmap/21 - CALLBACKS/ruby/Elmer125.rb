#  * EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.
# Doc: https://stackoverflow.com/questions/1677861/how-to-implement-a-callback-in-ruby

def say_hello(name, callback)
  puts "I'm going to say hello to #{name}"
  callback.call(name)
end

def greet(name)
  puts "Hello, #{name}!"
end

say_hello("Alice", method(:greet))

# def do_stuff(a, b, c, &block)
#   sum = a + b + c
#   yield sum
# end

def do_stuff(a, b, c)
  sum = a + b + c
  yield sum
end

do_stuff(1, 2, 3) { |sum| puts "The sum is #{sum}" }


#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.

def order_process(dish, confirm, ready, deliver)
  Thread.new do
    puts "Processing order for #{dish}..."
    sleep(rand(1..10))
    confirm.call(dish)
    sleep(rand(1..10))
    ready.call(dish)
    sleep(rand(1..10))
    deliver.call(dish)
  end
end

def confirm_order(dish)
  puts "Order confirmed for #{dish}"
end

def ready_order(dish)
  puts "#{dish} is ready"
end

def deliver_order(dish)
  puts "#{dish} has been delivered"
end

pizza = order_process("Pizza", method(:confirm_order), method(:ready_order), method(:deliver_order))
hot_dog = order_process("Hot dog", method(:confirm_order), method(:ready_order), method(:deliver_order))
soup = order_process("Soup", method(:confirm_order), method(:ready_order), method(:deliver_order))
rice_with_chicken = order_process("Rice with chicken", method(:confirm_order), method(:ready_order), method(:deliver_order))

[pizza, hot_dog, soup, rice_with_chicken].each(&:join)