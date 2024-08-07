from enum import Enum


class Day(int, Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @property
    def spanish_name(self) -> str:
        return {
            self.MONDAY: "lunes",
            self.TUESDAY: "martes",
            self.WEDNESDAY: "miércoles",
            self.THURSDAY: "jueves",
            self.FRIDAY: "viernes",
            self.SATURDAY: "sábado",
            self.SUNDAY: "domingo",
        }.get(self, "DESCONOCIDO")


def main(index: int):
    print("==== EJERCICIO ====")

    print(f"\nAl índice {index} le corresponde el siguiente objeto:")
    day = Day(index)
    print(f">>> day = Day({index})")
    print(f">>> str(day) == '{str(day)}'")
    print(f"El valor correspondiente es:")
    print(f">>> day.name == '{day.name}'")
    print("Para imprimir un valor 'humano' usaremos un método personalizado,")
    print("que deberemos haber implementado nosotros:")
    print(f">>> day.spanish_name == '{day.spanish_name}'")


class Status(int, Enum):
    """
    Uso nombres en castellano por respeto al enunciado, pero niños,
    nunca uséis otra cosa que no sea inglés para nombrar variables.
    """
    PENDIENTE = 0
    ENVIADO = 1
    ENTREGADO = 2
    CANCELADO = 3


class Order:
    """
    Implemento la funcionalidad como métodos de la clase, y no como funciones,
    porque modifican el estado del objeto, porque no modifican nada externo,
    y porque sólo requieren el propio estado del objeto como entrada.

    Si se dieran otras circunstancias, podría valorarse implementar una función
    send(order), en vez de un método order.send().
    """

    def __init__(self, oid: int, status: Status = Status.PENDIENTE):
        self.oid = oid
        self.status = status

    def send(self) -> bool:
        """
        Returns:
             True if succeeded, False otherwise.
        """
        if self.status == Status.PENDIENTE:
            print(f"El pedido {self.oid} pasa de estado {self.status.name} a {Status.ENVIADO.name}.")
            self.status = Status.ENVIADO
            return True

        if self.status == Status.ENVIADO:
            print(f"El pedido {self.oid} ya se encuentra en estado {self.status.name}. Ignorando orden...")
            return True

        print(f"El pedido {self.oid} se encuentra en el estado {self.status.name}, y no puede ser enviado.")
        return False

    def cancel(self) -> bool:
        """
        Returns:
             True if succeeded, False otherwise.
        """
        if self.status == Status.CANCELADO:
            print(f"El pedido {self.oid} ya se encuentra en estado {self.status.name}. Ignorando orden...")
            return True

        if self.status == Status.ENTREGADO:
            print(f"El pedido {self.oid} se encuentra en estado {self.status.name}, no puede cancelarse.")
            return False

        print(f"El pedido {self.oid} pasa de estado {self.status.name} a {Status.CANCELADO.name}.")
        self.status = Status.CANCELADO
        return True

    def deliver(self) -> bool:
        """
        Returns:
             True if succeeded, False otherwise.
        """
        if self.status == Status.ENVIADO:
            print(f"El pedido {self.oid} pasa de estado {self.status.name} a {Status.ENTREGADO.name}.")
            self.status = Status.ENVIADO
            return True

        print(f"El pedido {self.oid} se encuentra en estado {self.status.name}, y no puede ser entregado.")
        return False


def extra():
    print("\n==== EXTRA ====")

    print("\nCreamos un pedido con ciclo de vida normal:")
    print('>>> order = Order(1)')
    order = Order(1)
    print('>>> order.send()')
    order.send()
    print('>>> order.deliver()')
    order.deliver()

    print("\nCreamos un pedido que intentamos enviar dos veces:")
    print('>>> order = Order(2)')
    order = Order(2)
    print('>>> order.send()')
    order.send()
    print('>>> order.send()')
    order.send()

    print("\nCreamos un pedido que cancelamos antes de enviar, y luego intentamos enviar:")
    print('>>> order = Order(3)')
    order = Order(3)
    print('>>> order.cancel()')
    order.cancel()
    print('>>> order.send()')
    order.send()

    print("\nCreamos un pedido que intentamos cancelar tras haber sido entregado:")
    print('>>> order = Order(4)')
    order = Order(4)
    print('>>> order.send()')
    order.send()
    print('>>> order.deliver()')
    order.deliver()
    print('>>> order.cancel()')
    order.cancel()

    print("\nCreamos un pedido que intentamos entregar antes de enviar:")
    print('>>> order = Order(5)')
    order = Order(5)
    print('>>> order.deliver()')
    order.deliver()


if __name__ == "__main__":
    main(index=1)
    extra()
