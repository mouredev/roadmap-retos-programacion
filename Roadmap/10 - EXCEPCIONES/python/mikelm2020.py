def divition(divider: int, dividend: int):
    try:
        result = dividend / divider
        return result
    except ZeroDivisionError:
        print("Error: La división entre cero no es permitida")
    except TypeError:
        print("Error: El Dividendo y el divisor deben ser números enteros.")
    except Exception as e:
        print("Un error inesperado ha ocurrido:", str(e))


class DictTypeError(Exception):
    pass


def process_parameters(parameters: list):
    if len(parameters) < 2:
        raise IndexError("La lista debe tener al menos dos elementos.")
    elif type(parameters[0]) is not int or type(parameters[1]) is not int:
        raise DictTypeError("Los elementos de la lista deben ser números enteros.")

    try:
        result = divition(parameters[0], parameters[1])
        print(
            f"El resultado de dividir {parameters[0]} entre {parameters[1]} es: {result}"
        )
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


if __name__ == "__main__":
    print(f"El resultado de dividir 120 entre cero es: {divition(0,120)}")

    try:
        process_parameters([2, "a"])
    except IndexError as e:
        print(f"{e}")
    except ZeroDivisionError as e:
        print(f"{e}")
    except DictTypeError as e:
        print(f"{e}")
    except Exception as e:
        print(f"{e}")
    else:
        print("No se ha producido ningún error.")
    finally:
        print("El programa finaliza sin detenerse.")
