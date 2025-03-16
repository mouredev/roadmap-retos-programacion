""" * EJERCICIO:
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

from random import randint

def is_prime(number:int):
    if number ==1: #en el caso de este programa, el número nunca podrá ser 0. En otro caso habría que evaluar number < 2
        return False
    else:
        for index in range(2,int(number**0.5)+1): #se evalúan valores desde 2 hasta la raíz cuadrada del número
            if number % index == 0: # y si la división entre el número y alguno de esos valorers tien resto 0
                return False #entonces no es un número primo.
    return True
    
def is_odd(number:int):
    return number % 2 != 0

def is_even(number:int):
    return number %2 == 0

THE_ONE_RING = 1
print("Te doy la bienvenida al programa de reparto de LOS ANILLOS DE PODER")
rings = int(input("Dime el número de Anillos de Poder a Repartir: "))
#rings = 9
if rings <= 5:
    print("No hay suficientes anillos para repartir")
else:
    sauron = THE_ONE_RING
    while True:
        rings_aux = rings-sauron
        men = randint(1,rings_aux)
        if is_even(men):
            rings_aux -= men
            if rings_aux >= 3:
                dwarven = randint(1,rings_aux)
                if is_prime(dwarven):
                    rings_aux -= dwarven
                    
                    if rings_aux > 0:
                        elven = rings_aux
                        if is_odd(elven):
                            if sauron+men+dwarven+elven == rings:
                                print("LOS ANILLOS SE HAN REPARTIDO CORRECTAMENTE")
                                print(f"TOTAL DE ANILLOS: {rings}\n- SAURON: {sauron}\n- HOMBRES: {men}\n- ENANOS: {dwarven}\n- ELFOS: {elven}")
                                break
