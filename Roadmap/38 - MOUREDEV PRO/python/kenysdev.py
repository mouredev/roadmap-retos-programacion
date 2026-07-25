# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 38 MOUREDEV PRO
# ------------------------------------
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
from typing import Optional

def read_csv(file_path) -> Optional[list]:
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"Error reading '{file_path}': {e}")
        return None

def get_active_entries(entries) -> list:
    active_entries = []
    
    for entry in entries:
        if entry['status'].lower() == "active":
            active_entry = {
                'id': entry['id'],
                'email': entry['email'],
                'status': entry['status']
            }
            active_entries.append(active_entry)
    
    return active_entries

def select_winners(active_entries, num_winners) -> list:
    return random.sample(active_entries, min(num_winners, len(active_entries)))

def distribute_prizes(winners, prizes):
    random.shuffle(prizes)
    for winner, prize in zip(winners, prizes):
        print(f"{prize:<11} -> Id({winner['id']}): {winner['email']}")

if __name__ == "__main__":
    print("Usuarios ganadores de 'MOUREDEV PRO:'")
    csv_file = 'users.csv'
    prizes = ["Suscripción", "Descuento", "Libro"]
    
    entries = read_csv(csv_file)
    if entries:
        active_entries = get_active_entries(entries)
        winners = select_winners(active_entries, 3)
        distribute_prizes(winners, prizes)

    else:
        print("No se encontraron entradas activas.")

