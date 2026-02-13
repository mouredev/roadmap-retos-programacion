# @Author Daniel Grande (Mhayhem)

import random

# EJERCICIO:
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
def prime_number(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def distribution_of_the_rings(num_rings):
    dwarfs = [num for num in range(2, num_rings) if prime_number(num)]
    elfs = [num for num in range(1, num_rings) if num % 2 != 0]
    sauron = 1

    result = []

    for numd in dwarfs:
        for nume in elfs:
            numh = num_rings - nume - numd - sauron
            if numh > 0 and numh % 2 == 0:
                rings_delivery = numh + nume + numd + sauron
                result.append(f"Sauron: {sauron}; Elfos: {nume}; Enanos: {numd}; Humanos: {numh}. Resultado: {rings_delivery}")

    if not result:
        print("No existe combinación.")
    else:
        print(random.choice(result))

distribution_of_the_rings(200)