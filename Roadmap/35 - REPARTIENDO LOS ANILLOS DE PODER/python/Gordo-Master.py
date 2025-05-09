# 35 - Repartiendo los anillos del poder

def is_prime(number) -> bool:
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    else:
        return True

def distr_rings(rings):

    sauron = 1
    rings -= sauron

    distributed_rings = []

    for humans in range(2, rings, 2):
        for elves in range(1, rings, 2):
            dwarfs = rings - humans - elves
            if dwarfs > 0 and is_prime(dwarfs):
                distributed_rings.append({
                    "Sauron" : sauron,
                    "Elfs" : elves,
                    "Dwarfs" : dwarfs,
                    "Humans" : humans
                    }
                )
    
    if distributed_rings:
        return distributed_rings
    else:
        print("No se puede distribuir los anillos de poder")

try:
    rings = int(input("Elige la cantidad de anillos: "))
    if rings < 0:
        raise ValueError

except ValueError:
    print("Ingresa un numero entero, mayor que 0")

else:
    distributed_rings = distr_rings(rings)

    if isinstance(distributed_rings, list):
        print("Posibles combinaciones de distribución")

        for index, i in enumerate(distributed_rings):
            print(f"{index}. {i}")

        print(f"Distribución media: {distributed_rings[int(len(distributed_rings)/2)]}")

