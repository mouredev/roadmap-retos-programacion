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


n_rings = int(input("Introduce el número de anillos a repartirse: "))
total_rings = {"Sauron": 0, "Elfos": 0, "Hombres": 0, "Enanos": 0}

def es_primo(number):
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

if n_rings > 0:
    n_rings -= 1
    total_rings["Sauron"] += 1

while n_rings > 0: 
    distributed = False
    if (total_rings["Hombres"] + 1) % 2 == 0:
        n_rings -= 1
        total_rings["Hombres"] += 1
        distributed = True

    if (total_rings["Elfos"] + 1) % 3 == 0:
        n_rings -= 1
        total_rings["Elfos"] += 1
        distributed = True

    if es_primo(total_rings["Enanos"]+1):
        n_rings -= 1
        total_rings["Enanos"] +=1
        distributed = True

    if not distributed and n_rings > 0: 
        min_group = min(total_rings, key = lambda x: total_rings[x] if x != "Sauron" else float("inf"))
        total_rings[min_group] += 1
        n_rings -= 1  

for key, value in total_rings.items():
    print(f"{key} recibe {value}")

print(f"Quedan {n_rings}")



    