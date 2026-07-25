# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import csv
import random

def leer_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Filtrar solo los registros con status "activo"
        activos = [row for row in reader if row['status'] == 'activo']
    return activos

def seleccionar_ganadores(participantes):
    # Evitar que un participante gane más de una vez
    ganadores = random.sample(participantes, 3)
    
    suscripcion = ganadores[0]
    descuento = ganadores[1]
    libro = ganadores[2]
    
    print(f"Ganador de suscripción: ID {suscripcion['id']} | Email: {suscripcion['email']}")
    print(f"Ganador de descuento: ID {descuento['id']} | Email: {descuento['email']}")
    print(f"Ganador de libro: ID {libro['id']} | Email: {libro['email']}")

if __name__ == "__main__":
    participantes_activos = leer_csv('suscriptores.csv')
    if len(participantes_activos) < 3:
        print("No hay suficientes participantes activos para seleccionar 3 ganadores.")
    else:
        seleccionar_ganadores(participantes_activos)
