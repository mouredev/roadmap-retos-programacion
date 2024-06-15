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


if __name__ == "__main__":
    main()
