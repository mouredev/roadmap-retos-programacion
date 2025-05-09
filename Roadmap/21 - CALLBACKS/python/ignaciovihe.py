"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""
import random

my_grades = [random.randint(0,10) for i in range (10)]

def process_grades(grades, callback):
    return callback(grades)

def get_passed(grades):
    return [grade for grade in grades if grade >= 5]

def get_failed(grades):
    return [grade for grade in grades if grade < 5]

def average(grades):
    return sum(grades) / len(grades)

print(process_grades(my_grades, get_passed))
print(process_grades(my_grades, get_failed))
print(process_grades(my_grades, average))


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

import time
import threading

#print_lock = threading.Lock()  Con esto podría hacer que bloques de codigo fueras sincronos (with print_lock:)

def confirm_order(order_name):
    print(f"Tu pedido {order_name} Ha sido confirmada.")

def order_ready(order_name):
    print(f"Tu pedido {order_name} esta listo.")

def order_delivered(order_name):
    print(f"Tu pedido {order_name} Ha sido entregado.")

def process_order(order_name, callback_confirm, callback_ready, callback_delivered):
    
    def process():
        callback_confirm(order_name)
        time.sleep(random.randint(1,10))
        callback_ready(order_name)
        time.sleep(random.randint(1,10))
        callback_delivered(order_name)

    threading.Thread(target=process).start()

process_order("Pizza Margarita", confirm_order, order_ready, order_delivered)
process_order("Hamburguesa", confirm_order, order_ready, order_delivered)
process_order("Shushi", confirm_order, order_ready, order_delivered)
process_order("Arroz frito", confirm_order, order_ready, order_delivered)

    

