#38 { Retos para Programadores } MOUREDEV PRO 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

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

"""  Example of csv:
id,email,status
1,softbaby@hotmail.com,active
2,psicotrogato@gmail.com,active
3,coders@io.com,inactive
4,chap_gtp@microsoft.com,active
5,applesupport@mac.com,active
6,someone@proton.me,inactive
7,zeigest@movement.sw,active
8,duendeintemporal@hotmail.com,active
9,freelancer@developer.dev,inactivo
10,crazycat@miau.miau,active
"""

""" In a console run the next comands:
mkdir mouredev-pro
cd mouredev-pro
npm init -y
npm install csv-parser
"""

log = print

import csv
import random

# Define a dictionary to hold the winners
winners = {
    'subscription': None,
    'discount': None,
    'book': None
}

active_emails = []

# Read the CSV file
with open('subscribers.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['status'] == 'active':
            active_emails.append({'id': row['id'], 'email': row['email']})

def select_winners():
    # Shuffle the list of active emails
    shuffled = random.sample(active_emails, len(active_emails))

    # Select unique winners
    winners['subscription'] = shuffled[0]
    winners['discount'] = shuffled[1]
    winners['book'] = shuffled[2]

def display_winners():
    log('Winners:')
    log(f"Subscription: ID: {winners['subscription']['id']}, Email: {winners['subscription']['email']}")
    log(f"Discount: ID: {winners['discount']['id']}, Email: {winners['discount']['email']}")
    log(f"Book: ID: {winners['book']['id']}, Email: {winners['book']['email']}")

# Select winners and display them
select_winners()
display_winners()


"""
Possible Output: 

Winners:
Subscription: ID: 10, Email: crazycat@miau.miau
Discount: ID: 7, Email: zeigest@movement.sw
Book: ID: 5, Email: applesupport@mac.com

"""


