import random
import time
import threading
from typing import Callable

MIN_DELAY = 1
MAX_DELAY = 10


# ejercicio
def greeting_process(name: str, callback):
    print("Ejecutando el proceso de saludo.......")
    callback(name)
    
def greet_callback(name: str):
    print(f"Hola, {name}!")
    
greeting_process("Rick", greet_callback)

# EXTRA

def simulate_delay():
    time.sleep(random.randint(MIN_DELAY, MAX_DELAY))

def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback) -> threading.Thread:
    
    def process():
        confirm_callback(dish_name)
        simulate_delay()
        ready_callback(dish_name)
        simulate_delay()
        delivered_callback(dish_name)

    thread = threading.Thread(target=process)
    thread.start()
    return thread

def confirm_order(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido confirmado")
    
def order_ready(dish_name: str):
    print(f"Tu pedido {dish_name} está listo")
    
def order_delivered(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido entregado")

if __name__ == "__main__":
    dishes = ["Pizza Barbacoa", "Pizza 4 Quesos", "Pizza Margarita", "Pizza con Piña" ]    

    threads =[
        order_process(dish, confirm_order, order_ready, order_delivered)
        for dish in dishes
    ]  

    for thread in threads:
        thread.join()
        
    print("Todos los pedidos fueron entregados")    