"""
 EJERCICIO:
 He presentado mi proyecto más importante del año: mouredev pro.
 Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 programación de una manera diferente.
 Cualquier persona suscrita a la newsletter de https://mouredev.pro
 accederá a sorteos mensuales de suscripciones, regalos y descuentos.

 Desarrolla un programa que lea los registros de un fichero .csv y
 seleccione de manera aleatoria diferentes ganadores.
 Requisitos:
 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
    o "inactivo" (y datos ficticios).
    Ejemplo: 1 | test@test.com | activo
             2 | test2@test.com | inactivo
    (El .csv no debe subirse como parte de la corrección)
 2. Recupera los datos desde el programa y selecciona email aleatorios.
 Acciones:
 1. Accede al fichero .csv y selecciona de manera aleatoria un email
    ganador de una suscripción, otro ganador de un descuento y un último
    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 2. Muestra los emails ganadores y su id.
 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
    no debe tenerse en cuenta.
"""
import csv
from os import remove
from random import randint


def create_csv():
    users = [
        {"id": 1, "email": "tito@gmail.com", "status": 0},
        {"id": 2, "email": "pepe@gmail.com", "status": 0},
        {"id": 3, "email": "salo@gmail.com", "status": 1},
        {"id": 4, "email": "tula@gmail.com", "status": 1},
        {"id": 5, "email": "tilo@gmail.com", "status": 1},
        {"id": 6, "email": "pipa@gmail.com", "status": 1},
        {"id": 7, "email": "toto@gmail.com", "status": 0},
        {"id": 8, "email": "calo@gmail.com", "status": 0},
        {"id": 9, "email": "tolo@gmail.com", "status": 0},
        {"id": 10, "email": "pepo@gmail.com", "status": 1},
        {"id": 11, "email": "sali@gmail.com", "status": 1},
        {"id": 12, "email": "chino@gmail.com", "status": 0},
        {"id": 13, "email": "chona@gmail.com", "status": 1},
        {"id": 14, "email": "tano@gmail.com", "status": 0},
        {"id": 15, "email": "tina@gmail.com", "status": 1},
    ]

    with open("reto_38_neslarra.csv", "w", newline="") as fichero:
        writer = csv.writer(fichero, delimiter=",")
        writer.writerow(["id", "email", "status"])
        for line in users:
            writer.writerow([line["id"], line["email"], line["status"]])


def read_csv():
    users = []
    with open("reto_38_neslarra.csv", "r") as fichero:
        reader = csv.reader(fichero, delimiter=",")
        for row in reader:
            if reader.line_num == 1:
                headers = row
                continue
            users.append({headers[0]: row[0], headers[1]: row[1], headers[2]: row[2]})
    return users


def remove_csv():
    remove("reto_38_neslarra.csv")


create_csv()

users = read_csv()
active_users = [x for x in users if x["status"] == "1"]              # status 1 = ACTIVO / status 0 = INACTIVO

ganador_suscripcion = active_users.pop(randint(0, active_users.__len__() - 1))
print(f"El ganador de la suscripción es {ganador_suscripcion['email']}")

ganador_libro = active_users.pop(randint(0, active_users.__len__() - 1))
print(f"El ganador del libro es {ganador_libro['email']}")

ganador_descuento = active_users.pop(randint(0, active_users.__len__() - 1))
print(f"El ganador del descuento es {ganador_descuento['email']}")

remove_csv()
