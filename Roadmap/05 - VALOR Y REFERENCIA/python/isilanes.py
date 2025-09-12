def assignation():
    print("Python trata, de manera más o menos automática, a las variables INMUTABLES (p.e. int, str, tuple),")
    print("como pasadas por valor:")
    a = 1
    print("a = 1")
    b = a
    print("b = a")
    a += 1
    print("a += 1")
    print(f"a vale {a}, pero b sigue valiendo {b}")
    print(f"Podemos ver que a y b son objetos diferentes, porque id(a) == {id(a)} != id(b) == {id(b)}")
    print("¿Puedes ver el truqui? Efectivamente, el 'a+=1' NO modifica 'a', sino que le ASIGNA un nuevo valor.")

    print("\nPor otro lado, las variables MUTABLES (p.e. list, dict) se tratan como pasadas por referencia:")
    a = [1, 2, 3]
    print("a = [1, 2, 3]")
    b = a
    print("b = a")
    a.append(4)
    print("a.append(4)")
    print(f"a vale {a}, y b también se ha actualizado a {b}")
    print(f"Podemos ver que a y b son referencias al mismo objeto, porque id(a) == {id(a)} == id(b) == {id(b)}")

    print("\nSin embargo, es importante entender que la referencia común existe mientras ambos objetos mutables")
    print("sean MODIFICADOS:")
    a = [1, 2, 3]
    b = a
    print(f"id(a) == {id(a)} == id(b) == {id(b)}")
    b.pop()
    print("b.pop()")
    print(f"a == {a} == b == {b}")
    print(f"id(a) == {id(a)} == id(b) == {id(b)}")
    print("Si son REASIGNADOS, entonces la referencia común se rompe:")
    a = [4, 5, 6]
    print("a = [4, 5, 6]")
    print(f"b == {b} != a")
    print(f"id(b) sigue siendo {id(b)}, pero id(a) es {id(a)}")
    print("Realmente los objetos mutables se comportan como los inmutables: si los reasignas, se pierde")
    print("la referencia común. La diferencia es que en los inmutables esto es lo único que se puede hacer.")
    print("En los mutables, además, se pueden MODIFICAR (no reasignar) sin perder la referencia.")


def immutable_by_value(var: int) -> None:
    var += 1
    print(f"Dentro de la función: var == {var}")


def mutable_by_reference(var: dict) -> None:
    var["b"] = 123
    print(f"Dentro de la función: var == {var}")


def mutable_by_value(var: list) -> None:
    var = [e for e in var]  # var is now a local copy, separated from the argument passed
    var.append(3)
    print(f"Dentro de la función: var == {var}")


def main():
    assignation()

    print("\nUso de función que 'modifica' variable inmutable (mentira, las variables inmutables no se modifican)")
    print("El efecto es como si se pasara por valor:")
    var = 1
    print(f"Variable antes de función: var == {var}")
    immutable_by_value(var)
    print(f"Variable después de función: var == {var}")

    print("\nUso de función que modifica variable mutable. El efecto es como si se pasara por referencia:")
    var = {"a": 1, "b": 1}
    print(f"Variable antes de función: var == {var}")
    mutable_by_reference(var)
    print(f"Variable después de función: var == {var}")

    print("\nUso de función que modifica variable mutable localmente, siendo el efecto como pasar por valor:")
    var = [1, 2]
    print(f"Variable antes de función: var == {var}")
    mutable_by_value(var)
    print(f"Variable después de función: var == {var}")


def extra_function_1(var_a: list, var_b: list) -> tuple[list, list]:
    """
    This function receives two mutable variables 'var_a' and 'var_b'. It swaps their values in a
    'by value' fashion, so that the swap is NOT reflected out of the function.
    """
    var_b, var_a = var_a, var_b

    return var_a, var_b


def extra_function_2(var_a: list, var_b: list) -> tuple[list, list]:
    """
    This function receives two mutable variables 'var_a' and 'var_b'. It swaps their values in a
    'by reference' fashion, so that the swap IS reflected out of the function.

    This is a contrived example, nobody would do that in Python.
    """
    tmp = [e for e in var_a]
    var_a.clear()
    for e in var_b:
        var_a.append(e)
    var_b.clear()
    for e in tmp:
        var_b.append(e)

    return var_a, var_b


def extra():
    """
    Entiendo que el enunciado "crea dos programas" significa "crea dos funciones".
    """
    print("\nContenido extra:")
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(f"Antes de llamar a la Función 1 (pase por valor): a == {a}, b == {b}")
    x, y = extra_function_1(a, b)
    print("Después de llamar a la Función 1 (pase por valor):")
    print(f"Los valores de retorno están invertidos: {x} : {y}")
    print(f"Los valores originales no se modifican: {a} : {b}")

    a = [1, 2, 3]
    b = [4, 5, 6]
    print(f"\nAntes de llamar a la Función 2 (pase por referencia): a == {a}, b == {b}")
    x, y = extra_function_2(a, b)
    print("Después de llamar a la Función 2 (pase por referencia):")
    print(f"Los valores de retorno están invertidos: {x} : {y}")
    print(f"Los valores originales también están invertidos: {a} : {b}")


if __name__ == "__main__":
    main()
    extra()
