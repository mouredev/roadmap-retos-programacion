"""
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
"""
import csv
import random

def get_data_from_csv(file_name):
    """Method to get data from csv file"""
    data = []
    with open(file_name, 'r', encoding="utf-8", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if row[2] == 'activo':
                data.append(row)
    return data


def get_random_winners(data):
    """Method to get random winners"""
    used_numbers = []
    winners = []
    # Winner 1
    random_number = get_unique_random_number(len(data)-1, used_numbers)
    winners.append(data[random_number])
    # Winner 2
    random_number = get_unique_random_number(len(data)-1, used_numbers)
    winners.append(data[random_number])
    # Winner 3
    random_number = get_unique_random_number(len(data)-1, used_numbers)
    winners.append(data[random_number])
    return winners


def print_winners(winners):
    """Method to print winners"""
    prizes = ['Suscripción', 'Descuento', 'Libro']
    for i, winner in enumerate(winners):
        print(f"Ganador {prizes[i]} -> Id: {winner[0]}, Email: {winner[1]}")


def get_unique_random_number(max_number, used_numbers):
    """Method to get unique random number"""
    random_number = random.randint(0, max_number)
    while random_number in used_numbers:
        random_number = random.randint(0, max_number)
    used_numbers.append(random_number)
    return random_number


# import os
# print(os.getcwd())
csv_data = get_data_from_csv('38/mouredev38.csv')
# print(csv_data)
chosen = get_random_winners(csv_data)
print_winners(chosen)
