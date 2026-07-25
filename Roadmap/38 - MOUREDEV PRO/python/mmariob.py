import csv
import random

# Creo lista para guardar los datos del csv
results = []

# Leo el csv
with open('data.csv', 'r', newline='') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)

# Función para seleccionar un ganador aleatorio y eliminarlo de la lista
def seleccionar_ganador(lista):
    if not lista:
        return None
    indice = random.randint(0, len(lista) - 1)
    return lista.pop(indice)

# Ganador de suscripción
ganador_sub = seleccionar_ganador(results)
if ganador_sub:
    print(f"El ganador de la suscripción es: {ganador_sub['email']}")
else:
    print("No hay participantes para la suscripción")

# Ganador de descuento
ganador_des = seleccionar_ganador(results)
if ganador_des:
    print(f"El ganador del descuento es: {ganador_des['email']}")
else:
    print("No hay participantes para el descuento")

# Ganador del libro (solo si es activo)
ganador_libro = None
while results and not ganador_libro:
    posible_ganador = seleccionar_ganador(results)
    if posible_ganador['status'] == 'activo':
        ganador_libro = posible_ganador
        print(f"El ganador del libro es: {ganador_libro['email']}")
    else:
        print(f"El participante {posible_ganador['email']} no es elegible para el libro (inactivo)")

if not ganador_libro:
    print("No se encontró un ganador activo para el libro")

# Imprimir participantes restantes
print(f"\nParticipantes restantes: {len(results)}")
for participante in results:
    print(f"ID: {participante['id']}, Email: {participante['email']}, Status: {participante['status']}")