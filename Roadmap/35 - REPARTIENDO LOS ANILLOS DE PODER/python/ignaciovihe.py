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

def prime_generator():
    """Generador infinito de números primos (modo eficiente)."""

    n = 2
    while True:
        for i in range (2, int(n ** 0.5) +1):#solo hace falta llegar hasta la raiz cuadrada del numero mas alla no habra divisores.
            if n % i == 0:
                break
        else:# el bloque else de un for se ejecuta si no se usa un break.
            yield n
        n += 1


def distribute_rings(total_rings: int):
    """Genera posibles distribuciones de anillos entre razas, dejando 1 para Sauron
    y asegurando que los Enanos reciban un número primo de anillos."""

    possibilities= []
    prime = prime_generator()
    rings_for_dwarfs = next(prime)

    while total_rings - rings_for_dwarfs >= 4:
        resting_rings = total_rings
        rings_for_sauron = 1
        resting_rings -=  rings_for_sauron # One ring for Sauron.
        
        if (resting_rings - rings_for_dwarfs) % 2 != 0:
            resting_rings -=  rings_for_dwarfs
            for rings_for_elfs in range(1, resting_rings, 2):
                rings_for_men = resting_rings - rings_for_elfs
                possibilities.append({
                    "Sauron": rings_for_sauron,
                    "Elves": rings_for_elfs,
                    "Dwarfs": rings_for_dwarfs,
                    "Men": rings_for_men
                })

        rings_for_dwarfs = next(prime)
    
    return possibilities
        
def print_distribution(distributed_rings):
    if distributed_rings:
        print("Posibles distribuciones encontradas:")
        for index, distribution in enumerate(distributed_rings):
            print(f"{index + 1}._ {distribution}")
        print(f"\nTotal de posibilidades encontradas: {len(distributed_rings)}")

        print("Distribucion equitativa:")
        print(distributed_rings[int(len(distributed_rings) / 2) - 1])
    else:
        print("No hay suficientes anillos para todos.")  


def main():
    while True:
        try:
            total_rings = int(input("Introduce el numero total de anillos a repartir: "))
            distributed_rings = distribute_rings(total_rings)
            print_distribution(distributed_rings)
            break
        except ValueError as e:
            print(f"Introduce un número entero.")
            continue

main()