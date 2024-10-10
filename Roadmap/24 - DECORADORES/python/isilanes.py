def verbose(func: callable) -> callable:

    def wrapper(*args, **kwargs):
        print(f"Llamamos a {func.__name__}() con argumentos: {args} y {kwargs}")

        return func(*args, **kwargs)

    # Hacemos esto para preservar el nombre de la función decorada, si se usan múltiples decoradores:
    wrapper.__name__ = func.__name__

    return wrapper


@verbose
def suma(a: int, b: int) -> int:
    return a + b


@verbose
def resta(a: int, b: int) -> int:
    return a - b


def count(func: callable) -> callable:

    def wrapper(*args, **kwargs):
        c = getattr(func, "count", 0)
        func.count = c + 1

        x = func(*args, **kwargs)

        print(f"Veces que se ha llamado a {func.__name__}(): {func.count}")

        return x

    # Hacemos esto para preservar el nombre de la función decorada, si se usan múltiples decoradores:
    wrapper.__name__ = func.__name__

    return wrapper


@count
def print_good_morning() -> None:
    print("Buenos días")


@count
def print_good_afternoon() -> None:
    print("Buenas tardes")


@count
@verbose
def print_good_night() -> None:
    print("Buenas noches")


@verbose
@count
def print_good_bye() -> None:
    print("Que te den")


def main():
    print("===== MAIN =====")

    print(suma(1, 2))
    print(suma(a=1, b=3))
    print(resta(1, 2))


def extra():
    print("\n===== EXTRA =====")
    print_good_morning()
    print_good_morning()
    print_good_morning()
    print_good_afternoon()

    print("\nLos decoradores se pueden componer, como con esta función que hemos decorado con @count y @verbose:")
    print_good_night()
    print_good_night()
    print_good_night()

    print("\nEn este caso, nuestros decoradores tienen la propiedad conmutativa (no siempre es el caso):")
    print("(print_good_bye() se ha decorado primero con @verbose y luego con @count)")
    print_good_bye()
    print_good_bye()

    print("\nLos decoradores también se pueden usar on-the-fly, sin tener que definir la función con ellos.")
    print("Por ejemplo, podemos aplicar @verbose a print_good_afternoon(), que ya usa @count de por sí:")
    print("(Notablemente, en este caso la cuenta sigue, porque hemos decorado la función que ya estaba decorada con @count)")
    f = verbose(print_good_afternoon)
    f()
    f()
    f()

    print("\nO podemos aplicar @count y @verbose a una función que no usaba decoradores:")

    def naked():
        print("Soy una función definida sin decoradores")

    f = count(verbose(naked))
    f()


if __name__ == "__main__":
    main()
    extra()
