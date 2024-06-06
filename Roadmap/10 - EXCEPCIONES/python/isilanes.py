class NotThreeError(Exception):

    def __init__(self, n: int):
        msg = f"Sadly, {n} is not 3, which is the best number."
        super().__init__(msg)


def main():
    elements = [1, 2, 3, 4]
    x = None
    try:
        index = 10
        x = elements[index]
        print("Esta línea no será imprimida, por dar la anterior error.")
    except IndexError as e:
        print(f"No pudimos extraer el elemento {index}, porque 'elements' sólo tiene {len(elements)} elementos.")
        print(f"El error fue: {e}")

    if x is None:
        print("Pues no, no pudimos extraer x.")


def extra():
    value_pairs = (
        (1, "a"),
        (1.0, 2),
        (1, 0),
        (1, 2),
        (3, 2),
    )

    for num, dem in value_pairs:
        try:
            ret = division(num, dem)
        except TypeError as e:
            print(f"Error (tipo {e.__class__.__name__}) en argumentos ({num}, {dem}): {e}")
            continue
        except ZeroDivisionError as e:
            print(f"Error (tipo {e.__class__.__name__}) en denominador ({num}, {dem}): {e}")
            continue
        except NotThreeError as e:
            print(f"Error (tipo {e.__class__.__name__}) en numerador ({num}, {dem}): {e}")
            continue

        print(f"Éxito: {num}/{dem} es {ret}")

    print("La ejecución ha finalizado.")


def division(numerator: int, denominator: int) -> float:
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Qué parte de 'numerator and denominator must be integers' no entendiste?")

    if denominator == 0:
        raise ZeroDivisionError("Vamos, tío, sabes que no se puede dividir entre cero!")

    if numerator != 3:
        raise NotThreeError(numerator)

    return numerator/denominator


if __name__ == "__main__":
    main()
    extra()
