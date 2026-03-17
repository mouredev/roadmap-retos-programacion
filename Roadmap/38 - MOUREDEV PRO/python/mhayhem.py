# @Author Daniel Grande (Mhayhem)

import csv
import random

# EJERCICIO:
# He presentado mi proyecto más importante del año: mouredev pro.
# Un campus para la comunidad, que lanzaré en octubre, donde estudiar
# programación de una manera diferente.
# Cualquier persona suscrita a la newsletter de https://mouredev.pro
# accederá a sorteos mensuales de suscripciones, regalos y descuentos.
#
# Desarrolla un programa que lea los registros de un fichero .csv y
# seleccione de manera aleatoria diferentes ganadores.
# Requisitos:
# 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
#    o "inactivo" (y datos ficticios).
#    Ejemplo: 1 | test@test.com | activo
#             2 | test2@test.com | inactivo
#    (El .csv no debe subirse como parte de la corrección)
# 2. Recupera los datos desde el programa y selecciona email aleatorios.
# Acciones:
# 1. Accede al fichero .csv y selecciona de manera aleatoria un email
#    ganador de una suscripción, otro ganador de un descuento y un último
#    ganador de un libro (sólo si tiene status "activo" y no está repetido).
# 2. Muestra los emails ganadores y su id.
# 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
#    no debe tenerse en cuenta.


def get_info_csv(path: str):
    active_users = []
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            if row["status"].lower() == "active":
                active_users.append(row)
    
    return active_users

def lottery(array: list):
    if len(array) < 3:
        print("No hay suficientes subscriptores para el sorteo.")
        return
    
    winners = random.sample(array, 3)
    annual_subscribe = winners[0]
    discount = winners[1]
    book = winners[2]
    
    print(f"El correo {annual_subscribe['email']} con ID {annual_subscribe["id"]}, ha ganado una subscripcion a Mouredev.pro.")
    print(f"El correo {discount['email']} con ID {discount["id"]}, ha ganado un descuento del 15%.")
    print(f"El correo {book['email']} con ID {book["id"]}, ha ganado el libro de Brais Moure")

def main():
    array = get_info_csv(path)
    lottery(array)

if __name__=="__main__":
    main()