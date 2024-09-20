'''
/*
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
 */'''
import pandas as pd
import random

df = pd.read_csv('csv.csv')
lista = []

for index, row in df.iterrows():
    if row['status'] == 'activo':
        lista.append([row['id'], row['email']])

print(lista)

premios = []

for _ in range(3):
    p = random.choice(lista)
    premios.append(p)
    lista = [x for x in lista if x != p]  
print(f'''
Ganador de una suscripción --> ID: {premios[0][0]}, Email: {premios[0][1]}
Ganador de un descuento --> ID: {premios[1][0]}, Email: {premios[1][1]}
Ganador de un libro --> ID: {premios[2][0]}, Email: {premios[2][1]}
''')
