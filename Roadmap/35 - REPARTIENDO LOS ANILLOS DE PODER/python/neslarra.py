"""
 EJERCICIO:
 ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
 ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 entre las razas de la Tierra Media?
 Desarrolla un programa que se encargue de distribuirlos.
 Requisitos:
 1. Los Elfos recibirán un número impar.
 2. Los Enanos un número primo.
 3. Los Hombres un número par.
 4. Sauron siempre uno.
 Acciones:
 1. Crea un programa que reciba el número total de anillos
    y busque una posible combinación para repartirlos.
 2. Muestra el reparto final o el error al realizarlo.
"""
import math


def is_prime(num: int):
    if num == 1 or (num % 2 == 0 and num > 2):
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))


def odd_even(num: int):
    return False if num % 2 else True


def group_of_three(num: int):
    elfos = [x for x in range(1, num) if not odd_even(x)]
    hombres = [x for x in range(1, num) if odd_even(x)]       # OJO el 0 es par PERO si lo considero los hombres NO estarían recibiendo anillos
    enanos = [x for x in range(1, num) if is_prime(x)]

    combinacion = []

    for elfo in elfos:
        anillos = elfo
        for enano in enanos:
            anillos += enano
            for hombre in hombres:
                anillos += hombre
                if anillos == num - 1:
                    combinacion.append({"elfos": elfo, "enanos": enano, "hombres": hombre, "sauron": 1})
                anillos -= hombre
            anillos -= enano

    return combinacion


anillos = int(input("Ingresa la cantidad de anillos de poder: "))
combinacion = group_of_three(anillos)
if not combinacion:
    print(f"No hay posible combinación de {anillos} anillos")
else:
    for combineta in combinacion:
        print(combineta)
