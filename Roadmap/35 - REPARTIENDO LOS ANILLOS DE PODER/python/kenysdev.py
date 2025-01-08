# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 35 REPARTIENDO LOS ANILLOS DE PODER
# ------------------------------------
# ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
# ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
# entre las razas de la Tierra Media?
# Desarrolla un programa que se encargue de distribuirlos.
# Requisitos:
# 1. Los Elfos recibirán un número impar.
# 2. Los Enanos un número primo.
# 3. Los Hombres un número par.
# 4. Sauron siempre uno.
# Acciones:
# 1. Crea un programa que reciba el número total de anillos
#    y busque una posible combinación para repartirlos.
# 2. Muestra el reparto final o el error al realizarlo.

import statistics

def get_total_rings() -> int:
    while True:
        input_ = input("Cantidad de anillos: ")
        if input_.isdigit() and int(input_) >= 1:
            return int(input_)
        print("Debe ser un valor entero '>= 1'.")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def distribute(total: int) -> list:
    combinations = []
    for elves in range(1, total, 2):
        for men in range(2, total, 2):
            dwarves = total - (men + elves)
            if dwarves > 0 and is_prime(dwarves):
                combinations.append((elves, men, dwarves))

    return combinations

def standard_deviation(tup: tuple) -> float:
    return statistics.stdev(tup)

def the_most_balanced(combinations: list) -> tuple:
    deviations: list = [standard_deviation(tup) for tup in combinations]
    index_of_least_deviation = deviations.index(min(deviations))
    return combinations[index_of_least_deviation]

def print_result(distribution: tuple, sauron: int):
    if not distribution:
        print("Error en la selección equitativa.")
        return

    elves, men, dwarves = distribution
    print("_________________________")
    print(f"Elfos   -> {elves} : # Impar\nEnanos  -> {dwarves} : # Primo")
    print(f"Hombres -> {men} : # Par\nSauron  -> {sauron} : # Fijo")
    print("-------------------------")

def main(total: int):
    sauron = 1
    total -= sauron
    combinations: list = distribute(total)

    if not combinations:
        print("No existe una combinación posible.")
        return

    distribution: tuple = the_most_balanced(combinations)
    print_result(distribution, sauron)
    
if __name__ == "__main__":
    print("REPARTIENDO LOS ANILLOS DE PODER")
    total: int = get_total_rings()
    main(total)

