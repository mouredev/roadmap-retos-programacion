# 19 - Enumeraciones
from enum import Enum

class WeekDay(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def show_day(num):
    print(WeekDay(num).name)

show_day(2)

"""
Ejercicio Extra
"""
class State(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Request():

    def __init__(self,id: int, state: State = State(1)) -> None:
        self.id = id
        self.state = state
    
    def send(self):
        if self.state == State.PENDIENTE:
            self.state = State.ENVIADO
            print(f"Se ha {State(self.state).name} el pedido {self.id}")

        elif self.state == State.ENVIADO:
            print(f"El pedido ({self.id}) ya se encuentra: {State(self.state).name}")

        else:
            print(f"No se pudo ejecutar el envio de {self.id}, porque esta: {State(self.state).name}")

    def cancel(self):
        if self.state != State.ENTREGADO and self.state != State.CANCELADO:
            self.state = State.CANCELADO
            print(f"Se ha {State(self.state).name} el pedido {self.id}")

        elif self.state == State.CANCELADO:
            print(f"El pedido ({self.id}) ya se encuentra: {State(self.state).name}")

        else:
            print(f"No se pudo cancelar pedido ({self.id}), porque esta: {State(self.state).name}")

    def delivered(self):
        if self.state == State.ENVIADO:
            self.state = State.ENTREGADO
            print(f"Se ha {State(self.state).name} el pedido {self.id}")

        elif self.state == State.ENTREGADO:
            print(f"El pedido ({self.id}) ya se encuentra: {State(self.state).name}")

        else:
            print(f"No se pudo entregar el pedido ({self.id}), porque esta: {State(self.state).name}")

    def show_state(self):
        print(f"El estado del pedido {self.id} es: {State(self.state).name}")

requet_1 = Request("r_1")
requet_2 = Request("r_2")

print(requet_1.id)
print(requet_1.state)

# Pendiente
requet_1.send()
# Enviado
requet_1.cancel()
# Cancelado
requet_1.send()
requet_1.delivered()
requet_1.show_state()

# Pendiente
requet_2.delivered()
requet_2.send()
# Enviado
requet_2.send()
requet_2.delivered()
# Entregado
requet_2.send()
requet_2.cancel()
requet_2.delivered()
