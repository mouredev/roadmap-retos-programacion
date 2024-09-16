"""
/*
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
 */
"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_all_primes(max_n):
    return [i for i in range(2, max_n + 1) if is_prime(i)]

def find_all_pars(max_n):
    return [i for i in range(2, max_n + 1, 2)]

def find_all_odds(max_n):
    return [i for i in range(1, max_n + 1, 2)]

def distribute_rings(rings):
    rings = int(rings) - 1  # Uno es siempre para Sauron
    if rings < 3:
        print("El número de anillos es insuficiente para cumplir con los requisitos.")
        return None

    primes = find_all_primes(rings)
    odds = find_all_odds(rings)
    pars = find_all_pars(rings)

    best_distribution = None

    for dwarf_rings in primes:
        for elf_rings in odds:
            for human_rings in pars:
                if dwarf_rings + elf_rings + human_rings == rings:
                    current_distribution = {
                        "Enanos": dwarf_rings,
                        "Elfos": elf_rings,
                        "Humanos": human_rings,
                        "Sauron": 1
                    }
                    if best_distribution is None or (
                        current_distribution["Enanos"] + current_distribution["Elfos"] + current_distribution["Humanos"] >
                        best_distribution["Enanos"] + best_distribution["Elfos"] + best_distribution["Humanos"]
                    ):
                        best_distribution = current_distribution

    if best_distribution:
        return best_distribution
    else:
        print("No se pudo encontrar una distribución válida.")
        return None

def print_distribution(distribution):
    for race, count in distribution.items():
        print(f"{race}: {count} anillos")

def main():
    rings = input("Introduce el número de anillos de poder: ")
    distribution = distribute_rings(rings)
    if distribution:
        print_distribution(distribution)
    else:
        print('No se han podido repartir los anillos correctamente.')

if __name__ == "__main__":
    main()

