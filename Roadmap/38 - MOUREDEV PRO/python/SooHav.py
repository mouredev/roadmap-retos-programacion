# 38 MOUREDEV PRO
import csv
import os
import random

# Ruta al directorio
directorio = os.path.join("sofiah", "documentos", "temporal", "datos")


# Crea el directorio si no existe
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Nombre del archivo
nombre_archivo = "fichero.csv"

# Ruta completa del archivo
ruta_archivo = os.path.join(directorio, nombre_archivo)

# Datos a escribir en el archivo
datos_usuario = [
    {
        'id': 1,
        'email': 'soo@gmail.com',
        'estatus': 'Activo'
    },
    {
        'id': 2,
        'email': 'pepe@gmail.com',
        'estatus': 'Activo'
    },
    {
        'id': 3,
        'email': 'juani@gmail.com',
        'estatus': 'Inactivo'
    },
    {
        'id': 4,
        'email': 'luquitas@gmail.com',
        'estatus': 'Activo'
    },
    {
        'id': 5,
        'email': 'nico@gmail.com',
        'estatus': 'Inactivo'
    },
    {
        'id': 6,
        'email': 'alma@gmail.com',
        'estatus': 'Activo'
    },
]

# Nombre de las columnas
columnas = ['id', 'email', 'estatus']

# Crea el fichero
with open(ruta_archivo, mode='w', newline='') as file:
    documento = csv.DictWriter(file, delimiter=',', fieldnames=columnas)
    documento.writeheader()
    for dato in datos_usuario:
        documento.writerow(dato)

print(f"Archivo guardado en: {ruta_archivo}")

# Lista para guardar la información
info = []

# Lectura de fichero
with open(ruta_archivo, mode='r', newline='') as file:
    documento = csv.DictReader(file, delimiter=',')
    for fila in documento:
        info.append([fila['id'], fila['email'], fila['estatus']])

# Usuarios con estatus 'Activo'
activos = [usuario for usuario in info if usuario[2] == 'Activo']

# Lista filtrada
print("Usuarios activos:", activos)

# Selección aleatoria de 3 usuarios activos sin repetición
if len(activos) >= 3:
    ganador1, ganador2, ganador3 = random.sample(activos, 3)

    # Imprimir los ganadores
    print(f"ID ganador de la suscripción: {ganador1[0]} email: {ganador1[1]}")
    print(f"ID ganador del descuento: {ganador2[0]} email: {ganador2[1]}")
    print(f"ID ganador del libro: {ganador3[0]} email: {ganador3[1]}")
else:
    print("No hay suficientes usuarios activos para realizar el sorteo.")
