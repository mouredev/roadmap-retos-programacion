import csv
import random

def obtener_suscriptores_activos(archivo_csv):
    suscriptores = []
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            id_, email, status = row
            if status.strip().lower() == 'activo':
                suscriptores.append({'id': id_.strip(), 'email': email.strip()})
    return suscriptores

def seleccionar_ganadores(suscriptores, numero_ganadores):
    if len(suscriptores) < numero_ganadores:
        return None  
    return random.sample(suscriptores, numero_ganadores)

archivo_csv = 'suscriptores.csv'

suscriptores_activos = obtener_suscriptores_activos(archivo_csv)

if suscriptores_activos:
    ganadores = seleccionar_ganadores(suscriptores_activos, 3)
    if ganadores:
        print(f"Ganador de la suscripción: {ganadores[0]}")
        print(f"Ganador del descuento: {ganadores[1]}")
        print(f"Ganador del libro: {ganadores[2]}")
    else:
        print("No hay suficientes suscriptores activos para seleccionar 3 ganadores.")
else:
    print("No hay suscriptores activos.")
