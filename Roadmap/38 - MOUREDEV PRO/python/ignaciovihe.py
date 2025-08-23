"""
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
import os


users = [
    [1 , "pedro@test.com" , "activo"],
    [2 , "juan@test.com" , "activo"],
    [3 , "carlos@test.com" , "activo"],
    [4 , "rodrigo@test.com" , "activo"],
    [5 , "palomana@test.com" , "activo"],
    [6 , "carmen@test.com" , "inactivo"],
    [7 , "maria@test.com" , "activo"],
    [8 , "teresa@test.com" , "inactivo"],
    [9 , "susanat@test.com" , "activo"],
    [10 , "manuel@test.com" , "activo"],
]


file_dir = os.path.dirname(os.path.abspath(__file__))
file_name = f"{file_dir}/subs.csv"

def create_csv(f_name):
    with open(f_name, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["id", "email", "estado"])
        writer.writerows(users)

def get_participants(f_name):
    subs = []
    with open(f_name, "r", newline='', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            if fila["estado"] == "activo":
                subs.append(fila)
    return subs

def get_winners(data: list):
    if len(data) >=3:
        return random.sample(data, 3)
    else:
        raise ValueError("El número de participantes debe ser minimo 3")

def print_winners(data: list):
    
    prizes = ["suscripción", "descuebto", "libro"]
    print("GANADORES DE LOS PREMIOS")
    for prize , winner in zip(prizes, data):
        print(f"Premio: {prize} - Ganador: (ID:{winner["id"]}) - {winner["email"]}")

try:
    create_csv(file_name)
    participants = get_participants(file_name)
    winners = get_winners(participants)
    print_winners(winners)
except Exception as e:
    print(e)
