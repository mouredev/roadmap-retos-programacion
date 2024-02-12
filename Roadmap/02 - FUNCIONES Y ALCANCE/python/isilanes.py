COLOR = "rojo"   # global variable
main_a = 2
main_b = 3


def i_accept_no_arg() -> None:
    print("Llamaste a una función sin argumentos (y que no retorna nada).")


def i_accept_two_arguments(first: str, second: str) -> None:
    print(f"Llamaste a una función con dos argumentos: {first}, {second} (y que no retorna nada).")


def i_have_a_default_argument(value: int = 33) -> None:
    print(f"Llamaste a una función con el argumento value = {value}")


def i_return_something(value: int = 0) -> int | None:
    print(f"Llamaste a una función con el argumento value = {value}")

    if not isinstance(value, int):
        return None

    return value * 2


def i_work_with_local_and_global() -> None:
    print(f"Dentro de la función conozco la variable global COLOR = {COLOR}")
    global main_a
    main_a = 4
    main_b = 5  # because this is not declared global, it will not affect outside
    print(f"Dentro de la función, las variables valen {main_a} y {main_b}")


def main():
    i_accept_no_arg()

    print("\nLlamo a una función con argumentos sin nombre:")
    i_accept_two_arguments("primero", "segundo")
    print("Llamo a la misma función con argumentos nombrados:")
    i_accept_two_arguments(first="primero", second="segundo")

    print("\nLlamo a una función pasando argumento:")
    i_have_a_default_argument(45)
    print("Llamo a la misma función sin argumento, usando el valor por defecto:")
    i_have_a_default_argument()

    print("\nLlamo a una función que devuelve algo, e imprimo lo que devolvió:")
    ret = i_return_something(123)
    print(f"El valor de retorno fue {ret}")

    print("\nLlamo a una función que usa variables globales y locales:")
    print(f"Antes de llamar a la funcíon, tengo dos variables con valor {main_a} y {main_b}")
    i_work_with_local_and_global()
    print(f"Tras llamar a la funcíon, los valores son {main_a} y {main_b}. Sólo la primera varió, porque la hice global.")


def extra(first: str, second: str) -> int:
    n_number = 0
    for i in range(1, 101):
        string = ""
        if not i % 3:
            string = first

        if not i % 5:
            string = f"{string}{second}"

        if string:
            print(string)
        else:
            print(i)
            n_number += 1

    return n_number


if __name__ == "__main__":
    main()
    n = extra("fiz", "buzz")
    print(f"Se escribió un número {n} veces")
