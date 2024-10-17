'''
/*
 * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */
'''

import csv
import os
import random

def read_csv() -> list:

    file_dir = os.path.dirname(os.path.realpath(__file__))
    csv_file = f"{file_dir}/subs.csv"

    data = []

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['status'] == 'activo':
                data.append(row)

    return data

def select_winner(data: list) -> list:

    if len(data) < 3:
        raise Exception("No hay suficientes registros activos, mínimo 3.")
    
    winners = random.sample(data, 3)

    return winners

def print_winners(winners: list):
    
    for winner, trophy in zip(winners, ['una suscripción', 'un descuento', 'un libro']):
        print(f'El suscriptor "{winner['email']}" (ID:{winner['id']}) ha ganado {trophy}.')

try:
    data = read_csv()
    select_winner(data)
    print_winners(select_winner(data))
except Exception as e:
    print(e)

