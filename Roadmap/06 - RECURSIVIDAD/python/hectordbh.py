"""EJERCICIO"""

def decrease(num):
    """Función que devuelve valores decrecientes uno a uno
    hasta cero.

    Args:
        num (int): valor inicial

    Returns:
        int: valores
    """
    # Caso final
    if num < 0:
        return num
    print(num)
    decrease(num-1)

decrease(100)
