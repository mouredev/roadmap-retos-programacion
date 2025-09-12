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
 */
"""	

import csv
import random

#Introduce la url del archivo
PATH_CSV_FILE = "D:\\Desarrollo\\roadmap-retos-programacion\\Roadmap\\38 - MOUREDEV PRO\\python\\concurso.csv"

#Abrir el archivo
def open_csv(file):
    with open (file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        #Borra la primera fila
        next(reader)
        #ID, email, status
        listdata = list(reader)
        #Diccionario para almacenar los datos
        data = {}
        for row in listdata[1:]:
            id = row[0]
            email = row[1]
            status = row[2]
            data[id] = {"email": email, "status": status}
        return data
    
def select_winners(data):
    winners = {"subscription": None, "discount": None, "book": None}
    set_winners = set()
    while len(set_winners) < 3:
        if len(set_winners) == 0:
            winner = random.choice(list(data.keys()))
            if winner not in set_winners:
                winners["subscription"] = data[winner]["email"]
                set_winners.add(winner)
        
        elif len(set_winners) == 1:
            winner = random.choice(list(data.keys()))
            if winner not in set_winners:
                winners["discount"] = data[winner]["email"]
                set_winners.add(winner)
        elif len(set_winners) == 2:
            winner = random.choice(list(data.keys()))
            active = data[winner]["status"].strip() == "activo"
            if winner not in set_winners and active:
                winners["book"] = data[winner]["email"]
                set_winners.add(winner)

    return winners

def print_winners(winners):
    print("Ganador de la suscripción: ", winners["subscription"])
    print("Ganador del descuento: ", winners["discount"])
    print("Ganador del libro: ", winners["book"])

def main():
    data = open_csv(PATH_CSV_FILE)
    winners = select_winners(data)
    print_winners(winners)

if __name__ == "__main__":
    main()
