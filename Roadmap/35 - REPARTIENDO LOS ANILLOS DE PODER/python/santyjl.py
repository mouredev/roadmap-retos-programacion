# #35 REPARTIENDO LOS ANILLOS DE PODER
#### Dificultad: Media | Publicación: 26/08/24 | Corrección: 02/09/24

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

import random


def pares (num):
    lista = []
    for i in range(num):
        if i % 2 == 0 and i != 0:
            lista.append(i)

    return random.choice(lista)

def impar(num):
    lista= []
    for i in range(num):
        if i % 2 != 0 and i != 0:
            lista.append(i)

    return random.choice(lista)

def es_primo(num:int):
    if num == 1:
        return False

    for i in range(2 , int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def repartir_anillos(num:int):
    num_total = num - 1

    anillos_elfos = 0
    anillos_enanos = 0
    anillos_humanos = 0
    SAURON = 1


    while num_total > 0 :
        anillos_elfos = impar(num_total)
        num_total -= anillos_elfos

        anillos_humanos = pares(num_total)
        num_total -= anillos_humanos

        if es_primo(num_total):
            anillos_enanos = num_total
            num_total = 0

            return anillos_elfos , anillos_humanos , anillos_enanos , SAURON

        num_total = num - 1


try:
    anillos_elfos , anillos_humanos , anillos_enanos , SAURON = repartir_anillos(10)

    print("los elfos tienen un total de : " , anillos_elfos , "anillos del poder")
    print("los humanos tienen un total de : " , anillos_humanos , "anillos del poder")
    print("los enanos tienen un total de : " , anillos_enanos , "anillos del poder")
    print("los Sauron tienen un total de : " , SAURON , "anillos del poder")
except Exception:
        print("ha habido un error al momento de repartir los anillos")