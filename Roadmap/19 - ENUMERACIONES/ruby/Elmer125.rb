#  * EJERCICIO:
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).

class Week
  DAYS_OF_THE_WEEK = { 1 => "Monday", 2 => "Tuesday", 3 => "Wednesday", 4 => "Thursday", 5 => "Friday", 6 => "Saturday", 7 => "Sunday" }

  def self.get_day(day)
    puts DAYS_OF_THE_WEEK[day]
  end
end

Week.get_day(1) # monday
Week.get_day(2) # tuesday
Week.get_day(3) # wednesday

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.

class Orders
  attr_accessor :id, :state
  ORDERS_STATES = { 1 => "PENDING", 2 => "SENT", 3 => "DELIVERED", 4 => "CANCELED" }

  def initialize(id)
    @id = id
    @state = 1
  end

  def show_state
    puts "The state of order #{@id} is #{ORDERS_STATES[@state]}"
  end

  def send_order
    if @state == 1
      @state = 2
      show_state
    else
      puts "Order #{@id} can't be sent"
    end
  end

  def deliver_order
    if @state == 2
      @state = 3
      show_state
    else
      puts "Order #{@id} can't be delivered"
    end
  end

  def cancel_order
    case @state
    when 2
      puts "Order #{@id} can't be canceled because it has been sent"
      show_state
    when 3
      puts "Order #{@id} can't be canceled because it has been delivered"
      show_state
    else
      @state = 4
      show_state
    end
  end
end

box = Orders.new(1)
box.show_state
box.send_order
box.cancel_order
box.deliver_order
