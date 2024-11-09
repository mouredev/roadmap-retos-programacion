"""
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
"""

import csv
import random

# Leer el archivo CSV
def leer_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Seleccionar ganadores aleatorios
def seleccionar_ganadores(suscriptores):
    activos = [s for s in suscriptores if s['status'] == 'activo']
    ganadores = random.sample(activos, 3)
    return ganadores

# Mostrar los ganadores
def mostrar_ganadores(ganadores):
    premios = ['suscripción', 'descuento', 'libro']
    for ganador, premio in zip(ganadores, premios):
        print(f"Ganador de {premio}: ID {ganador['id']}, Email {ganador['email']}")

# Main
if __name__ == "__main__":
    suscriptores = leer_csv('d:/Proyectos Github/roadmap-retos-programacion/Roadmap/38 - MOUREDEV PRO/python/suscriptores.csv')
    ganadores = seleccionar_ganadores(suscriptores)
    mostrar_ganadores(ganadores)
