""" /*
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
 */ """

#EJERCICIO

import os
import csv
import random

def read_csv_data() -> list:

    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = f"{file_dir}/sub.csv"

    data = []

    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "activo":
                data.append(row)
    return data

def select_winners(data: list) -> list:

    if len(data) < 3:
        raise ValueError("El número de elementos debe de ser mínimo 3.")
    
    return random.sample(data, 3)

def display_winners(winners):
    prizes = ["Suscripción", "Descuento", "Libro"]
    for winner, prizes in zip(winners, prizes):
        print(f"{prizes}: {winner["email"]} (ID: {winner["id"]})")

try:
    data = read_csv_data()
    winners = select_winners(data)
    display_winners(winners)
except Exception as e:
    print(e)