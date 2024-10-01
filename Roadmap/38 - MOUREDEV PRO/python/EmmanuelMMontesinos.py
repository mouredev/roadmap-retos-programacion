"""
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
 */
"""
import csv
from random import choice

nombre_csv = "roadmap/38 - MOUREDEV PRO/python/Prueba.csv"

class Archivo:
    def __init__(self,nombre,delimitador):
        self.nombre = nombre
        self.delimitador = delimitador

    def sorteo(self):
        self.leer_csv()
        Ganadores.seleccionar_ganador(Ganadores)
    
    def leer_csv(self):
        with open(self.nombre,"r") as archivo:
            lector = csv.reader(archivo,delimiter=self.delimitador)
            lector = list(lector)
            for row in lector[1::]:
                id,email,status = row
                Ganadores(id,email,status)
                
                print(f"{id} Email: {email} Status: {status}")
            
class Ganadores:
    lista_participantes = []
    lista_ganadores = []
    def __init__(self,id,email,status):
        self.id = id
        self.email = email
        self.status = status
        if self.status == "activo":
            Ganadores.lista_participantes.append(self)
    
    def seleccionar_ganador(self):
        print()
        print("Sorteo de MoureDev Pro")
        while len(Ganadores.lista_ganadores) < 3:
            participante = choice(Ganadores.lista_participantes)
            if participante not in Ganadores.lista_ganadores:
                Ganadores.lista_ganadores.append(participante)
            else:
                continue
        self.ganador_libro = Ganadores.lista_ganadores[0]
        self.ganador_descuento = Ganadores.lista_ganadores[1]
        self.subscripcion = Ganadores.lista_ganadores[2]

        print(f"Ganador de la subscripción: ID: {self.subscripcion.id} Email: {self.subscripcion.email}")
        print(f"Ganador del descuento: ID: {self.ganador_descuento.id} Email: {self.ganador_descuento.email}")
        print(f"Ganador del libro: ID: {self.ganador_libro.id} Email: {self.ganador_libro.email}")

# Pruebas
prueba = Archivo(nombre_csv,delimitador="|")
prueba.leer_csv()

prueba.sorteo()