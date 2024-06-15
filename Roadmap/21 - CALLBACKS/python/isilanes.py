import random
from time import sleep


def main():
    print("===== MAIN =====")

    # Definimos funciones que usaremos como callback:
    def add(a: int, b: int) -> int:
        return a + b

    def multiply(a: int, b: int) -> int:
        return a * b

    # Definimos funcion que usa callbacks:
    def perform_operation(first: int, second: int, operation: callable) -> int:
        return operation(first, second)

    # Usamos la función con callbacks:
    assert perform_operation(1, 2, add) == 3
    assert perform_operation(1, -2, add) == -1
    assert perform_operation(1, -2, multiply) == -2
    assert perform_operation(0, -2, multiply) == 0
    print("main() ejecutado con éxito")


def extra():
    print("===== EXTRA =====")

    def confirm_base(dish: str) -> None:
        print(f"Pedido '{dish}' confirmado!")

    def confirm_premium(dish: str) -> None:
        print(f"Su excelencia, su pedido '{dish}' ha sido confirmado.")

    def ready_base(dish: str) -> None:
        print(f"Pedido '{dish}' listo!")

    def ready_premium(dish: str) -> None:
        print(f"Vuecencia, su pedido '{dish}' está ya listo.")

    def delivered_base(dish: str) -> None:
        print(f"Pedido '{dish}' entregado!")

    def delivered_premium(dish: str) -> None:
        print(f"Alteza, su pedido '{dish}' ha sido ya entregado.")

    def process_dish(dish: str, user_credit: int) -> None:
        confirm, ready, delivered = confirm_base, ready_base, delivered_base
        if user_credit > 1000:
            confirm, ready, delivered = confirm_premium, ready_premium, delivered_premium

        confirm(dish)
        sleep(random.randrange(1, 10))
        ready(dish)
        sleep(random.randrange(1, 10))
        delivered(dish)

    process_dish("Ostras rellenas de caviar", user_credit=5000)
    process_dish("Bocata de fuagrás", user_credit=5)


if __name__ == "__main__":
    main()
    extra()
