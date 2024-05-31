from enum import Enum


class Day_of_the_week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class State(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    CANCELADO = 3
    ENTREGADO = 4


class Order:
    id: int
    state: State

    def __init__(self, id):
        self.id = id
        self.state = State.PENDIENTE

    def pedido_enviado(self):
        if self.state != State.CANCELADO:
            self.state = State.ENVIADO
        else:
            print(f"El pedido {self.id} ha sido cancelado")

    def pedido_cancelado(self):
        if self.state == State.PENDIENTE:
            self.state = State.CANCELADO
        else:
            print(f"El pedido {self.id} ya ha sido enviado o entregado")

    def pedido_entregado(self):
        if self.state == State.ENVIADO:
            self.state = State.ENTREGADO
        else:
            print(f"El pedido {self.id} no ha sido enviado")

    def print_state(self):
        print(f"El estado del pedido {self.id} es: {self.state.name}")


def number_of_the_day(day: Day_of_the_week):
    print(f"{day.name} is the {day.value} day of the week")


def main():
    number_of_the_day(Day_of_the_week.MONDAY)

    order1 = Order(1)
    order2 = Order(2)
    order3 = Order(3)

    order1.print_state()
    order2.print_state()
    order3.print_state()

    order1.pedido_cancelado()
    order2.pedido_enviado()
    order3.pedido_entregado()

    order1.print_state()
    order2.print_state()
    order3.print_state()

if __name__ == '__main__':
    main()
