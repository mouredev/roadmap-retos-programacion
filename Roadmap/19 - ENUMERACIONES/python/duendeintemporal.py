#19 { Retos para Programadores } ENUMERACIONES

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 

"""

# Function to simulate console.log
log = print
# Days of the week as a constant dictionary
class DaysOfWeek:
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

# Function to show the day based on input
def show_day(day):
    w_days = [DaysOfWeek.MONDAY, DaysOfWeek.TUESDAY, DaysOfWeek.WEDNESDAY,
              DaysOfWeek.THURSDAY, DaysOfWeek.FRIDAY, DaysOfWeek.SATURDAY,
              DaysOfWeek.SUNDAY]
    return w_days[day - 1] if 1 <= day <= 7 else 'You entered an invalid day, try between 1 and 7'

log(DaysOfWeek.MONDAY)  # Monday
log(show_day(3))  # Wednesday

# Extra Difficulty Exercise

# Enum simulation
class OrderStatus:
    PENDING = 'Pending'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELED = 'Canceled'

# Order class
class Order:
    def __init__(self, id):
        self.id = id
        self.state = OrderStatus.PENDING

    def set_state(self, state):
        self.state = getattr(OrderStatus, state)

    def get_state(self):
        return self.state

    def ship_order(self):
        if self.state.lower() == OrderStatus.PENDING.lower():
            log('The order is Shipped')
            self.set_state('SHIPPED')
        else:
            log(f'Cannot ship. Current state: {self.state}')

    def deliver_order(self):
        if self.state.lower() == OrderStatus.SHIPPED.lower():
            log('The order is Delivered')
            self.set_state('DELIVERED')
        else:
            log(f'Cannot deliver. The order state is: {self.state}')

    def cancel_order(self):
        if self.state.lower() == OrderStatus.DELIVERED.lower():
            log('Cannot cancel. The order has already been delivered.')
        log('The order is Canceled')
        self.set_state('CANCELED')

    def describe_order(self):
        log(f'Order ID: {self.id}, Current State: {self.state}')

# Creating order instances
order15 = Order('001')
order16 = Order('002')
order17 = Order('003')

order16.ship_order()  # The order is Shipped
order15.deliver_order()  # Cannot deliver. The order state is: Pending
order17.ship_order()  # The order is Shipped

order16.deliver_order()  # The order is Delivered
order15.ship_order()  # The order is Shipped
order17.cancel_order()  # The order is Canceled

log(order16.get_state())  # Delivered
log(order15.get_state())  # Shipped
log(order17.get_state())  # Canceled

order16.ship_order()  # Cannot ship. Current state: Delivered
