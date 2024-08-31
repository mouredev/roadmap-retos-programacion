"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""


def main():
    for number in range(10, 56):
        if number % 2 == 0 and number != 16 and number % 3 != 0:
            print(number)


if __name__ == "__main__":
    main()
