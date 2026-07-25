import random
import time
import threading
""" Ejercicio Numero 21 Callbacks  """

def greeting_process(callback,name:str):
    print(f"Ejecutando el proceso de saludo...")
    callback(name)

def greet_callback(name:str):
    print(f"Hola {name}!")

greeting_process(greet_callback,"Gallito")
""" Dificultad extra """

def order_process(dish_name: str,order_confirmed,order_ready,order_delivered):
    def process():
        order_confirmed(dish_name)
        time.sleep(random.randint(1, 10))
        order_ready(dish_name)
        time.sleep(random.randint(1, 10))
        order_delivered(dish_name)

    threading.Thread(target=process).start()

def order_confirmed(dish_name:str):
    print(f"Su pedido de {dish_name} ha sido confirmado")

def order_ready(dish_name:str):
    print(f"Su pedido {dish_name} esta listo para ser entreagado")

def order_delivered(dish_name:str    ):
    print(f"Su pedido {dish_name} ha sido entregado.")


order_process("Pizza carbonara",order_confirmed,order_ready,order_delivered)



