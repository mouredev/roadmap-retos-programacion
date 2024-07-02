import time
import random

def process_data(data, function_callback): 
    for element in data:
        function_callback(element)

def print_data(data):
    print(f"El dato es: {data}")

def squared_data(data):
    print(f"El cuadrado del dato es: {data ** 2}")

data = [1, 2, 3, 4, 5]
process_data(data, print_data)
process_data(data, squared_data)

### Ejercicio Extra ###

def order_process(dish: str, callback_confirmation, callback_ready, callback_delivered):
    callback_confirmation(dish)
    preparation_time = random.randint(1, 15)
    time.sleep(preparation_time)

    callback_ready(dish)
    delivery_time = random.randint(1, 30) 
    time.sleep(delivery_time)

    callback_delivered(dish)

def order_confirm(dish):
    print(f"Pedido confirmado: {dish}")

def order_ready(dish):
    print(f"Pedido listo: {dish}")

def order_delivered(dish):
    print(f"Pedido {dish} ha sido entregado.")

dishes_names = ["Pizza Margherita", "Sushi", "Hamburguesa", "Tacos", "Ensalada César"]
dish_random = random.choice(dishes_names)
order_process(dish_random, order_confirm, order_ready, order_delivered)