"""
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
"""


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for n in range(2, number):
        if number % n == 0:
            return False

    return True


def odd_numbers(number: int) -> list[int]:
    return list(filter(lambda n: not is_even(n), range(1, number)))


def even_numbers(number: int) -> list[int]:
    return list(filter(lambda n: is_even(n), range(1, number)))


def ask_rings() -> int:
    while True:
        try:
            rings = input("Introduce la cantidad de anillos a repartir:\n > ")
            assert (
                rings.isnumeric() and int(rings) > 0
            ), "\nDebes introducir un número entero positivo (>0)."
        except AssertionError as error:
            print(error)
        else:
            return int(rings)


def combine_options(total_rings: int) -> list[dict[str, int]]:
    solution = []

    # Give one ring to Sauron
    total_rings -= 1

    # Get possible values for the rest races
    for man in even_numbers(total_rings):
        for elf in odd_numbers(total_rings):
            dwarf = total_rings - elf - man
            if dwarf > 0 and is_prime(dwarf):
                solution.append(
                    {
                        "Elfos": elf,
                        "Enanos": dwarf,
                        "Hombres": man,
                        "Sauron": 1,
                    }
                )

    return solution


def print_result(results: list[dict[str, int]]):
    if not results:
        print("No se ha encontrado ninguna solución.")
        return

    for i, result in enumerate(results):
        print(f"\nSOLUCIÓN {i + 1}:")
        for race, ring_qty in result.items():
            print(f"{race}: {ring_qty}")


def repartition():
    total_rings = ask_rings()

    results = combine_options(total_rings)
    print_result(results)


if __name__ == "__main__":
    repartition()
