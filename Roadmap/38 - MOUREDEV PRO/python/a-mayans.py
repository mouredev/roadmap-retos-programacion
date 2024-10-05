import csv
import random

# Leer los datos del archivo CSV
def leer_datos_csv(archivo_csv):
    with open(archivo_csv, mode='r') as file:
        reader = csv.DictReader(file)
        usuarios_activos = [row for row in reader if row['status'] == 'activo']
    return usuarios_activos

# Seleccionar ganadores aleatorios
def seleccionar_ganadores(usuarios):
    if len(usuarios) < 3:
        raise ValueError("No hay suficientes usuarios activos para seleccionar 3 ganadores.")
    
    ganadores = random.sample(usuarios, 3)
    
    ganador_suscripcion = ganadores[0]
    ganador_descuento = ganadores[1]
    ganador_libro = ganadores[2]
    
    return {
        "suscripcion": ganador_suscripcion,
        "descuento": ganador_descuento,
        "libro": ganador_libro
    }

# Mostrar ganadores
def mostrar_ganadores(ganadores):
    print("Ganador de la suscripción:")
    print(f"ID: {ganadores['suscripcion']['id']}, Email: {ganadores['suscripcion']['email']}")
    
    print("\nGanador del descuento:")
    print(f"ID: {ganadores['descuento']['id']}, Email: {ganadores['descuento']['email']}")
    
    print("\nGanador del libro:")
    print(f"ID: {ganadores['libro']['id']}, Email: {ganadores['libro']['email']}")

# Archivo CSV con usuarios
archivo_csv = 'usuarios.csv'

# Leer los datos del archivo CSV
usuarios_activos = leer_datos_csv(archivo_csv)

# Seleccionar ganadores aleatorios
ganadores = seleccionar_ganadores(usuarios_activos)

# Mostrar los ganadores
mostrar_ganadores(ganadores)