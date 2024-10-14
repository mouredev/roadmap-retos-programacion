"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""
def sum_five_to_value(value):
    return value + 5 

def add_five_to_value(value,func):
    return func(value)

print(add_five_to_value(5,sum_five_to_value))

"""
* DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
"""
from time import sleep
from random import randint

def begin_processing(plate):
    time = randint(1,10)
    print (f"El plato {plate} ha empezado a procesarse y tardará en estar procesado {time} min...")
    sleep(time)

def plate_ready(plate):
    time = randint(1,10)
    print(f"El plato {plate} estará listo en {time} min...")
    sleep(time)

def plate_delivered(plate):
    time = randint(1,10)
    print(f"El plato {plate} será entregado en {time} min...")
    sleep(time)

def main(plate,func_begin,func_ready,func_delivered):
    func_begin(plate)
    func_ready(plate)
    func_delivered(plate)
    print(f"El plato {plate} ha sido entregado!!\n")

plate = "Pollo con Almendras"
main(plate,begin_processing,plate_ready,plate_delivered)
plate = "Macarrones con Queso"
main(plate,begin_processing,plate_ready,plate_delivered)
