#  * EJERCICIO:
#  * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
#  * asíncrona una función que tardará en finalizar un número concreto de
#  * segundos parametrizables. También debes poder asignarle un nombre.
#  * La función imprime su nombre, cuándo empieza, el tiempo que durará
#  * su ejecución y cuando finaliza.
# Doc: https://ruby-doc.org/core-2.5.1/Thread.html

def async_method(name, seconds)
  Thread.new do
    puts "Task #{name} started at #{Time.now}, will run for #{seconds} seconds"
    sleep(seconds)
    puts "Task #{name} finished at #{Time.now}"
  end
end

thread1 = async_method("A", 5)
thread2 = async_method("B", 3)

thread1.join
thread2.join


#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando el concepto de asincronía y la función anterior, crea
#  * el siguiente programa que ejecuta en este orden:
#  * - Una función C que dura 3 segundos.
#  * - Una función B que dura 2 segundos.
#  * - Una función A que dura 1 segundo.
#  * - Una función D que dura 1 segundo.
#  * - Las funciones C, B y A se ejecutan en paralelo.
#  * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.

method_c = async_method("C", 3)
method_b = async_method("B", 2)
method_a = async_method("A", 1)
[ method_c, method_b, method_a ].each(&:join)
method_d = async_method("D", 1)
method_d.join
