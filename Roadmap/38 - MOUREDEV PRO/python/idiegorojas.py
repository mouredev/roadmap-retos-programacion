""" # 38 - Mouredev Pro  """

# Desarrolla un programa que lea los registros de un fichero .csv y seleccione de manera aleatoria diferentes ganadores.

"""
Requisitos:
"""
# 1. Crea un .csv con 3 columnas: id, email y status con valor "activo" o "inactivo" (y datos ficticios).
    # Ejemplo: 1 | test@test.com | activo
    # 2 | test2@test.com | inactivo
    # (El .csv no debe subirse como parte de la corrección)
# 2. Recupera los datos desde el programa y selecciona email aleatorios.

"""
Acciones: 
"""
# 1. Accede al fichero .csv y selecciona de manera aleatoria un email
    # ganador de una suscripción, otro ganador de un descuento y un último
    # ganador de un libro (sólo si tiene status "activo" y no está repetido).
# 2. Muestra los emails ganadores y su id.
# 3. Ten en cuenta que la primera fila (con el nombre de las columnas) no debe tenerse en cuenta.



import csv
import random

def select_winners(csv_file):
    """
    Selecciona ganadores aleatorios de un archivo CSV.
    """
    # Lista para almacenar usuarios activos
    active_users = []
    
    # Leer el archivo CSV
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltamos la primera fila (cabecera)
        
        for row in reader:
            if len(row) >= 3 and row[2].lower() == 'true':
                active_users.append({"id": row[0], "email": row[1]})
    
    # Verificar si hay suficientes usuarios activos
    if len(active_users) < 3:
        print("No hay suficientes usuarios activos para seleccionar 3 ganadores.")
        return
    
    # Seleccionar ganadores aleatorios sin repetición
    winners = random.sample(active_users, 3)
    
    # Mostrar los ganadores
    prizes = ["suscripción", "descuento", "libro"]
    
    print("\n=== GANADORES ===")
    for i, winner in enumerate(winners):
        print(f"Ganador de {prizes[i]}:")
        print(f"ID: {winner['id']}, Email: {winner['email']}")

# Ruta del archivo CSV
csv_file = "users.csv"

# Ejecutar el programa
try:
    select_winners(csv_file)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{csv_file}'.")
    print("Primero debes crear el archivo CSV con los datos requeridos.")
except Exception as e:
    print(f"Error: {e}")