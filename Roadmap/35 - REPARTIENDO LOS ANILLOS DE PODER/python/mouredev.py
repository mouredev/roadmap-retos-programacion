def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if (number % i) == 0:
            return False
    return True


def distribute_rings(total_rings: int):

    sauron = 1
    total_rings -= sauron

    distributed_rings = []

    for men in range(2, total_rings, 2):
        for elves in range(1, total_rings, 2):
            dwarves = total_rings - men - elves
            if dwarves > 0 and is_prime(dwarves):
                distributed_rings.append({
                    "Hombres": men,
                    "Elfos": elves,
                    "Enanos": dwarves,
                    "Sauron": sauron
                })

    if distributed_rings:
        return distributed_rings

    return "No es posible distribuir los anillos de poder."


try:
    total_rings = int(
        input("Introduce el número de anillos de poder que quieres repartir: ")
    )
    distributed_rings = distribute_rings(total_rings)

    if isinstance(distributed_rings, list):
        print("Posibles distribuciones de los anillos de poder:\n")

        for index, distribution in enumerate(distributed_rings):
            print(f"{index + 1}. {distribution}")

        print(
            f"\nDistribución media {
                distributed_rings[int(len(distributed_rings) / 2)]}"
        )

    else:
        print(distributed_rings)
except ValueError:
    print("Por favor, introduce un número entero de anillos.")
