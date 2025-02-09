#21 { Retos para Programadores } CALLBACKS

# Bibliography reference
#Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras) (z-lib.org)
#Eloquent Javascript A Modern Introduction to Programming by Marijn Haverbeke (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

"""   
* EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
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

import random
import threading

# Function to simulate console.log
log = print

log('Retosparaprogramadores #21.')

# Function to confirm an order
def order_confirm(order, callback):
    log(f'The order: {order} is confirmed. Tell you when it\'s ready.')
    processing_time = random.randint(1, 10)  # Random processing time between 1 and 10 seconds
    threading.Timer(processing_time, callback, args=[order]).start()

# Function to indicate that the order is ready
def order_ready(order, callback):
    log(f'The order: {order} is ready. Waiting to deliver.')
    delivery_time = random.randint(1, 10)  # Random delivery time between 1 and 10 seconds
    threading.Timer(delivery_time, callback, args=[order]).start()

# Function to deliver the order
def order_deliver(order):
    log(f'Order: {order} delivered.')

# Function to make an order
def make_order(list_order):
    today_menu = ['pizza', 'hamburger', 'paella', 'arabian food', 'posole', 
                  'pastel azteca', 'carbonara past', 'napolitana past', 'fish', 'beef']
    
    for order in list_order:
        if any(elm.lower() == order.lower() for elm in today_menu):
            order_confirm(order, lambda confirmed_order: order_ready(confirmed_order, order_deliver))
        else:
            log(f'The order: {order} is not in today\'s menu. Please choose another dish.')


    
order_list1 = ['pastiche', 'hamburger', 'pizza']
order_list2 = ['arabian food', 'fish', 'pastel azteca']
make_order(order_list1)
make_order(order_list2)

# Output Example:
"""  
Retosparaprogramadores #21.
The order: pastiche is not in today's menu. Please choose another dish.
The order: hamburger is confirmed. Tell you when it's ready.
The order: pizza is confirmed. Tell you when it's ready.
The order: arabian food is confirmed. Tell you when it's ready.
The order: fish is confirmed. Tell you when it's ready.
The order: pastel azteca is confirmed. Tell you when it's ready.
The order: hamburger is ready. Waiting to deliver.
The order: fish is ready. Waiting to deliver.
Order: fish delivered.
The order: arabian food is ready. Waiting to deliver.
The order: pastel azteca is ready. Waiting to deliver.
Order: hamburger delivered.
The order: pizza is ready. Waiting to deliver.
Order: pastel azteca delivered.
Order: arabian food delivered.
Order: pizza delivered.

""" 