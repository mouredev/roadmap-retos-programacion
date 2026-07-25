import csv
import random

def seleccionar_activos(csvfile):

    activos = []
    emails_activos = []

    with open(csvfile) as file:
        csv_reader = csv.reader(file, delimiter=',')

        next(csv_reader)    # saltar la cabecera

        for row in csv_reader:
            id, email, status = row
            if status == "activo" and email not in emails_activos:
                emails_activos.append(email)    # evitar correos duplicados
                activos.append((id, email))     # añadir la tupla (id, email) de los usuarios activos

    return activos

def seleccionar_ganadores(activos, cantidad_ganadores=3):
    
    if len(activos) >= cantidad_ganadores:
        ganadores = random.sample(activos, cantidad_ganadores)  # seleccionar de manera aleatoria

        ganador_suscripcion = ganadores[0]
        ganador_descuento = ganadores[1]
        ganador_libro = ganadores[2]

        print(f"\nGanador/a de la suscripción:")
        print(f"id: {ganador_suscripcion[0]}, email: {ganador_suscripcion[1]}")
        print(f"\nGanador/a del descuento:")
        print(f"id: {ganador_descuento[0]}, email: {ganador_descuento[1]}")
        print(f"\nGanador/a del libro:")
        print(f"id: {ganador_libro[0]}, email: {ganador_libro[1]}")
        return ganadores
    
    else:
        print("No hay suficientes usuarios activos para seleccionar 3 ganadores.")
        return []


if __name__ == '__main__':
    
    seleccionar_ganadores(activos=seleccionar_activos('registros.csv'))