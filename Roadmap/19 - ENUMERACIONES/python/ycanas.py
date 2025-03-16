from enum import Enum

# ------ Ejercicio

class Days(Enum):

    MONDAY: int = 1
    TUESDAY: int = 2
    WEDNESDAY: int = 3
    THURSDAY: int = 4
    FRIDAY: int = 5
    SATURDAY: int = 6
    SUNDAY: int = 7


for i in range(7):
    print(Days(i + 1).name)


# ------ Extra

class State(Enum):

    OPEN: int = 1
    SHIPPED: int = 2
    DELIVERED: int = 3
    CANCELLED: int = 4


class Order:

    identifier: int
    state: State


    def __init__(self, state: State, identifier: int) -> None:
        self.state = state
        self.identifier = identifier


    def get_state(self):
        return f"* Order #{self.identifier} {self.state.name}"

    
    def send(self):
        if self.state == State.OPEN:
            self.state = State.SHIPPED
            print(f"* Order #{self.identifier} {self.state.name}")
            return
        
        self.__error()


    def deliver(self):
        if self.state == State.SHIPPED:
            self.state = State.DELIVERED
            print(f"* Order #{self.identifier} {self.state.name}")
            return
        
        self.__error()


    def cancel(self):
        if self.state == State.OPEN or self.state == State.SHIPPED:
            self.state = State.CANCELLED
            print(f"* Order #{self.identifier} {self.state.name}")
            return
        
        self.__error()

    
    def __error(self):
        print(f"* [Error] imposible change state, actual state ({self.state.name})")



pc = Order(State.OPEN, 1587454)
print(pc.get_state())
pc.send()
pc.deliver()
pc.cancel()
